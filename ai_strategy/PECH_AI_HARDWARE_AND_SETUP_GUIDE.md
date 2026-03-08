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
2. [Option A — Starter AI Server](#2-option-a--starter-ai-server)
3. [Option B — Production AI Cluster](#3-option-b--production-ai-cluster)
4. [Option C — Hybrid (Own + Cloud GPU)](#4-option-c--hybrid-own--cloud-gpu)
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

### Philosophy

PECH's AI hardware strategy follows a **crawl → walk → run** approach:

| Phase | Timeline | Hardware | AI Capability |
|-------|----------|----------|---------------|
| **Phase 1 (Crawl)** | Months 1-6 | 1× Starter Server (RTX 4090) | Run 2-3 models simultaneously; develop & test |
| **Phase 2 (Walk)** | Months 7-12 | Starter + cloud GPU burst | Production AI with cloud overflow for peak demand |
| **Phase 3 (Run)** | Months 13-24 | Production Cluster (2× RTX 4090) + cloud | Full production; fine-tuned models; high concurrency |

### Key Decision: Own vs Cloud

| Factor | Own Hardware | Cloud GPU |
|--------|-------------|-----------|
| **Monthly cost** | ₦0 after purchase (power only) | ₦200K-₦2M/month |
| **Upfront cost** | ₦9.5M-₦22.4M | ₦0 |
| **Latency** | <10ms (local) | 50-200ms (internet) |
| **Data sovereignty** | Full control (NDPA compliant) | Depends on provider |
| **Scaling** | Limited by hardware | Instant scale |
| **Maintenance** | PECH team responsibility | Provider handles |
| **Power dependency** | Lagos grid + backup | Provider's problem |

**PECH Recommendation:** Start with **own Starter Server + cloud GPU for overflow** (Phase 1-2). Add Production Cluster when revenue justifies (Phase 3).

---

## 2. OPTION A — STARTER AI SERVER

**Purpose:** Run 2-3 AI models simultaneously for development, testing, and initial production.

### Bill of Materials (BOM)

| # | Component | Specification | China Price (USD) | US Retail (USD) |
|---|-----------|--------------|-------------------|-----------------|
| 1 | **GPU** | NVIDIA RTX 4090 24GB GDDR6X | $1,200-$1,400 | $1,600-$1,800 |
| 2 | **CPU** | AMD Ryzen 9 7950X (16C/32T, 5.7GHz) | $380-$450 | $500-$550 |
| 3 | **Motherboard** | ASUS/MSI X670E (PCIe 5.0, 4× DDR5) | $180-$250 | $250-$350 |
| 4 | **RAM** | 128GB DDR5-5600 ECC (4×32GB) | $220-$280 | $300-$400 |
| 5 | **Storage (OS)** | 1TB Samsung 990 Pro NVMe Gen4 | $50-$70 | $80-$100 |
| 6 | **Storage (Data)** | 4TB Samsung 990 Pro NVMe Gen4 | $200-$280 | $300-$350 |
| 7 | **PSU** | Corsair/Seasonic 1000W 80+ Gold | $100-$140 | $150-$200 |
| 8 | **Case** | Full-tower with mesh airflow (Meshify 2 XL type) | $80-$120 | $120-$180 |
| 9 | **CPU Cooler** | Noctua NH-D15 / Arctic 360mm AIO | $60-$80 | $90-$110 |
| 10 | **Fans** | 3× 140mm Noctua NF-A14 case fans | $30-$45 | $45-$60 |
| | **Subtotal** | | **$2,500-$3,115** | **$3,435-$4,100** |

### Why These Specs

| Component | Why This Spec | Overkill? |
|-----------|--------------|-----------|
| **RTX 4090 (24GB)** | Runs Qwen2.5-14B (Q4, 8GB), Coder-7B (4.5GB), VL-3B (2GB), Whisper (1GB) simultaneously with headroom | No — 24GB is the minimum for serious AI work |
| **Ryzen 9 7950X** | 16 cores handle model loading, preprocessing, and web services. PCIe 5.0 for GPU bandwidth | Could use 7900X (12C) to save $100 |
| **128GB DDR5** | Models load to RAM first, then GPU. 128GB handles multiple model queues | Could start with 64GB, upgrade later |
| **4TB NVMe** | Models are 5-40GB each. 15+ models + datasets + logs fill up fast | Essential — don't skimp on storage |
| **1000W PSU** | RTX 4090 draws 450W peak. System total ~650W under AI load. 1000W gives headroom | Don't go below 850W with RTX 4090 |

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
| CPU | Piper TTS, PaddleOCR, DistilBERT, XGBoost, Prophet | RAM only | CPU-based inference |

---

## 3. OPTION B — PRODUCTION AI CLUSTER

**Purpose:** Full production deployment with higher quality models and concurrency.

### Bill of Materials (BOM)

| # | Component | Specification | China Price (USD) | US Retail (USD) |
|---|-----------|--------------|-------------------|-----------------|
| 1 | **GPU 1** | NVIDIA RTX 4090 24GB | $1,200-$1,400 | $1,600-$1,800 |
| 2 | **GPU 2** | NVIDIA RTX 4090 24GB | $1,200-$1,400 | $1,600-$1,800 |
| 3 | **CPU** | AMD EPYC 9354 (32C/64T) or Threadripper 7970X | $800-$1,200 | $1,200-$1,800 |
| 4 | **Motherboard** | ASUS/Supermicro TRX50/SP5 (2× PCIe 5.0 x16) | $400-$600 | $600-$900 |
| 5 | **RAM** | 256GB DDR5-4800 ECC (8×32GB) | $450-$600 | $600-$800 |
| 6 | **Storage (OS)** | 2TB NVMe Gen4 (RAID 1) | $100-$140 | $160-$200 |
| 7 | **Storage (Data)** | 8TB NVMe Gen4 (2×4TB) | $400-$560 | $600-$700 |
| 8 | **PSU** | 1600W 80+ Platinum (dual GPU) | $200-$280 | $300-$400 |
| 9 | **Case/Chassis** | 4U rackmount or full-tower | $150-$250 | $250-$400 |
| 10 | **Cooling** | Custom loop or dual 360mm AIO + 6× fans | $200-$300 | $300-$450 |
| | **Subtotal** | | **$5,100-$6,730** | **$7,210-$9,250** |

### What This Can Run

| GPU | Model | VRAM | Purpose |
|-----|-------|------|---------|
| **GPU 1** | Qwen2.5-14B (Q4) | 8 GB | Production AI assistant |
| GPU 1 | Qwen2.5-Coder-14B (Q4) | 8 GB | Full coding assistant |
| GPU 1 | Faster-Whisper (Large-v3) | 4 GB | Best accuracy STT |
| **GPU 2** | Qwen2.5-32B (Q4) | 18 GB | Complex reasoning / premium tier |
| GPU 2 | Qwen2.5-VL-7B (Q4) | 5 GB | Production vision |
| **CPU** | All CPU-based models | RAM | OCR, TTS, NLP, ML |

---

## 4. OPTION C — HYBRID (OWN + CLOUD GPU)

**Recommended for PECH Phase 1-2.**

| Component | Source | Monthly Cost |
|-----------|--------|-------------|
| Starter Server (own) | China purchase | ₦0 (after purchase) |
| Cloud GPU burst | RunPod / Vast.ai / Lambda | ₦200K-₦500K/month |
| Power + Internet | Lagos | ₦150K-₦250K/month |
| **Total monthly** | | **₦350K-₦750K/month** |

### When to Use Cloud vs Local

| Scenario | Use Local | Use Cloud |
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

### Starter Server — Landed Lagos

| Cost Component | Amount (USD) | Amount (₦) |
|---------------|-------------|------------|
| Hardware (China price) | $2,500-$3,115 | ₦3,750,000-₦4,672,500 |
| Shipping (air freight) | $400-$800 | ₦600,000-₦1,200,000 |
| Insurance (2%) | $50-$62 | ₦75,000-₦93,000 |
| **CIF Value** | **$2,950-$3,977** | **₦4,425,000-₦5,965,500** |
| Import duties (~25%) | $737-$994 | ₦1,106,250-₦1,491,375 |
| Clearing agent | $100 | ₦150,000 |
| Local transport | $30 | ₦45,000 |
| **Total Landed** | **$3,817-$5,101** | **₦5,726,250-₦7,651,875** |

**Round estimate: ₦5.7M-₦7.7M for Starter Server landed Lagos**

### Production Cluster — Landed Lagos

| Cost Component | Amount (USD) | Amount (₦) |
|---------------|-------------|------------|
| Hardware (China price) | $5,100-$6,730 | ₦7,650,000-₦10,095,000 |
| Shipping (air freight, 2 GPUs) | $600-$1,000 | ₦900,000-₦1,500,000 |
| Insurance (2%) | $102-$135 | ₦153,000-₦202,500 |
| **CIF Value** | **$5,802-$7,865** | **₦8,703,000-₦11,797,500** |
| Import duties (~25%) | $1,450-$1,966 | ₦2,175,750-₦2,949,375 |
| Clearing agent | $100 | ₦150,000 |
| Local transport | $50 | ₦75,000 |
| **Total Landed** | **$7,402-$9,981** | **₦11,103,750-₦14,971,875** |

**Round estimate: ₦11M-₦15M for Production Cluster landed Lagos**

> **Exchange rate used:** ₦1,500/$1 (March 2026 parallel market estimate). Adjust for current rates.

---

## 8. SUPPORTING INFRASTRUCTURE

### What ChatGPT Missed Entirely

Both ChatGPT conversations assumed hardware "just works" once purchased. In Lagos, Nigeria, you need significant supporting infrastructure:

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
| Starter Server (1× RTX 4090) | 150 | 550 | 700 |
| Production Cluster (2× RTX 4090) | 250 | 900 | 1,200 |
| Networking (switch, router, firewall) | 50 | 50 | 50 |
| Cooling (AC unit) | 500 | 1,000 | 1,500 |
| UPS overhead (10%) | 70 | 150 | 225 |
| **Total (Starter)** | **770W** | **1,750W** | **2,475W** |
| **Total (Production)** | **870W** | **2,100W** | **2,975W** |

**Monthly electricity cost (Starter, 24/7 AI load):** ~1,260 kWh = ₦75,000-₦100,000 at Band A tariff

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

### One-Time Costs

| Category | Starter Setup (₦) | Production Setup (₦) |
|----------|-------------------|---------------------|
| **Hardware (landed Lagos)** | 5,700,000-7,700,000 | 11,000,000-15,000,000 |
| **Power infrastructure** | 2,900,000-5,000,000 | 4,500,000-7,500,000 |
| **Cooling** | 650,000-1,000,000 | 650,000-1,000,000 |
| **Network (one-time)** | 230,000-550,000 | 230,000-550,000 |
| **Server room setup** | 200,000-400,000 | 200,000-400,000 |
| **IoT monitoring sensors** | 30,000-60,000 | 30,000-60,000 |
| **Clearing/shipping/insurance** | Included in hardware | Included in hardware |
| **Total One-Time** | **₦9,710,000-₦14,710,000** | **₦16,610,000-₦24,510,000** |

### Monthly Recurring Costs

| Category | Monthly (₦) |
|----------|-------------|
| **Electricity** | 75,000-150,000 |
| **Internet (primary + backup)** | 130,000-250,000 |
| **Cloud GPU (overflow)** | 200,000-500,000 |
| **Maintenance/consumables** | 50,000-100,000 |
| **Total Monthly** | **₦455,000-₦1,000,000** |

### 24-Month Total Cost of Ownership

| Setup Level | One-Time | Monthly × 24 | **24-Month Total** |
|-------------|----------|-------------|-------------------|
| **Starter + Cloud** | ₦9.7M-₦14.7M | ₦10.9M-₦24M | **₦20.6M-₦38.7M** |
| **Production + Cloud** | ₦16.6M-₦24.5M | ₦10.9M-₦24M | **₦27.5M-₦48.5M** |

### How This Maps to PECH Financial Proposal (₦250M)

| Proposal Line Item | Allocated (₦) | AI Hardware Fits? |
|--------------------|---------------|-------------------|
| Technology & Hardware | 75,000,000 | ✓ Starter hardware + infra = ₦10-15M (13-20% of allocation) |
| Technology & Hardware | 75,000,000 | ✓ Production hardware + infra = ₦17-25M (23-33% of allocation) |
| Operational Expenses | 28,800,000 | ✓ Monthly cloud + power + internet from here |

**Verdict:** AI hardware fits comfortably within the ₦75M technology allocation. The ₦250M proposal already budgets adequately.

---

*This document is confidential to PECH Group Holdings Ltd. Last updated: March 2026.*
