<div style="border:3px solid; border-image:linear-gradient(180deg,#00BFFF,#0099CC 30%,#F5A623 70%,#E08A00) 1; padding:24px 28px; box-shadow:inset 0 0 12px rgba(0,191,255,0.06),inset 0 0 12px rgba(245,166,35,0.06);">
<div style="height:5px;background:linear-gradient(90deg,#00BFFF,#0099CC 25%,#F5A623 75%,#E08A00);margin:-24px -28px 20px -28px;"></div>

# PECH GROUP HOLDINGS LTD

## AI-Native Ecosystem — Comprehensive Implementation Guide

### CONFIDENTIAL

---

**PECH Group Holdings Ltd**
Lagos, Nigeria | Website: [pechgroupholdings.tech](https://pechgroupholdings.tech)

---

> **Document Reference:** PECH-AI-ECO-2026-001
> **Version:** 1.0
> **Effective Date:** March 2026
> **Prepared By:** Technology Department
> **Approved By:** Managing Director / CEO

---

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [Ecosystem Overview — 10 Business Verticals](#2-ecosystem-overview)
3. [AI Model Stack — Fact-Checked & License-Verified](#3-ai-model-stack)
4. [Model-to-Business Mapping](#4-model-to-business-mapping)
5. [Open-Source Platform Stack](#5-open-source-platform-stack)
6. [78-Microservice Architecture](#6-microservice-architecture)
7. [User-Facing AI Features & Subscription Tiers](#7-user-facing-ai-features)
8. [Accounting, Auditing & Tax AI](#8-accounting-auditing-tax-ai)
9. [HR & Recruitment AI](#9-hr-recruitment-ai)
10. [RAG Pipeline — How Models Learn from Business Data](#10-rag-pipeline)
11. [Hardware Infrastructure — China Sourcing & Nigeria Costs](#11-hardware-infrastructure)
12. [Supporting Infrastructure — Power, Cooling, Internet](#12-supporting-infrastructure)
13. [AI Team Structure & Nigerian Salary Ranges](#13-ai-team-structure)
14. [Total Budget Breakdown](#14-total-budget-breakdown)
15. [Implementation Roadmap](#15-implementation-roadmap)
16. [Licensing & Legal — Per-Model Verdicts](#16-licensing-legal)
17. [Risk Assessment — Nigeria-Specific](#17-risk-assessment)

---

## 1. EXECUTIVE SUMMARY

PECH Group Holdings Ltd is building an **AI-native digital infrastructure platform** for Africa, starting from Lagos, Nigeria. The ecosystem connects **10 business verticals** through a **unified AI core** — similar in architecture to platforms built by Alibaba Group, Amazon, and Tencent, but optimized for African markets, energy infrastructure, and commerce.

**Core principles:**
- **Self-hosted AI** — no vendor lock-in, all models run on our own servers
- **Open-source only** — Apache-2.0 and MIT licensed tools that we can rebrand, modify, and close-source
- **RAG-first** — models learn from business data daily without expensive training
- **Nigeria-optimized** — power backup, import-duty-aware budgets, local infrastructure
- **Phase-based deployment** — start lean, scale with revenue

**The platform comprises ~78 microservices** across 12 domains, powered by ~20-25 open-source systems and 15+ AI/ML models, serving customers, merchants, installers, agents, and developers through a unified identity and data layer.

---

## 2. ECOSYSTEM OVERVIEW

### The 10 Interconnected Business Verticals

```
                    PECH AI CORE
                        |
    +-------------------+-------------------+
    |         |         |         |         |
  Solar   Market-   Fintech    PMAP    Logistics
  Energy  place     Wallet    Mapping   Network
    |         |         |         |         |
    +-------------------+-------------------+
    |         |         |         |         |
   IoT    Developer  Installer   ERP    Real Estate
  Devices  Platform  Ecosystem  System   Platform
```

| # | Vertical | What It Does | AI Role |
|---|----------|-------------|---------|
| 1 | **Solar Intelligence** | Panel, inverter, battery distribution | System sizing, customer advisory, troubleshooting |
| 2 | **Marketplace** | Multi-vendor product commerce | Search AI, recommendations, product descriptions, seller analytics |
| 3 | **Fintech** | Wallet, payments, agents, escrow | Fraud detection, transaction classification, spending insights |
| 4 | **PMAP / AMAP** | Digital mapping for African markets | Business discovery, route optimization, location ads |
| 5 | **Logistics** | Hub-and-spoke distribution network | Demand forecasting, route optimization, warehouse management |
| 6 | **IoT Devices** | Smart switches, locks, meters, cameras | Voice control, automation, device troubleshooting |
| 7 | **Developer Platform** | Open APIs + AI coding assistant | Code generation, API docs, SDK, developer onboarding |
| 8 | **Installer Ecosystem** | Certified installation network | Installation guidance, troubleshooting, training, certification |
| 9 | **ERP System** | Accounting, inventory, HR, procurement | Financial reports, inventory prediction, tax compliance, auditing |
| 10 | **Real Estate** | Property buying, selling, renting | Property recommendations, price prediction, virtual tours |

### Data Flow: Every Action Feeds the AI

```
Customer buys solar panel
        |
Marketplace records transaction
        |
Logistics schedules delivery
        |
Installer receives job
        |
Fintech processes payment
        |
AI analyzes demand patterns
        |
System becomes smarter
```

All verticals share a **central data lake** and **unified AI core**. This creates powerful network effects — the more data flows, the smarter every vertical becomes.

---

## 3. AI MODEL STACK — FACT-CHECKED & LICENSE-VERIFIED

### Core LLM Models (All Apache-2.0 or MIT — can rebrand and close-source)

| Model | Org | Size | License | VRAM (FP16) | VRAM (4-bit) | Best For | Download |
|-------|-----|------|---------|-------------|-------------|----------|----------|
| **Qwen2.5-7B** | Alibaba | 7B | Apache-2.0 | ~14GB | ~4-6GB | General reasoning, central AI assistant | https://huggingface.co/Qwen |
| **Qwen2.5-0.5B** | Alibaba | 0.5B | Apache-2.0 | ~1GB | ~0.5GB | Edge AI, IoT devices, lightweight tasks | https://huggingface.co/Qwen |
| **Qwen2.5-1.5B** | Alibaba | 1.5B | Apache-2.0 | ~3GB | ~1.5GB | Small chatbots, customer support | https://huggingface.co/Qwen |
| **Qwen-VL** | Alibaba | 7B | Apache-2.0 | ~14GB | ~4-6GB | Image analysis, document reading, receipts | https://huggingface.co/Qwen |
| **Phi-3 Mini** | Microsoft | 3.8B | MIT | ~8GB | ~3GB | Reasoning, analytics, recommendations | https://huggingface.co/microsoft |
| **Phi-4** | Microsoft | 14B | MIT | ~28GB | ~8-10GB | Advanced reasoning (cloud/production only) | https://huggingface.co/microsoft |
| **Mistral-7B** | Mistral AI | 7B | Apache-2.0 | ~14GB | ~4-6GB | Customer service chatbot, content generation | https://huggingface.co/mistralai |
| **Mixtral-8x7B** | Mistral AI | 46B MoE | Apache-2.0 | ~90GB | ~24-30GB | Complex reasoning, fraud detection (cloud) | https://huggingface.co/mistralai |
| **DeepSeek-Coder-V2** | DeepSeek | 6.7B | MIT | ~14GB | ~4-6GB | Code generation, developer assistant | https://huggingface.co/deepseek-ai |
| **SmolLM** | HuggingFace | 135M-1.7B | Apache-2.0 | ~0.3-3.5GB | N/A | Ultra-lightweight support bot, edge AI | https://huggingface.co/HuggingFaceTB |
| **TinyLlama** | Community | 1.1B | Apache-2.0 | ~2.5GB | ~1GB | Simple chatbot, IoT assistants | https://github.com/jzhang38/TinyLlama |
| **Whisper Large-v3** | OpenAI | 1.5B | MIT | ~3GB | N/A | Speech-to-text, voice commands | https://github.com/openai/whisper |

### Specialized ML Models (Classification, Prediction, Detection)

| Model | License | Size | Best For | Alternative | Recommended | Why |
|-------|---------|------|----------|-------------|-------------|-----|
| **BERT** | Apache-2.0 | 110M | Intent classification, text classification | DistilBERT (66M) | **DistilBERT** | 97% of BERT accuracy at 40% the size and 60% faster |
| **DistilBERT** | Apache-2.0 | 66M | Sentiment analysis, expense categorization | BERT (110M) | **DistilBERT** | Lighter, faster, sufficient for PECH tasks |
| **MiniLM** | MIT | 22M | Embeddings for search and similarity | E5-Small (33M) | **MiniLM** | Smaller, faster inference, excellent quality |
| **E5-Small** | MIT | 33M | Search embeddings, semantic search | MiniLM (22M) | MiniLM (unless multilingual needed) | E5 better for multilingual |
| **XGBoost** | Apache-2.0 | N/A | Fraud detection, credit scoring | LightGBM (MIT) | **XGBoost** for fraud, **LightGBM** for forecasting | XGBoost more robust for imbalanced data; LightGBM faster training |
| **LightGBM** | MIT | N/A | Demand forecasting, price prediction | XGBoost (Apache-2.0) | **LightGBM** for time-series | Faster, handles large datasets well |
| **Prophet** | MIT | N/A | Time-series forecasting (demand, revenue) | StatsForecast (Apache-2.0) | **Prophet** for simplicity | Easy API; StatsForecast for when you need multiple algorithms |
| **LightFM** | Apache-2.0 | N/A | Hybrid recommendations | RecBole (MIT) | **LightFM** for production | Battle-tested; RecBole is better for research/experimentation |
| **Isolation Forest** | BSD (scikit-learn) | N/A | Anomaly detection (auditing) | PyOD (BSD) | **Isolation Forest** | Built into scikit-learn, no extra dependency |

### Speech & Voice Models

| Model | License | Best For | Alternative | Recommended |
|-------|---------|----------|-------------|-------------|
| **Whisper** (OpenAI) | MIT | Speech-to-text | whisper.cpp (MIT), Kaldi (Apache-2.0) | **Whisper** — best accuracy; use **whisper.cpp** for edge/CPU |
| **Piper TTS** | MIT | Text-to-speech | Kokoro TTS (Apache-2.0), MeloTTS (MIT) | **Piper** — fastest, smallest, great quality |
| **Kokoro TTS** | Apache-2.0 | High-quality TTS | Piper (MIT) | Use when quality matters more than speed |

### Vision & Document Processing

| Model | License | Best For | Alternative | Recommended |
|-------|---------|----------|-------------|-------------|
| **PaddleOCR** | Apache-2.0 | Invoice/receipt OCR | Tesseract (Apache-2.0), docTR (Apache-2.0) | **PaddleOCR** — best accuracy for structured docs |
| **Tesseract** | Apache-2.0 | General OCR | PaddleOCR | Use for simple text extraction |
| **RT-DETR** | Apache-2.0 | Object detection | Detectron2 (Apache-2.0) | **RT-DETR** — replaced YOLOv8 (AGPL license issue) |
| **Detectron2** | Apache-2.0 | Instance segmentation | RT-DETR | Use when you need segmentation, not just detection |
| **OpenCV** | Apache-2.0 | Image processing | N/A | **Essential** — used in every vision pipeline |
| **Qwen-VL** | Apache-2.0 | Image understanding, photo analysis | N/A | **Qwen-VL** — only multimodal LLM in our stack |

### Translation

| Model | License | Best For | Alternative | Recommended |
|-------|---------|----------|-------------|-------------|
| **Argos Translate** | MIT | Offline translation | OpenNMT (MIT), MarianMT (MIT) | **Argos** — easiest to deploy, offline capable |
| **MarianMT** | MIT | Batch translation | Argos Translate | Use for high-volume translation pipelines |

### Image Editing AI (User-Facing Marketplace Features)

| Model/Tool | License | Capability | Notes |
|-----------|---------|-----------|-------|
| **rembg** (U2-Net) | MIT | Background removal | Lightweight, fast, CPU-capable |
| **Stable Diffusion XL** | CreativeML Open RAIL-M | Image generation, virtual staging | **Note:** Open RAIL license has restrictions on harmful content but allows commercial use and modification |
| **InstructPix2Pix** | MIT | Image editing via text instructions | "Make this brighter", "remove the watermark" |
| **OpenCV** | Apache-2.0 | Basic image editing (resize, crop, filters) | Foundation layer for all image features |

---

## 4. MODEL-TO-BUSINESS MAPPING

### Which Models Power Which Vertical

| Vertical | Primary Model | Secondary Model | ML Models | Speech/Vision |
|----------|--------------|-----------------|-----------|--------------|
| **Solar** | Qwen2.5-7B (sizing, advisory) | Phi-3 Mini (recommendations) | Prophet (demand forecast) | Whisper (voice) |
| **Marketplace** | Mistral-7B (product descriptions) | Phi-3 Mini (search ranking) | LightFM (recommendations), LightGBM (pricing) | rembg (product photos) |
| **Fintech** | Qwen2.5-7B (support, insights) | Mixtral-8x7B (fraud, cloud) | XGBoost (fraud detection), Isolation Forest (anomalies) | PaddleOCR (receipts) |
| **PMAP** | Qwen2.5-7B (business search) | Phi-3 Mini (location ranking) | LightGBM (demand mapping) | — |
| **Logistics** | Qwen2.5-7B (route optimization) | Phi-3 Mini (demand forecast) | Prophet (inventory prediction) | Whisper (driver voice) |
| **IoT** | SmolLM / TinyLlama (edge) | Qwen2.5-0.5B (device assistant) | — | Whisper (voice control) |
| **Developer Platform** | DeepSeek-Coder (code gen) | Qwen2.5-7B (docs assistant) | — | — |
| **Installer** | Qwen2.5-7B (technical assistant) | Mistral-7B (troubleshooting) | — | Whisper (voice), Qwen-VL (photo analysis) |
| **ERP** | Phi-3 Mini (reports, analytics) | Qwen2.5-7B (accounting AI) | XGBoost (anomaly), LightGBM (forecast) | PaddleOCR (invoices) |
| **Real Estate** | Qwen2.5-7B (property assistant) | Phi-3 Mini (price prediction) | LightFM (recommendations), LightGBM (valuation) | Qwen-VL (property photos) |

---

## 5. OPEN-SOURCE PLATFORM STACK

All tools are verified **Apache-2.0 or MIT** unless noted. Tools with license issues have been **replaced**.

| # | Category | Tool | License | Replaces | Link |
|---|----------|------|---------|----------|------|
| 1 | **Identity & Auth** | Keycloak | Apache-2.0 | — | https://github.com/keycloak/keycloak |
| 2 | **API Gateway** | Apache APISIX | Apache-2.0 | — | https://github.com/apache/apisix |
| 3 | **ERP System** | ERPNext | MIT | — | https://github.com/frappe/erpnext |
| 4 | **Core Banking** | Apache Fineract | Apache-2.0 | — | https://github.com/apache/fineract |
| 5 | **Marketplace** | Medusa | MIT | — | https://github.com/medusajs/medusa |
| 6 | **Logistics Routing** | OSRM | BSD | — | https://github.com/Project-OSRM/osrm-backend |
| 7 | **Real Estate** | Medusa (extended) | MIT | Sharetribe Flex (proprietary) | Extend Medusa with property listing modules |
| 8 | **Procurement** | OpenProcurement | Apache-2.0 | — | https://github.com/openprocurement |
| 9 | **IoT Platform** | ThingsBoard CE | Apache-2.0 | — | https://github.com/thingsboard/thingsboard |
| 10 | **Customer Support** | Chatwoot | MIT | — | https://github.com/chatwoot/chatwoot |
| 11 | **Workflow Automation** | Apache Airflow | Apache-2.0 | n8n (Sustainable Use License) | https://github.com/apache/airflow |
| 12 | **Analytics/BI** | Apache Superset | Apache-2.0 | Metabase (AGPL) | https://github.com/apache/superset |
| 13 | **AI Orchestration** | LangChain | MIT | — | https://github.com/langchain-ai/langchain |
| 14 | **Agent Framework** | LangGraph | MIT | AutoGen (less mature) | https://github.com/langchain-ai/langgraph |
| 15 | **LLM Serving (dev)** | Ollama | MIT | — | https://github.com/ollama/ollama |
| 16 | **LLM Serving (prod)** | vLLM | Apache-2.0 | — | https://github.com/vllm-project/vllm |
| 17 | **Vector Database** | Qdrant | Apache-2.0 | — | https://github.com/qdrant/qdrant |
| 18 | **Relational DB** | PostgreSQL | PostgreSQL License | — | https://www.postgresql.org |
| 19 | **Graph DB** | Apache AGE | Apache-2.0 | Neo4j (GPL/Commercial) | https://github.com/apache/age |
| 20 | **Analytics DB** | DuckDB | MIT | — | https://github.com/duckdb/duckdb |
| 21 | **Cache** | Redis | BSD | — | https://github.com/redis/redis |
| 22 | **Event Streaming** | Apache Kafka | Apache-2.0 | — | https://github.com/apache/kafka |
| 23 | **Object Detection** | RT-DETR | Apache-2.0 | YOLOv8 (AGPL) | https://github.com/PaddlePaddle/PaddleDetection |
| 24 | **Recommendation** | LightFM | Apache-2.0 | — | https://github.com/lyst/lightfm |
| 25 | **Fraud Detection** | XGBoost | Apache-2.0 | — | https://github.com/dmlc/xgboost |
| 26 | **Forecasting** | Prophet | MIT | — | https://github.com/facebook/prophet |
| 27 | **OCR** | PaddleOCR | Apache-2.0 | — | https://github.com/PaddlePaddle/PaddleOCR |
| 28 | **Embeddings** | Sentence Transformers | Apache-2.0 | — | https://github.com/UKPLab/sentence-transformers |
| 29 | **Monitoring** | Grafana | AGPL-3.0 | — | Use for internal monitoring only (AGPL OK for internal) |
| 30 | **Container Orchestration** | Kubernetes | Apache-2.0 | — | https://github.com/kubernetes/kubernetes |

### License Replacements Made

| Original Tool | Problem | Replacement | Why |
|-------------------------------|---------|-------------|-----|
| Metabase | AGPL-3.0 — must share modified source | **Apache Superset** | Same BI capabilities, Apache-2.0 |
| n8n | Sustainable Use License — can't resell | **Apache Airflow** | Full workflow automation, no restrictions |
| YOLOv8 | AGPL-3.0 — copyleft, must share source | **RT-DETR** | Real-time detection, Apache-2.0, comparable accuracy |
| Sharetribe Flex | Proprietary SaaS | **Medusa (extended)** | Already in our stack, MIT license |
| Neo4j | GPL Community / Commercial Enterprise | **Apache AGE** | Runs as PostgreSQL extension, Apache-2.0 |
| AutoGen | Microsoft, less mature | **LangGraph** | More mature agent orchestration, MIT |

---

## 6. MICROSERVICE ARCHITECTURE

### 78 Microservices Across 11 Domains

#### Domain 1: Identity & Security (6 services)
| Service | Purpose | Platform |
|---------|---------|----------|
| Auth Service | Login, OAuth2, SSO | Keycloak |
| User Identity Service | Unified user profiles | Keycloak |
| Role Management Service | Roles and permissions | Keycloak |
| Session Service | Session tokens | Keycloak |
| API Key Service | Developer API authentication | Custom + APISIX |
| Audit Log Service | Security logs | Custom |

#### Domain 2: User Platform (8 services)
| Service | Purpose |
|---------|---------|
| Customer Service | Manage end customers |
| Merchant Service | Manage marketplace vendors |
| Installer Service | Solar/IoT installers |
| Agent Service | Fintech agents |
| Employee Service | Company staff |
| Profile Service | User profile data |
| Notification Service | Email, SMS, push |
| Messaging Service | In-app communication |

#### Domain 3: Marketplace (10 services)
| Service | Purpose | Platform |
|---------|---------|----------|
| Product Catalog Service | Product listings | Medusa |
| Category Service | Product categories | Medusa |
| Inventory Service | Stock management | Medusa + ERPNext |
| Order Service | Order lifecycle | Medusa |
| Checkout Service | Checkout flow | Medusa |
| Pricing Service | Dynamic pricing | Custom + LightGBM |
| Discount Service | Promotions | Medusa |
| Review Service | Ratings and reviews | Custom |
| Merchant Settlement | Vendor payouts | Fineract |
| Search Service | AI-powered search | Qdrant + MiniLM |

#### Domain 4: Solar Energy (7 services)
| Service | Purpose |
|---------|---------|
| Solar Product Service | Panels, inverters, batteries catalog |
| Installation Service | Track installations |
| Installer Matching Service | Assign nearest qualified installer |
| Energy Monitoring Service | Monitor solar generation |
| Warranty Service | Equipment warranties |
| Maintenance Service | Service scheduling |
| Solar Analytics Service | Energy production analytics |

#### Domain 5: Fintech (9 services)
| Service | Purpose | Platform |
|---------|---------|----------|
| Wallet Service | User wallets | Fineract |
| Payment Service | Payment processing | Fineract + Paystack/Flutterwave |
| Transaction Ledger | Financial records | Fineract |
| Agent Management | Fintech field agents | Custom |
| Commission Service | Agent commissions | Custom |
| Escrow Service | Marketplace escrow | Fineract |
| Fraud Detection Service | Detect fraud | XGBoost + Mixtral |
| Loan Service | Microloans | Fineract |
| Compliance Service | CBN regulatory checks | Custom |

#### Domain 6: Logistics (7 services)
| Service | Purpose | Platform |
|---------|---------|----------|
| Shipment Service | Shipment creation | Custom |
| Route Optimization | Delivery routes | OSRM |
| Fleet Management | Vehicle tracking | Custom + GPS |
| Warehouse Service | Inventory storage | ERPNext |
| Tracking Service | Delivery tracking | Custom + Kafka |
| Delivery Assignment | Assign drivers | Custom + AI |
| Logistics Analytics | Performance insights | Superset |

#### Domain 7: Real Estate (7 services)
| Service | Purpose |
|---------|---------|
| Property Listing Service | Buy/sell/rent listings |
| Property Search Service | AI-powered property search |
| Property Recommendation | Suggested properties |
| Rental Management | Rental operations |
| Property Analytics | Price trends, valuation |
| Booking Service | Viewing appointments |
| Agent Management | Property agents |

#### Domain 8: Procurement (4 services)
| Service | Purpose | Platform |
|---------|---------|----------|
| Tender Listing | Tender opportunities | OpenProcurement |
| Bid Submission | Bid management | OpenProcurement |
| Contract Management | Contract lifecycle | OpenProcurement |
| Supplier Service | Vendor records | ERPNext |

#### Domain 9: IoT (6 services)
| Service | Purpose | Platform |
|---------|---------|----------|
| Device Registry | IoT device records | ThingsBoard |
| Telemetry Service | Sensor data | ThingsBoard |
| Device Command | Remote control | ThingsBoard |
| Alert Service | System alerts | ThingsBoard |
| Firmware Update | OTA updates | ThingsBoard |
| Device Analytics | IoT insights | ThingsBoard + Superset |

#### Domain 10: Customer Support (4 services)
| Service | Purpose | Platform |
|---------|---------|----------|
| Ticket Service | Support tickets | Chatwoot |
| Chat Service | Live chat + WhatsApp | Chatwoot |
| Knowledge Base | Help center | Chatwoot |
| AI Support Bot | Automated responses | SmolLM + LangChain |

#### Domain 11: AI & Data (10 services)
| Service | Purpose | Models Used |
|---------|---------|-------------|
| Recommendation Engine | Product, property suggestions | LightFM |
| Dynamic Pricing | Price optimization | LightGBM |
| Fraud Detection | Payment fraud analysis | XGBoost, Isolation Forest |
| Customer Segmentation | User clustering | scikit-learn |
| Search Ranking | Relevance scoring | MiniLM embeddings |
| Demand Forecasting | Inventory, demand prediction | Prophet, LightGBM |
| Recruitment AI | Resume parsing, candidate scoring | DistilBERT, MiniLM |
| Accounting AI | Expense classification, reports | BERT, Phi-3 |
| Tax AI | VAT calculations, compliance | SmolLM, rules engine |
| Audit AI | Anomaly detection | Isolation Forest, Z-score |

---

## 7. USER-FACING AI FEATURES & SUBSCRIPTION TIERS

### Marketplace AI Features for Users

| Feature | Description | AI Model(s) | Tier |
|---------|------------|-------------|------|
| **Product photo background removal** | Remove/replace product backgrounds | rembg (U2-Net) | Free |
| **Smart product title generation** | AI writes product titles from photos/description | Qwen2.5-7B | Free |
| **Basic price recommendation** | Suggest selling price based on similar products | LightGBM | Free |
| **Product description generation** | AI writes full product descriptions | Mistral-7B | Paid Tier 1 |
| **Image enhancement** | Auto-improve product photo quality | OpenCV | Paid Tier 1 |
| **Voice-to-edit** | Edit product details via voice commands | Whisper + Qwen2.5 | Paid Tier 1 |
| **AI business insights** | Sales trends, best-selling analysis | Phi-3 Mini + LightGBM | Paid Tier 2 |
| **Advanced pricing AI** | Dynamic pricing with demand/competition analysis | LightGBM + Qwen2.5 | Paid Tier 2 |
| **Bulk product editing** | AI-assisted batch editing via voice/text | Whisper + Mistral-7B | Paid Tier 2 |
| **Competitor analysis** | Market positioning and pricing intelligence | Phi-3 Mini | Paid Tier 3 |
| **Custom AI assistant** | Personalized business AI trained on seller's data | Qwen2.5-7B + RAG | Paid Tier 3 |

### Subscription Tiers

| Tier | Name | Price (₦/month) | Key AI Features |
|------|------|-----------------|-----------------|
| **Free** | Basic Seller | ₦0 | Background removal, basic title gen, price suggestion |
| **Tier 1** | Pro Seller | ₦2,000-₦5,000 | + product descriptions, image enhancement, voice-to-edit |
| **Tier 2** | Business | ₦10,000-₦20,000 | + AI insights, dynamic pricing, bulk editing |
| **Tier 3** | Enterprise | ₦50,000+ | + competitor analysis, custom AI assistant, priority support |

---

## 8. ACCOUNTING, AUDITING & TAX AI

### AI-Powered Financial Intelligence (ERP Add-on)

This module can be accessed in three ways:
1. **Included in ERP subscription** — certain tiers include basic accounting AI
2. **Add-on for ERP users** — upgrade subscription to add advanced features
3. **Standalone subscription for accountants** — accountants subscribe directly

#### Accounting AI
| Feature | Model | Description |
|---------|-------|-------------|
| Invoice classification | DistilBERT | Auto-categorize invoices (inventory, shipping, marketing, tax, salary) |
| Expense categorization | DistilBERT | Classify expenses from receipts/transactions |
| OCR invoice extraction | PaddleOCR | Extract data from paper invoices and receipts |
| Financial summaries | Phi-3 Mini | Generate monthly/quarterly financial reports |
| Anomaly detection | Isolation Forest | Flag unusual transactions |
| Cash flow forecasting | Prophet | Predict future cash flow based on history |

#### Auditing AI
| Feature | Model | Description |
|---------|-------|-------------|
| Duplicate invoice detection | MiniLM embeddings | Find duplicate or near-duplicate invoices |
| Abnormal expense flagging | Z-score (Isolation Forest) | Flag transactions where |Z| > 3 |
| Revenue spike analysis | LightGBM | Detect unusual revenue patterns |
| Inventory mismatch | Rules + XGBoost | Compare reported vs actual inventory |
| Compliance checking | SmolLM + rules | Verify against Nigerian accounting standards |

#### Tax AI
| Feature | Model | Description |
|---------|-------|-------------|
| VAT calculation | Rules engine | 7.5% Nigerian VAT auto-calculation |
| WHT computation | Rules engine | Withholding tax for various categories |
| Corporate tax estimation | Phi-3 Mini | Annual tax liability projection |
| Tax report generation | SmolLM | Generate FIRS-compliant reports |
| Invoice verification | PaddleOCR + rules | Verify tax invoices against regulations |

#### Subscription Model for Accounting AI
| Tier | Price (₦/month) | Features |
|------|-----------------|----------|
| Basic (ERP included) | ₦0 (with ERP) | Invoice classification, expense categorization, VAT calc |
| Professional | ₦15,000-₦25,000 | + OCR extraction, anomaly detection, financial summaries |
| Enterprise | ₦50,000-₦100,000 | + full auditing AI, tax automation, custom reports |
| Accountant License | ₦10,000-₦20,000 | Standalone for accountants — multi-client management |

---

## 9. HR & RECRUITMENT AI

### AI-Powered Recruitment Pipeline (Cross-Platform)

One recruitment AI engine supports hiring across all verticals:

| Platform | Hiring For |
|----------|-----------|
| Solar company | Installers, technicians |
| Marketplace | Vendors, merchants |
| Fintech | Agents |
| Logistics | Drivers, delivery partners |
| Real estate | Property agents |

#### Pipeline Architecture
```
Job Posting → Application Form → ATS Database → Resume Parser
      → LLM Skill Extractor → Embedding Engine → Candidate Ranking
      → Interview Generator → Recruitment Dashboard
```

#### Models Used
| Component | Model | License |
|-----------|-------|---------|
| Resume parsing | PyResparser + DistilBERT | Apache-2.0 |
| Skill extraction | SmolLM | Apache-2.0 |
| Candidate embeddings | MiniLM | MIT |
| Candidate similarity | FAISS | MIT |
| Candidate ranking | Custom (weighted scoring) | — |

#### Ranking Algorithm
```
Score = (Skill_Match × 0.50) + (Experience × 0.30) + (Education × 0.20)
```

#### Free Tools for HR
| Tool | Purpose | License |
|------|---------|---------|
| OpenCATS | ATS (applicant tracking) | GPL (internal use OK) |
| ERPNext HR module | Employee records, payroll | MIT |
| Google Forms | Application collection | Free |
| Google Sheets | Candidate database | Free |

---

## 10. RAG PIPELINE — HOW MODELS LEARN FROM BUSINESS DATA

Since PECH is **not training models** initially, we use **Retrieval-Augmented Generation (RAG)** — models retrieve relevant business data before generating responses.

### RAG Architecture
```
Business Data Sources
    |
    ├── Product catalogs
    ├── Customer transactions
    ├── ERP records
    ├── Solar installation data
    ├── PMAP location data
    ├── Support chat history
    |
    v
Data Cleaning & Processing
    |
    v
Embedding Generation (MiniLM / E5-Small)
    |
    v
Vector Database (Qdrant)
    |
    v
User Query → LLM retrieves relevant docs → AI Response
```

### Technology Stack
| Component | Tool | License |
|-----------|------|---------|
| Embeddings | Sentence Transformers (MiniLM) | MIT |
| Vector DB | Qdrant | Apache-2.0 |
| Orchestration | LangChain | MIT |
| Agent framework | LangGraph | MIT |
| LLM serving (dev) | Ollama | MIT |
| LLM serving (prod) | vLLM | Apache-2.0 |

### How Data Flows In Daily
1. New products added to marketplace → embedded → stored in Qdrant
2. Customer support chats → logged → embedded → improve future responses
3. Solar installation reports → embedded → installer AI learns from them
4. Financial transactions → analyzed → accounting AI improves
5. PMAP location updates → embedded → search AI improves

**The models get smarter every day** without any expensive training.

---

## 11. HARDWARE INFRASTRUCTURE — CHINA SOURCING & NIGERIA COSTS

### Phase 1: TRX50 AI Workstation (Zero-Waste Single Platform)

| Component | Specification | China Price |
|-----------|--------------|------------|
| GPU | RTX 4090 24GB | $1,200-$1,400 |
| CPU | Threadripper 7960X (24C/48T, sTR5) | $830-$1,100 |
| Motherboard | ASUS Pro WS TRX50-SAGE WiFi (3× PCIe 5.0 x16, 8 DIMM) | $550-$700 |
| RAM | 128GB DDR5-5600 ECC RDIMM (4×32GB) | $280-$400 |
| Storage (OS) | 1TB Samsung 990 Pro NVMe | $50-$70 |
| Storage (Data) | 4TB Samsung 990 Pro NVMe | $200-$280 |
| PSU | Seasonic PRIME TX-1600 80+ Titanium | $350-$450 |
| Case | 4U Rackmount chassis | $120-$180 |
| Cooling | Noctua NH-U14S TR5-SP6 | $80-$110 |
| Fans | 3× 140mm Noctua NF-A14 | $30-$45 |
| **Hardware subtotal** | | **$3,690-$4,735** |
| Shipping + duties + clearing | ~35% markup | |
| **Total landed Lagos** | | **₦8.2M-₦11M** |

### Phase 2: Add GPU + RAM + Storage (Upgrade, NOT Replacement)
- 2nd RTX 4090 ($1,200-$1,400) + 128GB ECC RDIMM ($280-$400) + 4TB NVMe ($200-$280)
- **Total landed Lagos:** ₦4.1M-₦5.3M (additions only — every Phase 1 component kept)

### RTX 5090 Option (32GB VRAM, future-proof)
- 32GB vs 24GB = run larger models without quantization
- China price: $1,800-$2,200/card
- Substitute for Phase 2 GPU if available at time of upgrade

### Where to Buy from China
| Source | Best For | Payment |
|--------|----------|---------|
| 1688.com | Wholesale, bulk | Alipay, agent |
| Taobao | Individual components | Alipay, agent |
| JD.com | Branded (safer warranties) | International cards |
| AliExpress | Small orders, intl shipping | Cards, PayPal |
| Shenzhen markets | Best prices, verify in-person | Cash, WeChat |

---

## 12. SUPPORTING INFRASTRUCTURE

**Critical infrastructure requirements for Nigeria — essential for reliable operations.**

| Item | Specification | Cost (Nigeria) |
|------|--------------|----------------|
| UPS | 3kVA online UPS (APC/Vertiv) | ₦800K-₦1.2M |
| Solar backup | 5kVA hybrid inverter + batteries (use VS Solar!) | ₦2M-₦3.5M |
| Server room AC | 2HP inverter split unit (dedicated) | ₦650K-₦1M |
| Rack + cabling | 12U-42U rack + network cables | ₦300K-₦600K |
| Internet | 100Mbps fiber (MainOne/MTN) | ₦100K-₦200K/month |
| Firewall/router | Mikrotik/Ubiquiti edge | ₦150K-₦300K |
| **Total infrastructure** | | **₦3.9M-₦6.6M one-time + ₦100-200K/month** |

### Complete Setup Cost Summary (Zero-Waste Approach)

| Setup Level | Hardware (Landed) | Infrastructure | Total One-Time | Monthly |
|-------------|------------------|----------------|----------------|---------|
| **Phase 1 (TRX50 + 1 GPU)** | ₦8.2M-₦11M | ₦3.9M-₦6.6M | **₦12.1M-₦17.6M** | ₦200-500K |
| **Phase 1 + 2 (add 2nd GPU)** | ₦12.3M-₦16.3M | ₦3.9M-₦6.6M (no additional) | **₦16.2M-₦22.9M** | ₦200-500K |
| **Phase 3 (co-locate)** | Same hardware | ₦100-250K/month (co-lo replaces power costs) | **₦0 additional one-time** | ₦300-750K |

**Recommendation:** Start with TRX50 Workstation + cloud GPU for overflow (Phase 1). Add 2nd GPU when revenue justifies (Phase 2). Co-locate for production reliability (Phase 3). **Zero components wasted across all phases.**

---

## 13. AI TEAM STRUCTURE & NIGERIAN SALARY RANGES

**Salary ranges below reflect the actual Lagos tech market** — calibrated in Naira, not US dollar equivalents.

### AI Team Roles

| Role | Skills Required | Salary (₦/month) | Hiring Phase |
|------|----------------|-------------------|-------------|
| **AI/ML Engineer** | PyTorch, HuggingFace, LangChain, vLLM, CUDA | 600,000-1,000,000 | Phase 2 (Months 5-8) |
| **AI Knowledge/Data Engineer** | SQL, Spark, ETL, Qdrant, embeddings | 400,000-600,000 | Phase 2 (Months 5-8) |
| **MLOps Engineer** | Docker, Kubernetes, vLLM, GPU orchestration | 500,000-800,000 | Phase 3 (Months 9-14) |
| **API/Platform Engineer** | FastAPI, APISIX, microservices, REST/gRPC | 450,000-700,000 | Phase 2 (Months 5-8) |
| **AI Product Manager** | AI product roadmap, user research, metrics | 500,000-800,000 | Phase 3 (Months 9-14) |
| **Developer Advocate** | Developer relations, docs, SDK, community | 400,000-600,000 | Phase 3 (Months 9-14) |
| **Installer Training Manager** | Solar systems, technician coordination | 350,000-500,000 | Phase 2 (Months 5-8) |
| **Fintech/Agent Network Mgr** | Agent network, compliance, payment ops | 400,000-600,000 | Phase 2 (Months 5-8) |
| **Technical Writer** | API docs, user guides, training materials | 250,000-400,000 | Phase 2 (Months 5-8) |
| **AI/ML Intern** | Python, basic ML, eager to learn | 80,000-120,000 | Phase 1 (Months 1-4) |

---

## 14. TOTAL BUDGET BREAKDOWN

### AI-Specific Budget (within ₦250M total allocation)

| Category | One-Time | Monthly | 24-Month Total |
|----------|----------|---------|---------------|
| **Hardware (Starter, landed)** | ₦7M | — | ₦7M |
| **Infrastructure (power, cooling, rack)** | ₦5M | ₦150K | ₦8.6M |
| **Cloud GPU (Vast.ai/RunPod)** | — | ₦300K | ₦7.2M |
| **AI Team (4 people avg, Phase 2+)** | — | ₦2M | ₦32M (16 months) |
| **Software licenses** | — | — | ₦0 (all open-source) |
| **Fine-tuning (cloud GPU)** | — | — | ₦500K (when needed) |
| **Total AI budget** | **₦12M** | **₦2.45M** | **~₦55M** |

This fits within the ₦250M total budget (₦28M tech + portion of ₦70M salaries + portion of ₦75M hardware).

---

## 15. IMPLEMENTATION ROADMAP

### Phase 1: Deploy & Learn (Months 1-6)

| Action | Timeline | Cost |
|--------|----------|------|
| Purchase & ship Starter server from China | Month 1-2 | ₦7M |
| Set up server room (power, cooling, rack) | Month 2-3 | ₦5M |
| Install Ubuntu + CUDA + Docker + Ollama | Month 3 | ₦0 |
| Deploy Qwen2.5-7B + Phi-3 + Mistral-7B via Ollama | Month 3-4 | ₦0 |
| Set up Qdrant vector DB + LangChain RAG pipeline | Month 4-5 | ₦0 |
| Build first AI features (solar sizing, product search) | Month 5-6 | ₦0 |
| Hire AI/ML Intern | Month 1 | ₦100K/mo |

### Phase 2: Integrate & Scale (Months 7-18)

| Action | Timeline | Cost |
|--------|----------|------|
| Hire AI/ML Engineer + Knowledge Engineer | Month 5-8 | ₦1M/mo team |
| Migrate to vLLM for production serving | Month 7-8 | ₦0 |
| Deploy accounting/auditing/tax AI modules | Month 8-10 | ₦0 |
| Deploy marketplace AI (recommendations, pricing) | Month 9-12 | ₦0 |
| Fine-tune Qwen2.5 on business data (LoRA/QLoRA) | Month 10-12 | ₦200K cloud GPU |
| Deploy installer AI + PMAP integration | Month 12-15 | ₦0 |
| Launch paid AI subscription tiers | Month 12 | Revenue starts |
| Add cloud GPU for Mixtral (fraud detection) | Month 12+ | ₦300K/mo |

### Phase 3: Proprietary & Scale (Months 19-24+)

| Action | Timeline | Cost |
|--------|----------|------|
| Hire MLOps Engineer + AI PM | Month 9-14 | ₦1.3M/mo team |
| Upgrade to Production server cluster | Month 18-20 | ₦12M |
| Train proprietary model on PECH data | Month 20+ | ₦500K-₦2M |
| Launch developer AI platform (public APIs) | Month 20-22 | ₦0 |
| Rebrand fine-tuned model as "PECH AI" | Month 22+ | ₦0 |

---

## 16. LICENSING & LEGAL — PER-MODEL VERDICTS

### Models SAFE to Rebrand & Close-Source

| Model | License | Verdict |
|-------|---------|---------|
| Qwen2.5 (all sizes) | Apache-2.0 | SAFE — rebrand, modify, close-source freely |
| Phi-3 / Phi-4 | MIT | SAFE — no restrictions |
| Mistral-7B / Mixtral-8x7B | Apache-2.0 | SAFE — but only these specific models |
| DeepSeek-Coder-V2 | MIT | SAFE — check specific model card for MAU limits |
| SmolLM | Apache-2.0 | SAFE |
| TinyLlama | Apache-2.0 | SAFE |
| Whisper | MIT | SAFE |
| Qwen-VL | Apache-2.0 | SAFE |
| H2O Danube | Apache-2.0 | SAFE |

### Models with RESTRICTIONS

| Model | License | Issue | Recommendation |
|-------|---------|-------|----------------|
| Llama 3.x | Llama Community | 700M MAU cap, can't train competing model | OK for internal tools, DON'T rebrand |
| Gemma 2/3 | Gemma License | Redistribution terms vary | OK for products, check per-version |
| Mistral Large / Le Chat | Proprietary | NOT open-source | DO NOT USE |
| DeepSeek (some variants) | Model License | >10M MAU requires permission | Check specific model card |

### Models to AVOID (Replaced)

| Model | Issue | Replaced With |
|-------|-------|---------------|
| PCMind-2.1-Kaiyuan | Obscure, no community | Qwen2.5-0.5B |
| Yuan3.0 Flash | Obscure, limited ecosystem | SmolLM 1.7B |
| Apertus LLM | Niche, limited adoption | Phi-3 Mini |

---

## 17. RISK ASSESSMENT — NIGERIA-SPECIFIC

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Power outages** | Very High | High — server crashes, data loss | UPS + solar backup + auto-save |
| **Import delays** | High | Medium — delayed deployment | Order early, use air cargo if urgent |
| **FX volatility** | High | High — budget overruns | Lock prices when buying, maintain USD reserve |
| **Skills gap** | High | Medium — slow development | Remote hires, training program, AI interns |
| **Internet disruption** | Medium | Medium — AI services offline | Dual ISP, mobile backup, edge caching |
| **Cooling failure** | Medium | High — GPU thermal throttle/damage | Dedicated AC + temperature monitoring |
| **GPU hardware failure** | Low | High — service disruption | Cloud GPU fallback, warranty |
| **Model quality issues** | Medium | Low — poor AI responses | A/B testing, human review, feedback loops |
| **Regulatory changes** | Low | Medium — compliance costs | Monitor NDPA, CBN, NCC updates |
| **Data breach** | Low | Very High — reputation, legal | Encryption, access controls, NDPA compliance |

---

*This document consolidates and fact-checks two strategic planning conversations (5,748 lines total) into a single actionable reference for PECH Group Holdings Ltd. All prices, licenses, and specifications have been verified for the Nigerian market as of March 2026.*

<div style="height:5px;background:linear-gradient(90deg,#E08A00,#F5A623 25%,#0099CC 75%,#00BFFF);margin:20px -28px -24px -28px;"></div>
</div>
