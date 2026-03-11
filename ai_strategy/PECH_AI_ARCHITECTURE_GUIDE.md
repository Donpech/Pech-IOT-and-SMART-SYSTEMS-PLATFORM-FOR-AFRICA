<div align="center">
<div style="background:linear-gradient(135deg,#1B2838 0%,#0d1b2a 50%,#162435 100%);border-radius:16px;padding:0;overflow:hidden;border:2px solid #0099CC;box-shadow:0 8px 32px rgba(0,153,204,0.15),0 4px 16px rgba(245,166,35,0.1);">
<div style="height:5px;background:linear-gradient(90deg,#0099CC,#00BFFF 20%,#F5A623 40%,#E08A00 60%,#0099CC 80%,#00BFFF);"></div>
<div style="height:2px;background:linear-gradient(90deg,#F5A623,#0099CC 50%,#F5A623);"></div>
<div style="padding:28px 40px 20px;">
<div style="display:inline-block;background:linear-gradient(135deg,#0099CC,#00BFFF);border-radius:12px;padding:12px 16px;margin-bottom:10px;box-shadow:0 4px 16px rgba(0,153,204,0.25);"><span style="font-size:2em;">🏗️</span></div>
<h1 style="margin:8px 0 0;font-size:1.9em;background:linear-gradient(90deg,#0099CC,#F5A623);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">PECH GROUP HOLDINGS LTD</h1>
<h2 style="margin:6px 0 12px;font-size:1.1em;color:#0099CC;font-weight:500;">AI Architecture Guide — Technical Blueprint</h2>
<p>
<img src="https://img.shields.io/badge/CONFIDENTIAL-🔒-E08A00?style=for-the-badge&labelColor=1B2838" alt="Confidential" />
<img src="https://img.shields.io/badge/78-Microservices-0099CC?style=for-the-badge&labelColor=1B2838" alt="78 Microservices" />
<img src="https://img.shields.io/badge/12-Domains-F5A623?style=for-the-badge&labelColor=1B2838" alt="12 Domains" />
</p>
<p><img src="https://img.shields.io/badge/Lagos%2C%20Nigeria-pechgroupholdings.tech-0099CC?style=flat-square" alt="Location" /></p>
<div style="height:2px;background:linear-gradient(90deg,#0099CC,#F5A623 50%,#0099CC);margin:12px -40px 0;"></div>
<div style="height:4px;background:linear-gradient(90deg,#F5A623,#E08A00 25%,#00BFFF 50%,#0099CC 75%,#F5A623);margin:0 -40px -20px;"></div>
</div>
</div>
</div>

---

> **Document Reference:** PECH-AI-ARCH-2026-001
> **Version:** 1.0
> **Effective Date:** March 2026
> **Prepared By:** Technology Department
> **Approved By:** Managing Director / CEO

---

## TABLE OF CONTENTS

1. [Architecture Overview](#1-architecture-overview)
2. [AI Core Design](#2-ai-core-design)
3. [RAG Pipeline Architecture](#3-rag-pipeline-architecture)
4. [78-Microservice Architecture](#4-78-microservice-architecture)
5. [API Gateway Design (Apache APISIX)](#5-api-gateway-design)
6. [AI Agent Framework (LangGraph)](#6-ai-agent-framework)
7. [Data Flow Per Vertical](#7-data-flow-per-vertical)
8. [Event Streaming Architecture](#8-event-streaming-architecture)
9. [User-Facing AI Features](#9-user-facing-ai-features)
10. [Accounting, Auditing & Tax AI](#10-accounting-auditing-tax-ai)
11. [HR & Recruitment AI](#11-hr-recruitment-ai)
12. [Security & NDPA Compliance](#12-security-ndpa-compliance)
13. [Deployment Architecture](#13-deployment-architecture)
14. [Nigeria-Specific Considerations](#14-nigeria-specific-considerations)
15. [AI Team Structure](#15-ai-team-structure)

---

## 1. ARCHITECTURE OVERVIEW

### System Layers

```
┌──────────────────────────────────────────────────────────────┐
│ LAYER 5: USER INTERFACES                                      │
│ Web Apps │ Mobile Apps │ WhatsApp Bot │ API Consumers │ IoT    │
├──────────────────────────────────────────────────────────────┤
│ LAYER 4: API GATEWAY (Apache APISIX)                          │
│ Authentication │ Rate Limiting │ Load Balancing │ Routing      │
├──────────────────────────────────────────────────────────────┤
│ LAYER 3: BUSINESS MICROSERVICES (78 services)                 │
│ Identity │ Commerce │ Solar │ Fintech │ Logistics │ IoT │ ...  │
├──────────────────────────────────────────────────────────────┤
│ LAYER 2: AI CORE                                              │
│ LLM Serving │ RAG │ Vision │ Speech │ ML │ Embeddings │ Agents │
├──────────────────────────────────────────────────────────────┤
│ LAYER 1: DATA & INFRASTRUCTURE                                │
│ PostgreSQL │ Qdrant │ Redis │ NATS/Kafka │ Blob Storage        │
└──────────────────────────────────────────────────────────────┘
```

### Design Principles

1. **AI-native** — AI is not a bolt-on; every service talks to the AI Core
2. **Self-hosted first** — all models and data on PECH infrastructure
3. **Cloud burst** — overflow to cloud GPU when local capacity exhausted
4. **API-first** — all services expose REST/gRPC APIs via APISIX
5. **Event-driven** — services communicate via NATS/Kafka, not direct calls
6. **Multi-tenant** — each vertical's users are isolated (Keycloak realms)

---

## 2. AI CORE DESIGN

The AI Core is the central intelligence layer. All business services call it via internal APIs.

### AI Core Components

```
┌──────────────────────────────────────────────┐
│                  AI CORE                      │
│                                               │
│  ┌─────────────┐  ┌─────────────────────┐    │
│  │ Model Router │──│ Ollama / vLLM        │   │
│  │ (APISIX)    │  │ (LLM Serving)        │   │
│  └──────┬──────┘  └─────────────────────┘    │
│         │                                     │
│  ┌──────▼──────┐  ┌─────────────────────┐    │
│  │ RAG Engine  │──│ Qdrant (Vectors)     │   │
│  │ (LangChain) │  │ + Embeddings         │   │
│  └─────────────┘  └─────────────────────┘    │
│                                               │
│  ┌─────────────┐  ┌─────────────────────┐    │
│  │ Agent System │  │ Specialized Models   │   │
│  │ (LangGraph) │  │ STT │ TTS │ OCR │ CV │   │
│  └─────────────┘  └─────────────────────┘    │
│                                               │
│  ┌─────────────────────────────────────────┐  │
│  │ ML Pipeline (XGBoost, Prophet, LightFM) │  │
│  └─────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```

### Model Serving Architecture

#### Phase 1: Ollama (Simple)

```
Client → APISIX → Ollama API (port 11434)
                    ├── qwen2.5:7b (loaded)
                    ├── qwen2.5-coder:7b (loaded on demand)
                    └── nomic-embed-text (loaded)
```

- **Pros:** Single binary, easy model management, pull & run
- **Cons:** No request batching, lower throughput, single-queue
- **Capacity:** ~5-10 concurrent users

#### Phase 2: vLLM (Production)

```
Client → APISIX → Load Balancer
                    ├── vLLM Instance 1 (Qwen2.5-14B, GPU 0)
                    ├── vLLM Instance 2 (Qwen2.5-Coder-14B, GPU 0)
                    └── vLLM Instance 3 (Qwen2.5-32B, GPU 1)
```

- **Pros:** Continuous batching, PagedAttention, OpenAI-compatible API
- **Cons:** More complex setup
- **Capacity:** ~50-100 concurrent users per GPU

### Model Routing Logic

APISIX routes requests to the appropriate model based on the request type:

| Request Type | Model | Priority |
|-------------|-------|----------|
| General chat | Qwen2.5-7B/14B | Default |
| Code generation | Qwen2.5-Coder-7B/14B | Detect code context |
| Complex reasoning | Qwen2.5-32B | Premium tier or flagged queries |
| Image analysis | Qwen2.5-VL-7B | Image attached |
| Voice input | Faster-Whisper → LLM | Audio attached |
| Embeddings | all-MiniLM / Nomic | Internal RAG calls |

---

## 3. RAG PIPELINE ARCHITECTURE

RAG (Retrieval-Augmented Generation) is how PECH's AI answers questions using business data without fine-tuning.

### Pipeline Flow

```
┌─────────────────────────────────────────────────────┐
│ DATA INGESTION (Apache Airflow — scheduled daily)    │
│                                                      │
│  Sources:                                            │
│  ├── Product catalog (Medusa) ──────┐                │
│  ├── Support tickets (Chatwoot) ────┤                │
│  ├── Solar manuals (PDF/docs) ──────┤                │
│  ├── Financial data (ERPNext) ──────┤                │
│  ├── IoT device docs (ThingsBoard) ─┤                │
│  ├── Knowledge base (Strapi) ───────┤                │
│  └── HR policies (internal docs) ───┘                │
│                                      │                │
│                               ┌──────▼──────┐        │
│                               │ Chunking    │        │
│                               │ (LangChain) │        │
│                               │ 512 tokens  │        │
│                               └──────┬──────┘        │
│                                      │                │
│                               ┌──────▼──────┐        │
│                               │ Embedding   │        │
│                               │ (MiniLM/    │        │
│                               │  Nomic)     │        │
│                               └──────┬──────┘        │
│                                      │                │
│                               ┌──────▼──────┐        │
│                               │ Qdrant      │        │
│                               │ (Store +    │        │
│                               │  Metadata)  │        │
│                               └─────────────┘        │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ QUERY TIME (real-time, <2 seconds)                   │
│                                                      │
│  User Question                                       │
│       │                                              │
│  ┌────▼────┐                                         │
│  │ Embed   │ ← Same embedding model                  │
│  │ Query   │                                         │
│  └────┬────┘                                         │
│       │                                              │
│  ┌────▼────┐                                         │
│  │ Qdrant  │ ← Top-5 nearest neighbors               │
│  │ Search  │   + metadata filtering (by vertical)     │
│  └────┬────┘                                         │
│       │                                              │
│  ┌────▼────────────────────────┐                     │
│  │ Prompt: System + Context    │                     │
│  │  + Retrieved Chunks + Query │                     │
│  └────┬────────────────────────┘                     │
│       │                                              │
│  ┌────▼────┐                                         │
│  │ LLM     │ ← Qwen2.5 generates answer              │
│  │ (Qwen)  │   grounded in retrieved context          │
│  └────┬────┘                                         │
│       │                                              │
│  ┌────▼────┐                                         │
│  │ Response│ ← With source citations                  │
│  └─────────┘                                         │
└─────────────────────────────────────────────────────┘
```

### RAG Configuration

| Parameter | Value | Why |
|-----------|-------|-----|
| Chunk size | 512 tokens | Balance between context and precision |
| Chunk overlap | 50 tokens | Avoid losing context at boundaries |
| Top-K retrieval | 5 | More context = better answers, but slower |
| Embedding model | all-MiniLM-L6-v2 (Phase 1), Nomic-Embed (Phase 2) | Fast, small, good quality |
| Vector dimensions | 384 (Phase 1), 768 (Phase 2) | Match embedding model output |
| Distance metric | Cosine similarity | Standard for text embeddings |
| Metadata filters | vertical, document_type, date_range | Scope retrieval to relevant data |

---

## 4. 78-MICROSERVICE ARCHITECTURE

Services organized by domain. Each service is a Docker container with its own database schema in PostgreSQL.

### Domain 1: Identity & Access (3 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 1 | auth-service | Keycloak | SSO, OAuth2, OIDC, social login |
| 2 | user-profile-service | Node.js | User profiles, preferences, KYC |
| 3 | rbac-service | Node.js | Role-based access control, permissions |

### Domain 2: Core User Platform (6 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 4 | notification-service | Node.js | Email, SMS, push, WhatsApp notifications |
| 5 | search-service | Python | Unified search across all verticals |
| 6 | file-service | Node.js | File upload, storage, CDN |
| 7 | billing-service | Node.js | Subscription billing, invoicing |
| 8 | analytics-service | Python | User analytics, event tracking |
| 9 | feedback-service | Node.js | Reviews, ratings, NPS |

### Domain 3: Marketplace & Commerce (10 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 10 | product-catalog-service | Medusa | Product listings, categories, attributes |
| 11 | vendor-service | Node.js | Vendor onboarding, verification, management |
| 12 | order-service | Medusa | Order lifecycle, tracking |
| 13 | cart-service | Medusa | Shopping cart, wishlist |
| 14 | payment-service | Node.js | Paystack/Flutterwave integration |
| 15 | pricing-service | Python | Dynamic pricing, discounts (AI-powered) |
| 16 | shipping-service | Node.js | Shipping rates, tracking integration |
| 17 | review-service | Node.js | Product reviews, seller ratings |
| 18 | recommendation-service | Python | LightFM product recommendations |
| 19 | image-service | Python | Background removal (rembg), enhancement |

### Domain 4: Solar & Energy (8 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 20 | solar-product-service | Node.js | Solar panels, inverters, batteries catalog |
| 21 | solar-calculator-service | Python | System sizing, ROI calculator |
| 22 | installer-service | Node.js | Installer marketplace, certification |
| 23 | installation-service | Node.js | Job scheduling, tracking, completion |
| 24 | warranty-service | Node.js | Warranty registration, claims |
| 25 | energy-monitor-service | Python | ThingsBoard integration, energy analytics |
| 26 | maintenance-service | Python | Predictive maintenance (AI-powered) |
| 27 | solar-inspection-service | Python | Panel defect detection (RT-DETR) |

### Domain 5: Fintech & Payments (8 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 28 | wallet-service | Fineract | Digital wallet, balance, transfers |
| 29 | agent-banking-service | Fineract | Cash-in/cash-out agent network |
| 30 | loan-service | Fineract | Micro-loans for solar equipment |
| 31 | savings-service | Fineract | Savings accounts, interest |
| 32 | bill-payment-service | Node.js | Utility bills, airtime, cable |
| 33 | kyc-service | Python | KYC verification (OCR + face match) |
| 34 | fraud-detection-service | Python | XGBoost + Isolation Forest |
| 35 | transaction-ledger-service | Fineract | Transaction history, statements |

### Domain 6: Logistics & Delivery (7 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 36 | route-optimization-service | Python/OSRM | Delivery route planning |
| 37 | fleet-service | Node.js | Vehicle management, GPS tracking |
| 38 | dispatch-service | Node.js | Order-to-driver assignment |
| 39 | tracking-service | Node.js | Real-time delivery tracking |
| 40 | hub-service | Node.js | Hub/warehouse management |
| 41 | last-mile-service | Node.js | Last-mile delivery management |
| 42 | delivery-pricing-service | Python | Delivery cost calculation |

### Domain 7: Real Estate (5 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 43 | property-listing-service | Node.js | Property listings, search |
| 44 | property-valuation-service | Python | AI property valuation |
| 45 | virtual-tour-service | Node.js | 360° tours, image galleries |
| 46 | agent-matching-service | Python | LightFM agent-client matching |
| 47 | rental-management-service | Node.js | Lease management, payments |

### Domain 8: Procurement & Tenders (5 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 48 | tender-service | Python | OpenProcurement integration |
| 49 | bid-management-service | Node.js | Bid submission, evaluation |
| 50 | supplier-service | Node.js | Supplier registry, verification |
| 51 | contract-service | Node.js | Contract management, milestones |
| 52 | procurement-analytics-service | Python | Spend analysis, savings |

### Domain 9: IoT & Monitoring (5 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 53 | device-management-service | ThingsBoard | Device registration, provisioning |
| 54 | telemetry-service | ThingsBoard | Real-time data collection |
| 55 | alert-service | Python | Rule-based and AI-powered alerts |
| 56 | dashboard-service | ThingsBoard | Customer-facing IoT dashboards |
| 57 | firmware-update-service | Node.js | OTA firmware updates |

### Domain 10: Customer Support (5 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 58 | chatbot-service | Python | AI chatbot (Qwen2.5 + RAG) |
| 59 | ticket-service | Chatwoot | Support ticket management |
| 60 | knowledge-base-service | Python | RAG-powered knowledge base |
| 61 | sentiment-service | Python | DistilBERT sentiment analysis |
| 62 | escalation-service | Node.js | Auto-escalation rules |

### Domain 11: AI & Data Platform (10 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 63 | llm-gateway-service | Python | Route to appropriate LLM |
| 64 | embedding-service | Python | Generate embeddings for RAG |
| 65 | rag-service | Python | RAG pipeline orchestration |
| 66 | stt-service | Python | Speech-to-text (Faster-Whisper) |
| 67 | tts-service | Python | Text-to-speech (Piper) |
| 68 | ocr-service | Python | Document OCR (PaddleOCR) |
| 69 | vision-service | Python | Image analysis (Qwen-VL) |
| 70 | ml-prediction-service | Python | XGBoost/LightGBM predictions |
| 71 | training-pipeline-service | Python | Model fine-tuning orchestration |
| 72 | data-ingestion-service | Python | ETL pipelines (Airflow) |

### Domain 12: Accounting & Business (6 services)

| # | Service | Tech | Purpose |
|---|---------|------|---------|
| 73 | accounting-service | ERPNext/Frappe | GL, AP, AR, journal entries |
| 74 | tax-service | Python | FIRS compliance, VAT, WHT |
| 75 | audit-trail-service | Python | Transaction audit logging |
| 76 | payroll-service | ERPNext | Employee payroll |
| 77 | hr-service | Python | HR management, recruitment AI |
| 78 | reporting-service | Python | Apache Superset integration |

---

## 5. API GATEWAY DESIGN

### Apache APISIX Configuration

```
Internet → DNS → Nginx (TLS) → APISIX → Microservices
                                  │
                                  ├── /api/v1/auth/*     → Keycloak
                                  ├── /api/v1/products/* → product-catalog-service
                                  ├── /api/v1/ai/chat    → llm-gateway-service
                                  ├── /api/v1/ai/embed   → embedding-service
                                  ├── /api/v1/ai/stt     → stt-service
                                  ├── /api/v1/ai/ocr     → ocr-service
                                  ├── /api/v1/solar/*    → solar-*-service
                                  ├── /api/v1/fintech/*  → wallet/agent/loan-service
                                  ├── /api/v1/logistics/* → route/fleet/dispatch-service
                                  └── /api/v1/iot/*      → ThingsBoard
```

### Rate Limiting by Tier

| Tier | AI Requests/min | General API/min | Monthly Limit |
|------|----------------|-----------------|---------------|
| **Free** | 10 | 60 | 100 AI queries |
| **Basic (₦2,000/mo)** | 30 | 300 | 1,000 AI queries |
| **Pro (₦5,000/mo)** | 100 | 1,000 | 10,000 AI queries |
| **Enterprise** | Custom | Custom | Unlimited |

---

## 6. AI AGENT FRAMEWORK

### LangGraph for Multi-Step AI Tasks

LangGraph enables AI agents that can plan, execute, and iterate on complex tasks:

**Example: Solar System Design Agent**

```
User: "Design a solar system for my 3-bedroom house in Lekki"
  │
  ├── Step 1: Estimate load (AI calculates from house type)
  │     → Estimated load: 5kW peak, 25kWh/day
  │
  ├── Step 2: Query product catalog (RAG → Medusa products)
  │     → Retrieved: 5× 400W panels, 5kVA inverter, 200Ah LiFePO4
  │
  ├── Step 3: Calculate system (solar-calculator-service)
  │     → System: 2kWp, ~8kWh/day solar, ₦2.1M installed
  │
  ├── Step 4: Find installers (installer-service + LightFM matching)
  │     → Top 3 certified installers in Lekki area
  │
  └── Step 5: Generate proposal (LLM writes formatted proposal)
        → PDF with specs, pricing, installer options, ROI analysis
```

---

## 7. DATA FLOW PER VERTICAL

### Solar Vertical — Complete Flow

```
Customer → Web/Mobile App
  │
  ├── Browse products → product-catalog-service → Medusa
  ├── AI chat about solar → chatbot-service → RAG → Qwen2.5
  ├── System design → solar-calculator-service → AI agent
  ├── Order panels → order-service → payment-service → Paystack
  ├── Schedule install → installation-service → installer-service
  ├── Monitor system → energy-monitor-service → ThingsBoard → IoT
  ├── Detect faults → solar-inspection-service → RT-DETR
  ├── Maintenance alert → maintenance-service → notification-service
  └── Support request → chatbot-service → ticket-service → Chatwoot
```

### Fintech Vertical — Complete Flow

```
Customer/Agent → Mobile App
  │
  ├── Create wallet → wallet-service → Fineract
  ├── KYC verification → kyc-service → PaddleOCR + face match
  ├── Deposit (agent) → agent-banking-service → Fineract
  ├── Transfer → wallet-service → fraud-detection-service → XGBoost
  ├── Apply for loan → loan-service → credit scoring (XGBoost)
  ├── Pay bills → bill-payment-service → Paystack
  ├── View statement → transaction-ledger-service → Fineract
  └── Support → chatbot-service → RAG → Chatwoot
```

---

## 8. EVENT STREAMING ARCHITECTURE

### NATS (Phase 1) / Kafka (Phase 3) Event Topics

| Topic | Publisher | Subscribers | Events |
|-------|----------|-------------|--------|
| `order.created` | order-service | payment, shipping, notification | New order placed |
| `payment.completed` | payment-service | order, notification, accounting | Payment confirmed |
| `product.updated` | product-catalog | search, recommendation, embedding | Product changed |
| `iot.telemetry` | telemetry-service | alert, dashboard, analytics | Device data |
| `ai.embedding.request` | data-ingestion | embedding-service | New data to embed |
| `support.ticket.created` | ticket-service | sentiment, escalation | New support ticket |
| `fraud.alert` | fraud-detection | notification, compliance | Suspicious transaction |
| `solar.fault.detected` | inspection-service | maintenance, notification | Panel defect found |

---

## 9. USER-FACING AI FEATURES

### Feature Matrix by Subscription Tier

| Feature | Free | Basic | Pro | Enterprise |
|---------|------|-------|-----|------------|
| **AI Chat Assistant** | 100 queries/mo | 1,000/mo | 10,000/mo | Unlimited |
| **Product Recommendations** | Basic | Personalized | Advanced | Custom model |
| **Image Background Removal** | 5/mo | 50/mo | 500/mo | Unlimited |
| **Voice-to-Edit** | — | 10/mo | 100/mo | Unlimited |
| **AI Product Descriptions** | — | 20/mo | 200/mo | Unlimited |
| **Dynamic Pricing Insights** | — | — | ✓ | ✓ |
| **Solar System Design AI** | Basic | Full | Full + custom | White-label |
| **Invoice OCR** | 5/mo | 50/mo | 500/mo | Unlimited |
| **AI Financial Reports** | — | — | ✓ | ✓ |

### Image Background Removal (rembg)

```
User uploads product photo
  → image-service receives image
  → rembg (U²-Net) removes background
  → Real-ESRGAN upscales if low-res
  → Return clean product image on white/transparent background
  → User can choose template backgrounds
```

### Voice-to-Edit

```
User speaks edit command (e.g., "Change the price to 15,000 naira")
  → stt-service (Faster-Whisper) → text: "Change the price to 15,000 naira"
  → NLU parsing (Qwen2.5) → intent: update_price, value: 15000, currency: NGN
  → API call to product-catalog-service
  → Confirmation via tts-service (Piper TTS) → "Price updated to 15,000 naira"
```

---

## 10. ACCOUNTING, AUDITING & TAX AI

### Subscription Product: PECH AI Accountant

A standalone AI-powered accounting tool that accountants and businesses subscribe to:

| Tier | Price (₦/mo) | Features |
|------|-------------|----------|
| **Sole Trader** | 3,000 | Invoice OCR, basic bookkeeping, VAT calculation |
| **SME** | 8,000 | Full GL, bank reconciliation, FIRS filing, payroll |
| **Enterprise** | 25,000 | Multi-entity, audit trail, custom reports, API access |
| **Accounting Firm** | 50,000 | Multi-client, team access, white-label reports |

### AI Features

| Feature | Model/Tool | How It Works |
|---------|-----------|-------------|
| **Invoice OCR** | PaddleOCR → Qwen2.5 | Scan invoice → extract fields → create journal entry |
| **Bank Reconciliation** | XGBoost | Match bank transactions to GL entries (pattern learning) |
| **Tax Computation** | Rule engine + Qwen2.5 | Calculate VAT (7.5%), WHT, CIT based on transaction type |
| **Audit Anomaly Detection** | Isolation Forest | Flag unusual transactions, duplicate payments, round amounts |
| **Financial Forecasting** | Prophet | Revenue/expense forecasting from historical data |
| **Natural Language Queries** | Qwen2.5 + RAG | "What were our top 5 expenses last quarter?" |
| **Auto-Categorization** | DistilBERT | Classify transactions into chart of accounts categories |
| **FIRS Filing Assistant** | Qwen2.5 + templates | Generate FIRS-compliant tax returns from accounting data |

---

## 11. HR & RECRUITMENT AI

### AI Features for HR Module

| Feature | Model/Tool | How It Works |
|---------|-----------|-------------|
| **Resume Parsing** | PaddleOCR + Qwen2.5 | Extract structured data from CV (PDF/image) |
| **Candidate Scoring** | XGBoost | Score candidates against job requirements |
| **Interview Q&A Generation** | Qwen2.5 + RAG | Generate role-specific interview questions from job handbook |
| **Skill Gap Analysis** | Qwen2.5 | Compare candidate skills to role requirements |
| **Offer Letter Generation** | Qwen2.5 + templates | Auto-generate offer letters with correct salary/benefits |
| **Onboarding Checklist** | Rule engine | Auto-assign tasks based on role and department |
| **Performance Review AI** | Qwen2.5 | Summarize peer feedback, suggest development areas |

---

## 12. SECURITY & NDPA COMPLIANCE

### Nigeria Data Protection Act (NDPA) 2023

| Requirement | PECH Implementation |
|-------------|-------------------|
| Data minimization | Collect only necessary data; anonymize where possible |
| Consent management | Keycloak consent flows; explicit opt-in for AI features |
| Data residency | All primary data stored on Nigeria-based servers |
| Right to erasure | User deletion API in user-profile-service |
| Data breach notification | 72-hour notification via alert-service |
| DPO appointment | Required — assign Data Protection Officer |
| DPIA | Data Protection Impact Assessment for AI features |

### Security Architecture

| Layer | Implementation |
|-------|---------------|
| **Network** | pfSense firewall, VPN for remote access, private VLAN for servers |
| **Application** | APISIX rate limiting, JWT auth, CORS, input validation |
| **Data** | PostgreSQL row-level security, encryption at rest (LUKS), TLS in transit |
| **AI** | Prompt injection filtering, output sanitization, no PII in embeddings |
| **Access** | Keycloak RBAC, MFA for admin, audit logging |
| **Monitoring** | Fail2ban, OSSEC, Prometheus alerting |

---

## 13. DEPLOYMENT ARCHITECTURE

### Phase 1: Docker Compose

```
┌─────────────────────────────────────┐
│    TRX50 WORKSTATION (Phase 1)       │
│                                      │
│  Docker Compose                      │
│  ├── ollama (GPU)                   │
│  ├── qdrant                         │
│  ├── postgres                       │
│  ├── redis                          │
│  ├── faster-whisper (GPU)           │
│  ├── paddleocr                      │
│  ├── keycloak                       │
│  ├── medusa                         │
│  ├── chatwoot                       │
│  ├── apisix                         │
│  ├── prometheus + grafana           │
│  └── application services           │
│                                      │
│  Portainer (management UI)           │
└─────────────────────────────────────┘
```

### Phase 2: K3s (Lightweight Kubernetes)

```
┌────────────────────────────────────────────┐
│              K3s CLUSTER                    │
│                                             │
│  Node 1 (TRX50 Workstation — upgraded)       │
│  ├── AI workloads (Ollama/vLLM, Whisper)   │
│  ├── Qdrant                                │
│  └── GPU-dependent services                │
│                                             │
│  Node 2 (Application server)               │
│  ├── Business microservices                │
│  ├── Keycloak, Medusa, ERPNext             │
│  └── APISIX, monitoring                    │
│                                             │
│  Node 3 (Database server)                  │
│  ├── PostgreSQL (primary)                  │
│  ├── Redis                                 │
│  └── NATS                                  │
└────────────────────────────────────────────┘
```

---

## 14. NIGERIA-SPECIFIC CONSIDERATIONS

| Challenge | Impact | Architecture Solution |
|-----------|--------|----------------------|
| **Power outages** | Services go offline | UPS + solar + auto-restart Docker containers |
| **Slow internet** | High latency for users | Self-hosted everything; CDN for static assets |
| **Bandwidth costs** | Expensive data | Compress API responses; optimize image sizes |
| **Mobile-first users** | 70%+ mobile traffic | Mobile-optimized APIs; progressive web app |
| **USSD banking** | Feature phones need access | USSD gateway for fintech services |
| **Multiple languages** | Yoruba, Hausa, Igbo, Pidgin | Whisper for voice; Argos for text translation |
| **Cash-heavy economy** | Digital payments adoption | Agent banking network (Fineract) |
| **Low smartphone storage** | Users can't install large apps | PWA (progressive web app) instead of native |

---

## 15. AI TEAM STRUCTURE

### Organization Chart

```
┌─────────────────────────────────────┐
│      CTO / Managing Director        │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
┌───▼───┐ ┌───▼───┐ ┌───▼───┐
│ AI &  │ │Product│ │ Ops & │
│ Eng.  │ │ & Biz │ │ Infra │
└───┬───┘ └───┬───┘ └───┬───┘
    │         │         │
    ├── AI/ML Engineer (×2)        ₦600K-₦1M/mo
    ├── AI Data Engineer            ₦400K-₦600K/mo
    ├── MLOps Engineer              ₦500K-₦800K/mo
    ├── API/Platform Engineer       ₦450K-₦700K/mo
    │         │
    │         ├── AI Product Manager ₦500K-₦800K/mo
    │         ├── Developer Advocate ₦400K-₦600K/mo
    │         ├── Technical Writer   ₦250K-₦400K/mo
    │         │
    │         │         ├── Installer Training Mgr  ₦350K-₦500K/mo
    │         │         ├── Fintech Ops / Agent Mgr  ₦400K-₦600K/mo
    │
    └── AI/ML Intern (×2)          ₦80K-₦120K/mo
```

### Monthly Team Cost

| Role | Count | Monthly (₦) | Annual (₦) |
|------|-------|-------------|------------|
| AI/ML Engineers | 2 | 1,200,000-2,000,000 | 14,400,000-24,000,000 |
| AI Data Engineer | 1 | 400,000-600,000 | 4,800,000-7,200,000 |
| MLOps Engineer | 1 | 500,000-800,000 | 6,000,000-9,600,000 |
| API/Platform Engineer | 1 | 450,000-700,000 | 5,400,000-8,400,000 |
| AI Product Manager | 1 | 500,000-800,000 | 6,000,000-9,600,000 |
| Developer Advocate | 1 | 400,000-600,000 | 4,800,000-7,200,000 |
| Technical Writer | 1 | 250,000-400,000 | 3,000,000-4,800,000 |
| Installer Training Mgr | 1 | 350,000-500,000 | 4,200,000-6,000,000 |
| Fintech Ops Mgr | 1 | 400,000-600,000 | 4,800,000-7,200,000 |
| AI/ML Interns | 2 | 160,000-240,000 | 1,920,000-2,880,000 |
| **Total AI Team** | **12** | **₦4,610,000-₦7,240,000** | **₦55,320,000-₦86,880,000** |

### Hiring Timeline

| Phase | Month | Hires |
|-------|-------|-------|
| **Phase 1** | 1-3 | 2× AI/ML Interns, 1× AI/ML Engineer |
| **Phase 2** | 4-9 | 1× AI Data Engineer, 1× API/Platform Engineer, 1× Installer Training Mgr, 1× Fintech Ops Mgr, 1× Technical Writer |
| **Phase 3** | 10-18 | 1× AI/ML Engineer #2, 1× MLOps Engineer, 1× AI Product Manager, 1× Developer Advocate |

---

*This document is confidential to PECH Group Holdings Ltd. Last updated: March 2026.*

<div style="height:5px;background:linear-gradient(90deg,#E08A00,#F5A623 25%,#0099CC 75%,#00BFFF);margin:20px -28px -24px -28px;"></div>
</div>
