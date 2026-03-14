# PECH African Business Intelligence Platform

> **Document Reference:** PECH-ABIP-2026-001
> **Version:** 1.0
> **Effective Date:** March 2026
> **Status:** Strategic Planning

---

## 1. PLATFORM OVERVIEW

The **PECH African Business Intelligence Platform** is PECH Group Holdings' 11th business vertical — a lead generation, market research, and B2B marketplace platform purpose-built for African markets. It operates similarly to ZoomInfo, Apollo.io, LinkedIn Sales Navigator, Lusha, Seamless.ai, and LeadIQ, but is **Africa-focused** and **self-hosted** using PECH's AI infrastructure.

### Core Modules

| # | Module | Description | Revenue Model |
|---|--------|-------------|---------------|
| 1 | **Lead Generation** | AI-powered contact discovery, business profiling, lead scoring | Subscription tiers + per-lead credits |
| 2 | **Market Research** | Industry analysis, competitor mapping, trend reports | Report sales + subscription |
| 3 | **Supplier Discovery** | Verified supplier database for solar, electrical, IoT components | Listing fees + premium placement |
| 4 | **Installer Networks** | Certified installer matching, skills verification | Commission per job match |
| 5 | **B2B Marketplace** | Business-to-business product/service directory | Transaction fees + advertising |

---

## 2. TARGET SECTORS & LEAD CATEGORIES

### 2.1 Education Sector

**Target Leads:**
- Private schools (primary, secondary, tertiary) — administrators, owners, IT heads
- EdTech startups in Nigeria and across Africa
- STEM training centers and coding bootcamps
- University departments (Engineering, Computer Science, Business)
- Vocational training institutes
- Online education platforms operating in Africa

**Data Points to Collect:**
- School name, address, LGA, state
- Decision maker name, title, phone, email
- School website, social media handles
- Student population size
- Technology adoption level (has computer lab, uses LMS, etc.)
- Registration status (WAEC center, NUC accredited, etc.)

**How They Use PECH Platform:**
- Schools register on marketplace for educational technology purchases
- Use PECH IoT for smart campus solutions (energy monitoring, security)
- Access PECH Fintech for fee collection and payment processing
- Use PECH Solar for campus power solutions

### 2.2 Healthcare & Telemedicine

**Target Leads:**
- Hospitals (private and public) — administrators, medical directors
- Pharmacies and pharmaceutical distributors
- Telemedicine practitioners (doctors, nurses, pharmacists)
- Medical content creators on social media
- Nigerian medical practitioners abroad (diaspora doctors)
- Medical students interested in content creation or marketing
- Health-tech startups
- Traditional medicine practitioners with online presence

**Data Points to Collect:**
- Practitioner name, specialty, license number (MDCN, PCN, NMCN)
- Practice/hospital name, address
- Phone numbers (office, personal/WhatsApp)
- Social media: Instagram, Twitter/X, YouTube, TikTok, LinkedIn
- Website/blog URL
- Online consultation platforms they use
- For diaspora: current country, specialty, willingness to do telemedicine
- Content creation history (YouTube channel, blog posts, social media health content)

**How They Use PECH Platform:**
- Create paid health content and answer questions on the platform
- Sell medical supplies via marketplace
- Offer telemedicine consultations through PECH's video integration
- Use PECH Fintech for payment processing

### 2.3 Solar & Electrical (Direct Sales Targets)

**Target Leads:**
- Solar installation companies
- Electrical contractors and electricians
- Energy consultants
- Solar panel and inverter distributors
- Battery suppliers
- Building contractors who subcontract electrical work
- Facility managers (hotels, factories, offices)
- Real estate developers

**Data Points to Collect:**
- Company name, owner/manager name
- Business address, LGA, state
- Phone, WhatsApp, email
- CAC registration number
- Product lines carried
- Installation capacity (residential, commercial, industrial)
- Social media presence
- Existing marketplace presence (Jumia, Jiji, etc.)

### 2.4 Logistics & Transportation

**Target Leads:**
- Logistics companies (last-mile, freight, warehousing)
- Fleet owners and operators
- Individual drivers (motorcycle, van, truck)
- Ride-hailing drivers (Bolt, Uber, InDrive)
- Courier services
- Cold chain logistics companies
- Import/export agents and clearing agents
- Warehouse operators

**Data Points to Collect:**
- Company/individual name
- Fleet size and vehicle types
- Service area (local, interstate, international)
- Phone, WhatsApp, email
- Social media handles
- Past companies worked for (LinkedIn)
- Professional certifications
- Driver's license class
- Vehicle registration details (if available)

### 2.5 General Commerce & Marketplace Vendors

**Target Leads:**
- Existing sellers on Jumia, Jiji, Konga
- Social commerce sellers (Instagram, WhatsApp, Facebook)
- Market traders in major markets (Computer Village, Alaba, Trade Fair, etc.)
- Wholesale distributors
- Import traders (China, Dubai, UK)
- Small business owners registered with SMEDAN

### 2.6 Social Media Influencers & Brand Ambassadors

**Target Leads:**
- Nigerian social media influencers (all platforms)
- Content creators across niches (tech, lifestyle, education, health, comedy)
- Brand ambassadors currently or previously engaged
- Micro-influencers (5K-50K followers)
- Macro-influencers (50K-500K followers)
- Mega-influencers (500K+ followers)
- UGC (User Generated Content) creators
- Hidden talent — people with skills but low following

**Data Points to Collect:**
- Full name, stage name/handle
- All social media platforms and handles with follower counts
- Content niche/category
- Engagement rate
- Previous brand deals and estimated rates
- Current brand ambassadorships
- Contact information (email, phone, management)
- Location (state, city)
- Demographics of audience

### 2.7 Graphic Designers & Creative Professionals

**Target Leads:**
- Freelance graphic designers
- Design agencies
- UI/UX designers
- Motion graphics artists
- Video editors
- Photographers
- Brand identity designers

### 2.8 Marketers & Sales Professionals

**Target Leads:**
- Digital marketers (SEO, SEM, social media marketing)
- Field marketers and brand activators
- Sales executives and business development professionals
- Affiliate marketers
- Event marketers
- Real estate marketers/agents

**Data Points to Collect:**
- Full name, current title
- LinkedIn profile URL
- Current and past employers
- Academic background
- Professional certifications (Google Ads, HubSpot, etc.)
- Skills inventory
- Years of experience
- Availability status
- Portfolio or work samples URL
- References or endorsements
- Contact: phone, email, WhatsApp
- Location and willingness to relocate

---

## 3. DATA SOURCING STRATEGY

### 3.1 Primary Data Sources (Web Scraping & APIs)

| Source | What to Extract | Method |
|--------|----------------|--------|
| **Google Maps** | Business listings, addresses, phone numbers, reviews, categories | Google Places API + custom crawler |
| **Jumia** | Seller profiles, product categories, ratings, contact info | Web scraper (BeautifulSoup/Scrapy) |
| **Jiji** | Seller listings, phone numbers, locations, product categories | Web scraper |
| **Konga** | Vendor profiles, product ranges | Web scraper |
| **LinkedIn** | Professional profiles, work history, skills, connections | LinkedIn Sales Navigator + custom enrichment |
| **Instagram** | Influencer profiles, follower counts, engagement, bio links | Instagram Graph API + scraper |
| **Twitter/X** | Influencer profiles, follower counts, tweet frequency | X API |
| **YouTube** | Creator profiles, subscriber counts, content categories | YouTube Data API |
| **TikTok** | Creator profiles, follower counts, video categories | TikTok API |
| **Facebook** | Business pages, groups, marketplace listings | Facebook Graph API |
| **CAC Portal** | Company registration details, directors | Manual + API (when available) |
| **MDCN Portal** | Medical practitioner registration verification | Manual lookup |
| **PCN Portal** | Pharmacist registration verification | Manual lookup |
| **NUC Portal** | University accreditation status | Public data |
| **WAEC** | School registration status | Public data |
| **SMEDAN** | Registered SMEs | Public database |

### 3.2 Secondary Data Sources

| Source | What to Extract |
|--------|----------------|
| **Nairaland** | Business discussions, service providers, reviews |
| **BuyPower.ng / NERC** | Licensed electricity distributors |
| **NESREA** | Environmental service providers |
| **SON** | Standards-certified product manufacturers |
| **Nigerian Yellow Pages** | Business listings |
| **ConnectNigeria** | Business directory |
| **VConnect** | Service provider listings and reviews |
| **Nairametrics** | Business news, company profiles |

### 3.3 Enrichment & Verification

For every lead collected, the platform runs:

1. **Phone verification** — Check if number is active (WhatsApp API, Truecaller API)
2. **Email verification** — SMTP validation, disposable email check
3. **Social media cross-reference** — Match phone/email to social profiles
4. **Address geocoding** — Convert addresses to coordinates via Google Geocoding / OpenStreetMap Nominatim
5. **Duplicate detection** — AI-powered fuzzy matching to prevent duplicate entries
6. **Lead scoring** — ML model scores each lead based on relevance, engagement potential, business size

---

## 4. AI/ML COMPONENTS

### Models Used (All License-Safe)

| Component | Model | License | Purpose |
|-----------|-------|---------|---------|
| **Entity Extraction** | Qwen2.5-7B | Apache-2.0 | Extract names, addresses, phones from unstructured text |
| **Lead Scoring** | XGBoost | Apache-2.0 | Score leads by conversion probability |
| **Classification** | LightGBM | MIT | Classify businesses by sector, size, relevance |
| **Text Similarity** | MiniLM-L6 | MIT | Deduplicate leads, match similar businesses |
| **Embeddings** | Nomic-Embed | Apache-2.0 | Semantic search across lead database |
| **Web Scraping** | Scrapy + BeautifulSoup | BSD | Structured data extraction |
| **OCR** | PaddleOCR | Apache-2.0 | Extract text from business card images, flyers |
| **Vision** | Qwen2.5-VL | Apache-2.0 | Analyze business photos, storefronts |

### Data Pipeline

```
Web Scrapers → Raw Data Store (PostgreSQL)
                     ↓
            Data Cleaning (Airflow DAG)
                     ↓
            Entity Extraction (Qwen2.5)
                     ↓
            Deduplication (MiniLM-L6 embeddings)
                     ↓
            Lead Scoring (XGBoost)
                     ↓
            Enrichment (phone/email verification)
                     ↓
            Indexed in Qdrant (vector search)
                     ↓
            Available via API / Dashboard
```

---

## 5. LEAD RANKING SYSTEM

Every lead and potential hire is ranked using a weighted scoring system:

### For Business Leads (Potential Customers/Vendors)

| Factor | Weight | Score Range |
|--------|--------|-------------|
| Business size (employees, revenue) | 20% | 1-10 |
| Online presence strength | 15% | 1-10 |
| Technology adoption readiness | 15% | 1-10 |
| Location accessibility | 10% | 1-10 |
| Decision-maker contact availability | 15% | 1-10 |
| Sector relevance to PECH | 15% | 1-10 |
| Engagement signals (responded to outreach, etc.) | 10% | 1-10 |

### For Potential Hires (Marketers, Creators, Ambassadors)

| Factor | Weight | Score Range |
|--------|--------|-------------|
| Relevant experience (years + quality) | 25% | 1-10 |
| Skills match | 20% | 1-10 |
| Portfolio/work quality | 15% | 1-10 |
| Availability | 10% | 1-10 |
| Online reputation/references | 10% | 1-10 |
| Academic background | 10% | 1-10 |
| Location/logistics | 10% | 1-10 |

### For Influencers/Ambassadors

| Factor | Weight | Score Range |
|--------|--------|-------------|
| Follower count (across platforms) | 15% | 1-10 |
| Engagement rate | 20% | 1-10 |
| Content relevance to PECH sectors | 20% | 1-10 |
| Previous brand deal track record | 15% | 1-10 |
| Estimated cost per post | 10% | 1-10 |
| Audience demographics match | 10% | 1-10 |
| Professionalism / hidden talent potential | 10% | 1-10 |

---

## 6. MICROSERVICES ARCHITECTURE

The Business Intelligence Platform adds these microservices to the PECH ecosystem:

| # | Service | Tech Stack | Description |
|---|---------|------------|-------------|
| 1 | `bi-scraper-service` | Python (Scrapy + Airflow) | Web crawling and data extraction |
| 2 | `bi-enrichment-service` | Python (FastAPI) | Lead enrichment and verification |
| 3 | `bi-scoring-service` | Python (XGBoost + FastAPI) | Lead scoring and ranking |
| 4 | `bi-search-service` | Python (Qdrant + FastAPI) | Semantic search across lead database |
| 5 | `bi-dashboard-api` | Node.js (Express) | Dashboard backend API |
| 6 | `bi-dashboard-web` | React (Next.js) | Dashboard frontend |
| 7 | `bi-export-service` | Python (FastAPI) | CSV/Excel/PDF export of lead lists |
| 8 | `bi-notification-service` | Node.js | Lead alerts and notifications |
| 9 | `bi-marketplace-bridge` | Python (FastAPI) | Integration with PECH Marketplace |
| 10 | `bi-crm-bridge` | Python (FastAPI) | Integration with PECH ERP/CRM |

---

## 7. SUBSCRIPTION TIERS

| Tier | Price (₦/month) | Leads/month | Features |
|------|-----------------|-------------|----------|
| **Starter** | ₦15,000 | 100 | Basic search, lead export, email only |
| **Growth** | ₦50,000 | 500 | Phone + email, lead scoring, basic filters |
| **Professional** | ₦150,000 | 2,000 | All contacts, advanced filters, API access, CRM integration |
| **Enterprise** | Custom | Unlimited | Dedicated scraping, custom reports, priority support |

---

## 8. COMPETITIVE LANDSCAPE

| Platform | Coverage | Pricing | Africa Focus |
|----------|----------|---------|-------------|
| ZoomInfo | Global (US-heavy) | $15,000+/yr | Minimal |
| Apollo.io | Global | $49-119/mo | Limited |
| LinkedIn Sales Nav | Global | $79-139/mo | Some Africa data |
| Lusha | Global | $29-69/mo | Minimal |
| **PECH BI Platform** | **Africa-first (Nigeria start)** | **₦15K-150K/mo** | **100% Africa-focused** |

### PECH Advantages:
- **Africa-native data** — sourced from African platforms, markets, directories
- **Local language support** — Yoruba, Igbo, Hausa, Pidgin via Whisper STT
- **Mobile-first** — designed for African mobile users
- **Integrated ecosystem** — connected to PECH's 10 other verticals
- **Self-hosted AI** — data never leaves Nigerian servers (NDPA compliant)
- **Affordable pricing** — designed for Nigerian SMEs and startups

---

## 9. IMPLEMENTATION ROADMAP

### Phase 1: Crawl (Months 1-3)
- Build core scrapers for Google Maps, Jumia, Jiji, LinkedIn
- Implement basic lead storage in PostgreSQL
- Build simple dashboard for lead viewing and export
- Manual verification workflow

### Phase 2: Walk (Months 4-6)
- Add AI scoring with XGBoost
- Implement vector search with Qdrant
- Add enrichment pipeline (phone/email verification)
- Build API for third-party integrations
- Launch subscription model

### Phase 3: Run (Months 7-12)
- Scale to 10+ African countries
- Add real-time monitoring of new business listings
- Implement AI-powered market research reports
- B2B marketplace features
- Installer network matching
- Integration with all PECH verticals

---

## 10. COMPLIANCE & ETHICS

### Data Protection
- **NDPA 2023** (Nigeria Data Protection Act) — full compliance
- Consent-based data collection where required
- Data minimization — collect only what's needed
- Right to be forgotten — businesses can request data removal
- Regular data audits and retention policies

### Ethical Scraping
- Respect robots.txt
- Rate limiting on all scrapers
- No scraping of private/authenticated data without consent
- Publicly available information only
- Clear privacy policy and terms of service

---

## 11. BUDGET ALLOCATION

| Item | Cost (₦) | Notes |
|------|----------|-------|
| Scraper development | ₦2,000,000 | Python developers, 3 months |
| AI model fine-tuning | ₦1,500,000 | Lead scoring, entity extraction |
| Dashboard development | ₦2,500,000 | Frontend + backend |
| Data verification tools | ₦500,000 | Phone/email verification APIs |
| Infrastructure (Year 1) | ₦1,000,000 | Additional storage, compute |
| Marketing & launch | ₦1,500,000 | Product launch, early adopters |
| **Total** | **₦9,000,000** | ~$5,800 USD |

---

*This document is part of the PECH Group Holdings Ltd ecosystem documentation. Confidential — internal use only.*
