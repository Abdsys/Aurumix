"""
Verification for the simplified Aurumix revenue model, read from the
RECALCULATED workbook.

Usage:  python recalc_lo.py Aurumix_Revenue_Model.xlsx
        python verify_model.py _recalc/Aurumix_Revenue_Model.xlsx
"""
import sys
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

PATH = sys.argv[1] if len(sys.argv) > 1 else "_recalc/Aurumix_Revenue_Model.xlsx"
wb = load_workbook(PATH, data_only=True)
N, PCOL0, N_MONTHLY = 29, 3, 24
def pc(i): return get_column_letter(PCOL0 + i)

results = []
def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))


def all_num(seq):
    """NON-EMPTY and every element numeric - guards the vacuous-truth trap."""
    seq = list(seq)
    return bool(seq) and all(isinstance(x, (int, float)) for x in seq)


EXPECTED = ["Cover", "Assumptions", "Scenario Parameters", "Model", "Summary"]
check("Exactly the 5 standard sheets, in order", wb.sheetnames == EXPECTED, "%r" % (wb.sheetnames,))
asm, sc, mdl, summ = wb["Assumptions"], wb["Scenario Parameters"], wb["Model"], wb["Summary"]

# ---- 0. the reference chain: Scenario -> Assumptions -> Model -> Summary ---
# Read from the FORMULA copy, since the recalculated one holds cached values.
import os
_src = os.path.join(os.path.dirname(os.path.abspath(PATH)) or ".", os.path.basename(PATH))
wbf = load_workbook(_src, data_only=False)


def refs(sheet, target):
    n = 0
    for r_ in wbf[sheet].iter_rows():
        for c in r_:
            if isinstance(c.value, str) and c.value.startswith("=") and target in c.value:
                n += 1
    return n


check("Model reads Assumptions, never Scenario Parameters directly",
      refs("Model", "Scenario Parameters") == 0 and refs("Model", "Assumptions") > 0,
      "Model -> Scenario %d, Model -> Assumptions %d"
      % (refs("Model", "Scenario Parameters"), refs("Model", "Assumptions")))
check("Summary reads only the Model",
      refs("Summary", "Scenario Parameters") == 0 and refs("Summary", "Model") > 0,
      "Summary -> Scenario %d" % refs("Summary", "Scenario Parameters"))
# No sheet may carry a duplicate row label. A repeated label is how a lookup
# silently reads the wrong row - it has caused two real defects in this build.
for _sh in ("Model", "Summary", "Assumptions"):
    _seen, _dupes = {}, []
    for _r in range(1, wbf[_sh].max_row + 1):
        _lv = wbf[_sh]["A%d" % _r].value
        if isinstance(_lv, str) and _lv.strip() and not _lv.startswith("="):
            _seen.setdefault(_lv, []).append(_r)
    # Indented region-block rows repeat by design; so do per-section column
    # headers. Everything else must be unique.
    _HDRS = {"Parameter", "Funnel step", "Scenario", "Switch"}
    _dupes = {k: v for k, v in _seen.items()
              if len(v) > 1 and not k.startswith("  ") and k not in _HDRS}
    check("%s has no duplicate top-level row labels" % _sh, not _dupes,
          "%r" % list(_dupes.items())[:3])

check("Assumptions carries a scenario-linked mirror block",
      refs("Assumptions", "Scenario Parameters") > 0,
      "mirror links found: %d" % refs("Assumptions", "Scenario Parameters"))

# EVERY scenario parameter must appear on Assumptions. A parameter row is a
# label in A with a live formula in B (CHOOSE, a derivation, or a switch IF).
_fsc, _fasm = wbf["Scenario Parameters"], wbf["Assumptions"]
_params = [(r, _fsc["A%d" % r].value.strip())
           for r in range(1, _fsc.max_row + 1)
           if isinstance(_fsc["A%d" % r].value, str) and _fsc["A%d" % r].value.strip()
           and isinstance(_fsc["B%d" % r].value, str) and _fsc["B%d" % r].value.startswith("=")]
_mirror = {}
for r in range(1, _fasm.max_row + 1):
    b = _fasm["B%d" % r].value
    if isinstance(b, str) and b.startswith("=") and "Scenario Parameters" in b:
        _mirror[int(b.split("$B$")[1].split(")")[0].strip())] = (_fasm["A%d" % r].value or "").strip()
_missing = [n for r, n in _params if r not in _mirror]
check("EVERY scenario parameter is mirrored onto Assumptions",
      not _missing and len(_params) == len(_mirror),
      "%d parameters, %d mirrored. Missing: %s" % (len(_params), len(_mirror), _missing[:5]))
_mismatch = [(n, _mirror[r]) for r, n in _params if r in _mirror and _mirror[r] != n]
check("Mirrored labels match their Scenario Parameters labels exactly",
      not _mismatch, "%r" % _mismatch[:3])

# NO ORPHANS. Added 2026-08-21 after "Spot-to-SIP conversion" was found defined,
# mirrored, scenario-flexed - and referenced by nothing. A dead input is worse
# than a missing one: it reads as a modelled mechanism, it implies a population
# the model does not have, and flipping the scenario appears to do something.
# Mirroring alone never catches this, because an orphan mirrors perfectly.
import re as _re


def _cited(formula, sheet=None):
    """Every $B$n row a formula touches, EXPANDING RANGES.

    Ranges matter: the annual schedules are read as INDEX(Assumptions!$B$a:$B$b,
    year), so only the first row carries the sheet prefix. Matching single cells
    alone reports rows 2..n of every schedule as orphans."""
    pat = (r"%s!\$B\$(\d+)(?::\$B\$(\d+))?" % sheet) if sheet else r"(?<![!\w])\$B\$(\d+)(?::\$B\$(\d+))?"
    out = set()
    for lo, hi in _re.findall(pat, formula):
        lo = int(lo)
        out.update(range(lo, int(hi) + 1) if hi else [lo])
    return out


_used_asm = set()          # Assumptions rows the Model reads
for _r in wbf["Model"].iter_rows():
    for _c in _r:
        if isinstance(_c.value, str) and _c.value.startswith("="):
            _used_asm |= _cited(_c.value, "Assumptions")
_used_sc = set()           # Scenario rows other Scenario formulas read
for _r in _fsc.iter_rows():
    for _c in _r:
        if isinstance(_c.value, str) and _c.value.startswith("="):
            # Derived rows refer to their OWN sheet BY NAME ("'Scenario
            # Parameters'!$B$10"), not as a bare local ref, so both forms count.
            _used_sc |= _cited(_c.value) | _cited(_c.value, "'Scenario Parameters'")

# Map each mirrored Assumptions row back to the Scenario row it came from.
_mirror_asm = {}
for r in range(1, _fasm.max_row + 1):
    b = _fasm["B%d" % r].value
    if isinstance(b, str) and b.startswith("=") and "Scenario Parameters" in b:
        _mirror_asm[r] = (int(b.split("$B$")[1].split(")")[0].strip()),
                          (_fasm["A%d" % r].value or "").strip())
# A parameter EARNS ITS PLACE if the Model reads its Assumptions mirror, OR a
# derived scenario parameter reads it upstream (persistency, for instance, is
# consumed by the monthly-churn derivation rather than by the Model directly -
# it is mirrored for visibility, at the client's explicit request).
_orphans = sorted(n for r, (sr, n) in _mirror_asm.items()
                  if r not in _used_asm and sr not in _used_sc)
check("NO ORPHANED scenario parameters - every one is read by the Model or a derivation",
      not _orphans, "scenario-flexed but referenced nowhere: %r" % _orphans)


def rowof(ws, label):
    """Exact match INCLUDING indentation, and it must be UNIQUE.

    Indentation is meaningful: region-block rows are indented ("  Stream 2 ...")
    and whole-book totals are not, so an exact match distinguishes a regional
    line from the total of the same name. Uniqueness is asserted because a
    duplicate label is how a lookup silently reads the wrong row."""
    hits = [r for r in range(1, ws.max_row + 1) if ws["A%d" % r].value == label]
    if len(hits) > 1:
        raise AssertionError("label %r is ambiguous on %s: rows %r" % (label, ws.title, hits))
    return hits[0] if hits else None


def mv(label, i):
    r = rowof(mdl, label)
    return mdl["%s%d" % (pc(i), r)].value if r else None


def row(label): return [mv(label, i) for i in range(N)]
def sval(label):
    r = rowof(sc, label)
    return sc["B%d" % r].value if r else None
def aval(label):
    r = rowof(asm, label)
    return asm["B%d" % r].value if r else None


# ---- 1. no errors ----------------------------------------------------------
ERRS = ("#REF!", "#VALUE!", "#DIV/0!", "#NAME?", "#NULL!", "#NUM!", "#N/A")
bad = []
for ws in wb.worksheets:
    for r_ in ws.iter_rows():
        for c in r_:
            if isinstance(c.value, str) and c.value in ERRS:
                bad.append("%s!%s=%s" % (ws.title, c.coordinate, c.value))
check("No formula errors in any sheet", not bad, "; ".join(bad[:6]))

# ---- 2. period grid --------------------------------------------------------
check("29 periods indexed 1..29", row("Period #") == list(range(1, 30)))
yrs, n = row("Model year"), row("Months in period")
check("Years run 1x12, 2x12, then 3..7",
      yrs[:12] == [1] * 12 and yrs[12:24] == [2] * 12 and yrs[24:] == [3, 4, 5, 6, 7])
check("Monthly block = 1 month, annual block = 12", n[:24] == [1] * 24 and n[24:] == [12] * 5)

# ---- 3. seasonality --------------------------------------------------------
sr = rowof(mdl, "Seasonality sum check (must be exactly 12.000)")
a_s, s_s = mdl["%s%d" % (pc(0), sr)].value, mdl["%s%d" % (pc(1), sr)].value
check("Acquisition seasonality sums to EXACTLY 12.000", abs(a_s - 12.0) < 1e-9, "%r" % a_s)
check("Card spend seasonality sums to EXACTLY 12.000", abs(s_s - 12.0) < 1e-9, "%r" % s_s)

# ---- 4. the customer engine ------------------------------------------------
cons = row("CHECK: paying + holders = cumulative ever acquired")
check("CONSERVATION - paying + holders = cumulative ever acquired, every period",
      all_num(cons) and max(abs(x) for x in cons) < 1e-6,
      "max delta %r" % (max(abs(x) for x in cons) if all_num(cons) else cons))
pay, hold, cum = row("PAYING CUSTOMERS"), row("HOLDERS (stopped paying, still hold gold)"), row("Cumulative ever acquired")
check("No negative populations", all(x >= -1e-9 for x in pay + hold + cum))
check("Cumulative ever acquired strictly increases", all(cum[i] > cum[i - 1] for i in range(1, N)))
check("Holders overtake payers as the book matures", hold[-1] > pay[-1],
      "Y7 holders %.0f vs paying %.0f" % (hold[-1], pay[-1]))
# Found by PREFIX, so renaming a region does not silently break the check.
ceil_rows = [r for r in range(1, asm.max_row + 1)
             if isinstance(asm["A%d" % r].value, str)
             and asm["A%d" % r].value.startswith("Reachable SIP ceiling")]
REGION_NAMES = [asm["A%d" % r].value.split(" - ", 1)[1] for r in ceil_rows]
check("At least three regional ceilings are defined", len(ceil_rows) >= 3,
      "found %d: %r" % (len(ceil_rows), REGION_NAMES))
ceil_tot = sum(asm["B%d" % r].value for r in ceil_rows)
# Re-anchored 2026-08-20: the UAE Indian population was corrected from 3.5m to
# the official 4.36m, which legitimately raises the ceiling. The check still
# guards against accidental rescaling, just against the corrected figure.
check("Reachable ceilings sum to the market-size anchor (~181,150, within 1%)",
      abs(ceil_tot - 181150) / 181150 < 0.01, "%.0f vs 181,150" % ceil_tot)

# The funnel must be live arithmetic, not typed numbers.
_fa = wbf["Assumptions"]
_fun_rows = {}
for r in range(1, _fa.max_row + 1):
    v = _fa["A%d" % r].value
    if isinstance(v, str) and v.strip() in ("= Addressable base", "= REACHABLE SIP ACCOUNTS",
                                            "Source population"):
        _fun_rows[v.strip()] = r
check("The market-sizing funnel is present on Assumptions", len(_fun_rows) == 3,
      "found %r" % sorted(_fun_rows))
if len(_fun_rows) == 3:
    ar_ = _fun_rows["= Addressable base"]
    rr_ = _fun_rows["= REACHABLE SIP ACCOUNTS"]
    live = all(isinstance(_fa.cell(row=ar_, column=6 + k).value, str)
               and _fa.cell(row=ar_, column=6 + k).value.startswith("=") for k in range(4))
    live2 = all(isinstance(_fa.cell(row=rr_, column=6 + k).value, str)
                and _fa.cell(row=rr_, column=6 + k).value.startswith("=") for k in range(4))
    check("Addressable base and reachable accounts are COMPUTED, not typed", live and live2)
    # and the region ceilings must be derived from the funnel, not typed
    derived = all(isinstance(_fa["B%d" % r].value, str) and _fa["B%d" % r].value.startswith("=")
                  for r in ceil_rows)
    check("Region ceilings are DERIVED from the funnel, not typed", derived)
    # arithmetic: population x filters x ceiling reproduces reachable accounts
    pr_ = _fun_rows["Source population"]
    ok_arith = True
    for k in range(4):
        col = get_column_letter(6 + k)
        pop = asm["%s%d" % (col, pr_)].value
        acct = asm["%s%d" % (col, rr_)].value
        chain = pop
        for off in (1, 2, 3):
            chain *= asm["%s%d" % (col, pr_ + off)].value
        chain *= asm["%s%d" % (col, pr_ + 5)].value
        if abs(chain - acct) > 1:
            ok_arith = False
    check("Funnel arithmetic reconciles end to end (population -> accounts)", ok_arith)
check("Cumulative ever acquired never breaches the ceiling", cum[-1] <= ceil_tot + 1,
      "%.0f vs %.0f" % (cum[-1], ceil_tot))
_sat_rows = [r for r in range(1, mdl.max_row + 1)
             if mdl["A%d" % r].value == "  Saturation (this region's own headroom)"]
check("Saturation is applied PER REGION, not just on the whole book",
      len(_sat_rows) == len(REGION_NAMES), "found %d for %d regions" % (len(_sat_rows), len(REGION_NAMES)))
for sr_ in _sat_rows:
    vals = [mdl["%s%d" % (pc(i), sr_)].value for i in range(N)]
    if all_num(vals):
        check("Regional saturation decays monotonically (row %d)" % sr_,
              all(vals[i] <= vals[i - 1] + 1e-12 for i in range(1, N)))

# No region may breach its OWN ceiling - the whole-book total staying inside the
# sum of ceilings is not sufficient, since one channel can concentrate in one
# market. Agents route to India only, which is exactly that risk.
_cum_rows = [r for r in range(1, mdl.max_row + 1)
             if mdl["A%d" % r].value == "  Cumulative ever acquired"]
breach = []
for rn, cr_ in zip(REGION_NAMES, _cum_rows):
    cap = aval("Reachable SIP ceiling - %s" % rn)
    end = mdl["%s%d" % (pc(N - 1), cr_)].value
    if isinstance(end, (int, float)) and isinstance(cap, (int, float)) and end > cap * 1.001:
        breach.append("%s %.0f > %.0f" % (rn, end, cap))
check("NO region breaches its own reachable ceiling", not breach, "; ".join(breach))

# The salesforce is deployed across every market, not India alone.
ash = {rn: aval("Share of salesforce deployed - %s" % rn) for rn in REGION_NAMES}
check("Agent-share allocation sums to 100%", abs(sum(ash.values()) - 1.0) < 1e-9, "%r" % ash)
_cac = {rn: sval("Marketing CAC - %s" % rn) for rn in REGION_NAMES}
_mks = {rn: sval("Marketing spend share - %s" % rn) for rn in REGION_NAMES}
check("CAC is regionalised, not one global figure", len(set(_cac.values())) > 1, "%r" % _cac)
check("Marketing spend shares sum to 100%", abs(sum(_mks.values()) - 1.0) < 1e-9, "%r" % _mks)
_ind = [rn for rn in REGION_NAMES if "India" in rn]
_uae = [rn for rn in REGION_NAMES if rn == "UAE"]
if _ind and _uae:
    check("India CAC is far below the UAE's, matching the published gap",
          _cac[_ind[0]] < _cac[_uae[0]] * 0.35,
          "India %r vs UAE %r" % (_cac[_ind[0]], _cac[_uae[0]]))
check("Every region acquires through its own marketing budget and CAC",
      len([r for r in range(1, mdl.max_row + 1)
           if mdl["A%d" % r].value == "  Direct-driven (this market's budget at its own CAC)"])
      == len(REGION_NAMES))
check("Every region refers from its OWN paying base",
      len([r for r in range(1, mdl.max_row + 1)
           if mdl["A%d" % r].value == "  Referral-driven (from this market's own base)"])
      == len(REGION_NAMES))
# REVISED 2026-08-21. The old check asserted the OPPOSITE - that at least one
# region had no salesforce - which encoded a cut of the model where 100% sat in
# India and the licensed home market had nobody selling at all. Every market
# now gets people; what differs by region is what those people COST, which is a
# cost-build concern and deliberately absent here.
check("Every market has a deployed salesforce, including the licensed home market",
      all(isinstance(v, (int, float)) and v > 0 for v in ash.values()), "%r" % ash)
check("UAE, the licensed home market, is not out-weighted by the Gulf expansion",
      ash.get("UAE", 0) > ash.get("Oman and Bahrain", 1), "%r" % ash)

# churn must reproduce the stated persistency over 12 months
pers, churn = sval("Persistency - customers still paying after 12 months"), sval("Monthly churn rate (derived)")
check("Derived monthly churn reproduces the stated persistency over 12 months",
      abs((1 - churn) ** 12 - pers) < 1e-9, "(1-%.5f)^12 = %.4f vs %.2f" % (churn, (1 - churn) ** 12, pers))

# ---- 5. eligibility - the two cells that replace the archetype engine ------
q, cards = row("Cleared the six-payment gate"), row("ACTIVE CARDS")
ever_q = sval("Customers who EVER clear the six-payment gate")
check("Qualified customers never exceed the card-eligible base x the qualify rate",
      all(q[i] <= (pay[i] + hold[i]) * ever_q + 1e-6 for i in range(N)))
check("ELIGIBILITY BITES - qualified is strictly below the whole book",
      q[-1] < (pay[-1] + hold[-1]) * 0.999,
      "qualified %.0f vs book %.0f" % (q[-1], pay[-1] + hold[-1]))
card_m = aval("Stream 2 - Card interchange")
check("Active cards are ZERO before the card launch month",
      all(abs(x) < 1e-9 for x in cards[:card_m - 1]) and cards[card_m - 1] > 0,
      "M%d %r  M%d %r" % (card_m - 1, cards[card_m - 2], card_m, cards[card_m - 1]))

# ---- 6. every stream fires on exactly the month the calendar says ----------
# The month is READ FROM the Assumptions activation calendar, not hardcoded, so
# these checks follow the calendar if a launch date is moved again.
for label, nm in (("Stream 1a - Entry fee, SIP", "stream 1a"),
                  ("Stream 1b - Entry fee, SPOT", "stream 1b"),
                  ("Stream 3 - Family plan and Digital Will", "stream 3"),
                  ("Stream 2 - Card interchange", "stream 2"),
                  ("Stream 4 - Cardholder fees", "stream 4"),
                  ("Stream 5 - Lending revenue share", "stream 5"),
                  ("Stream 6 - B2B platform fee", "stream 6")):
    m = aval(label)
    v = row(label)
    assert m <= N_MONTHLY, "activation M%d is outside the monthly block - check needs the annual mapping" % m
    before_zero = all(abs(x) < 1e-9 for x in v[:m - 1])
    on_nonzero = abs(v[m - 1]) > 1e-9
    check("%s is zero before M%d and non-zero from M%d" % (nm, m, m), before_zero and on_nonzero,
          "M%d %r  M%d %r" % (m - 1, v[m - 2] if m > 1 else None, m, v[m - 1]))
# Redemption is a COST and has been removed from the revenue model - only the
# event count survives, as a driver for the later cost build.
check("Redemption is NOT in the revenue model", rowof(mdl, "Stream 0 - Redemption cost") is None)
redem = row("Redemption events (memo - drives cost, not revenue)")
check("Redemption event count is retained as a cost-build memo",
      all_num(redem) and redem[28] > 0, "Y7 events %r" % redem[28])

# ---- 7. the fabrication premium is borne ONCE, by the customer ------------
# Client decision 2026-08-21. The customer's money buys metal at spot+premium,
# so they receive fewer grams; the entry fee reaches Aurumix whole. These two
# checks are a matched pair and exist to catch the premium being deducted
# TWICE - once from the customer's grams and again from Aurumix's fee, which
# is what an earlier cut of the model did.
fee, prem = aval("Entry fee charged"), aval("Fabrication premium paid")
s1a, sip = row("Stream 1a - Entry fee, SIP"), row("SIP contributions")
spot, grams_in, price = row("Spot purchase volume"), row("Grams purchased"), aval("Gold price (flat)")

# (a) Aurumix keeps the WHOLE entry fee - no premium term on the revenue side.
check("Stream 1 earns the full entry fee (premium is NOT netted off revenue)",
      all_num(s1a) and all(abs(s1a[i] - sip[i] * fee) < 1e-6 for i in range(N) if sip[i]),
      "implied rate %.5f vs headline fee %.5f" % (s1a[13] / sip[13] if sip[13] else 0, fee))

# (b) ...and the customer therefore DOES bear it, in grams. Metal delivered
# must fall short of the post-fee cash by exactly the premium factor. If the
# (1+premium) divisor is ever dropped, nobody pays the premium and this fails.
inflow = [(sip[i] + spot[i]) * (1 - fee) for i in range(N)]
check("The customer bears the premium - grams delivered are short by exactly (1+premium)",
      all_num(grams_in) and all(
          abs(grams_in[i] * price - inflow[i] / (1 + prem)) < 1e-6 for i in range(N) if inflow[i]),
      "M14 metal %.2f vs cash %.2f, implied premium %.5f" % (
          grams_in[13] * price, inflow[13],
          inflow[13] / (grams_in[13] * price) - 1 if grams_in[13] else 0))

# (c) the incidence is material and lands on ONE side of the trade only.
check("Premium incidence is material and single-sided",
      abs(inflow[13] - grams_in[13] * price) > 1e-6 and abs(s1a[13] - sip[13] * fee) < 1e-6,
      "customer bears %.2f USD at M14; Aurumix bears 0" % (inflow[13] - grams_in[13] * price))

# ---- 8. the ATM distribution earns what a mean would not ------------------
# Verified from the parameters directly, so the check survives the stream-4
# components being combined into one regional formula.
BK_ATM = ("AED 0-500", "AED 500-1,500", "AED 1,500-3,000", "AED 3,000+")
allowance = aval("Free ATM allowance (Gold)")
shares = [sval("ATM %s - share of cardholders" % b) for b in BK_ATM]
mids = [sval("ATM %s - midpoint draw" % b) for b in BK_ATM]
mean_draw = sum(s * m for s, m in zip(shares, mids))
over_mean = max(0.0, mean_draw - allowance)
over_dist = sum(s * max(0.0, m - allowance) for s, m in zip(shares, mids))
check("The MEAN ATM draw sits below the free allowance (so a mean earns zero)",
      mean_draw < allowance and over_mean == 0,
      "mean %.0f vs allowance %.0f" % (mean_draw, allowance))
check("The DISTRIBUTION still earns ATM revenue where the mean would not",
      over_dist > 0, "distribution yields AED %.1f per cardholder, mean yields %.1f"
      % (over_dist, over_mean))

# The partner schedule must supply a partner by the month stream 6 activates,
# or the stream switches on with nothing to earn on.
b2b_m = aval("Stream 6 - B2B platform fee")
b2b_year = (b2b_m - 1) // 12 + 1
check("A B2B partner exists by the year stream 6 activates",
      (sval("B2B partners - Y%d" % b2b_year) or 0) >= 1,
      "stream 6 at M%d (Y%d) but Y%d partners = %r" % (b2b_m, b2b_year, b2b_year,
                                                       sval("B2B partners - Y%d" % b2b_year)))
check("Partner count rises monotonically once B2B is live",
      all((sval("B2B partners - Y%d" % y) or 0) >= (sval("B2B partners - Y%d" % (y - 1)) or 0)
          for y in range(2, 8)),
      "%r" % [sval("B2B partners - Y%d" % y) for y in range(1, 8)])

# ---- 8b. regions are handled consistently across BOTH inflow lanes --------
# REPLACED 2026-08-21. The two checks here read a "Share of new customers" row
# that has been deleted: it claimed acquisition followed the ceiling share, but
# acquisition is now driven per region by budget, CAC, salesforce and referrals,
# so the split is an OUTCOME. Both checks were also tautological - the row was
# derived from the ceilings, so testing it against the ceilings proved nothing.
# What is worth asserting is that the OUTCOME is sane.
ceil_share = [asm["B%d" % r].value / ceil_tot for r in ceil_rows]
check("Region ceiling shares sum to 1.000", abs(sum(ceil_share) - 1.0) < 1e-9,
      "sum %r" % sum(ceil_share))
_newr = [r for r in range(1, mdl.max_row + 1) if mdl["A%d" % r].value == "  New customers"]
_newy7 = [mdl["%s%d" % (pc(N - 1), r)].value for r in _newr]
check("Every region is still acquiring at Y7 (none has been starved by the mix)",
      len(_newy7) == len(REGION_NAMES) and all_num(_newy7) and all(v > 0 for v in _newy7),
      "Y7 new by region %r" % [round(v, 1) for v in _newy7])
# The emergent split should bear SOME relation to opportunity - not equality,
# since CAC and salesforce deliberately differ, but not a wild inversion either.
_share = [v / sum(_newy7) for v in _newy7]
check("Emergent regional acquisition is within 3x of each region's opportunity share",
      all(c / 3 <= s <= c * 3 for s, c in zip(_share, ceil_share)),
      "acquired %r vs opportunity %r" % ([round(x, 3) for x in _share],
                                         [round(x, 3) for x in ceil_share]))
# REPLACED 2026-08-21. The old check asserted the regional spot multipliers
# averaged 1.00 - a property of a DERIVED number that no longer exists. The
# tickets are now observed per region, so the thing worth defending is that
# they still carry the ORDERING the sources establish.
stkt = {r: aval("Spot ticket - %s" % r) for r in REGION_NAMES}
check("Every region carries its own observed spot ticket",
      all(isinstance(v, (int, float)) and v > 0 for v in stkt.values()), "%r" % stkt)
# The finding that motivated the rebuild: published UAE tickets run ~5x India's.
# The old SIP-derived multiplier put India at 0.95x the UAE, inverting this.
check("UAE spot ticket is MULTIPLES of India's, as the published data shows",
      stkt["UAE"] > stkt["India"] * 3,
      "UAE %r vs India %r (ratio %.2f)" % (stkt["UAE"], stkt["India"], stkt["UAE"] / stkt["India"]))
# Tie the UAE figure to its source in AED, the unit Botim reported it in, so a
# drift in the peg or the ticket shows up against the observation itself.
_aed = stkt["UAE"] * aval("AED/USD peg")
check("UAE spot ticket still reconciles to Botim's observed AED 700",
      600 <= _aed <= 800, "implies AED %.0f" % _aed)
check("The inferred Gulf ticket sits between the two observed ones",
      stkt["India"] < stkt["Oman and Bahrain"] < stkt["UAE"], "%r" % stkt)
# The point of regionalising: as the mix shifts, the implied blended spot ticket
# must MOVE. If it is constant the regional scaling is not wired through.
spot, pay_all = row("Spot purchase volume"), row("PAYING CUSTOMERS")
implied = [spot[i] / pay_all[i] for i in (11, 23, 28) if pay_all[i]]
check("Blended spot ticket MOVES as the region mix shifts (regional scaling is live)",
      max(implied) - min(implied) > 1e-6,
      "implied per-customer spot %r" % [round(x, 2) for x in implied])

# ---- 8c. the regional block structure -------------------------------------
subs = {}
for rn in REGION_NAMES:
    lbl = "  SUBTOTAL - %s" % rn
    if rowof(mdl, lbl):
        subs[rn] = row(lbl)
check("Every region has its own revenue subtotal", len(subs) == len(REGION_NAMES),
      "found %r of %r" % (sorted(subs), REGION_NAMES))
tot_chk = row("CHECK: regional subtotals + B2B = sum of streams")
check("Regional subtotals + B2B reconcile to the sum of streams, every period",
      all_num(tot_chk) and max(abs(x) for x in tot_chk) < 1e-6,
      "max delta %r" % (max(abs(x) for x in tot_chk) if all_num(tot_chk) else tot_chk))
s6r = row("Stream 6 - B2B platform fee")
check("Grand total = sum of regional subtotals + non-regional B2B",
      all(abs(sum(subs[rn][i] for rn in subs) + s6r[i] - row("TOTAL NET REVENUE")[i]) < 1e-6
          for i in (0, 12, 28)))
# Every region must actually contribute - a silent zero would mean a region
# block is wired but never populated.
for rn in REGION_NAMES:
    check("Region %s contributes revenue by Y7" % rn, subs[rn][28] > 0, "Y7 %r" % subs[rn][28])
# The staged region must be empty until it opens.
gulf = [rn for rn in REGION_NAMES if "Oman" in rn]
if gulf:
    g = row("  SUBTOTAL - %s" % gulf[0])
    gm = aval("Region opens - %s" % gulf[0])
    check("The staged region earns nothing before it opens",
          all(abs(x) < 1e-9 for x in g[:gm - 1]) and g[gm - 1] != 0,
          "opens M%d; M%d=%r M%d=%r" % (gm, gm - 1, g[gm - 2], gm, g[gm - 1]))
# The real constraint is PER REGION: a cardholder cannot spend more in a month
# than the limit their own gold supports.
per_region_ok, worst = True, 0.0
_spc_rows = [r for r in range(1, mdl.max_row + 1)
             if mdl["A%d" % r].value == "  Card spend per card per month"]
_lim_rows = [r for r in range(1, mdl.max_row + 1)
             if mdl["A%d" % r].value == "  Credit limit per customer (gold x LTV)"]
check("Every region has a per-card spend row and a credit limit row",
      len(_spc_rows) == len(REGION_NAMES) and len(_lim_rows) == len(REGION_NAMES),
      "%d spend, %d limit, %d regions" % (len(_spc_rows), len(_lim_rows), len(REGION_NAMES)))
for sr_, lr_ in zip(_spc_rows, _lim_rows):
    for i in range(N):
        s_, l_ = mdl["%s%d" % (pc(i), sr_)].value, mdl["%s%d" % (pc(i), lr_)].value
        if isinstance(s_, (int, float)) and isinstance(l_, (int, float)) and l_ > 0:
            worst = max(worst, s_ / l_)
            if s_ > l_ * 1.001:
                per_region_ok = False
check("PER REGION - monthly card spend never exceeds the limit the gold supports",
      per_region_ok, "worst utilisation %.2fx" % worst)
# Under the drawdown model the constraint is satisfied BY CONSTRUCTION - spend
# IS the drawdown - so what matters is that annual drawdown stays inside a
# sensible multiple of the limit rather than a monthly cap binding.
_dr_rows = [r for r in range(1, mdl.max_row + 1)
            if mdl["A%d" % r].value == "  Annual drawdown per card (limit x drawn x draws)"]
_lim_rows2 = [r for r in range(1, mdl.max_row + 1)
              if mdl["A%d" % r].value == "  Credit limit per customer (gold x LTV)"]
check("Annual drawdown is a sane multiple of the credit limit (0.5x-3x)",
      all(0.5 <= (mdl["%s%d" % (pc(28), d)].value or 0) / (mdl["%s%d" % (pc(28), l)].value or 1) <= 3.0
          for d, l in zip(_dr_rows, _lim_rows2)),
      "%r" % [round((mdl["%s%d" % (pc(28), d)].value or 0) / (mdl["%s%d" % (pc(28), l)].value or 1), 2)
              for d, l in zip(_dr_rows, _lim_rows2)])
lim = row("  CHECK: card spend vs credit capacity (must be <= 1.00)")
check("Whole-book card spend stays within total credit capacity",
      all_num(lim) and max(lim) <= 1.001, "max %.2fx" % (max(lim) if all_num(lim) else -1))

# ---- 8d. average ticket is DERIVED and scales with the SIP contribution ----
_avg_rows = [r for r in range(1, mdl.max_row + 1)
             if mdl["A%d" % r].value == "  Average transaction size (derived)"]
check("Average transaction size is derived per region, not a single input",
      len(_avg_rows) == len(REGION_NAMES) and rowof(asm, "Average transaction size") is None,
      "%d rows; stale absolute input present: %s"
      % (len(_avg_rows), rowof(asm, "Average transaction size") is not None))
_avg = [mdl["%s%d" % (pc(28), r)].value for r in _avg_rows]
_lims = [mdl["%s%d" % (pc(28), r)].value for r in _lim_rows2]
# Under the drawdown model the ticket follows the CREDIT LIMIT (gold held), not
# the monthly SIP amount - a customer with more gold can draw and spend more.
check("Average ticket ORDERS the same way as the credit limit across regions",
      [i for i, _ in sorted(enumerate(_avg), key=lambda t: t[1])]
      == [i for i, _ in sorted(enumerate(_lims), key=lambda t: t[1])],
      "limits %r -> avg txn %r" % ([round(x) for x in _lims], [round(x) for x in _avg]))
check("Average ticket is a plausible size for a borrowed lump (AED 80-600)",
      all(80 <= x <= 600 for x in _avg), "%r" % [round(x) for x in _avg])
check("Average ticket sits well below the UAE all-population average of AED 313",
      max(_avg) < 313, "max derived ticket AED %.0f" % max(_avg))

# ---- 9. totals -------------------------------------------------------------
tot = row("TOTAL NET REVENUE")
parts = ["Stream 1a - Entry fee, SIP", "Stream 1b - Entry fee, SPOT",
         "Stream 2 - Card interchange", "Stream 3 - Family plan and Digital Will",
         "Stream 4 - Cardholder fees", "Stream 5 - Lending revenue share",
         "Stream 6 - B2B platform fee"]
sums = [sum(row(p)[i] for p in parts) for i in range(N)]
check("TOTAL NET REVENUE equals the sum of its streams",
      all(abs(tot[i] - sums[i]) < 1e-6 for i in range(N)))
check("Revenue is positive from M1 and grows", tot[0] > 0 and tot[-1] > tot[0])
aum = row("COLLATERAL-ELIGIBLE AUM")
check("AUM is positive and grows", all(x >= 0 for x in aum) and aum[-1] > aum[0])
check("Grams held never go negative", all(x >= 0 for x in row("GRAMS HELD")))

# ---- 10. Summary ties to Model --------------------------------------------
def sumv(label, y):
    r = rowof(summ, label)
    return summ["%s%d" % (get_column_letter(4 + y - 1), r)].value if r else None


y1 = sum(tot[i] for i in range(12))
check("Summary Y1 total revenue ties to the Model's twelve monthly columns",
      abs(sumv("TOTAL REVENUE", 1) - y1) < 1e-6,
      "summary %r vs model %r" % (sumv("TOTAL REVENUE", 1), y1))
check("Summary Y7 total revenue ties to the Model's Y7 column",
      abs(sumv("TOTAL REVENUE", 7) - tot[28]) < 1e-6)
# The revenue mix must sum to 100% - it once divided regional rows by the wrong
# denominator and produced percentages in the hundreds.
for y_ in (1, 3, 5, 7):
    mixsum = sumv("CHECK: mix sums to 100%", y_)
    check("Revenue mix sums to 100%% at Y%d" % y_,
          isinstance(mixsum, (int, float)) and abs(mixsum - 1.0) < 1e-6, "%r" % mixsum)
check("Summary paying customers at Y1 is the CLOSING month, not a sum",
      abs(sumv("Paying customers", 1) - pay[11]) < 1e-6,
      "summary %r vs M12 %r" % (sumv("Paying customers", 1), pay[11]))

print("=" * 78)
print("REVENUE MODEL VERIFICATION - %s" % PATH)
print("=" * 78)
npass = sum(1 for _, ok, _ in results if ok)
for name, ok, detail in results:
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name))
    if not ok and detail:
        print("         -> %s" % detail)
print("-" * 78)
print("%d/%d passed" % (npass, len(results)))
print("=" * 78)
sys.exit(0 if npass == len(results) else 1)
