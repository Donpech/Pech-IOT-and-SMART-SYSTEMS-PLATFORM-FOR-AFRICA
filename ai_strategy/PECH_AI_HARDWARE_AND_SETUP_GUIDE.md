# PECH GROUP HOLDINGS LTD

## AI Hardware & Setup Guide — Procurement, Installation, Configuration

### CONFIDENTIAL

---

**PECH Group Holdings Ltd**
Lagos, Nigeria | Website: [pechgroupholdings.tech](https://pechgroupholdings.tech)

---

> **Document Reference:** PECH-AI-HW-2026-001
> **Version:** 1.0
> **Effective Date:** March 2026
> **Prepared By:** Technology Department
> **Approved By:** Managing Director / CEO

---

## TABLE OF CONTENTS

1. [Hardware Strategy Overview](#1-hardware-strategy-overview)
2. [Phase 1 — TRX50 Workstation (1 GPU)](#2-phase-1--trx50-workstation-1-gpu)
3. [Phase 2 — Upgrade (Add GPU + RAM + Storage)](#3-phase-2--upgrade-add-gpu--ram--storage)
4. [Phase 3 — Co-Location & Scaling](#4-phase-3--co-location--scaling)
5. [China Sourcing Guide](#5-china-sourcing-guide)
6. [Nigeria Import Process](#6-nigeria-import-process)
7. [Landed Cost Calculations](#7-landed-cost-calculations)
8. [Supporting Infrastructure](#8-supporting-infrastructure)
9. [Server Room Setup](#9-server-room-setup)
10. [Software Installation Guide](#10-software-installation-guide)
11. [Cloud GPU Options](#11-cloud-gpu-options)
12. [Co-Location Options (Lagos)](#12-co-location-options-lagos)
13. [Monitoring & Maintenance](#13-monitoring-maintenance)
14. [Total Budget Summary](#14-total-budget-summary)

---

## 1. HARDWARE STRATEGY OVERVIEW

### Zero-Waste Philosophy

PECH's AI hardware strategy follows a **zero-waste single-platform** approach: buy the right platform from Day 1, add components as you grow, never throw anything away.

| Phase | Timeline | Hardware | AI Capability |
|-------|----------|----------|---------------|
| **Phase 1 (Crawl)** | Months 1-6 | TRX50 Workstation + 1× RTX 4090 | Run 2-3 models simultaneously; develop & test |
| **Phase 2 (Walk)** | Months 7-12 | Same box + 2nd RTX 4090 + more RAM/storage | Production AI with dual-GPU; cloud burst for overflow |
| **Phase 3 (Run)** | Months 13-24 | Co-locate same box + optional 2nd node | Full production; fine-tuned models; high concurrency |

**Every Phase 1 component carries through to Phase 3.** Zero waste. Zero rebuilds. Zero downtime for migration.

### Why Zero-Waste Matters

The old approach (buy a cheap AM5 starter, then replace with a TRX50 production box) wastes money:

| Approach | Phase 1 Cost | Phase 2-3 Cost | 24-Month Total | Waste |
|----------|-------------|----------------|----------------|-------|
| **Old (Starter → Replace)** | ₦5.7M-₦7.7M | ₦11M-₦15M (new box) | ₦16.7M-₦22.7M | ₦1.4M-₦1.9M (entire Phase 1 CPU, mobo, RAM, PSU, case) |
| **Zero-Waste (TRX50 → Upgrade)** | ₦8.2M-₦11M | ₦4.1M-₦5.3M (add GPU+RAM) | ₦12.3M-₦16.3M | ₦0 |
| **Savings** | — | — | **₦4.3M-₦6.4M saved** | **100% reuse** |

### Key Decision: Own vs Cloud

| Factor | Own Hardware | Cloud GPU |
|--------|-------------|-----------|
| **Monthly cost** | ₦0 after purchase (power only) | ₦200K-₦2M/month |
| **Upfront cost** | ₦8.2M-₦16.3M (Phase 1-2) | ₦0 |
| **Latency** | <10ms (local) | 50-200ms (internet) |
| **Data sovereignty** | Full control (NDPA compliant) | Depends on provider |
| **Scaling** | Limited by hardware | Instant scale |
| **Maintenance** | PECH team responsibility | Provider handles |
| **Power dependency** | Lagos grid + backup | Provider's problem |

**PECH Recommendation:** Start with **TRX50 Workstation + cloud GPU for overflow** (Phase 1). Add 2nd GPU when revenue justifies (Phase 2). Co-locate for production reliability (Phase 3).

---

## 2. PHASE 1 — TRX50 WORKSTATION (1 GPU)

**Purpose:** Run 2-3 AI models simultaneously for development, testing, and initial production. Built on a platform that scales to Phase 3 without replacing anything.

### Bill of Materials (BOM)

| # | Component | Specification | China Price (USD) | US Retail (USD) |
|---|-----------|--------------|-------------------|-----------------|
| 1 | **GPU** | NVIDIA RTX 4090 24GB GDDR6X | $1,200-$1,400 | $1,600-$1,800 |
| 2 | **CPU** | AMD Threadripper 7960X (24C/48T, sTR5) | $830-$1,100 | $1,100-$1,400 |
| 3 | **Motherboard** | ASUS Pro WS TRX50-SAGE WiFi (3× PCIe 5.0 x16, 8 DIMM) | $550-$700 | $750-$950 |
| 4 | **RAM** | 128GB DDR5-5600 ECC RDIMM (4×32GB) | $280-$400 | $400-$550 |
| 5 | **Storage (OS)** | 1TB Samsung 990 Pro NVMe Gen4 | $50-$70 | $80-$100 |
| 6 | **Storage (Data)** | 4TB Samsung 990 Pro NVMe Gen4 | $200-$280 | $300-$350 |
| 7 | **PSU** | Seasonic PRIME TX-1600 80+ Titanium (ATX 3.1) | $350-$450 | $450-$550 |
| 8 | **Case** | 4U Rackmount chassis (Rosewill RSV-L4500U) | $120-$180 | $180-$280 |
| 9 | **CPU Cooler** | Noctua NH-U14S TR5-SP6 | $80-$110 | $100-$130 |
| 10 | **Fans** | 3× 140mm Noctua NF-A14 case fans | $30-$45 | $45-$60 |
| | **Subtotal** | | **$3,690-$4,735** | **$5,005-$6,170** |

### Why TRX50 from Day 1 (Not AM5)

| Component | Why This Spec | Why Not AM5 (Cheaper)? |
|-----------|--------------|----------------------|
| **Threadripper 7960X** | 24 cores handle AI inference + web services + data pipelines. 128 PCIe 5.0 lanes for multi-GPU bandwidth | Ryzen 9 7950X has only 28 PCIe lanes — can't feed 2 GPUs properly. Entire CPU+mobo wasted at Phase 2 |
| **TRX50-SAGE** | 3× PCIe 5.0 x16 slots (2 for GPUs + 1 spare), 8 DIMM slots (up to 512GB), 4× M.2 NVMe | X670E only has 1× PCIe x16 + limited DIMM slots. No upgrade path |
| **128GB DDR5 ECC RDIMM** | Required by Threadripper (non-ECC won't work). ECC = production-grade reliability. 4 of 8 DIMM slots used — add 128GB more in Phase 2 | AM5 uses UDIMM (consumer-grade, 4 slots max). If you start AM5, you throw away all RAM when moving to TRX50 |
| **1600W PSU** | Sized for 2× RTX 4090 from Day 1 (dual-GPU peak ~1,200W). Zero power upgrade needed at Phase 2 | A 1000W PSU can't handle 2 GPUs. You'd buy it, then replace it — wasted ₦150K-₦200K |
| **4U Rackmount** | Co-location ready from Day 1. Standard 19" rack compatible. Fits 2× full-length GPUs | A full-tower case can't go into a data center rack. You'd replace the case at Phase 3 |
| **Noctua TR5-SP6** | Purpose-built for Threadripper sTR5 socket. Silent, 250W TDP rated | Different cooler mount from AM5 — another wasted component |

**The TRX50 premium is ₦2.5M-₦3.3M more than AM5 upfront. It saves ₦4.3M-₦6.4M by eliminating a full rebuild at Phase 2.**

### Quality Recommendations (Specific Brands)

| Component | Recommended | Why This One |
|-----------|------------|-------------|
| **PSU** | Seasonic PRIME TX-1600 (NOT generic 1600W) | 80+ Titanium = 94% efficiency, 12-year warranty, ATX 3.1 native GPU power connector. No adapter cables needed for RTX 4090 |
| **Cooler** | Noctua NH-U14S TR5-SP6 (NOT AIO liquid) | Air coolers have zero pump failure risk. Critical in Lagos heat (28-35°C ambient). Noctua has 6-year warranty |
| **Motherboard** | ASUS Pro WS TRX50-SAGE (NOT consumer boards) | Workstation-class VRM (16+2 phase), 10Gbe LAN, IPMI remote management, validated for 24/7 operation |
| **RAM** | Samsung or SK Hynix ECC RDIMM (NOT third-party) | Threadripper is picky about RAM compatibility. Samsung/SK Hynix have the highest compatibility rates with TRX50 |
| **Case** | Rosewill RSV-L4500U or Chenbro RM41300 | Hot-swap bays, dual 120mm rear fans, tool-less rails. Standard co-lo form factor |

### What This Can Run (Simultaneously)

| Slot | Model | VRAM Used | Purpose |
|------|-------|-----------|---------|
| 1 | Qwen2.5-7B (Q4) | 4.5 GB | General AI assistant |
| 2 | Qwen2.5-Coder-7B (Q4) | 4.5 GB | Developer platform |
| 3 | Qwen2.5-VL-3B (Q4) | 2 GB | Image understanding |
| 4 | Faster-Whisper (Small) | 1 GB | Voice input |
| 5 | RT-DETR-L | 2 GB | Solar panel inspection |
| 6 | all-MiniLM-L6-v2 | 0.1 GB | RAG embeddings |
| | **Total VRAM** | **~14 GB** | **10 GB headroom on 24GB GPU** |
| CPU | Piper TTS, PaddleOCR, DistilBERT, XGBoost, Prophet | RAM only | CPU-based inference (24 cores handle it easily) |

---

## 3. PHASE 2 — UPGRADE (ADD GPU + RAM + STORAGE)

**Purpose:** Full production deployment with dual GPUs, higher quality models, and concurrency. **This is NOT a new build — it's components added to the Phase 1 TRX50 Workstation.**

### Upgrade BOM (Additions Only)

| # | Component | Specification | China Price (USD) | US Retail (USD) |
|---|-----------|--------------|-------------------|-----------------|
| 1 | **GPU 2** | NVIDIA RTX 4090 24GB (or RTX 5090 if available) | $1,200-$1,400 | $1,600-$1,800 |
| 2 | **RAM** | +128GB DDR5-5600 ECC RDIMM (4×32GB, fills remaining 4 DIMM slots) | $280-$400 | $400-$550 |
| 3 | **Storage** | +4TB Samsung 990 Pro NVMe Gen4 (fills 3rd M.2 slot) | $200-$280 | $300-$350 |
| | **Upgrade Subtotal** | | **$1,680-$2,080** | **$2,300-$2,700** |

### Component Reuse Matrix

Every Phase 1 component carries forward. Nothing is replaced:

| Component | Phase 1 | Phase 2 | Phase 3 | Status |
|-----------|---------|---------|---------|--------|
| CPU (Threadripper 7960X) | ✓ Installed | ✓ Kept | ✓ Kept (co-located) | **Zero waste** |
| Motherboard (TRX50-SAGE) | ✓ Installed | ✓ Kept — 2nd GPU slot now used | ✓ Kept | **Zero waste** |
| RAM (128GB ECC) | ✓ 4 of 8 DIMMs | ✓ All 8 DIMMs = 256GB | ✓ Kept | **Zero waste** |
| PSU (Seasonic TX-1600) | ✓ Already sized for 2 GPUs | ✓ No change needed | ✓ Kept | **Zero waste** |
| Case (4U Rackmount) | ✓ Already co-lo ready | ✓ No change needed | ✓ Slides into rack | **Zero waste** |
| Cooler (Noctua TR5-SP6) | ✓ Installed | ✓ No change needed | ✓ Kept | **Zero waste** |
| GPU 1 (RTX 4090) | ✓ Slot 1 | ✓ Slot 1 | ✓ Slot 1 | **Zero waste** |
| GPU 2 (RTX 4090) | — | ✓ **NEW** — Slot 2 | ✓ Slot 2 | Added in Phase 2 |
| Storage (5TB) | ✓ 2 of 4 M.2 | ✓ 3 of 4 M.2 = 9TB | ✓ Kept | **Zero waste** |

### What This Can Run (Dual GPU)

| GPU | Model | VRAM | Purpose |
|-----|-------|------|---------|
| **GPU 1** | Qwen2.5-14B (Q4) | 8 GB | Production AI assistant |
| GPU 1 | Qwen2.5-Coder-14B (Q4) | 8 GB | Full coding assistant |
| GPU 1 | Faster-Whisper (Large-v3) | 4 GB | Best accuracy STT |
| **GPU 2** | Qwen2.5-32B (Q4) | 18 GB | Complex reasoning / premium tier |
| GPU 2 | Qwen2.5-VL-7B (Q4) | 5 GB | Production vision |
| **CPU** | All CPU-based models | RAM (256GB) | OCR, TTS, NLP, ML |

---

## 4. PHASE 3 — CO-LOCATION & SCALING

**Move the same TRX50 Workstation to a professional data center for production-grade reliability.**

### What Happens in Phase 3

| Action | Details | Cost |
|--------|---------|------|
| Move TRX50 Workstation to co-lo | MainOne MDXi, Rack Centre, or 21st Century (Lagos) | ₦100K-₦250K/month (rack + power + bandwidth) |
| 4U rackmount slides directly into rack | No case change — already co-lo ready from Phase 1 | ₦0 |
| Gain 99.99% uptime | Redundant power, precision cooling, 10Gbps+ | Included in co-lo fee |
| Optional: Add 2nd node | Cheaper Ryzen 9 / used Threadripper for non-GPU work (databases, app servers) | ₦3M-₦5M if needed |

### Monthly Cost After Co-Location

| Component | Source | Monthly Cost |
|-----------|--------|-------------|
| TRX50 Workstation (own) | Co-located at data center | ₦0 (after purchase) |
| Co-location fee | MainOne / Rack Centre | ₦100,000-₦250,000/month |
| Cloud GPU burst | RunPod / Vast.ai / Lambda | ₦200K-₦500K/month |
| **Total monthly** | | **₦300K-₦750K/month** |

Note: Office power + cooling costs (₦150K-₦250K/month) are **eliminated** when you co-locate — the data center handles power and cooling. Net monthly increase is modest.

### When to Use Cloud vs Local

| Scenario | Use Local (TRX50) | Use Cloud |
|----------|-----------|-----------|
| Development & testing | ✓ | |
| Low-traffic production (<50 concurrent) | ✓ | |
| High-traffic peaks (>50 concurrent) | | ✓ |
| Large model inference (72B+) | | ✓ |
| Fine-tuning / training | | ✓ |
| Sensitive data processing | ✓ | |
| Batch processing (reports, OCR) | ✓ | |

---

## 5. CHINA SOURCING GUIDE

### Recommended Platforms

| Platform | Best For | Language | Payment |
|----------|----------|----------|---------|
| **1688.com** (阿里巴巴) | Wholesale, bulk orders | Chinese (use agent) | Alipay, bank transfer |
| **Taobao** | Individual components | Chinese | Alipay |
| **AliExpress** | Small orders, international | English | Card, PayPal |
| **JD.com (京东)** | Genuine branded parts | Chinese | Card (international) |
| **Shenzhen markets** (in-person) | Best prices, inspect before buy | Chinese | Cash, bank transfer |

### Sourcing Strategy

**Option 1: Use a Purchasing Agent (Recommended)**
- Companies like Superbuy, CSSBuy, or Nigerian-Chinese traders
- Agent fee: 5-10% of order value
- They handle: purchasing, quality inspection, consolidation, shipping
- Best for: first-time buyers, quality assurance

**Option 2: Direct from 1688/Taobao**
- Requires Chinese payment method (Alipay)
- Use Shenzhen warehouse for consolidation
- Ship via sea freight (cheapest) or air (fastest)

**Option 3: Shenzhen Trip (Best Prices)**
- Visit Huaqiangbei electronics market
- Inspect components in person
- Negotiate bulk pricing
- Combine with factory visits
- Budget: $2,000-$3,000 for trip (flights, hotel, visa)

### Supplier Verification Checklist

- [ ] Check seller rating (>4.8/5 on 1688)
- [ ] Request component photos with serial numbers
- [ ] Verify warranty terms (international warranty?)
- [ ] Ask for anti-static packaging guarantee
- [ ] Confirm GPU is genuine (check with GPU-Z upon receipt)
- [ ] For bulk: request factory visit or video call

### Shipping from China to Lagos

| Method | Cost (per server ~25kg) | Timeline | Best For |
|--------|------------------------|----------|----------|
| **Sea freight** | $150-$300 | 35-45 days | Non-urgent, bulk |
| **Air freight** | $400-$800 | 5-10 days | Urgent, single units |
| **Express (DHL/FedEx)** | $600-$1,200 | 3-5 days | Very urgent, small items |

**PECH Recommendation:** Sea freight for bulk hardware. Air freight for GPU (high value, fragile).

### Packaging Requirements

- **GPU:** Original box + anti-static bag + bubble wrap + "FRAGILE" labels
- **RAM:** Anti-static bag + foam padding
- **NVMe:** Anti-static bag (small, can ship with GPU)
- **PSU/Case:** Standard packaging (durable items)
- **All:** Double-box with 5cm foam gap between inner and outer box

---

## 6. NIGERIA IMPORT PROCESS

### Duties & Taxes

| Tax | Rate | Applied To |
|-----|------|-----------|
| **CET (Common External Tariff)** | 5-20% | CIF value (varies by HS code) |
| **VAT** | 7.5% | CIF + CET |
| **CISS (Comprehensive Import Supervision Scheme)** | 1% | FOB value |
| **ETLS levy** | 0.5% | CIF value |
| **Surcharge** | 7% | CET value |
| **Total estimated** | **~25-35%** | On CIF value |

### HS Codes for Computer Parts

| Component | HS Code | CET Rate |
|-----------|---------|----------|
| GPU (graphics card) | 8471.80.00 | 10% |
| CPU (processor) | 8542.31.00 | 5% |
| Motherboard | 8473.30.00 | 10% |
| RAM / Memory | 8542.32.00 | 5% |
| Hard drives / SSD | 8471.70.00 | 10% |
| PSU / Cases | 8504.40.00 | 20% |
| Complete computer | 8471.49.00 | 20% |

> **Pro Tip:** Import as individual components (not assembled computer) to get lower duty rates on most parts. HS code 8471.49 (complete computer) attracts 20% CET vs 5-10% for individual parts.

### Clearing Agent

- Use a licensed customs clearing agent at Apapa/Tin Can ports (for sea) or MMIA (for air)
- Agent fee: ₦50,000-₦150,000 per shipment
- Documents needed: commercial invoice, packing list, bill of lading/airway bill, Form M, PAAR
- Timeline: 3-7 working days for customs clearance (Lagos)
- **Budget ₦100K-₦200K for clearing per shipment**

### Import Checklist

- [ ] Get Form M from bank (required for imports >$50,000)
- [ ] Obtain PAAR (Pre-Arrival Assessment Report) from customs
- [ ] Ensure SONCAP certification (if applicable)
- [ ] Prepare commercial invoice with itemized components
- [ ] Insurance: 1-2% of CIF value (recommended for electronics)
- [ ] Assign clearing agent before goods arrive
- [ ] Budget for demurrage if clearing takes >7 days

---

## 7. LANDED COST CALCULATIONS

### Phase 1: TRX50 Workstation — Landed Lagos

| Cost Component | Amount (USD) | Amount (₦) |
|---------------|-------------|------------|
| Hardware (China price) | $3,690-$4,735 | ₦5,535,000-₦7,102,500 |
| Shipping (air freight, ~30kg) | $500-$900 | ₦750,000-₦1,350,000 |
| Insurance (2%) | $74-$95 | ₦111,000-₦142,500 |
| **CIF Value** | **$4,264-$5,730** | **₦6,396,000-₦8,595,000** |
| Import duties (~25%) | $1,066-$1,432 | ₦1,599,000-₦2,148,750 |
| Clearing agent | $100 | ₦150,000 |
| Local transport | $30 | ₦45,000 |
| **Total Landed** | **$5,460-$7,292** | **₦8,190,000-₦10,938,750** |

**Round estimate: ₦8.2M-₦11M for Phase 1 TRX50 Workstation landed Lagos**

### Phase 2: Upgrade Components — Landed Lagos

| Cost Component | Amount (USD) | Amount (₦) |
|---------------|-------------|------------|
| Hardware (China price) | $1,680-$2,080 | ₦2,520,000-₦3,120,000 |
| Shipping (air freight, ~5kg — GPU + RAM + SSD) | $200-$400 | ₦300,000-₦600,000 |
| Insurance (2%) | $34-$42 | ₦51,000-₦63,000 |
| **CIF Value** | **$1,914-$2,522** | **₦2,871,000-₦3,783,000** |
| Import duties (~25%) | $478-$630 | ₦717,750-₦945,750 |
| Clearing agent | $80 | ₦120,000 |
| Local transport | $20 | ₦30,000 |
| **Total Landed** | **$2,492-$3,252** | **₦3,738,750-₦4,878,750** |

**Round estimate: ₦4.1M-₦5.3M for Phase 2 upgrade components landed Lagos**

### Zero-Waste vs Old Approach — 24-Month Hardware Comparison

| | Old Approach | Zero-Waste | Difference |
|---|-------------|-----------|-----------|
| Phase 1 hardware | ₦5.7M-₦7.7M (AM5 Starter) | ₦8.2M-₦11M (TRX50) | +₦2.5M-₦3.3M |
| Phase 2 hardware | ₦11M-₦15M (buy whole new TRX50 box) | ₦4.1M-₦5.3M (add GPU+RAM only) | **-₦6.9M-₦9.7M** |
| **Total hardware** | **₦16.7M-₦22.7M** | **₦12.3M-₦16.3M** | **₦4.4M-₦6.4M saved** |
| Components wasted | CPU, mobo, RAM, PSU, case (~₦1.4M-₦1.9M) | None | **100% reuse** |

> **Exchange rate used:** ₦1,500/$1 (March 2026 parallel market estimate). Adjust for current rates.

---

## 8. SUPPORTING INFRASTRUCTURE

### Power Infrastructure That Scales (Sized for Phase 2 from Day 1)

Both ChatGPT conversations assumed hardware "just works" once purchased. In Lagos, Nigeria, you need significant supporting infrastructure. **All infrastructure below is sized for 2× RTX 4090 (Phase 2) from Day 1** — so Phase 2 requires zero power infrastructure upgrades:

### Power Infrastructure

| Item | Specification | Cost (₦) | Why Essential |
|------|--------------|----------|---------------|
| **Online UPS** | 3kVA Pure Sine Wave (APC/CyberPower) | 800,000-1,200,000 | Protects against Lagos power fluctuations; provides 15-30 min battery backup |
| **Solar Inverter System** | 5kVA Hybrid Inverter + 200Ah LiFePO4 batteries | 2,000,000-3,500,000 | Provides 4-8 hrs backup during NEPA outages; reduces diesel costs |
| **Voltage Regulator** | 5kVA Stabilizer | 80,000-150,000 | Lagos voltage ranges from 160V-260V; servers need stable 220V |
| **Diesel Generator** | 10kVA soundproof (backup to backup) | 1,500,000-2,500,000 | For extended outages >8 hrs; optional if solar is adequate |
| **Dedicated Circuit** | 30A circuit from DB to server room | 50,000-100,000 | Isolate server power from office loads |
| **Surge Protection** | Industrial-grade SPD (Type 2) | 30,000-60,000 | Lightning protection (Lagos has severe thunderstorms) |

**Minimum power budget: ₦2.9M-₦5M**
**Recommended power budget: ₦4.5M-₦7.5M** (with solar + generator)

### Power Consumption Estimate

| Component | Idle (W) | AI Load (W) | Peak (W) |
|-----------|----------|-------------|----------|
| TRX50 Workstation — Phase 1 (1× RTX 4090) | 180 | 600 | 750 |
| TRX50 Workstation — Phase 2 (2× RTX 4090) | 280 | 1,050 | 1,300 |
| Networking (switch, router, firewall) | 50 | 50 | 50 |
| Cooling (AC unit) | 500 | 1,000 | 1,500 |
| UPS overhead (10%) | 73 | 165 | 250 |
| **Total (Phase 1)** | **803W** | **1,815W** | **2,550W** |
| **Total (Phase 2)** | **903W** | **2,265W** | **3,100W** |

**Monthly electricity cost (Phase 1, 24/7 AI load):** ~1,310 kWh = ₦80,000-₦110,000 at Band A tariff
**Monthly electricity cost (Phase 2, 24/7 AI load):** ~1,630 kWh = ₦100,000-₦135,000 at Band A tariff

> **Note:** The 3kVA UPS handles Phase 1 comfortably (1,815W peak < 2,400W capacity at 0.8 PF). For Phase 2 peak loads (2,265W), the UPS still covers AI workloads — only synthetic full-GPU torture tests would exceed capacity. The Seasonic TX-1600 PSU handles dual GPUs natively with no adapter cables needed.

### Cooling Infrastructure

| Item | Specification | Cost (₦) |
|------|--------------|----------|
| **Split AC Unit** | 2HP / 18,000 BTU (server room) | 350,000-500,000 |
| **Backup AC Unit** | 1.5HP / 12,000 BTU (redundancy) | 250,000-350,000 |
| **Temperature Monitor** | IoT sensor with alert (ThingsBoard integrated) | 15,000-30,000 |
| **Humidity Control** | Dehumidifier (Lagos is 70-90% humidity) | 50,000-100,000 |

**Lagos ambient: 28-35°C.** Server room target: 18-24°C, 40-60% humidity.

**Cooling budget: ₦650K-₦1M**

### Network Infrastructure

| Item | Specification | Cost (₦/month) |
|------|--------------|----------------|
| **Primary Internet** | Dedicated fiber 100Mbps (MainOne/Glo/MTN) | 100,000-200,000 |
| **Backup Internet** | 4G/5G router (MTN/Airtel) | 30,000-50,000 |
| **Managed Switch** | 24-port Gigabit PoE (TP-Link/Cisco) | 100,000-250,000 (one-time) |
| **Firewall** | pfSense on Mini PC or Mikrotik RB4011 | 80,000-200,000 (one-time) |
| **Ethernet Cabling** | Cat6A (server room + office) | 50,000-100,000 (one-time) |
| **Static IP** | Public static IP for remote access | Included or ₦10,000/mo |

**Network one-time: ₦230K-₦550K**
**Network monthly: ₦130K-₦250K**

---

## 9. SERVER ROOM SETUP

### Minimum Requirements

| Requirement | Specification |
|-------------|--------------|
| **Size** | Minimum 3m × 3m (9 sqm) dedicated room |
| **Floor** | Raised floor or anti-static tiles preferred |
| **Door** | Solid door with lock (access control) |
| **Walls** | No windows preferred (reduce heat ingress) |
| **Power outlets** | 4× 15A sockets on dedicated circuit |
| **Lighting** | LED overhead (low heat) |
| **Fire** | CO2 or clean agent fire extinguisher (NOT water) |

### Server Rack Layout

```
┌─────────────────────────────────┐
│         SERVER ROOM (3×3m)       │
│                                  │
│  ┌──────────┐     ┌──────────┐  │
│  │  12U Rack │     │   AC #1  │  │
│  │           │     │ (2HP)    │  │
│  │ [UPS    ] │     └──────────┘  │
│  │ [Switch ] │                   │
│  │ [Firewall]│     ┌──────────┐  │
│  │ [Server 1]│     │   AC #2  │  │
│  │ [Server 2]│     │ (1.5HP)  │  │
│  │ [Patch   ]│     └──────────┘  │
│  │ [Panel   ]│                   │
│  └──────────┘     ┌──────────┐  │
│                    │ Temp/    │  │
│  ┌──────────┐     │ Humidity │  │
│  │ Solar    │     │ Monitor  │  │
│  │ Inverter │     └──────────┘  │
│  │ + Battery│                   │
│  └──────────┘                   │
└─────────────────────────────────┘
```

### Environmental Monitoring

Integrate with **ThingsBoard** (already in PECH IoT stack):
- Temperature sensor (DS18B20 or DHT22)
- Humidity sensor (DHT22)
- Power monitoring (PZEM-004T)
- Door sensor (magnetic reed switch)
- Smoke detector (MQ-2 gas sensor)
- ESP32 gateway → MQTT → ThingsBoard → Alerts

**Cost: ₦30,000-₦60,000 for all sensors + ESP32**

---

## 10. SOFTWARE INSTALLATION GUIDE

### Step-by-Step: Bare Metal → Production AI Server

#### Step 1: Operating System

```bash
# Install Ubuntu 22.04 LTS Server (NOT Desktop — saves resources)
# Download: https://releases.ubuntu.com/22.04/
# Flash to USB: use Rufus (Windows) or dd (Linux)

# After install:
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git curl wget htop nvtop
```

#### Step 2: NVIDIA Drivers + CUDA

```bash
# Add NVIDIA driver PPA
sudo add-apt-repository ppa:graphics-drivers/ppa -y
sudo apt update

# Install driver (check latest for RTX 4090)
sudo apt install -y nvidia-driver-545
sudo reboot

# Verify
nvidia-smi
# Should show RTX 4090, 24GB, driver version

# Install CUDA Toolkit 12.x
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update
sudo apt install -y cuda-toolkit-12-4
```

#### Step 3: Docker + NVIDIA Container Toolkit

```bash
# Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# NVIDIA Container Toolkit (run AI models in Docker)
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt update && sudo apt install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# Verify
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi
```

#### Step 4: Ollama (Phase 1 Model Management)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull Phase 1 models
ollama pull qwen2.5:7b          # General assistant (4.5GB)
ollama pull qwen2.5-coder:7b    # Code generation (4.5GB)
ollama pull nomic-embed-text    # Embeddings for RAG

# Test
ollama run qwen2.5:7b "Hello, I am PECH AI. How can I help?"
```

#### Step 5: Docker Compose — Full AI Stack

```yaml
# docker-compose.yml — PECH AI Stack Phase 1
version: '3.8'

services:
  # Vector Database for RAG
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

  # PostgreSQL (primary database)
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: pech
      POSTGRES_USER: pech_admin
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - pg_data:/var/lib/postgresql/data

  # Redis (cache)
  redis:
    image: redis:7.0-alpine  # Use 7.0 for BSD-3 license
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # Faster-Whisper (Speech-to-Text)
  whisper:
    image: fedirz/faster-whisper-server:latest-cuda
    ports:
      - "8001:8000"
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    environment:
      WHISPER__MODEL: small  # Use "large-v3" for production
      WHISPER__DEVICE: cuda

  # PaddleOCR (Invoice/Receipt OCR)
  paddleocr:
    image: paddlecloud/paddleocr:latest
    ports:
      - "8002:8866"

  # Monitoring
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  uptime-kuma:
    image: louislam/uptime-kuma:latest
    ports:
      - "3001:3001"
    volumes:
      - uptime_data:/app/data

volumes:
  qdrant_data:
  pg_data:
  redis_data:
  uptime_data:
```

#### Step 6: vLLM (Phase 2 — Production Serving)

```bash
# When ready for production (higher throughput than Ollama)
pip install vllm

# Serve Qwen2.5-14B with OpenAI-compatible API
python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-14B-Instruct-AWQ \
  --quantization awq \
  --gpu-memory-utilization 0.9 \
  --max-model-len 8192 \
  --port 8000

# Now any OpenAI-compatible client can connect to http://localhost:8000
```

---

## 11. CLOUD GPU OPTIONS

### For Phase 1-2 Overflow and Fine-Tuning

| Provider | GPU Options | Price/hr (A100 80GB) | Billing | Nigeria Access |
|----------|-----------|---------------------|---------|---------------|
| **RunPod** | A100, H100, RTX 4090 | $1.89-$2.49 | Per-second | Yes (crypto OK) |
| **Vast.ai** | Community GPUs | $0.80-$1.50 | Per-second | Yes |
| **Lambda Cloud** | A100, H100 | $1.99-$2.49 | Per-hour | Yes |
| **Google Colab Pro+** | A100, V100 | $49.99/month | Monthly | Yes |
| **Paperspace** | A100, RTX 4090 | $1.89-$3.09 | Per-hour | Yes |

### Recommended Strategy

| Task | Provider | GPU | Cost Estimate |
|------|----------|-----|---------------|
| Fine-tuning (monthly) | RunPod | A100 80GB | $50-$200/session |
| Burst capacity | Vast.ai | RTX 4090 | $0.40-$0.80/hr |
| Training experiments | Google Colab Pro+ | A100 | $50/month flat |
| Production overflow | RunPod Serverless | A100 | Pay-per-inference |

**Monthly cloud budget estimate: ₦200,000-₦500,000**

---

## 12. CO-LOCATION OPTIONS (LAGOS)

For Phase 3, consider co-locating production servers in a professional data center:

| Data Center | Location | Price (per U/month) | Power | Connectivity |
|-------------|----------|-------------------|-------|-------------|
| **MainOne MDXi** | Lekki, Lagos | ₦50,000-₦100,000 | Redundant | 10Gbps+ |
| **Rack Centre** | Oregun, Lagos | ₦60,000-₦120,000 | 2N power | 40Gbps+ |
| **21st Century** | VI, Lagos | ₦40,000-₦80,000 | Redundant | 1Gbps+ |
| **Galaxy Backbone** | Multiple | ₦45,000-₦90,000 | Generator backup | 10Gbps |

### Co-Location vs Office Server Room

| Factor | Office Server Room | Co-Location |
|--------|-------------------|-------------|
| Power reliability | 95% (with solar+gen) | 99.99% |
| Cooling | 2 ACs, manual monitoring | Precision cooling, 24/7 |
| Security | Office security | Biometric, CCTV, guards |
| Internet | 100Mbps fiber | 1-10Gbps+ |
| Monthly cost | ₦150-₦250K (power+internet) | ₦100-₦200K (co-lo) + existing power/internet |
| Setup cost | ₦3.75-₦6.5M (infra) | ₦100K-₦200K (install) |

**PECH Recommendation:**
- **Phase 1-2:** Office server room (lower total cost, faster setup)
- **Phase 3:** Co-locate production servers at MainOne or Rack Centre (better uptime, cooling, connectivity)

---

## 13. MONITORING & MAINTENANCE

### Daily Checks

```bash
# GPU health
nvidia-smi

# Disk usage
df -h

# Docker containers
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Ollama models loaded
ollama list
```

### Automated Monitoring (integrate with PECH IoT stack)

| Metric | Tool | Alert Threshold |
|--------|------|----------------|
| GPU temperature | Prometheus + nvidia_exporter | >85°C |
| GPU memory usage | Prometheus | >90% |
| Disk usage | Prometheus + node_exporter | >85% |
| CPU load | Prometheus | >80% sustained |
| Room temperature | ThingsBoard (ESP32) | >28°C |
| Room humidity | ThingsBoard (ESP32) | >70% |
| UPS battery | SNMP / NUT | <50% |
| Internet uptime | Uptime Kuma | Any downtime |
| Model response time | Prometheus | >5s P95 |

### Weekly Maintenance

- [ ] Check and clear Docker logs (`docker system prune`)
- [ ] Verify backup integrity
- [ ] Review GPU utilization trends
- [ ] Update Ollama models if new versions available
- [ ] Check disk space and archive old logs
- [ ] Verify UPS battery health
- [ ] Clean dust filters on server and AC

### Monthly Maintenance

- [ ] Full system backup (rsync to external drive)
- [ ] Security updates (`sudo apt update && sudo apt upgrade`)
- [ ] Review cloud GPU spending
- [ ] AC filter cleaning
- [ ] Generator test run (15 minutes)
- [ ] Review model performance metrics

---

## 14. TOTAL BUDGET SUMMARY

### One-Time Costs (Zero-Waste Single-Platform)

| Category | Phase 1 (₦) | Phase 2 Upgrade (₦) |
|----------|------------|---------------------|
| **Hardware (landed Lagos)** | 8,200,000-11,000,000 | 4,100,000-5,300,000 |
| **Power infrastructure** | 2,900,000-5,000,000 | 0 (already sized for 2 GPUs) |
| **Cooling** | 650,000-1,000,000 | 0 (already sized) |
| **Network (one-time)** | 230,000-550,000 | 0 (already set up) |
| **Server room setup** | 200,000-400,000 | 0 (already set up) |
| **IoT monitoring sensors** | 30,000-60,000 | 0 (already installed) |
| **Total One-Time** | **₦12,210,000-₦18,010,000** | **₦4,100,000-₦5,300,000** |

**Phase 1 midpoint: ~₦15.1M** — comfortably within the ₦18M target cap.

### Monthly Recurring Costs

| Category | Monthly (₦) |
|----------|-------------|
| **Electricity** | 80,000-135,000 |
| **Internet (primary + backup)** | 130,000-250,000 |
| **Cloud GPU (overflow)** | 200,000-500,000 |
| **Maintenance/consumables** | 50,000-100,000 |
| **Total Monthly** | **₦460,000-₦985,000** |

### 24-Month Total Cost of Ownership

| Setup Level | One-Time | Monthly × 24 | **24-Month Total** |
|-------------|----------|-------------|-------------------|
| **Phase 1 Only + Cloud** | ₦12.2M-₦18M | ₦11M-₦23.6M | **₦23.2M-₦41.6M** |
| **Phase 1 + Phase 2 + Cloud** | ₦16.3M-₦23.3M | ₦11M-₦23.6M | **₦27.3M-₦46.9M** |

### How This Maps to PECH Financial Proposal (₦250M)

| Proposal Line Item | Allocated (₦) | AI Hardware Fits? |
|--------------------|---------------|-------------------|
| Technology & Hardware | 75,000,000 | ✓ Phase 1 hardware + infra = ₦12.2M-₦18M (16-24% of allocation) |
| Technology & Hardware | 75,000,000 | ✓ Phase 1+2 hardware + infra = ₦16.3M-₦23.3M (22-31% of allocation) |
| Operational Expenses | 28,800,000 | ✓ Monthly cloud + power + internet from here |

### Savings vs Old Approach

| | Old (Starter → Replace) | Zero-Waste (TRX50 → Upgrade) | **Saved** |
|---|------------------------|-----------------------------|----|
| Phase 1 | ₦9.7M-₦14.7M | ₦12.2M-₦18M | -₦2.5M (higher upfront) |
| Phase 2 | ₦11M-₦15M (whole new box) | ₦4.1M-₦5.3M (add components) | **+₦6.9M-₦9.7M** |
| **Net 24-month** | ₦20.7M-₦29.7M (one-time) | ₦16.3M-₦23.3M (one-time) | **₦4.4M-₦6.4M saved** |
| Components wasted | ~₦1.4M-₦1.9M | ₦0 | **100% reuse** |

**Verdict:** The zero-waste TRX50 approach saves ₦4.4M-₦6.4M over 24 months while delivering better hardware from Day 1. AI hardware fits comfortably within the ₦75M technology allocation.

---

*This document is confidential to PECH Group Holdings Ltd. Last updated: March 2026.*
