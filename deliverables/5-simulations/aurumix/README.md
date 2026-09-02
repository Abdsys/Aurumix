# Aurumix Simulation

Stage 1 population engine + Stage 2 full-book Monte Carlo + Stage 3 solver.
Spec: ../Aurumix_Simulation_Blueprint.md. Verification: ../Simulation_Verification.md.

## Run
    python scripts/extract_params.py            # refresh params from the workbook
    python scripts/verify_stage1.py             # 34 code-correctness checks
    python scripts/verify_stage2_equivalence.py # port vs calculated workbook, 36 series
    python scripts/run_mc.py 2000               # Monte Carlo -> outputs/mc_*.{csv,json}
    python scripts/run_analysis.py              # Q1-Q6 + stresses -> outputs/analysis.json

Reference of record: ../../4-revenue-modeling/tools/Aurumix_Revenue_Model_calculated.xlsx.
All seeds fixed; every figure reproducible.
