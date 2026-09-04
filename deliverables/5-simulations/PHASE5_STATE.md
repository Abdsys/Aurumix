# Phase 5 — Simulations: state and context

> **Read this before touching anything in `deliverables/5-simulations/`.** It is the Phase 5 equivalent of `handoff.md` §9. Detail lives in the code comments, which are written to be read.
>
> **Last updated:** 2026-09-04.

---

## 0. Where things stand

The simulation is **built, verified and running**. Both client documents exist and are current. The work in flight is a restructure of the results document and a rebuild of its recommendations.

| Thing | State |
|---|---|
| The engine (`aurumix/src/twin.py`) | ✅ Complete, verified |
| Base Monte Carlo, 2,000 paths, full resolution | ✅ Done |
| Stress Monte Carlo, 2,000 paths per scenario | ⚠ Complete for base + s1 to s7 (2026-09-04 21:12). s8 added since; full paired rerun pending, client has more changes coming |
| `SIMULATION_SETUP.md` | ✅ Current, 38 branded pages |
| `SIMULATION_RESULTS.md` | 🔄 Restructured today; Part 4 is a placeholder pending new recommendations |
| Recommendations | ⛔ **Being rebuilt.** The published three are weak (see §5) |

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
| `aurumix/scripts/run_analysis.py` | thresholds, tornado, ladder, concentration |
| `aurumix/scripts/run_conditions.py` | the conditions map and per-region economics |
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
python scripts/run_conditions.py
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

## 5. What is in flight

**The results document was restructured on 2026-09-04** to the client's requested flow: base case results first, then why, then stress, then recommendations, then what to learn. Parts 1 to 3 and 5 to 6 are done.

**Part 4 is a placeholder.** The published recommendations (trim the ladder, push standing instructions, reallocate marketing) were ranked by an earlier version of the model and are weak. Measured against the current model, by cumulative profit created over seven years:

| Lever | Profit created |
|---|--:|
| Three more partners | +990k |
| **Double or triple the India agent network** | +986k to +1.41m |
| Move marketing to India 40/10/50 | +833k |
| Halve partner onboarding time | +542k |
| Raise card take-up | +401k |
| Bigger monthly savings | +376k |
| Standing instructions | +361k |
| Better retention | +344k |
| **Trim the loyalty ladder** | **+315k, second from last** |

**Agents and the marketing shift overlap**: both push India, and India saturates. Doing both at full strength is worse than doing one properly.

**Client instruction, 2026-09-04:** cap the agent recommendation somewhere conservative rather than tripling. The model prices agent commission but not recruitment, training or management.

**Next step:** agree the recommendation set, then run `mc_config.py` for it at 2,000 paths and full resolution, then write Part 4.

**Recommendations are on hold (client, 2026-09-04).** The agent-network lever is parked entirely; do not bring it back without being asked. The client is reading the base and stress results first.

**Gold crash scenario redefined (client, 2026-09-04).** `s1_gold_crash_30` is now the shock PLUS s2's panic block verbatim; the client rejected a separate eighth scenario. The pure price channel is no longer a scenario; its measured result (~USD 5k across 2,000 paired paths, indistinguishable from nothing) lives in the code comment and should survive in the results prose as the reason the reaction is included. **Not yet run**: `stress_mc.json`'s s1 row still holds the old pure-shock definition, so the results document's crash row and its "gold does nothing" prose are stale the moment the rerun lands; expect s1 to land near s2. The client expects more model changes before the rerun. When they settle: rerun the full paired set, rewrite the results template crash prose, fill, check_docs, rebuild both PDFs.

**Recommended-configuration figures are now gated on `mc_recommended.json` (client-approved, 2026-09-04).** `charts.py`, `fill_results.py` and `revalidate.py` read that canonical name; `mc_config.py` still writes `mc_<tag>.json`, and promotion to `mc_recommended.json` is a deliberate copy once a set is agreed. The file does not exist today, so charts draw the plan alone and the `R_*` placeholders are undefined (a template referencing one fails loudly). The old cfg15 artifact (ladder 1.5x convex, rail 0.75, alloc 40/10/50) is archived as `_mc_cfg15.json`; do not promote it, the client rejected that set. Both branded PDFs are rebuilt without the recommended bars.

---

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

## 8. Headline numbers, as at 2026-09-04

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
