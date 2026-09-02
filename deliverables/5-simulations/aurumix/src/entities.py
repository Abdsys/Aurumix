"""
The agent pool. Struct-of-arrays, not per-agent objects.

Blueprint Part 2, State Variables. ~200k agents x 84 months x 1,000 paths makes
per-agent Python objects impossible, so every attribute is a numpy array indexed
by agent and every rule is a vectorised operation over those arrays.
"""

from dataclasses import dataclass, field
import numpy as np

from config import config as C
from src.mechanics import RecentWindow, draw_tickets


@dataclass
class AgentPool:
    """Every customer ever acquired. Agents are never removed, only marked dead."""

    # identity / fixed at acquisition
    region: np.ndarray            # int8 index into C.REGIONS
    archetype: np.ndarray         # int8 index into the active archetype list
    rail: np.ndarray              # bool: True = prefunded ("set and forget")
    door: np.ndarray              # bool: True = entered via SIP, False = spot-only
    born_month: np.ndarray        # int16
    ticket_base: np.ndarray       # float64, the centre of the monthly draw

    # behavioural parameters, expanded per agent for vectorised draws
    pay_prob0: np.ndarray         # float64, month-1 pay probability
    pay_decay: np.ndarray         # float64
    pay_floor: np.ndarray         # float64
    hazard: np.ndarray            # float64, own + background

    # the score's three facts
    months_counted: np.ndarray    # int16, NEVER decreases
    streak: np.ndarray            # int8, 0..6
    gated: np.ndarray             # bool, permanent once True

    # gold, for Retention
    grams: np.ndarray             # float64, currently held
    grams_year_open: np.ndarray   # float64, held 12 months ago
    grams_acquired_ytd: np.ndarray  # float64, acquired since that point

    # state machine - four independent clocks
    sip_active: np.ndarray        # bool
    card_active: np.ndarray       # bool
    alive: np.ndarray             # bool, False only on full exit

    # derived, recomputed each month
    ics: np.ndarray               # float64
    tier: np.ndarray              # int8

    recent: RecentWindow = None
    gate_month: np.ndarray = None   # int16, -1 until gated

    @property
    def n(self):
        return self.region.shape[0]


def _expand(archetypes, idx, attr):
    return np.array([getattr(archetypes[i], attr) for i in idx], dtype=np.float64)


def build_cohort(rng, n, archetypes, background_hazard, region_idx=0,
                 born_month=1, prefunded_share=C.RAIL_PREFUNDED_SHARE,
                 discipline_shift=C.RAIL_DISCIPLINE_SHIFT,
                 floor_share=C.TICKET_FLOOR_SHARE, ticket_mean=None):
    """
    Create n agents in one region at one month.

    Rail is assigned first, then archetype CONDITIONED on rail: a prefunded agent
    has a `discipline_shift` chance of being re-drawn from the top of the mix.
    That is the mechanism by which "set and forget" versus "one tap a month"
    becomes a difference in who clears six consecutive payments - and it is the
    one lever over the archetype mix that Aurumix actually controls.
    """
    weights = np.array([a.weight for a in archetypes], dtype=np.float64)
    weights = weights / weights.sum()

    rail = rng.random(n) < prefunded_share
    arche = rng.choice(len(archetypes), size=n, p=weights)

    # Prefunded agents: re-draw the shifted fraction from the disciplined half.
    disciplined = np.array([i for i, a in enumerate(archetypes)
                            if a.name in ("perfect", "occasional", "reducer")],
                           dtype=np.int64)
    if disciplined.size and prefunded_share > 0.0 and discipline_shift > 0.0:
        dw = weights[disciplined] / weights[disciplined].sum()
        shift = rail & (rng.random(n) < discipline_shift)
        if shift.any():
            arche[shift] = rng.choice(disciplined, size=int(shift.sum()), p=dw)

    if ticket_mean is None:
        ticket_mean = C.REGIONS[region_idx].ticket_mean
    ticket_base = draw_tickets(rng, n, ticket_mean, floor_share)

    pool = AgentPool(
        region=np.full(n, region_idx, dtype=np.int8),
        archetype=arche.astype(np.int8),
        rail=rail,
        door=np.ones(n, dtype=bool),
        born_month=np.full(n, born_month, dtype=np.int16),
        ticket_base=ticket_base,
        pay_prob0=_expand(archetypes, arche, "pay_prob"),
        pay_decay=_expand(archetypes, arche, "pay_decay"),
        pay_floor=_expand(archetypes, arche, "pay_floor"),
        hazard=_expand(archetypes, arche, "own_hazard") + background_hazard,
        months_counted=np.zeros(n, dtype=np.int16),
        streak=np.zeros(n, dtype=np.int8),
        gated=np.zeros(n, dtype=bool),
        grams=np.zeros(n),
        grams_year_open=np.zeros(n),
        grams_acquired_ytd=np.zeros(n),
        sip_active=np.ones(n, dtype=bool),
        card_active=np.zeros(n, dtype=bool),
        alive=np.ones(n, dtype=bool),
        ics=np.zeros(n),
        tier=np.zeros(n, dtype=np.int8),
    )
    pool.recent = RecentWindow(n)
    pool.gate_month = np.full(n, -1, dtype=np.int16)
    return pool
