# FPM Chart Scripts (`charts/`)

This directory is designated for reproducible plotting scripts that generate the charts, figures, and analytical maps published across *First Principles Manufacturing*.

---

## Purpose & Visualization Philosophy

Visualizations in FPM are treated as durable analytical assets rather than decorative illustrations. They fall into three primary categories:

1. **Empirical Data Charts**: Quantitative figures plotting verifiable numbers (venture capital volumes, trade figures, sensor frequencies, defect rates) backed by raw data in `data/`.
2. **Thesis Maps (论点图)**: Analytical diagrams mapping conceptual spaces (e.g., *Demo vs. Process Map*, *Automation vs. Variety*, *Amortize vs. Defer*).
3. **Control Architecture Diagrams**: Engineering schematics representing control loops, sensor-actuator latencies, and verification boundaries.

---

## Visual Standards & The Hand-Drawn Theme

- **Style Engine (`fpm_style.py`)**: All FPM figures utilize a unified custom Matplotlib theme (`fpm_style.py`) providing a hand-drawn, tactile visual identity that matches the publication's editorial tone.
- **Honest Plotting Rules**:
  - Qualitative thesis maps strictly feature bare axes (no fabricated numeric ticks for subjective assessments).
  - Every plotted coordinate must correspond to a documented source citation or an explicitly labeled qualitative engineering assessment.
  - Figure notes transparently distinguish between measured empirical data and author predictions.

---

## Contents (populated 2026-10-08, reviewed)

- `fpm_style.py` — shared hand-drawn Matplotlib theme (required dependency for all scripts below)
- `make_033_charts.py` — 033《Is Manufacturing at Dusk or Dawn?》(Physical AI 融资柱状图)
- `make_036_charts.py` — 036《Two Ledgers, One Price》(顺差 vs 产能利用率、光伏降价线)
- `make_037_charts.py` — 037《Engineering the Map》(T01 任务地图)
- `make_039_charts.py` — 039《Amortize or Defer》(T05/T06 指数轴)
- `make_040_charts.py` — 040《The Millennium Problem Was the Easy Part》(时间线泳道图等)
- `make_cognex_chart.py` — Cognex × RealSense 简评(视觉分层图)
- `make_mhs_chart.py` — MHS 简评(三层控制环频率阶梯图)
- `make_t04_charts.py` — 034《The Shape of Organizations》(T04 前沿线图)

All scripts generate charts from already-published articles only. Run with `python3 <script>.py` (requires matplotlib, numpy; `fpm_style.py` on path).
