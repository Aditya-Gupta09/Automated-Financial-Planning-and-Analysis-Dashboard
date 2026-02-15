# System Architecture

## Design Philosophy

This system is designed using strict separation of concerns:

- UI Layer (Orchestration only)
- ETL Layer (Data normalization)
- Financial Engine (Core modeling logic)
- KPI Engine (Derived metrics)
- Configuration Layer (Assumptions)

The architecture prioritizes:

- Determinism
- Testability
- Modularity
- Scalability

---

## High-Level Architecture

[ Raw Data Sources ]
↓
[ ETL Pipeline ]
↓
[ Canonical Financial Tables ]
↓
[ Assumptions Config ]
↓
[ 3-Statement Engine ]
↓
[ KPI Engine ]
↓
[ Streamlit UI ]
↓
[ Executive Output Layer ]


---

## Backend Modules

### 1. ETL (`src/etl/`)
Responsible for:
- Loading raw financial exports
- Validating schema
- Cleaning & transforming data
- Producing canonical financial tables

### 2. Modeling (`src/modeling/`)
Contains:
- Deterministic 3-statement financial model
- Working capital mechanics
- Capex & depreciation logic
- Balance sheet reconciliation

### 3. KPI Engine (`src/kpi/`)
Computes:
- Gross margin
- EBITDA margin
- Free cash flow margin
- Working capital ratios

---

## Frontend Layer

The Streamlit layer:
- Accepts scenario inputs
- Displays financial statements
- Shows KPI dashboards
- Triggers export functionality

No financial logic lives in the UI layer.

---

## Testing Strategy

Invariant testing will validate:

- Balance Sheet balances
- Cash reconciliation matches
- Retained earnings roll forward correctly
- KPI calculations remain consistent

---

## Future Scalability

- SQL-based canonical tables
- Multi-company support
- API-based ingestion
- Scheduled batch runs
- Deployment to cloud infrastructure
