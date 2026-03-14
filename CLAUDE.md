# PECH Group Holdings Ltd — Project Guidelines

## Brand Colors (from PECH Solar logo)

| Color | Hex | Usage |
|-------|-----|-------|
| **PECH Sky Blue** | `#00BFFF` | Primary brand color, headings, key elements |
| **PECH Orange/Amber** | `#F5A623` | Secondary brand color, accents, highlights |
| **Dark Blue** | `#0099CC` | Darker shade of brand blue |
| **Dark Orange** | `#E08A00` | Darker shade of brand orange |
| **Dark Background** | `#1B2838` | Dark navy for chart/image backgrounds |
| **White** | `#FFFFFF` | Text on dark backgrounds, clean layouts |

The logo uses a **blue-to-orange gradient** (top to bottom) on a hexagonal icon shape. Always use these brand colors for any generated images, charts, documents, or visual assets.

## Company Info
- **Full Name:** PECH Group Holdings Ltd
- **Location:** Lagos, Nigeria
- **Mission:** Technology and infrastructure enablers for people
- **Brand Philosophy:** Reliability, quality, and good price for your money — no bad products
- **Team Size:** 37 roles (24 FT + 5 contract + 8 intern)
- **Budget:** ₦250M (~$160K USD) total proposal

## AI Ecosystem Context

PECH is building an **AI-native platform** — all models self-hosted on RTX 4090 GPUs in Lagos, open-source only (Apache-2.0 / MIT). Key context for any AI assistant working on this project:

### Model Preferences (License-Safe Only)
- **Primary LLM:** Qwen2.5 family (Apache-2.0) — 0.5B to 72B parameter range
- **Secondary LLM:** Phi-4 (MIT), Mistral 7B (Apache-2.0)
- **Code:** Qwen2.5-Coder, DeepSeek-Coder-V2-Lite (MIT)
- **Speech-to-Text:** Whisper (MIT), whisper.cpp, Faster-Whisper
- **Text-to-Speech:** Piper TTS (MIT), Kokoro TTS (Apache-2.0)
- **Vision:** Qwen2-VL (Apache-2.0), Qwen2.5-VL
- **OCR:** PaddleOCR (Apache-2.0), Tesseract (Apache-2.0)
- **Embeddings:** MiniLM-L6 (MIT), Nomic-Embed (Apache-2.0)
- **Object Detection:** RT-DETR (Apache-2.0) — NOT YOLOv8 (AGPL)
- **ML/Forecasting:** XGBoost (Apache-2.0), LightGBM (MIT), Prophet (MIT)

### Models to AVOID (License Issues)
- Llama 3/3.1/3.2 (Meta license — can't rebrand)
- Gemma 2/3 (Google custom license — redistribution restrictions)
- YOLOv8 (AGPL-3.0 — copyleft)
- Stable Diffusion 3+ (Stability AI license — non-commercial)

### Platform Stack (Open-Source)
- **API Gateway:** Apache APISIX (Apache-2.0) — NOT Kong or Traefik
- **Identity:** Keycloak (Apache-2.0)
- **Commerce:** Medusa (MIT)
- **ERP:** ERPNext (MIT)
- **Fintech:** Apache Fineract (Apache-2.0)
- **IoT:** ThingsBoard CE (Apache-2.0)
- **Support:** Chatwoot (MIT)
- **Vector DB:** Qdrant (Apache-2.0)
- **BI/Analytics:** Apache Superset (Apache-2.0) — NOT Metabase (AGPL)
- **Workflow:** Apache Airflow (Apache-2.0) — NOT n8n (Sustainable Use License)
- **Graph DB:** Apache AGE on PostgreSQL (Apache-2.0) — NOT Neo4j (GPL)
- **Model Serving:** Ollama (MIT) → vLLM (Apache-2.0)
- **RAG Framework:** LangChain (MIT) + LangGraph

### Architecture
- 78 microservices across 11 domains
- 3-phase deployment: Crawl (TRX50 + Ollama) → Walk (add 2nd GPU + vLLM) → Run (co-locate + scale)
- Zero-waste single-platform: TRX50 Workstation from Day 1, add components, never replace
- Event streaming: NATS (Phase 1) → Apache Kafka (Phase 3)
- Database: PostgreSQL + Redis + Qdrant
- Container: Docker Compose (Phase 1) → K3s (Phase 2) → full K8s (Phase 3)

### Nigeria-Specific Considerations
- All hardware sourced from China with 25-35% import duties + 7.5% VAT
- Power instability: UPS + solar backup required
- NDPA 2023 compliance for data protection
- Mobile-first design (70%+ users on mobile)
- USSD fallback for feature phone users
- Lagos co-location options: MainOne, Rack Centre, 21st Century

### Key Documents
- `ai_strategy/PECH_ECOSYSTEM_COMPREHENSIVE_GUIDE.md` — master reference
- `ai_strategy/PECH_AI_MODEL_CATALOG.md` — all model details
- `ai_strategy/PECH_AI_ARCHITECTURE_GUIDE.md` — technical architecture
- `PECH_GROUP_FINANCIAL_PROPOSAL_250M_NAIRA.md` — budget context

### Business Intelligence Platform (11th Vertical)
- **Pech-African-Business-Intelligence-Platform** — Lead generation, market research, supplier discovery, installer networks, B2B marketplace
- Modules: Lead Generation, Market Research, Supplier Discovery, Installer Networks, B2B Marketplace
- Comparable to: ZoomInfo, Apollo.io, LinkedIn Sales Navigator, Lusha, Seamless.ai, LeadIQ
- Uses AI web crawlers + ML for data collection and enrichment
- Key document: `ai_strategy/PECH_AFRICAN_BUSINESS_INTELLIGENCE_PLATFORM.md`

### Industry Research
- `ai_strategy/NIGERIA_AFRICA_AUTOMATION_SMART_SYSTEMS_INDUSTRY_RESEARCH.md` — Automation & Smart Systems sector analysis
- Use `/industry-research [INDUSTRY] [COUNTRY/REGION]` slash command to generate new industry research reports
- Research template at `.claude/commands/industry-research.md` — auto-adapts to any industry with 16+ mandatory sections + adaptive sections based on industry type
