# Phase 5 — Simulations: state and context

> **Read this before touching anything in `deliverables/5-simulations/`.** It is the Phase 5 equivalent of `handoff.md` §9. Detail lives in the code comments, which are written to be read.
>
> **Last updated:** 2026-09-22.

---

## 0. Where things stand

**Phase 5 is CLOSED as of 2026-09-22.** The three client-agreed finalization items (§5b) all landed that day: per-cell Monte Carlos on the conditions map, the four decision-and-work levers re-measured on a recorded run, and the tornado upgraded to paired Monte Carlos per end. All verification gates pass and both branded documents are rebuilt in `final/`.

| Thing | State |
|---|---|
| The engine (`aurumix/src/twin.py`) | ✅ Complete, verified |
| Base Monte Carlo, 2,000 paths, full resolution | ✅ Done |
| Stress Monte Carlo, 2,000 paths per scenario | ✅ Rerun complete 2026-09-05 with the redefined s1 (crash + panic): cum -608k, right beside s2's -611k. The price fall adds ~USD 3k given the panic |
| Recommended configuration (`mc_recommended.json`) | ✅ Full resolution, 2,000 paths, 2026-09-05: raise p90 3.44m, break-even 74.5%, NP7 p50 1.10m, cum p50 +1.88m. Config: alloc 40/10/50, ladder 1.5x convex, partners plan [0,1,3,5,8,11,14], ramp 9 months, rail base |
| Part 4 | ✅ Written: eight levers in three groups plus the combined configuration, all values from the recorded 2026-09-22 run |
| Conditions map | ✅ Per-cell Monte Carlo, 500 paths per cell (2026-09-22). Plan cell -0.02m; first profitable column at base CAC is 14 partners |
| Tornado | ✅ Paired Monte Carlo per end, 2,000 paths (2026-09-22, `run_tornado_mc.py`). Top bars: partner_adopt 1.50m, partner_aum_user 1.03m, facility_takeup 0.86m |
| `SIMULATION_SETUP.md` | ✅ Current, 38 branded pages |
| `SIMULATION_RESULTS.md` | ✅ Current, regenerated 2026-09-22, all gates pass |

**The one item this phase hands onward (decision 54, 2026-09-22): a lapsed customer keeps the card and the credit facility.** Nobody has checked what the twin and the Phase 4 workbook actually assume about lapsed cardholders. Check before quoting card or credit stream figures again.

---

## 1. What was built, and why it looks like this

**One engine, not two.** `src/twin.py` runs the whole business on individual customers, 84 monthly steps. Every rule from the Phase 4 revenue model executes on simulated people rather than on averages.

An earlier build had two engines: a port of the workbook doing the economics on a 29-column grid, with a population running alongside. That was removed on 2026-09-03. The justification for the split had been speed, and the claim was never measured: it is 0.3 seconds a path, not hours.

**The rule that governs the design.** Anything that depends on a customer is computed on customers. Anything that is a genuine fixed company cost is a monthly schedule. Nothing is ever an average customer times a head count.

**What is still taken from Phase 4:** parameters only. Prices, fees, licence costs, the vault contract, card economics, the marketing budget. Not the logic, and not the grid.

---

## 2. File map

| Path | What it is |
|---|---|
| `aurumix/src/twin.py` | the engine. Read its module docstring first |
| `aurumix/src/mcmodel.py` | the Monte Carlo wrapper: parameter draws, gold paths, partner arrivals |
| `aurumix/src/charts.py` | 14 charts, all drawn from saved outputs, never re-running the model |
| `aurumix/src/detmodel.py` | the retired workbook port. **Runtime does not import it.** Survives only for reconciliation |
| `aurumix/config/overrides.py` | every deliberate departure from Phase 4, each with its reason |
| `aurumix/scripts/run_mc.py` | base Monte Carlo. Takes `n_paths` and `scale` |
| `aurumix/scripts/mc_config.py` | Monte Carlo for a candidate configuration |
| `aurumix/scripts/run_stress_mc.py` | stress scenarios, paired on identical seeds |
| `aurumix/scripts/run_analysis.py` | thresholds, tornado, ladder, concentration. Prefers `tornado_mc.json` for the tornado when it exists |
| `aurumix/scripts/run_tornado_mc.py` | the finalization tornado: a paired Monte Carlo per assumption end |
| `aurumix/scripts/run_conditions.py` | the conditions map (per-cell Monte Carlos) and per-region economics |
| `aurumix/scripts/run_partner_sweep.py` | partner dose-response on fixed schedules |
| `aurumix/scripts/run_program_levers.py` | all eight Part 4 lever attributions, paired |
| `aurumix/scripts/run_decisions.py` | what to learn first, and the trigger levels |
| `SIMULATION_RESULTS.template.md` | the prose. **Edit this, never the `.md`** |
| `aurumix/scripts/fill_results.py` | injects ~110 figures into the template |
| `_branded_working/meta_results.json` | the executive summary PAGE. **Not built from the markdown** |

---

## 3. How to regenerate everything

Order matters, because each step reads the last one's output.

```
python scripts/run_mc.py 2000 1.0        # base, ~1.6h at full resolution
python scripts/mc_config.py <tag> ...    # a candidate configuration
python scripts/run_stress_mc.py 2000     # stress, ~2.3h
python scripts/run_float.py
python scripts/run_analysis.py
python scripts/run_tornado_mc.py 2000   # ~4.4h; run_analysis then reuses its bars
python scripts/run_conditions.py 500    # ~25 min, per-cell Monte Carlos
python scripts/run_partner_sweep.py
python scripts/run_program_levers.py
python scripts/run_decisions.py
python -m src.charts
python scripts/fill_results.py
cd ../_branded_working && python build_sim.py results && node render_sim.js ...
```

**Then MOVE to `final/`.** The client reads `final/` only. Every rebuild ends with moving the built .html and .pdf out of `_branded_working/` into `final/` (plus a copy of the current .md), leaving no document copies in the build folder. Copies were left behind once (2026-09-04) and the client opened a stale PDF a day after the fix was built; the build folder is now kept clean by client request.

**Rendering the PDF needs `NODE_PATH` pointed at a folder with puppeteer-core**, e.g. `C:/Users/BlockApex/Desktop/BCCP/node_modules`. There is no local install.

---

## 4. The verification gates, and why each exists

Run all of these after any change. Each was written because its failure happened.

| Gate | Catches |
|---|---|
| `scripts/verify_stage1.py` | 29 checks on the customer engine |
| `scripts/audit_model.py` | 27 checks: priced ranges reach the Monte Carlo, the giveback is priced from real tiers, departures are declared |
| `scripts/reconcile.py` | every difference against the Phase 4 workbook has a written cause |
| `scripts/check_docs.py` | the documents, **including the branded summary page**, still match the model |
| `scripts/revalidate.py` | proves stored results still match current code, for changes that provably cannot move a number |

**The staleness guard in `fill_results.py` refuses to render from any output older than the newest model file.** It has caught four real bugs. Do not bypass it; use `revalidate.py`, which re-runs five paths and compares before refreshing timestamps.

---

## 5. How Part 4 got its numbers, and the decisions that shaped it

**The results document was restructured on 2026-09-04** to the client's requested flow: base case results first, then why, then stress, then recommendations, then what to learn.

**All eight lever values now come from one recorded run** (`run_program_levers.py`, 2,000 paired paths, 2026-09-22), closing the client's 2026-09-08 catch that the published values traced to an unrecorded run. The four program levers reproduced exactly (card take-up +1,316k, tickets +374k, retention +270k, standing instructions +217k), which validates the method. The four decision-and-work levers moved:

| Lever | Old published | Recorded 2026-09-22 |
|---|--:|--:|
| Move marketing to India 40/10/50 | +833k | **+688k** |
| Trim the loyalty ladder 1.5x convex | +315k | **+322k** |
| Three more partners | +990k | **+415k** |
| Halve partner onboarding | +542k | **+517k** |

**The partners lever more than halved, and the reason is the method, on purpose:** the recorded run raises the PLAN by three with arrivals still stochastic, so dead years and late arrivals are priced in. A partner that actually arrives is still worth ~USD 100k of NP7 (the designed sweep, `run_partner_sweep.py`). **Faster onboarding now beats the extra signings**, and the results prose says so.

**The agent-network lever stays parked; do not bring it back without being asked** (client, 2026-09-04: agents and the marketing shift overlap, both push India, India saturates, and the model prices commission but not recruitment or management).

**Part 4 shape agreed (client, 2026-09-04, second pass).** Not a chosen set of three. Part 4 shows ALL eight measured levers, ranked and grouped: pure decisions (marketing 40/10/50 +833k; ladder trim 1.5x convex +315k), business development (three more partners +990k; halve onboarding +542k), customer programs framed as budget ceilings, not promises (card take-up +401k; ticket size +376k; standing instructions +361k; retention +344k). The combined "recommended configuration" for the charts = both decisions plus both BD levers, rail and everything else at base. Fee increases are excluded from ranking because the model has no demand response. The agent-network lever stays parked; do not bring it back without being asked.

**mc_config.py extended (client-approved, 2026-09-04):** trailing `key=value` levers `partners_extra=` (raises the PLAN schedule so arrivals stay stochastic around it) and `ramp=` (freezes partner_ramp_months as a managed target). Smoke-tested. The recommended run: `python scripts/mc_config.py rec 1.5 convex 0.30 0.40 0.10 0.50 2000 1.0 partners_extra=3 ramp=9`, then promote `mc_rec.json` to `mc_recommended.json`.

**Gold crash scenario redefined (client, 2026-09-04) and RERUN COMPLETE (2026-09-05).** `s1_gold_crash_30` is the shock PLUS s2's panic block verbatim; the client rejected a separate eighth scenario. The rerun landed as expected: s1 cum -608k right beside s2's -611k, the price fall adding ~USD 3k given the panic. The pure price channel is no longer a scenario; its measured result (~USD 5k across 2,000 paired paths, indistinguishable from nothing) lives in the code comment and in the results prose as the reason the reaction is included. The template's crash row and prose were rewritten to match.

**Recommended-configuration figures are now gated on `mc_recommended.json` (client-approved, 2026-09-04).** `charts.py`, `fill_results.py` and `revalidate.py` read that canonical name; `mc_config.py` still writes `mc_<tag>.json`, and promotion to `mc_recommended.json` is a deliberate copy once a set is agreed. The file does not exist today, so charts draw the plan alone and the `R_*` placeholders are undefined (a template referencing one fails loudly). The old cfg15 artifact (ladder 1.5x convex, rail 0.75, alloc 40/10/50) is archived as `_mc_cfg15.json`; do not promote it, the client rejected that set. Both branded PDFs are rebuilt without the recommended bars.

---

## 5b. The three client-agreed finalization items. ALL LANDED 2026-09-22

**1. Conditions map: per-cell Monte Carlos. ✅ DONE.** `run_conditions.py` rewired: 49 cells x 500 paths on shared seeds, CAC pinned per row, partner schedules fixed per column the way `run_partner_sweep.py` fixes them, cell value the median. The complaint this fixes is resolved: the plan cell now reads **-0.02m** (was +0.2 on a single run, against the base MC median of -0.45), so the map and Part 1 tell one story with the difference explained in the prose (the cell pins partner arrivals; the full simulation does not). **The frontier hardened: at base CAC the first profitable column is now 14 partners, not 11**, and 11 clears only at 0.82x CAC. The 1.66x row clears at nothing. Template, exec summary page and chart all requoted.

**2. All eight lever attributions re-measured on a recorded run. ✅ DONE.** See §5 for the values and the partner-lever halving.

**3. Tornado upgraded to paired Monte Carlos. ✅ DONE.** `run_tornado_mc.py`: 75 assumptions x 2 ends x 2,000 shared-seed paths, bar = median paired difference in NP7. Writes `tornado_mc.json` and replaces `q6_tornado` in `analysis.json`; `run_analysis.py` prefers `tornado_mc.json` when present so a rerun cannot regress the bars to single runs. New top bars: partner_adopt 1.50m, partner_aum_user 1.03m, facility_takeup 0.86m, ceiling_mult 0.80m, b2b_fee 0.71m. Run cost ~4.4h on 10 workers; the run itself lives in `outputs/_tornado_mc.log`.

## 6. Standing constraints from the client

- **Push directly to main.** No feature branches, no PRs.
- **Answer briefly and in structured sentences**, not prose slop.
- **Apply the unslop rules to all content:** no em dashes, no en dashes, no curly quotes, no AI vocabulary, short sentences, sentence-case headings.
- **Plain language in client documents.** No analogies, no metaphors, every term explained at first use. Zero sentences over 28 words.
- **No client attribution anywhere in the documents.** The Aggressive/Conservative bands are *our* Phase 4 research, not figures anyone supplied. Say so where it is load-bearing.
- **Never anchor persistency to Indian mutual fund SIP stoppage ratios.** They measure discontinued-over-newly-opened and exceed 100%.
- **Escalate before writing:** if no plausible configuration reaches profitability, bring it to the client before it goes into a document.

---

## 7. Things that will bite you

**The executive summary page is built from `meta_results.json`, not from the markdown.** It silently kept its original text through four rewrites. It is now covered by `check_docs.py`.

**`SIMULATION_RESULTS.md` is generated.** Edit `SIMULATION_RESULTS.template.md`. A placeholder with no value is a hard error by design.

**A single deterministic run carries about USD 0.7m of noise** in cumulative profit. Never compare single runs. The stress tests were rebuilt as paired Monte Carlos for exactly this reason.

**Resolution barely matters; path count does.** Full resolution and one-tenth resolution differ by 0.4% on a p90 once 2,000 paths are averaged. Spend compute on paths.

**PowerShell corrupts UTF-8 markdown.** Never find-and-replace repo markdown through it. Use Edit or Python with explicit encoding.

**Heredocs with `\n` inside f-strings break.** Several times. Use `print()` on separate lines or `%` formatting.

---

## 8. Headline numbers, as at 2026-09-04. Still current: the 2026-09-22 finalization pass did not move the base Monte Carlo

Plan as written, 2,000 paths, one agent per customer:

| | |
|---|--:|
| Money to raise, 9 runs in 10 | USD 4.82m |
| Runs earning it back by year 7 | 43% |
| Profit in year 7, typical run | USD 0.69m |
| Paying customers at month 84 | 88,594 |
| Retail customers needed to cover fixed costs | 146,289 |
| Partners needed instead | 2.5 |

**Per region:** UAE loses USD 10.48 per customer a year, the Gulf loses USD 9.20, India makes USD 14.92. India alone covers all fixed costs with 23,475 customers against the 48,240 the plan reaches there.

**Stress:** no partner ever signs gives −USD 4.29m and needs USD 7.09m. **Zero of 2,000 runs earn it back.** Gold falling 30% moves the typical run by USD 5,000, which is nothing.
