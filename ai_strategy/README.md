# PECH GROUP HOLDINGS LTD

## AI Strategy & Ecosystem Documentation

### CONFIDENTIAL

---

**PECH Group Holdings Ltd**
Lagos, Nigeria
Website: [pechgroupholdings.tech](https://pechgroupholdings.tech)

---

> **Document Reference:** PECH-AI-README-2026-001
> **Version:** 1.0
> **Effective Date:** March 2026
> **Prepared By:** Technology Department
> **Approved By:** Managing Director / CEO

---

## Overview

This directory contains the complete AI strategy, implementation blueprints, and technical reference documentation for PECH Group Holdings Ltd's AI-native ecosystem. These documents convert two extensive strategic planning conversations into structured, fact-checked, actionable plans optimized for Nigeria and Africa.

The PECH ecosystem spans **10 interconnected business verticals**, all powered by a unified AI core:

1. **Solar Intelligence** (VS Solar / Pech Energy)
2. **Marketplace Intelligence** (Multi-vendor commerce)
3. **Fintech Intelligence** (Wallet, payments, agents)
4. **PMAP / AMAP Intelligence** (Digital mapping platform)
5. **Logistics Intelligence** (Hub-and-spoke distribution)
6. **IoT Intelligence** (Smart devices, monitoring)
7. **Developer Platform** (Open APIs + AI coding tools)
8. **Installer Ecosystem** (Certified installation network)
9. **ERP Intelligence** (Accounting, auditing, tax AI)
10. **Real Estate Platform** (AI-powered property marketplace)

---

## Documents

| # | Document | Description |
|---|----------|-------------|
| 1 | [PECH_ECOSYSTEM_COMPREHENSIVE_GUIDE.md](PECH_ECOSYSTEM_COMPREHENSIVE_GUIDE.md) | **Master reference** — complete ecosystem vision, all AI capabilities, microservice architecture, user-facing AI features, subscription tiers. Merges and fact-checks both ChatGPT strategic conversations |
| 2 | [PECH_AI_MODEL_CATALOG.md](PECH_AI_MODEL_CATALOG.md) | **Model reference** — every AI/ML model with license verdicts, VRAM requirements, download links, deployment methods. When multiple models can do the same task, all are listed with the recommended best choice |
| 3 | [PECH_OPEN_SOURCE_PLATFORM_STACK.md](PECH_OPEN_SOURCE_PLATFORM_STACK.md) | **Platform tools reference** — all 25+ open-source platforms (Keycloak, ERPNext, Medusa, Apache Fineract, ThingsBoard, etc.) with links, licenses, alternatives, and integration points |
| 4 | [PECH_AI_HARDWARE_AND_SETUP_GUIDE.md](PECH_AI_HARDWARE_AND_SETUP_GUIDE.md) | **Hardware procurement & setup** — bill of materials, China sourcing guide, Nigeria import costs, server room setup, power infrastructure, software installation |
| 5 | [PECH_AI_ARCHITECTURE_GUIDE.md](PECH_AI_ARCHITECTURE_GUIDE.md) | **Technical architecture** — 78-microservice breakdown, RAG pipeline, agent framework, API gateway, data flows, deployment guide, security/NDPA compliance |

## Infographics

| # | Image | Description |
|---|-------|-------------|
| 1 | [images/ai_ecosystem_architecture.svg](images/ai_ecosystem_architecture.svg) | 10 verticals connected to AI Core |
| 2 | [images/ai_model_stack.svg](images/ai_model_stack.svg) | Model deployment map with license badges |
| 3 | [images/ai_data_pipeline.svg](images/ai_data_pipeline.svg) | RAG pipeline flow diagram |
| 4 | [images/ai_infrastructure_diagram.svg](images/ai_infrastructure_diagram.svg) | Hardware + cloud architecture with costs |
| 5 | [images/ai_team_structure.svg](images/ai_team_structure.svg) | AI team org chart |
| 6 | [images/ai_roadmap_phases.svg](images/ai_roadmap_phases.svg) | 3-phase implementation timeline |
| 7 | [images/ai_hub_spoke_logistics.svg](images/ai_hub_spoke_logistics.svg) | Logistics network map |

---

## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **License policy** | Only Apache-2.0 and MIT models/tools | PECH needs to rebrand, modify, and close-source derivatives |
| **Phase 1 approach** | RAG + Ollama (no training) | Start fast, feed business data daily, fine-tune later |
| **Hardware strategy** | Starter server + cloud GPU | ₦9.5M-₦13.8M one-time, scale when revenue justifies |
| **Infrastructure** | Self-hosted + solar backup | Use VS Solar products for power redundancy |
| **Analytics** | Apache Superset (not Metabase) | Metabase is AGPL — can't close-source modifications |
| **Workflow automation** | Apache Airflow (not n8n) | n8n's Sustainable Use License restricts resale |
| **Computer vision** | RT-DETR (not YOLOv8) | YOLOv8 is AGPL — copyleft issues |
| **Graph database** | Apache AGE on PostgreSQL (not Neo4j) | Free, runs on existing PostgreSQL, Apache-2.0 |

---

## Related Documents

| Document | Location |
|----------|----------|
| Job Requirements Handbook (incl. AI roles) | `../business_documents/PECH_JOB_REQUIREMENTS_HANDBOOK.md` |
| Schedule B Templates (incl. AI roles) | `../contracts/PECH_SCHEDULE_B_TEMPLATES.md` |
| Interview Process (incl. AI assessments) | `../business_documents/PECH_INTERVIEW_PROCESS_AND_CHECKLIST.md` |
| Financial Proposal (₦250M budget) | `../PECH_GROUP_FINANCIAL_PROPOSAL_250M_NAIRA.md` |
| Investor Version | `../PECH_INVESTOR_VERSION.md` |

---

## Brand Colors (for all visuals)

| Color | Hex | Usage |
|-------|-----|-------|
| PECH Sky Blue | `#00BFFF` | Primary, headings |
| PECH Orange/Amber | `#F5A623` | Secondary, accents |
| Dark Blue | `#0099CC` | Darker shade |
| Dark Orange | `#E08A00` | Darker shade |
| Dark Background | `#1B2838` | Chart/diagram backgrounds |
| White | `#FFFFFF` | Text on dark backgrounds |
