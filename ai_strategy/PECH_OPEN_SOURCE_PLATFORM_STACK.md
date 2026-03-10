# PECH GROUP HOLDINGS LTD

## Open-Source Platform Stack — Complete Reference

### CONFIDENTIAL

---

**PECH Group Holdings Ltd**
Lagos, Nigeria | Website: [pechgroupholdings.tech](https://pechgroupholdings.tech)

---

> **Document Reference:** PECH-AI-PLATFORMS-2026-001
> **Version:** 1.0
> **Effective Date:** March 2026
> **Prepared By:** Technology Department
> **Approved By:** Managing Director / CEO

---

## TABLE OF CONTENTS

1. [License Policy](#1-license-policy)
2. [Identity & Access Management](#2-identity-access-management)
3. [API Gateway & Service Mesh](#3-api-gateway-service-mesh)
4. [E-Commerce / Marketplace](#4-e-commerce-marketplace)
5. [ERP / Accounting](#5-erp-accounting)
6. [Fintech / Core Banking](#6-fintech-core-banking)
7. [Logistics & Routing](#7-logistics-routing)
8. [IoT Platform](#8-iot-platform)
9. [Customer Support](#9-customer-support)
10. [Workflow Automation](#10-workflow-automation)
11. [Business Intelligence & Analytics](#11-business-intelligence-analytics)
12. [AI/ML Infrastructure](#12-ai-ml-infrastructure)
13. [Vector Database](#13-vector-database)
14. [Databases](#14-databases)
15. [Message Queue / Event Streaming](#15-message-queue-event-streaming)
16. [Mapping & Geospatial](#16-mapping-geospatial)
17. [Procurement / Tendering](#17-procurement-tendering)
18. [CMS / Content Management](#18-cms-content-management)
19. [Monitoring & Observability](#19-monitoring-observability)
20. [Container Orchestration](#20-container-orchestration)
21. [CI/CD](#21-ci-cd)
22. [License Replacements Summary](#22-license-replacements-summary)
23. [Integration Map](#23-integration-map)

---

## 1. LICENSE POLICY

PECH only uses platform tools with **Apache-2.0, MIT, or BSD** licenses. This allows us to:
- Modify and extend without sharing source code
- Embed in proprietary products
- Rebrand under PECH identity
- Sell as part of subscription services

**Excluded license types:** AGPL-3.0, GPL-3.0 (for platforms we modify and serve), Sustainable Use License, SSPL, BSL (Business Source License).

---

## 2. IDENTITY & ACCESS MANAGEMENT

### Primary: Keycloak

| Attribute | Detail |
|-----------|--------|
| **Website** | [keycloak.org](https://www.keycloak.org/) |
| **GitHub** | [github.com/keycloak/keycloak](https://github.com/keycloak/keycloak) |
| **License** | Apache-2.0 |
| **Language** | Java (Quarkus) |
| **PECH Use** | SSO across all 10 verticals, OAuth2/OIDC, user federation, social login, RBAC, multi-tenancy |

**Why Keycloak:**
- Industry standard for enterprise IAM
- Supports social login (Google, Facebook, Apple)
- Multi-realm for PECH's multi-tenant architecture (marketplace vendors, fintech agents, solar installers each get their own realm)
- Self-hosted, no per-user fees

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Authentik | Custom (source-available) | Less mature; enterprise features require paid license |
| Zitadel | Apache-2.0 | Newer; smaller community; could be future option |
| SuperTokens | Apache-2.0 | Good for simple auth but lacks Keycloak's multi-realm enterprise features |

---

## 3. API GATEWAY & SERVICE MESH

### Primary: Apache APISIX

| Attribute | Detail |
|-----------|--------|
| **Website** | [apisix.apache.org](https://apisix.apache.org/) |
| **GitHub** | [github.com/apache/apisix](https://github.com/apache/apisix) |
| **License** | Apache-2.0 |
| **Language** | Lua (OpenResty/Nginx) |
| **PECH Use** | API gateway for all 78 microservices, rate limiting, auth, load balancing, circuit breaking |

**Why APISIX:**
- Highest performance open-source API gateway (benchmarks show 2-5× faster than Kong)
- Plugin system for custom logic (auth, rate limiting, AI model routing)
- Dashboard for visual management
- Dynamic upstream configuration (route AI requests to different model servers)

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Kong | Apache-2.0 (Community) | Heavier; enterprise features are proprietary; APISIX is faster |
| Traefik | MIT | Better for simple setups; lacks APISIX's plugin ecosystem |
| Envoy | Apache-2.0 | Lower-level; better as sidecar proxy than standalone gateway |

---

## 4. E-COMMERCE / MARKETPLACE

### Primary: Medusa.js

| Attribute | Detail |
|-----------|--------|
| **Website** | [medusajs.com](https://medusajs.com/) |
| **GitHub** | [github.com/medusajs/medusa](https://github.com/medusajs/medusa) |
| **License** | MIT |
| **Language** | TypeScript (Node.js) |
| **PECH Use** | Multi-vendor marketplace, product catalog, cart, checkout, order management, vendor storefronts |

**Why Medusa:**
- Headless architecture — PECH builds its own frontend
- MIT license — can fully customize and close-source
- Plugin system for multi-vendor extension
- Modern stack (TypeScript, PostgreSQL)
- Built-in payment and fulfillment abstractions

**Medusa Extensions for PECH:**
- Multi-vendor plugin (vendor onboarding, commission splits)
- Solar product catalog (panels, inverters, batteries)
- Real estate listings (extend product model for property)
- Installer marketplace (service products)

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Saleor | BSD-3 | Strong alternative; Django/Python stack; smaller plugin ecosystem |
| WooCommerce | GPL-2.0 | WordPress dependency; PHP; license issues for PECH modifications |
| Sharetribe Go | Source-available | Not truly open-source; Sharetribe Flex is proprietary SaaS |

---

## 5. ERP / ACCOUNTING

### Primary: ERPNext

| Attribute | Detail |
|-----------|--------|
| **Website** | [erpnext.com](https://erpnext.com/) |
| **GitHub** | [github.com/frappe/erpnext](https://github.com/frappe/erpnext) |
| **License** | MIT (core Frappe framework) / GPL-3.0 (some ERPNext modules) |
| **Language** | Python (Frappe framework) |
| **PECH Use** | Accounting, HR, payroll, inventory, procurement, tax compliance (FIRS), auditing |

**Why ERPNext:**
- Full ERP suite in one platform
- Strong accounting module (multi-currency, multi-company)
- Nigerian tax compliance possible with customization
- Python/Frappe makes AI integration straightforward
- Large community in Africa

**License Note:** ERPNext's core Frappe framework is MIT. Some ERPNext modules are GPL-3.0. For PECH's accounting AI subscription product, we build our own AI layer on top (which is our proprietary code) and use ERPNext's MIT-licensed Frappe APIs. The GPL modules are used as-is without modification.

**PECH AI Integration:**
- AI-powered bookkeeping (auto-categorize transactions)
- Invoice OCR → automatic journal entries
- Tax computation AI (FIRS, VAT, WHT)
- Audit trail analysis and anomaly detection
- Financial forecasting with Prophet/LightGBM

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Odoo Community | LGPL-3.0 | LGPL is OK but Odoo's ecosystem pushes toward Enterprise (proprietary) |
| Apache OFBiz | Apache-2.0 | Outdated UI; smaller community; Java-heavy |
| Akaunting | AGPL-3.0 | AGPL — cannot close-source modifications |

---

## 6. FINTECH / CORE BANKING

### Primary: Apache Fineract

| Attribute | Detail |
|-----------|--------|
| **Website** | [fineract.apache.org](https://fineract.apache.org/) |
| **GitHub** | [github.com/apache/fineract](https://github.com/apache/fineract) |
| **License** | Apache-2.0 |
| **Language** | Java (Spring Boot) |
| **PECH Use** | Wallet management, savings, loans, agent banking, transaction ledger, payment gateway integration |

**Why Fineract:**
- Built for financial inclusion in emerging markets
- Proven in 100+ deployments across Africa and Asia
- Core banking features: accounts, transactions, interest, fees
- Agent banking module (perfect for PECH fintech agent network)
- Apache-2.0 — full freedom to modify and rebrand

**PECH Fintech Features:**
- PECH Wallet (powered by Fineract ledger)
- Agent network management (cash-in/cash-out)
- Micro-loans for solar equipment
- Bill payments integration
- Paystack/Flutterwave payment gateway integration

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Mifos X | Apache-2.0 | Same codebase as Fineract (Mifos donated to Apache) |
| Cyclos | AGPL-3.0 | AGPL — cannot close-source |
| Teller | Proprietary API | Not self-hosted |

---

## 7. LOGISTICS & ROUTING

### Primary: OSRM (Open Source Routing Machine)

| Attribute | Detail |
|-----------|--------|
| **Website** | [project-osrm.org](https://project-osrm.org/) |
| **GitHub** | [github.com/Project-OSRM/osrm-backend](https://github.com/Project-OSRM/osrm-backend) |
| **License** | BSD-2-Clause |
| **Language** | C++ |
| **PECH Use** | Delivery route optimization, hub-and-spoke logistics, installer dispatch, real-time routing |

**Why OSRM:**
- Fastest open-source routing engine
- Uses OpenStreetMap data (good Nigeria coverage from local mapping community)
- Handles matrix routing (100+ delivery points optimization)
- Self-hosted — no API call limits or costs

**PECH Logistics Features:**
- Hub-and-spoke delivery optimization (Lagos hubs → distribution points)
- Installer dispatch (nearest qualified installer)
- Real-time delivery tracking
- Fleet management route planning
- Last-mile delivery optimization

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Valhalla | MIT | Slightly slower; less mature than OSRM |
| GraphHopper | Apache-2.0 | Java-based; good alternative but OSRM is faster for pure routing |
| Google Maps API | Proprietary | Expensive at scale; vendor lock-in |

**Complementary Tools:**
| Tool | License | Purpose |
|------|---------|---------|
| OpenStreetMap | ODbL | Map data source for Nigeria |
| Nominatim | GPL-2.0 | Geocoding (address → coordinates) — use as service, don't modify |
| Leaflet.js | BSD-2 | Map frontend rendering |

---

## 8. IoT PLATFORM

### Primary: ThingsBoard Community Edition

| Attribute | Detail |
|-----------|--------|
| **Website** | [thingsboard.io](https://thingsboard.io/) |
| **GitHub** | [github.com/thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) |
| **License** | Apache-2.0 (Community Edition) |
| **Language** | Java |
| **PECH Use** | Solar panel monitoring, inverter telemetry, energy usage dashboards, device management, alerts |

**Why ThingsBoard:**
- Purpose-built for IoT device management
- Real-time dashboards and rule engine
- MQTT, CoAP, HTTP device protocols
- Multi-tenant — each customer sees their own devices
- Apache-2.0 — can extend and rebrand

**PECH IoT Features:**
- Solar panel performance monitoring (voltage, current, temperature, yield)
- Inverter status and fault alerts
- Battery state-of-charge tracking
- Energy consumption analytics
- Predictive maintenance alerts (AI-powered)
- Remote device configuration

> **Important:** Use **Community Edition only** (Apache-2.0). Professional Edition (PE) is proprietary.

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Mainflux (now SuperMQ) | Apache-2.0 | Lighter but less mature dashboards |
| Node-RED | Apache-2.0 | Good for prototyping; not a full IoT platform |
| AWS IoT Core | Proprietary | Vendor lock-in; expensive at scale |

---

## 9. CUSTOMER SUPPORT

### Primary: Chatwoot

| Attribute | Detail |
|-----------|--------|
| **Website** | [chatwoot.com](https://www.chatwoot.com/) |
| **GitHub** | [github.com/chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) |
| **License** | MIT |
| **Language** | Ruby on Rails |
| **PECH Use** | Customer support across all channels (web chat, WhatsApp, email, social), AI chatbot integration |

**Why Chatwoot:**
- Omnichannel support (web, WhatsApp, Facebook, email, Telegram)
- WhatsApp integration is critical for Nigeria (most-used messaging app)
- MIT license — embed and rebrand freely
- API for AI chatbot integration (connect PECH's LLMs)
- Conversation handoff from bot to human agents

**PECH AI Integration:**
- First-response AI chatbot (Qwen2.5-7B answers common questions)
- Auto-categorize and route tickets (DistilBERT)
- Suggested responses for human agents
- Sentiment analysis on conversations
- Knowledge base search (RAG pipeline)

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Zammad | AGPL-3.0 | AGPL — cannot close-source modifications |
| Rocket.Chat | MIT | More chat-focused; less support-workflow tooling |
| Freshdesk | Proprietary | Per-agent pricing; vendor lock-in |

---

## 10. WORKFLOW AUTOMATION

### Primary: Apache Airflow

| Attribute | Detail |
|-----------|--------|
| **Website** | [airflow.apache.org](https://airflow.apache.org/) |
| **GitHub** | [github.com/apache/airflow](https://github.com/apache/airflow) |
| **License** | Apache-2.0 |
| **Language** | Python |
| **PECH Use** | Data pipelines, ETL, model training schedules, report generation, batch processing |

**Why Airflow:**
- Industry standard for workflow orchestration
- Python-native — same language as PECH's AI/ML stack
- DAG-based scheduling (define complex dependencies)
- Huge connector ecosystem (databases, APIs, cloud services)
- Apache-2.0 — no restrictions

**PECH Workflows:**
- Daily RAG data ingestion (business data → embeddings → Qdrant)
- Model retraining pipelines (weekly/monthly)
- Financial report generation
- Invoice processing pipeline (OCR → categorization → journal entry)
- IoT data aggregation and alerting

> **Replaced n8n** — n8n uses a "Sustainable Use License" that restricts competing SaaS offerings. Since PECH may sell automation features, Airflow is the safe choice.

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| n8n | Sustainable Use License | **Cannot resell as automation platform** — license explicitly restricts this |
| Prefect | Apache-2.0 | Good alternative; newer; consider for simpler workflows |
| Temporal | MIT | Better for long-running workflows; more complex setup |
| Dagster | Apache-2.0 | Modern alternative; smaller community than Airflow |

---

## 11. BUSINESS INTELLIGENCE & ANALYTICS

### Primary: Apache Superset

| Attribute | Detail |
|-----------|--------|
| **Website** | [superset.apache.org](https://superset.apache.org/) |
| **GitHub** | [github.com/apache/superset](https://github.com/apache/superset) |
| **License** | Apache-2.0 |
| **Language** | Python (Flask) + TypeScript (React) |
| **PECH Use** | Business dashboards, sales analytics, energy monitoring charts, financial reports, AI metrics |

**Why Superset:**
- Enterprise-grade BI with beautiful visualizations
- SQL Lab for ad-hoc queries
- Dashboard embedding (embed PECH-branded dashboards in customer portals)
- Role-based access (different dashboards per vertical)
- Apache-2.0 — can embed in proprietary products

> **Replaced Metabase** — Metabase is **AGPL-3.0**, which requires sharing source code of modifications when served to users. Since PECH will embed custom dashboards in subscription products, AGPL is incompatible.

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Metabase | **AGPL-3.0** | **Must open-source modifications when served** — incompatible with PECH's model |
| Grafana | AGPL-3.0 | Same AGPL issue; better for metrics than BI |
| Redash | BSD-2 | Simpler than Superset; less visualization options |

---

## 12. AI/ML INFRASTRUCTURE

### Model Serving

| Tool | License | PECH Use | Link |
|------|---------|----------|------|
| **Ollama** | MIT | Phase 1 — simple model management, pull & run | [github.com/ollama/ollama](https://github.com/ollama/ollama) |
| **vLLM** | Apache-2.0 | Phase 2+ — production serving with batching, high throughput | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) |
| **llama.cpp** | MIT | CPU inference, GGUF quantized models | [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) |

### AI Frameworks

| Tool | License | PECH Use | Link |
|------|---------|----------|------|
| **LangChain** | MIT | RAG pipelines, chains, document loaders | [github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain) |
| **LangGraph** | MIT | AI agent framework (multi-step reasoning) | [github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) |
| **Haystack** | Apache-2.0 | Alternative RAG framework | [github.com/deepset-ai/haystack](https://github.com/deepset-ai/haystack) |
| **Sentence Transformers** | Apache-2.0 | Embedding generation | [github.com/UKPLab/sentence-transformers](https://github.com/UKPLab/sentence-transformers) |

### ML Libraries

| Tool | License | PECH Use | Link |
|------|---------|----------|------|
| **PyTorch** | BSD-3 | Deep learning framework | [github.com/pytorch/pytorch](https://github.com/pytorch/pytorch) |
| **Hugging Face Transformers** | Apache-2.0 | Model hub, tokenizers, fine-tuning | [github.com/huggingface/transformers](https://github.com/huggingface/transformers) |
| **PEFT** | Apache-2.0 | Parameter-efficient fine-tuning (LoRA, QLoRA) | [github.com/huggingface/peft](https://github.com/huggingface/peft) |
| **scikit-learn** | BSD-3 | Traditional ML | [github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) |

**Deployment Path:**
1. **Phase 1:** Ollama (pull models, run with one command)
2. **Phase 2:** Ollama for dev, vLLM for production (higher throughput)
3. **Phase 3:** vLLM cluster with load balancing via APISIX

---

## 13. VECTOR DATABASE

### Primary: Qdrant

| Attribute | Detail |
|-----------|--------|
| **Website** | [qdrant.tech](https://qdrant.tech/) |
| **GitHub** | [github.com/qdrant/qdrant](https://github.com/qdrant/qdrant) |
| **License** | Apache-2.0 |
| **Language** | Rust |
| **PECH Use** | Store embeddings for RAG pipeline, semantic search, product similarity |

**Why Qdrant:**
- Written in Rust — extremely fast and memory-efficient
- Built-in filtering (combine vector search with metadata filters)
- Scales from single node to cluster
- REST + gRPC APIs
- Apache-2.0

**PECH RAG Pipeline:**
1. Business data (products, docs, support tickets) → chunked
2. Chunks → embedding model (MiniLM/Nomic) → vectors
3. Vectors stored in Qdrant with metadata
4. User query → embed → Qdrant nearest-neighbor search → context
5. Context + query → LLM → answer

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Milvus | Apache-2.0 | Heavier; needs etcd + MinIO; overkill for Phase 1 |
| ChromaDB | Apache-2.0 | Simpler but less production-ready than Qdrant |
| Weaviate | BSD-3 | Good alternative; slightly less performance than Qdrant |
| pgvector | PostgreSQL License | Viable for small scale; lacks Qdrant's advanced features |

---

## 14. DATABASES

### Primary Stack

| Database | License | PECH Use | Link |
|----------|---------|----------|------|
| **PostgreSQL** | PostgreSQL License (MIT-like) | Primary OLTP database for all microservices | [postgresql.org](https://www.postgresql.org/) |
| **Apache AGE** | Apache-2.0 | Graph queries on PostgreSQL (knowledge graphs, relationships) | [github.com/apache/age](https://github.com/apache/age) |
| **Redis** | BSD-3 (v7.0) / RSALv2+SSPLv1 (v7.4+) | Caching, sessions, real-time pub/sub | [github.com/redis/redis](https://github.com/redis/redis) |
| **DuckDB** | MIT | Analytical queries, OLAP, data exploration | [github.com/duckdb/duckdb](https://github.com/duckdb/duckdb) |

> **Redis License Note:** Redis changed to dual RSALv2+SSPL from v7.4+. Use **Redis v7.0** (BSD-3) or switch to **Valkey** (BSD-3, Linux Foundation fork) or **KeyDB** (BSD-3) for fully permissive licensing.

> **Replaced Neo4j** — Neo4j Community is GPL-3.0, Enterprise is commercial. **Apache AGE** runs graph queries directly on PostgreSQL (which PECH already uses), saving an entire database deployment. Apache-2.0 licensed.

**Alternatives for Graph:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Neo4j Community | GPL-3.0 | GPL; requires separate database deployment |
| ArangoDB | Apache-2.0 | Full graph DB; overkill when AGE works on existing PostgreSQL |

---

## 15. MESSAGE QUEUE / EVENT STREAMING

### Primary: Apache Kafka

| Attribute | Detail |
|-----------|--------|
| **Website** | [kafka.apache.org](https://kafka.apache.org/) |
| **GitHub** | [github.com/apache/kafka](https://github.com/apache/kafka) |
| **License** | Apache-2.0 |
| **Language** | Java / Scala |
| **PECH Use** | Event streaming between microservices, real-time data pipelines, IoT data ingestion |

**Why Kafka:**
- Industry standard for event streaming
- Handles millions of events per second
- Durable message storage (replay capability)
- Connect ecosystem for database CDC (change data capture)

**Startup Alternative: NATS**

| Attribute | Detail |
|-----------|--------|
| **GitHub** | [github.com/nats-io/nats-server](https://github.com/nats-io/nats-server) |
| **License** | Apache-2.0 |
| **Why Consider** | Much simpler to deploy; single binary; lower resource usage; JetStream for persistence |

**PECH Recommendation:** Start with **NATS** (Phase 1 — simpler, lighter). Migrate to **Kafka** when event volume requires it (Phase 2/3).

---

## 16. MAPPING & GEOSPATIAL

### PMAP / AMAP Platform Stack

| Tool | License | PECH Use | Link |
|------|---------|----------|------|
| **OpenStreetMap** | ODbL | Base map data for Nigeria/Africa | [openstreetmap.org](https://www.openstreetmap.org/) |
| **MapLibre GL JS** | BSD-3 | Map rendering frontend (replaced Mapbox GL JS) | [github.com/maplibre/maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js) |
| **Nominatim** | GPL-2.0 | Geocoding (address lookup) — use as service | [github.com/osm-search/Nominatim](https://github.com/osm-search/Nominatim) |
| **tile-server-gl** | BSD-2 | Self-hosted map tile server | [github.com/maptiler/tileserver-gl](https://github.com/maptiler/tileserver-gl) |
| **PostGIS** | GPL-2.0 | Geospatial PostgreSQL extension — use as service | [postgis.net](https://postgis.net/) |
| **OSRM** | BSD-2 | Routing (see Logistics section) | [project-osrm.org](https://project-osrm.org/) |

**PECH PMAP Features:**
- Africa-focused digital mapping platform
- Business location directory
- Solar installation site assessment
- Delivery zone mapping
- Installer coverage visualization

---

## 17. PROCUREMENT / TENDERING

### Primary: OpenProcurement

| Attribute | Detail |
|-----------|--------|
| **Website** | [openprocurement.io](https://openprocurement.io/) |
| **GitHub** | [github.com/ProzorroUKR/openprocurement.api](https://github.com/ProzorroUKR/openprocurement.api) |
| **License** | Apache-2.0 |
| **Language** | Python |
| **PECH Use** | Solar project tenders, government procurement, vendor bidding, RFQ management |

**Why OpenProcurement:**
- Built for government/enterprise procurement
- Transparent bidding process
- Multi-lot tender support
- Apache-2.0

---

## 18. CMS / CONTENT MANAGEMENT

### Primary: Strapi

| Attribute | Detail |
|-----------|--------|
| **Website** | [strapi.io](https://strapi.io/) |
| **GitHub** | [github.com/strapi/strapi](https://github.com/strapi/strapi) |
| **License** | MIT (Community Edition) |
| **Language** | TypeScript (Node.js) |
| **PECH Use** | Blog, knowledge base, help center, marketing content, API documentation portal |

**Alternatives Considered:**
| Alternative | License | Why Not Chosen |
|-------------|---------|----------------|
| Directus | GPL-3.0 (core) / BSL (cloud) | GPL for core; business license issues |
| Ghost | MIT | Blog-focused only; less API flexibility |
| Payload CMS | MIT | Good alternative; newer; smaller community |

---

## 19. MONITORING & OBSERVABILITY

| Tool | License | PECH Use | Link |
|------|---------|----------|------|
| **Prometheus** | Apache-2.0 | Metrics collection | [github.com/prometheus/prometheus](https://github.com/prometheus/prometheus) |
| **Grafana** | AGPL-3.0 | Metrics dashboards (use as service, don't modify) | [github.com/grafana/grafana](https://github.com/grafana/grafana) |
| **Loki** | AGPL-3.0 | Log aggregation (use as service) | [github.com/grafana/loki](https://github.com/grafana/loki) |
| **Jaeger** | Apache-2.0 | Distributed tracing | [github.com/jaegertracing/jaeger](https://github.com/jaegertracing/jaeger) |
| **Uptime Kuma** | MIT | Uptime monitoring | [github.com/louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) |

> **Grafana/Loki Note:** These are AGPL-3.0 but we use them as internal monitoring tools (not modified or embedded in products). AGPL only triggers when you modify and serve the software — using as-is for internal dashboards is fine.

---

## 20. CONTAINER ORCHESTRATION

| Tool | License | PECH Use | Link |
|------|---------|----------|------|
| **Docker** | Apache-2.0 (Engine) | Container runtime | [github.com/moby/moby](https://github.com/moby/moby) |
| **Kubernetes (K8s)** | Apache-2.0 | Container orchestration (Phase 2+) | [github.com/kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) |
| **K3s** | Apache-2.0 | Lightweight Kubernetes (Phase 2) | [github.com/k3s-io/k3s](https://github.com/k3s-io/k3s) |
| **Portainer** | Zlib | Docker management UI | [github.com/portainer/portainer](https://github.com/portainer/portainer) |

**Deployment Path:**
1. **Phase 1:** Docker Compose + Portainer (simple, visual management)
2. **Phase 2:** K3s (lightweight K8s for single/few nodes)
3. **Phase 3:** Full Kubernetes cluster

---

## 21. CI/CD

| Tool | License | PECH Use | Link |
|------|---------|----------|------|
| **Gitea** | MIT | Self-hosted Git (code repository) | [github.com/go-gitea/gitea](https://github.com/go-gitea/gitea) |
| **Woodpecker CI** | Apache-2.0 | CI/CD pipelines | [github.com/woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker) |
| **Harbor** | Apache-2.0 | Container registry | [github.com/goharbor/harbor](https://github.com/goharbor/harbor) |

**Why Not GitHub/GitLab:**
- GitHub Actions is proprietary (vendor lock-in)
- GitLab CE is MIT but heavyweight
- Gitea + Woodpecker = lightweight, self-hosted, fully open

---

## 22. LICENSE REPLACEMENTS SUMMARY

Tools originally considered that had license issues, and their PECH-approved replacements:

| Original Tool | Problem License | Replacement | License | Why Better |
|--------------|----------------|-------------|---------|------------|
| **Metabase** | AGPL-3.0 | **Apache Superset** | Apache-2.0 | Same BI capabilities; can embed in products |
| **n8n** | Sustainable Use License | **Apache Airflow** | Apache-2.0 | Full workflow automation; no resale restrictions |
| **YOLOv8** | AGPL-3.0 | **RT-DETR (PaddlePaddle)** | Apache-2.0 | Real-time detection; no copyleft |
| **Sharetribe Flex** | Proprietary SaaS | **Medusa.js** | MIT | Already in stack; extend for all marketplace needs |
| **Neo4j** | GPL-3.0 (Community) | **Apache AGE** | Apache-2.0 | Graph queries on existing PostgreSQL; no extra DB |
| **AutoGen** | MIT (but deprecated) | **LangGraph** | MIT | More mature; better agent framework |
| **Redis 7.4+** | RSALv2+SSPL | **Redis 7.0 / Valkey** | BSD-3 | Pin version or use Linux Foundation fork |

---

## 23. INTEGRATION MAP

How all 25+ platforms connect in the PECH ecosystem:

```
┌─────────────────────────────────────────────────────────┐
│                    USER REQUESTS                         │
│         (Web, Mobile, WhatsApp, IoT Devices)            │
└──────────────────────┬──────────────────────────────────┘
                       │
                ┌──────▼──────┐
                │ Apache APISIX│  ← API Gateway (rate limit, auth, routing)
                │  (Gateway)   │
                └──────┬──────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   ┌────▼────┐   ┌────▼────┐   ┌────▼────┐
   │Keycloak │   │ Medusa  │   │ Chatwoot│
   │ (Auth)  │   │(Commerce│   │(Support)│
   └─────────┘   │ + Mktpl)│   └────┬────┘
                  └────┬────┘        │
                       │        ┌────▼────┐
        ┌──────────────┤        │ AI Core │ ← LLMs via Ollama/vLLM
        │              │        │(Qwen,   │
   ┌────▼────┐   ┌────▼────┐   │Whisper, │
   │ ERPNext │   │Fineract │   │ etc.)   │
   │  (ERP)  │   │(Fintech)│   └────┬────┘
   └─────────┘   └─────────┘        │
                                ┌────▼────┐
        ┌───────────────────────│ Qdrant  │ ← Vector DB for RAG
        │                       │(Vectors)│
   ┌────▼────┐                  └─────────┘
   │ThingsBoard
   │  (IoT)  │   ┌─────────┐   ┌─────────┐
   └─────────┘   │  OSRM   │   │ Superset│
                  │(Routing)│   │  (BI)   │
                  └─────────┘   └─────────┘
                       │
                ┌──────▼──────┐
                │ PostgreSQL  │ ← Primary database (+ AGE for graphs)
                │ + Redis     │ ← Cache + sessions
                │ + NATS/Kafka│ ← Event streaming
                └─────────────┘
```

---

*This document is confidential to PECH Group Holdings Ltd. Last updated: March 2026.*
