# Build scripts for the Zenith workstream workbooks

Python (openpyxl) generators that produced the three `Zenith_*_Models_and_WAVE_v1.xlsx` files
from the uploaded WAVE template. To regenerate: place
`abd10a23-Zenith_Business_Case_Template_by_Lever_1.xlsx` (the WAVE template) in this directory
and run `python3 build_sdlc.py`, `build_sales.py`, `build_servicing.py`.

- `framework.py` / `builders.py` / `builders2.py` / `common.py` — shared engine (styles, month
  grid, rate card, model-sheet layout, WAVE copy + linking, summary/cover).
- `build_*.py` — per-workstream initiative specs (assumptions, calc chains, milestones, run
  costs, WAVE driver blocks) and assembly.

Servicing seed values were extracted from `20260828_Servicing_S2sizing_vDraft5.xlsb`
(values-only via pyxlsb; tie-out targets embedded as comments in `build_servicing.py`).
