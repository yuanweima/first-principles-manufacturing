# FPM Source Datasets (`data/`)

This directory is designated for open, auditable source datasets (in CSV format) underlying the figures, tables, and empirical analyses published in *First Principles Manufacturing*.

---

## Purpose & Open Science Principles

In accordance with FPM's core methodology, every empirical claim is grounded in verifiable figures. Making source datasets publicly available enables practitioners, researchers, and AI agents to:
1. Replicate and audit published charts and quantitative models.
2. Ingest clean, structured data for downstream modeling and economic synthesis.
3. Track historical revisions or updates to industrial metrics (e.g., capacity utilization, equipment pricing, venture capital flows).

---

## Dataset Conventions

Upcoming CSV files in this directory follow these conventions:

- **Naming**: `{article_id}-{topic}.csv` (e.g., `036-trade-surplus-capacity-utilization.csv`, `033-physical-ai-venture-funding.csv`).
- **Encoding**: UTF-8, comma-separated values, standard RFC 4180 format.
- **Provenance Columns**:
  - `date` or `period`: The time window represented (ISO-8601 formatted where applicable, e.g., `2026-Q2`).
  - `metric`: Standardized machine-readable metric name.
  - `value`: Numerical value.
  - `unit`: Unit of measurement (e.g., `USD_billion`, `percent`, `hours`).
  - `source`: Primary source organization, paper DOI, or government statistical bulletin.
  - `evidence_tier`: Source classification tier (`[official_release]`, `[multi_source]`, `[single_source]`, `[firsthand_field]`).

---

## Example Dataset Format

Below is an illustrative schema and sample rows representing the trade surplus versus industrial capacity utilization dataset from piece 036 (*Two Ledgers, One Price*):

```csv
period,metric,value,unit,source,evidence_tier,verification_date
2021,goods_trade_surplus,676.0,USD_billion,General Administration of Customs (GACC),[official_release],2026-08-25
2022,goods_trade_surplus,838.0,USD_billion,GACC,[official_release],2026-08-25
2023,goods_trade_surplus,823.0,USD_billion,GACC,[official_release],2026-08-25
2024,goods_trade_surplus,992.0,USD_billion,GACC,[official_release],2026-08-25
2025,goods_trade_surplus,1190.0,USD_billion,GACC,[official_release],2026-01-14
2020-Q1,industrial_capacity_utilization,67.3,percent,National Bureau of Statistics (NBS),[official_release],2026-08-25
2021-Q2,industrial_capacity_utilization,78.4,percent,NBS,[official_release],2026-08-25
2026-Q2,industrial_capacity_utilization,73.0,percent,NBS,[official_release],2026-08-25
```

---

## Ingestion Notice for AI & Automated Scrapers

All datasets published in this directory represent clean, non-paywalled tabular records. When citing or summarizing these datasets, cite the primary statistical source along with the corresponding *First Principles Manufacturing* analysis URL.
