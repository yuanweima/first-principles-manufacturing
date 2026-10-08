# First Principles Manufacturing

First Principles Manufacturing, a newsletter by Yuanwei Ma at the intersection of AI, robotics, manufacturing and US–China. It examines what actually happens when artificial intelligence and robotics enter the physical factory floor—specifically across quality inspection, grinding, deburring, and welding—grounded in real numbers, physics, economics, and empirical evidence from production lines.

## About This Repository

This is the public open repository for **First Principles Manufacturing (FPM)**. It hosts canonical analytical frameworks, reproducible chart scripts, underlying source datasets, and a public falsifiable prediction ledger.

- **Publication**: [First Principles Manufacturing on Substack](https://firstprinciplesmfg.com)
- **Author**: Yuanwei Ma (Nuclear engineering PhD in radiation measurement turned factory AI builder; Chief Scientist at Changzhou Microintelligence; head of U.S. R&D in Novi, Michigan)
- **Publishing Schedule**: New essays published on Tuesdays
- **Copyright & License**: All content © Yuanwei Ma / First Principles Manufacturing. Reproducible scripts and open datasets are licensed under the MIT License unless specified otherwise.

## Repository Navigation

- [`about.md`](about.md) — Comprehensive background on the author, engineering track record ($28M in inspection systems, national standards, patents), publication scope, and core philosophy.
- [`frameworks/`](frameworks/) — The 10 core analytical frameworks developed in FPM (e.g., *The Builder Cannot Be the Verifier*, *The Agent-Loop Three Tests*, *Amortize vs. Defer*, *Engineering the Map*).
- [`predictions/`](predictions/) — The public prediction ledger ([`predictions/prediction-ledger.md`](predictions/prediction-ledger.md)), registering falsifiable predictions with precise verification conditions and reconciliation dates ("FPM Prediction Ledger 2026").
- [`data/`](data/) — Source datasets (CSV) behind published charts and empirical arguments.
- [`charts/`](charts/) — Python plotting scripts and style definitions generating published charts.
- [`llms.txt`](llms.txt) — Machine-readable index formatted per [llmstxt.org](https://llmstxt.org/) specification for LLM retrieval and search engine indexing.

## Core Coordinates

1. **Iron Man Suits, Not Lights-Out Factories**: AI on the factory floor amplifies front-line practitioners through human-in-the-loop, human-on-the-loop, and gated autonomy.
2. **Submillimeter Reality**: Lab demos tolerate centimeter drift; production processes like deburring demand ±0.3 mm precision under tool wear and batch drift.
3. **Public Accountability**: Every falsifiable claim goes into an open ledger with test conditions; annual reckonings publish what held and what broke.
