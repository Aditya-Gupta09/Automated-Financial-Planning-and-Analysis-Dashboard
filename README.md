# Automated-FP&A-Dashboard
# NVIDIA FP&A & Valuation Platform

## Overview

This repository contains the architectural foundation of a modular Financial Planning & Analysis (FP&A) system built around a deterministic 3-statement financial model using NVIDIA as a case study.

The long-term objective is to build a production-grade FP&A and valuation engine that:

- Ingests raw financial data
- Constructs canonical financial tables
- Executes a driver-based 3-statement financial model
- Computes key financial KPIs
- Supports scenario-based forecasting
- Generates executive-ready outputs

The system is currently under active development.

---

## Motivation

Most financial dashboards visualize historical outcomes.

This project focuses on modeling financial causality:

- Revenue drivers
- Margin structure
- Working capital mechanics
- Capital expenditure dynamics
- Cash flow reconciliation

Instead of building a static dashboard, this repository is structured as a modular financial engine with a thin presentation layer.

---

## Planned System Architecture

Raw Data (CSV / SQL / API)
↓
ETL Layer
(src/etl)
↓
Canonical Financial Tables
↓
Assumptions Layer
(config/)
↓
3-Statement Financial Engine
(src/modeling)
↓
KPI Engine
(src/kpi)
↓
Streamlit Orchestration Layer
(app/)
↓
Executive Outputs (PDF / PPTX)


### Separation of Concerns

**Frontend (app/)**  
- User inputs  
- Scenario controls  
- Visualization  
- Export triggers  

**Backend (src/)**  
- Data ingestion  
- Financial modeling  
- KPI computation  
- Validation & invariants  

---

## Current Status

- Repository structure established
- Architecture documented
- Core module scaffolding created
- Financial engine under implementation

This is an actively evolving project.

---

## Technology Stack

- Python
- Pandas
- Streamlit
- Pytest
- Modular backend architecture

---

## Roadmap

See `/docs/roadmap.md` for detailed development phases.

---

## Repository Structure

See `/docs/architecture.md` for detailed system design.

---

## License

This project is for educational and demonstration purposes.

