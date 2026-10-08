# About First Principles Manufacturing

First Principles Manufacturing, a newsletter by Yuanwei Ma at the intersection of AI, robotics, manufacturing and US–China. It looks at what actually happens when artificial intelligence and robotics meet the four workhorses of modern physical manufacturing: quality inspection, grinding, deburring, and welding.

Every essay starts from something concrete: a sensor measurement, an engineering tolerance, or a scene on a production line. It traces through the underlying physics, economics, or organizational coordination constraints, and concludes with actionable implications for practitioners and decision-makers.

---

## The Author

**Yuanwei Ma** works at the intersection of AI, robotics, manufacturing and US–China. 

He holds a PhD in nuclear engineering specializing in radiation measurement and protection, where the core discipline is extracting statistically verifiable signals from background noise in an auditable, reproducible manner. That exact mathematical and physical intuition translates directly into separating defect signatures from noisy industrial imaging in harsh manufacturing environments.

Since 2020, he has been building and deploying AI and robotics systems on factory floors. He serves as Chief Scientist at Changzhou Microintelligence and leads its U.S. R&D center in Novi, Michigan (Micro Intelligence Inc.).

Key engineering milestones include:
- **Production Systems**: Led the development of a flexible surface-defect inspection platform generating roughly $28M in commercial revenue, deployed in volume production lines at Microsoft, Apple, Amazon, BYD, JAC Motors, and China Mobile.
- **Intellectual Property**: Approximately 50 granted patents across machine vision, industrial optical inspection, and robotics.
- **National Standards**: Co-authored two national AI standards in China (GB/T 42755-2023, GB/T 43782-2024).
- **Academic Research**: Co-authored the AAAI 2025 paper introducing the 3CAD dataset for benchmark industrial anomaly detection.

Beyond the formal credentials, the publication is rooted in shop-floor realities: the 1 a.m. urgent customer calls, the plant manager's stare during line stoppages, and resolving finger-pointing loops between automation equipment vendors and algorithm teams.

Operating across both the United States and China provides a firsthand perspective on how identical technologies encounter vastly different supply chains, labor dynamics, and capital structures.

---

## Core Philosophy

- **Iron Man Suits, Not Lights-Out Factories**: The practical role of AI on the factory floor is augmenting and multiplying human capability—moving systematically from human-in-the-loop to human-on-the-loop, and finally toward guarded autonomy with rigorous verification gates at every transition.
- **The Submillimeter Gap**: While lab demos of embodied AI celebrate centimeter-level compliance, industrial production processes such as casting deburring demand ±0.3 mm repeatable accuracy in the presence of thermal drift, tool wear, and casting variance.
- **Independent Verification**: In safety-critical and high-throughput physical systems, the builder cannot serve as its own verifier. Execution and verification must remain architecturally separated.

---

## Analytical Frameworks

The publication maintains a living repository of named analytical frameworks, including:
- **The Builder Cannot Be the Verifier**: Execution and sign-off must reside on separate paths; humans occupy the verification side.
- **The Agent-Loop Three Tests**: A shop-floor process can enter an autonomous agent loop only if it is programmatically invocable, supports intermediate state handoff, and possesses an independent verification mechanism.
- **Engineering the Map**: Plotting manufacturing tasks along cost of failure versus cost of verification, and using engineering interventions (simulation, independent optical gates) to drag tasks into the automatable zone.
- **Amortize or Defer**: Analyzing computation tradeoffs in robot learning between amortizing intelligence into model parameters versus deferring computation to test-time search and certified safety envelopes.
- **Two Ledgers, One Price**: Deconstructing US–China industrial price dynamics through neoclassical and political-economy frameworks.

---

## Public Predictions & Cadence

Every falsifiable forecast made in the publication is registered in the public [Prediction Ledger](predictions/prediction-ledger.md) with specific verification conditions and timeframes. Each December, an annual audit is published reviewing which predictions held, which failed, and why.

- **Cadence**: New long-form analysis published every Tuesday.
- **Substack**: [https://firstprinciplesmfg.com](https://firstprinciplesmfg.com)
