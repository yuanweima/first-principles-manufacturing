# First Principles Manufacturing

[![Website](https://img.shields.io/badge/Website-firstprinciplesmfg.com-10b981?style=flat-square)](https://www.firstprinciplesmfg.com)
[![Substack](https://img.shields.io/badge/Substack-Subscribe-FF6719?style=flat-square&logo=substack)](https://www.firstprinciplesmfg.com)
[![Publishing](https://img.shields.io/badge/Publishing-Tuesdays-blue?style=flat-square)](https://www.firstprinciplesmfg.com)
[![Status](https://img.shields.io/badge/Status-Read--Only%20Archive-lightgrey?style=flat-square)](https://www.firstprinciplesmfg.com)

First Principles Manufacturing, a newsletter by Yuanwei Ma at the intersection of AI, robotics, manufacturing and US–China. It examines what actually happens when artificial intelligence and robotics enter the physical factory floor—specifically across quality inspection, grinding, deburring, and welding—grounded in real numbers, physics, economics, and empirical evidence from production lines.

> 📬 **Read & Subscribe**: [firstprinciplesmfg.com](https://www.firstprinciplesmfg.com)  
> *New long-form essays published every Tuesday.*

---

## At a Glance

| Dimension | Details |
| :--- | :--- |
| **What is this?** | The open companion repository for [*First Principles Manufacturing*](https://www.firstprinciplesmfg.com), hosting canonical analytical frameworks, reproducible chart scripts, source datasets, and a public prediction ledger. |
| **Who is it for?** | Manufacturing engineers, robotics practitioners, industrial AI researchers, founders, and investors seeking empirical ground truth beyond lab demos. |
| **What's inside?** | • **10 Analytical Frameworks** ([`frameworks/`](frameworks/))<br>• **Public Prediction Ledger** ([`predictions/`](predictions/))<br>• **Reproducible Chart Scripts** ([`charts/`](charts/))<br>• **Source Datasets** ([`data/`](data/))<br>• **LLM Ingestion Endpoint** ([`llms.txt`](llms.txt)) |
| **Repository Status** | **Read-Only Archive** — Accompanying published newsletter essays. Pull requests and issues are not monitored. |

---

## Canonical Analytical Frameworks

The 10 living analytical frameworks developed across FPM essays:

| # | Framework | Core Thesis |
|---|:---|:---|
| 01 | [The Builder Cannot Be the Verifier](frameworks/builder-cannot-verify.md) | Execution and verification must reside on separate paths; humans occupy the verification side. |
| 02 | [The Agent-Loop Three Tests](frameworks/agent-loop-three-tests.md) | A physical step can enter an agent loop only if it is invocable, state-handoff capable, and independently verifiable. |
| 03 | [Engineering the Map](frameworks/engineering-the-map.md) | Plotting tasks by failure cost vs. verification cost; engineering gates to drag tasks into the automatable zone. |
| 04 | [Amortize vs. Defer](frameworks/amortize-vs-defer.md) | Computation tradeoffs between amortizing policy into parameters vs. test-time search and certified safety. |
| 05 | [Two Narratives](frameworks/two-narratives.md) | Generalist humanoid robotics searching for forgiving workcells vs. agent-wrapped industrial equipment stacks. |
| 06 | [Organization Shape & Coordination Technology](frameworks/org-shape-coordination.md) | Physical AI agents restructure coordination overhead rather than replacing muscular work directly. |
| 07 | [Batch Drift and Tool ECG](frameworks/batch-drift-ecg.md) | Burr morphology as a drifting distribution under tool wear; operator adjustments as an unrecorded ECG. |
| 08 | [Contact Task Control Loops](frameworks/contact-task-control-loops.md) | Three-tier hierarchy: kHz servo loop, 125–500 Hz motion loop, slow drift/task agent loop. |
| 09 | [Two Ledgers, One Price](frameworks/two-ledgers-frames.md) | Neoclassical models vs. political-economy frames explaining capacity overhang and price dynamics. |
| 10 | [Equipment Agent-Readiness](frameworks/agent-readiness.md) | Procurement priorities shifting from spec-sheet hardware metrics to programmatic API invocability. |

---

## Repository Navigation

- [`frameworks/`](frameworks/) — Markdown essays for all 10 analytical frameworks.
- [`predictions/`](predictions/) — Public prediction register ([`predictions/prediction-ledger.md`](predictions/prediction-ledger.md)), tracking 16 falsifiable forecasts with verifiable conditions.
- [`charts/`](charts/) — Python plotting scripts and [`charts/fpm_style.py`](charts/fpm_style.py) (hand-drawn Matplotlib visual identity).
- [`data/`](data/) — Source CSV datasets backing published empirical analyses.
- [`about.md`](about.md) — Comprehensive background on author Yuanwei Ma ($28M in deployed inspection platforms, patents, national standards), publication scope, and core philosophy.
- [`llms.txt`](llms.txt) — Machine-readable index formatted per [llmstxt.org](https://llmstxt.org/) specification for LLM retrieval and search indexing.

---

## Core Operating Principles

1. **Iron Man Suits, Not Lights-Out Factories**: The practical role of AI on the factory floor is augmenting and multiplying human capability—moving systematically from human-in-the-loop to human-on-the-loop, and finally toward guarded autonomy with rigorous verification gates.
2. **Submillimeter Reality**: While lab demos celebrate centimeter-level compliance, industrial production processes (such as deburring) demand ±0.3 mm repeatable accuracy in the presence of thermal drift, tool wear, and casting variance.
3. **Public Accountability**: Every falsifiable forecast enters an open ledger with explicit verification conditions; annual audits publish what held, what broke, and why.

---

## The Author

**Yuanwei Ma** is a factory AI builder and Chief Scientist at Changzhou Microintelligence, leading U.S. R&D in Novi, Michigan (Micro Intelligence Inc.). Nuclear engineering PhD in radiation measurement. Led flexible surface-defect inspection platforms deployed across Apple, Microsoft, Amazon, BYD ($28M commercial revenue); ~50 patents; co-authored two Chinese national AI standards; AAAI 2025 paper (3CAD dataset).

For detailed engineering track record, credentials, and worldview, see [`about.md`](about.md).

---

## Repository Status & Contributing

This repository is a **read-only companion archive** for published *First Principles Manufacturing* articles. Pull requests and issues are not actively monitored.

To discuss ideas, read the latest essays, or subscribe, visit [firstprinciplesmfg.com](https://www.firstprinciplesmfg.com).

---

## Copyright & License

- **Essays & Frameworks**: © Yuanwei Ma / First Principles Manufacturing. All rights reserved.
- **Scripts & Datasets**: Reproducible Python plotting code (`charts/`) and source datasets (`data/`) are open under the [MIT License](https://opensource.org/licenses/MIT).
