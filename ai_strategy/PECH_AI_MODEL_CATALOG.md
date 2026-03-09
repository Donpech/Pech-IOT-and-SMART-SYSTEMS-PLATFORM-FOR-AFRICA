# PECH GROUP HOLDINGS LTD

## AI Model Catalog — Complete Reference

### CONFIDENTIAL

---

**PECH Group Holdings Ltd**
Lagos, Nigeria | Website: [pechgroupholdings.tech](https://pechgroupholdings.tech)

---

> **Document Reference:** PECH-AI-MODELS-2026-001
> **Version:** 1.0
> **Effective Date:** March 2026
> **Prepared By:** Technology Department
> **Approved By:** Managing Director / CEO

---

## TABLE OF CONTENTS

1. [License Policy](#1-license-policy)
2. [Large Language Models (LLMs)](#2-large-language-models)
3. [Small Language Models (SLMs)](#3-small-language-models)
4. [Code Generation Models](#4-code-generation-models)
5. [Speech-to-Text Models](#5-speech-to-text-models)
6. [Text-to-Speech Models](#6-text-to-speech-models)
7. [Vision & Multimodal Models](#7-vision-multimodal-models)
8. [OCR Models](#8-ocr-models)
9. [Embedding Models](#9-embedding-models)
10. [Computer Vision / Object Detection](#10-computer-vision-object-detection)
11. [Traditional ML Models](#11-traditional-ml-models)
12. [Recommendation Models](#12-recommendation-models)
13. [Image Processing / Generation](#13-image-processing-generation)
14. [Translation Models](#14-translation-models)
15. [NLP Models (Classification, NER, Sentiment)](#15-nlp-models)
16. [Model Deployment Summary](#16-model-deployment-summary)
17. [VRAM Quick-Reference](#17-vram-quick-reference)

---

## 1. LICENSE POLICY

**PECH only deploys models with Apache-2.0 or MIT licenses.** This ensures we can:
- Rebrand model outputs under the PECH brand
- Modify model weights (fine-tune, quantize)
- Close-source derivative products
- Sell AI features as paid subscriptions
- Embed models in proprietary services

**Models explicitly excluded:**
| Model | License | Why Excluded |
|-------|---------|-------------|
| Llama 3 / 3.1 / 3.2 | Meta Community License | Cannot rebrand; 700M MAU limit |
| Gemma 2 / 3 | Google Use Policy | Redistribution restrictions |
| YOLOv8 (Ultralytics) | AGPL-3.0 | Must open-source derivative code |
| Stable Diffusion 3+ | Stability AI License | Non-commercial restrictions |

---

## 2. LARGE LANGUAGE MODELS (LLMs)

These are the primary models powering chatbot features, document generation, analysis, and AI assistants across all 10 PECH verticals.

### Models Available (when multiple can do the same task, all listed)

| Model | Parameters | License | VRAM (FP16) | VRAM (Q4) | Download |
|-------|-----------|---------|-------------|-----------|----------|
| **Qwen2.5-72B** | 72B | Apache-2.0 | 144 GB | 40 GB | [huggingface.co/Qwen/Qwen2.5-72B](https://huggingface.co/Qwen/Qwen2.5-72B) |
| **Qwen2.5-32B** | 32B | Apache-2.0 | 64 GB | 18 GB | [huggingface.co/Qwen/Qwen2.5-32B](https://huggingface.co/Qwen/Qwen2.5-32B) |
| **Qwen2.5-14B** | 14B | Apache-2.0 | 28 GB | 8 GB | [huggingface.co/Qwen/Qwen2.5-14B](https://huggingface.co/Qwen/Qwen2.5-14B) |
| **Qwen2.5-7B** | 7B | Apache-2.0 | 14 GB | 4.5 GB | [huggingface.co/Qwen/Qwen2.5-7B](https://huggingface.co/Qwen/Qwen2.5-7B) |
| **Qwen3-8B** | 8B | Apache-2.0 | 16 GB | 5 GB | [huggingface.co/Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) |
| **Qwen3-4B** | 4B | Apache-2.0 | 8 GB | 2.5 GB | [huggingface.co/Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) |
| **Mistral-7B-v0.3** | 7B | Apache-2.0 | 14 GB | 4.5 GB | [huggingface.co/mistralai/Mistral-7B-v0.3](https://huggingface.co/mistralai/Mistral-7B-v0.3) |
| **Mixtral-8x7B** | 46.7B (MoE) | Apache-2.0 | 93 GB | 26 GB | [huggingface.co/mistralai/Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) |
| **Phi-4** | 14B | MIT | 28 GB | 8 GB | [huggingface.co/microsoft/phi-4](https://huggingface.co/microsoft/phi-4) |
| **Phi-3-Medium** | 14B | MIT | 28 GB | 8 GB | [huggingface.co/microsoft/Phi-3-medium-128k-instruct](https://huggingface.co/microsoft/Phi-3-medium-128k-instruct) |
| **DeepSeek-R1** | 671B (MoE) | MIT | 1.3 TB | 400 GB | [huggingface.co/deepseek-ai/DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) |
| **DeepSeek-R1-Distill-Qwen-7B** | 7B | MIT | 14 GB | 4.5 GB | [huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **General assistant (production)** | Qwen2.5-14B | Best quality-to-VRAM ratio; fits single RTX 4090 in Q4; strong multilingual | Phi-4 (14B, MIT) |
| **General assistant (starter)** | Qwen2.5-7B | Runs on 5 GB VRAM quantized; good enough for Phase 1 | Mistral-7B-v0.3 |
| **Complex reasoning** | Qwen2.5-32B (Q4) | Strong chain-of-thought; fits in 18 GB Q4 | DeepSeek-R1-Distill-7B |
| **Maximum quality** | Qwen2.5-72B (Q4) | Best open-source quality; needs cloud GPU or 2× RTX 4090 | Mixtral-8x7B |
| **Budget/edge deployment** | Qwen3-4B | Newest architecture; 2.5 GB Q4; good for mobile/edge | Phi-3-Mini (3.8B) |

**PECH Recommendation:** Start with **Qwen2.5-7B** (Phase 1 on starter hardware), upgrade to **Qwen2.5-14B** (Phase 2), then **Qwen2.5-32B/72B** (Phase 3 with production cluster or cloud).

---

## 3. SMALL LANGUAGE MODELS (SLMs)

For edge devices, IoT gateways, mobile apps, and lightweight tasks where large LLMs are overkill.

| Model | Parameters | License | VRAM (FP16) | VRAM (Q4) | Download |
|-------|-----------|---------|-------------|-----------|----------|
| **SmolLM2-1.7B** | 1.7B | Apache-2.0 | 3.4 GB | 1 GB | [huggingface.co/HuggingFaceTB/SmolLM2-1.7B](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B) |
| **SmolLM2-360M** | 360M | Apache-2.0 | 720 MB | 200 MB | [huggingface.co/HuggingFaceTB/SmolLM2-360M](https://huggingface.co/HuggingFaceTB/SmolLM2-360M) |
| **TinyLlama-1.1B** | 1.1B | Apache-2.0 | 2.2 GB | 700 MB | [huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) |
| **Phi-3-Mini** | 3.8B | MIT | 7.6 GB | 2.3 GB | [huggingface.co/microsoft/Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) |
| **Qwen2.5-1.5B** | 1.5B | Apache-2.0 | 3 GB | 1 GB | [huggingface.co/Qwen/Qwen2.5-1.5B](https://huggingface.co/Qwen/Qwen2.5-1.5B) |
| **Qwen2.5-0.5B** | 0.5B | Apache-2.0 | 1 GB | 350 MB | [huggingface.co/Qwen/Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B) |
| **H2O Danube3-500M** | 500M | Apache-2.0 | 1 GB | 350 MB | [huggingface.co/h2oai/h2o-danube3-500m-chat](https://huggingface.co/h2oai/h2o-danube3-500m-chat) |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **IoT gateway / edge** | Qwen2.5-0.5B | Smallest with usable quality; 350 MB Q4 | H2O Danube3-500M |
| **Mobile app assistant** | SmolLM2-1.7B | Best quality under 2B params; HuggingFace backed | Qwen2.5-1.5B |
| **Lightweight chatbot** | Phi-3-Mini (3.8B) | Punches above weight class; MIT license | TinyLlama-1.1B |
| **Embedded/constrained** | SmolLM2-360M | Runs on CPU; under 200 MB Q4 | Qwen2.5-0.5B |

**PECH Recommendation:** **SmolLM2-1.7B** for mobile/tablet apps, **Qwen2.5-0.5B** for IoT edge devices.

---

## 4. CODE GENERATION MODELS

For the Developer Platform, AI coding assistant, code review, and internal development tools.

| Model | Parameters | License | VRAM (Q4) | Download |
|-------|-----------|---------|-----------|----------|
| **DeepSeek-Coder-V2-Lite** | 16B (MoE) | MIT | 9 GB | [huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct) |
| **Qwen2.5-Coder-7B** | 7B | Apache-2.0 | 4.5 GB | [huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) |
| **Qwen2.5-Coder-14B** | 14B | Apache-2.0 | 8 GB | [huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) |
| **StarCoder2-7B** | 7B | Apache-2.0 | 4.5 GB | [huggingface.co/bigcode/starcoder2-7b](https://huggingface.co/bigcode/starcoder2-7b) |
| **CodeGemma-7B** | 7B | Google Terms | 4.5 GB | *(excluded — Google license restrictions)* |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **AI coding assistant** | Qwen2.5-Coder-14B | Best code quality in Apache-2.0 class; fits RTX 4090 Q4 | DeepSeek-Coder-V2-Lite |
| **Code completion (lightweight)** | Qwen2.5-Coder-7B | Fast; 4.5 GB Q4; great for autocomplete | StarCoder2-7B |
| **Code review / analysis** | DeepSeek-Coder-V2-Lite | Strong reasoning about code; MIT license | Qwen2.5-Coder-14B |

**PECH Recommendation:** **Qwen2.5-Coder-7B** for Phase 1 (autocomplete, simple tasks), upgrade to **Qwen2.5-Coder-14B** for Phase 2 (full coding assistant for developer platform).

---

## 5. SPEECH-TO-TEXT MODELS

For voice commands, customer support transcription, voice-to-edit features, and accessibility.

| Model | Size | License | Languages | VRAM | Download |
|-------|------|---------|-----------|------|----------|
| **Whisper Large-v3** | 1.5B | MIT | 100+ languages | 4 GB | [huggingface.co/openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) |
| **Whisper Medium** | 769M | MIT | 100+ | 2 GB | [huggingface.co/openai/whisper-medium](https://huggingface.co/openai/whisper-medium) |
| **Whisper Small** | 244M | MIT | 100+ | 1 GB | [huggingface.co/openai/whisper-small](https://huggingface.co/openai/whisper-small) |
| **Whisper Base** | 74M | MIT | 100+ | 500 MB | [huggingface.co/openai/whisper-base](https://huggingface.co/openai/whisper-base) |
| **whisper.cpp** | Same | MIT | 100+ | CPU | [github.com/ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp) |
| **Faster-Whisper** | Same | MIT | 100+ | 2 GB | [github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **Production transcription** | Faster-Whisper (Large-v3) | 4× faster than original; same accuracy; CTranslate2 backend | Whisper Large-v3 (original) |
| **Real-time voice input** | Faster-Whisper (Medium) | Good accuracy with low latency; 2 GB | Whisper Small |
| **Edge / mobile** | whisper.cpp (Base) | Pure CPU; C++ optimized; runs on phones | Whisper Small |
| **Nigerian languages** | Whisper Large-v3 | Best multilingual coverage (Yoruba, Hausa, Igbo, Pidgin) | None comparable |

**PECH Recommendation:** **Faster-Whisper with Large-v3** for server-side transcription, **whisper.cpp with Base/Small** for edge devices. Whisper is the only practical choice for African language coverage.

---

## 6. TEXT-TO-SPEECH MODELS

For voice assistants, accessibility, customer support bots, and automated notifications.

| Model | License | Quality | Languages | VRAM | Download |
|-------|---------|---------|-----------|------|----------|
| **Piper TTS** | MIT | Good | 30+ (incl. custom) | CPU | [github.com/rhasspy/piper](https://github.com/rhasspy/piper) |
| **Kokoro TTS** | Apache-2.0 | Very Good | English + Asian | 1 GB | [huggingface.co/hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) |
| **Coqui XTTS-v2** | MPL-2.0 | Excellent | 17 languages | 2 GB | [github.com/coqui-ai/TTS](https://github.com/coqui-ai/TTS) |
| **Edge-TTS** | MIT (client) | Good | 300+ voices | API | [github.com/rany2/edge-tts](https://github.com/rany2/edge-tts) |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **Self-hosted production** | Piper TTS | Fastest; runs on CPU; easy to add custom voices | Kokoro TTS |
| **High-quality English** | Kokoro TTS | More natural prosody; Apache-2.0 | Coqui XTTS-v2 (MPL) |
| **Voice cloning** | Coqui XTTS-v2 | Only option for custom voice cloning; MPL-2.0 is permissive | — |
| **Quick prototype** | Edge-TTS | Free Microsoft API; 300+ voices; no GPU needed | Piper |

**PECH Recommendation:** **Piper TTS** for all production use (CPU-only, fast, self-hosted). Add **Kokoro TTS** for premium high-quality English output. Consider **Coqui XTTS-v2** if custom brand voice is needed (MPL-2.0 is compatible with commercial use but requires sharing modifications to Coqui's code).

---

## 7. VISION & MULTIMODAL MODELS

For image understanding, visual Q&A, document analysis, and solar panel inspection.

| Model | Parameters | License | VRAM (Q4) | Capabilities | Download |
|-------|-----------|---------|-----------|-------------|----------|
| **Qwen2.5-VL-7B** | 7B | Apache-2.0 | 5 GB | Image + video understanding | [huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) |
| **Qwen2.5-VL-3B** | 3B | Apache-2.0 | 2 GB | Image understanding | [huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) |
| **Phi-3-Vision** | 4.2B | MIT | 3 GB | Image understanding | [huggingface.co/microsoft/Phi-3-vision-128k-instruct](https://huggingface.co/microsoft/Phi-3-vision-128k-instruct) |
| **InternVL2-8B** | 8B | Apache-2.0 | 5 GB | Image + document understanding | [huggingface.co/OpenGVLab/InternVL2-8B](https://huggingface.co/OpenGVLab/InternVL2-8B) |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **Solar panel inspection** | Qwen2.5-VL-7B | Best overall vision quality; Apache-2.0; video support | InternVL2-8B |
| **Product image analysis** | Qwen2.5-VL-3B | Lightweight; good enough for product Q&A; 2 GB | Phi-3-Vision |
| **Document understanding** | InternVL2-8B | Strong at reading documents/charts | Qwen2.5-VL-7B |
| **Edge deployment** | Qwen2.5-VL-3B | Smallest multimodal; 2 GB Q4 | Phi-3-Vision |

**PECH Recommendation:** **Qwen2.5-VL-7B** for production (solar inspection, product analysis, support), **Qwen2.5-VL-3B** for lightweight/mobile tasks.

---

## 8. OCR MODELS

For invoice processing, receipt scanning, document digitization, tax compliance, and ID verification.

| Model | License | Languages | GPU Required | Download |
|-------|---------|-----------|-------------|----------|
| **PaddleOCR v4** | Apache-2.0 | 80+ languages | Optional (CPU works) | [github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |
| **Tesseract OCR 5** | Apache-2.0 | 100+ languages | CPU only | [github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) |
| **EasyOCR** | Apache-2.0 | 80+ languages | Optional | [github.com/JaidedAI/EasyOCR](https://github.com/JaidedAI/EasyOCR) |
| **Surya OCR** | GPL-3.0 | 90+ languages | GPU recommended | *(excluded — GPL license)* |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **Invoice/receipt OCR** | PaddleOCR v4 | Best accuracy; table detection; layout analysis; Apache-2.0 | EasyOCR |
| **Simple text extraction** | Tesseract 5 | Fastest on CPU; most languages; battle-tested | PaddleOCR |
| **Handwriting recognition** | PaddleOCR v4 | Better handwriting support than Tesseract | EasyOCR |
| **ID card / KYC** | PaddleOCR v4 | Built-in ID card detection templates | — |

**PECH Recommendation:** **PaddleOCR v4** as primary (invoices, receipts, IDs, KYC), **Tesseract 5** as fallback for simple text extraction.

---

## 9. EMBEDDING MODELS

For RAG (Retrieval-Augmented Generation), semantic search, similarity matching, and knowledge retrieval.

| Model | Dimensions | License | Size | Download |
|-------|-----------|---------|------|----------|
| **all-MiniLM-L6-v2** | 384 | Apache-2.0 | 80 MB | [huggingface.co/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) |
| **all-MiniLM-L12-v2** | 384 | Apache-2.0 | 120 MB | [huggingface.co/sentence-transformers/all-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2) |
| **e5-small-v2** | 384 | MIT | 130 MB | [huggingface.co/intfloat/e5-small-v2](https://huggingface.co/intfloat/e5-small-v2) |
| **e5-base-v2** | 768 | MIT | 420 MB | [huggingface.co/intfloat/e5-base-v2](https://huggingface.co/intfloat/e5-base-v2) |
| **e5-large-v2** | 1024 | MIT | 1.3 GB | [huggingface.co/intfloat/e5-large-v2](https://huggingface.co/intfloat/e5-large-v2) |
| **BGE-M3** | 1024 | MIT | 2.2 GB | [huggingface.co/BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) |
| **Nomic-Embed-Text-v1.5** | 768 | Apache-2.0 | 550 MB | [huggingface.co/nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **RAG pipeline (starter)** | all-MiniLM-L6-v2 | Tiny (80 MB); fast; good enough for Phase 1 | e5-small-v2 |
| **RAG pipeline (production)** | Nomic-Embed-Text-v1.5 | Best quality in Apache-2.0 class; 768 dims; Matryoshka support | BGE-M3 (multilingual) |
| **Multilingual embeddings** | BGE-M3 | Best multilingual; supports 100+ languages including African | e5-large-v2 |
| **Product similarity** | all-MiniLM-L12-v2 | Good balance of speed and quality for product matching | Nomic-Embed |

**PECH Recommendation:** **all-MiniLM-L6-v2** for Phase 1, upgrade to **Nomic-Embed-Text-v1.5** for Phase 2 production RAG.

---

## 10. COMPUTER VISION / OBJECT DETECTION

For solar panel inspection, warehouse inventory, security, quality control, and logistics.

| Model | License | VRAM | Speed | Download |
|-------|---------|------|-------|----------|
| **RT-DETR (PaddlePaddle)** | Apache-2.0 | 2-4 GB | Real-time | [github.com/PaddlePaddle/PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection) |
| **RT-DETR (Ultralytics)** | AGPL-3.0 | 2-4 GB | Real-time | *(excluded — AGPL wrapper)* |
| **Detectron2** | Apache-2.0 | 4-8 GB | Near-real-time | [github.com/facebookresearch/detectron2](https://github.com/facebookresearch/detectron2) |
| **DETR (Facebook)** | Apache-2.0 | 2-4 GB | Moderate | [huggingface.co/facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50) |
| **OpenCV DNN** | Apache-2.0 | CPU | Fast | [github.com/opencv/opencv](https://github.com/opencv/opencv) |
| **YOLOv5** | GPL-3.0 | 2-4 GB | Real-time | *(excluded — GPL license)* |
| **YOLOv8** | AGPL-3.0 | 2-4 GB | Real-time | *(excluded — AGPL license)* |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **Solar panel defect detection** | RT-DETR (PaddlePaddle) | Real-time; Apache-2.0; better accuracy than YOLO on small objects | Detectron2 |
| **Warehouse inventory** | RT-DETR (PaddlePaddle) | Fast counting and detection | DETR |
| **General object detection** | Detectron2 | Most flexible; strong ecosystem; instance segmentation | RT-DETR |
| **Lightweight / edge** | OpenCV DNN | CPU-only; deploy anywhere | — |

**PECH Recommendation:** **RT-DETR via PaddleDetection** for all computer vision tasks. It replaces YOLOv8 with no license issues and comparable performance. Use **Detectron2** for advanced segmentation tasks.

> **IMPORTANT:** Use the **PaddlePaddle RT-DETR** implementation, NOT the Ultralytics wrapper (which is AGPL).

---

## 11. TRADITIONAL ML MODELS

For tabular data tasks: fraud detection, pricing, demand forecasting, credit scoring, anomaly detection.

| Model/Library | License | Use Case | Download |
|--------------|---------|----------|----------|
| **XGBoost** | Apache-2.0 | Classification, regression, ranking | [github.com/dmlc/xgboost](https://github.com/dmlc/xgboost) |
| **LightGBM** | MIT | Fast gradient boosting; large datasets | [github.com/microsoft/LightGBM](https://github.com/microsoft/LightGBM) |
| **CatBoost** | Apache-2.0 | Categorical features; less preprocessing | [github.com/catboost/catboost](https://github.com/catboost/catboost) |
| **scikit-learn** | BSD-3 | All-purpose ML toolkit | [github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) |
| **Prophet** | MIT | Time-series forecasting | [github.com/facebook/prophet](https://github.com/facebook/prophet) |
| **statsmodels** | BSD-3 | Statistical modeling | [github.com/statsmodels/statsmodels](https://github.com/statsmodels/statsmodels) |
| **Isolation Forest** | BSD-3 (scikit-learn) | Anomaly/fraud detection | Part of scikit-learn |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **Fraud detection** | XGBoost + Isolation Forest | XGBoost for classification, IF for anomaly detection | LightGBM |
| **Dynamic pricing** | LightGBM | Fastest training; handles large catalogs | XGBoost |
| **Credit scoring** | XGBoost | Most interpretable GBM; regulatory compliance | CatBoost |
| **Demand forecasting** | Prophet | Built for business time series; handles seasonality | statsmodels ARIMA |
| **Solar yield prediction** | LightGBM | Fast retraining with weather data | XGBoost |

**PECH Recommendation:** Use **XGBoost** as the primary ML workhorse, **LightGBM** for speed-critical tasks, **Prophet** for all time-series forecasting.

---

## 12. RECOMMENDATION MODELS

For product recommendations, content suggestions, installer matching, and personalization.

| Model/Library | License | Type | Download |
|--------------|---------|------|----------|
| **LightFM** | Apache-2.0 | Hybrid (collaborative + content) | [github.com/lyst/lightfm](https://github.com/lyst/lightfm) |
| **RecBole** | MIT | Framework (30+ algorithms) | [github.com/RUCAIBox/RecBole](https://github.com/RUCAIBox/RecBole) |
| **Implicit** | MIT | Collaborative filtering (ALS) | [github.com/benfred/implicit](https://github.com/benfred/implicit) |
| **Surprise** | BSD-3 | Classic recommendation algorithms | [github.com/NicolasHug/Surprise](https://github.com/NicolasHug/Surprise) |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **Product recommendations** | LightFM | Handles cold-start (new products); uses item metadata | RecBole |
| **"Customers also bought"** | Implicit | Fast ALS; GPU-accelerated | LightFM |
| **Installer matching** | LightFM | Uses both installer features + customer preferences | — |
| **Research / experimentation** | RecBole | 30+ algorithms to test | Surprise |

**PECH Recommendation:** **LightFM** for all production recommendations (marketplace, solar installers, logistics partners). Use **RecBole** for experimentation when optimizing recommendation quality.

---

## 13. IMAGE PROCESSING / GENERATION

For marketplace product images: background removal, enhancement, AI-generated descriptions from images.

| Tool | License | Function | Download |
|------|---------|----------|----------|
| **rembg** | MIT | Background removal | [github.com/danielgatis/rembg](https://github.com/danielgatis/rembg) |
| **U²-Net** | Apache-2.0 | Salient object detection (powers rembg) | [github.com/xuebinqin/U-2-Net](https://github.com/xuebinqin/U-2-Net) |
| **OpenCV** | Apache-2.0 | Image processing, filters, resize | [github.com/opencv/opencv](https://github.com/opencv/opencv) |
| **Pillow** | HPND (permissive) | Python image library | [github.com/python-pillow/Pillow](https://github.com/python-pillow/Pillow) |
| **Real-ESRGAN** | BSD-3 | Image upscaling / super-resolution | [github.com/xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) |

### PECH Use Cases

| Feature | Tool | Where Used |
|---------|------|------------|
| Product background removal | rembg + U²-Net | Marketplace, real estate |
| Image enhancement | Real-ESRGAN + OpenCV | Product photos, listings |
| Thumbnail generation | OpenCV + Pillow | All platforms |
| Image-to-description | Qwen2.5-VL-7B | Marketplace AI features |

**PECH Recommendation:** **rembg** for background removal (Canva-like feature in marketplace), **Real-ESRGAN** for upscaling low-quality product images, **Qwen2.5-VL** for AI-generated product descriptions from images.

---

## 14. TRANSLATION MODELS

For multilingual support across Nigerian and African languages.

| Model | License | Languages | Size | Download |
|-------|---------|-----------|------|----------|
| **Argos Translate** | MIT | 30+ language pairs | ~100 MB/pair | [github.com/argosopentech/argos-translate](https://github.com/argosopentech/argos-translate) |
| **NLLB-200** | CC-BY-NC-4.0 | 200 languages | 600M-3.3B | *(excluded — non-commercial)* |
| **OPUS-MT** | MIT/CC-BY-4.0 | 1000+ pairs | ~300 MB/pair | [github.com/Helsinki-NLP/Opus-MT](https://github.com/Helsinki-NLP/Opus-MT) |
| **Whisper** (translation mode) | MIT | 100+ → English | 1.5B | Same as STT above |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **General translation** | Argos Translate | MIT; offline; easy to deploy | OPUS-MT |
| **African languages** | Whisper (translate mode) | Best coverage of Nigerian languages → English | — |
| **UI/interface translation** | Argos Translate | Fast; lightweight; installable per-language | — |

**PECH Recommendation:** **Argos Translate** for general text translation, **Whisper translate mode** for speech translation from Nigerian languages to English.

> **Note:** African language NLP is still developing. For Yoruba, Hausa, Igbo — Whisper has basic support. For production-quality translation in these languages, consider contributing to or fine-tuning on local datasets (Phase 3).

---

## 15. NLP MODELS (Classification, NER, Sentiment)

For text classification, named entity recognition, sentiment analysis, and intent detection.

| Model | License | Parameters | Use Case | Download |
|-------|---------|-----------|----------|----------|
| **DistilBERT** | Apache-2.0 | 66M | Fast classification, sentiment | [huggingface.co/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) |
| **BERT-base** | Apache-2.0 | 110M | NER, classification | [huggingface.co/google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) |
| **DeBERTa-v3-small** | MIT | 44M | Better classification quality | [huggingface.co/microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) |
| **Jais-13B** | Apache-2.0 | 13B | Arabic + English bilingual | [huggingface.co/inception-mbzuai/jais-13b](https://huggingface.co/inception-mbzuai/jais-13b) |

### Comparison & Recommendation

| Use Case | Best Choice | Why | Runner-Up |
|----------|-------------|-----|-----------|
| **Sentiment analysis** | DistilBERT | Fastest; 66M params; CPU-friendly | DeBERTa-v3-small |
| **Named entity recognition** | BERT-base | Best NER ecosystem; many pre-trained NER heads | DeBERTa-v3-small |
| **Intent classification** | DeBERTa-v3-small | Higher accuracy than DistilBERT; still small | DistilBERT |
| **Support ticket routing** | DistilBERT | Fast inference; fine-tune on PECH support categories | — |

**PECH Recommendation:** **DistilBERT** for all lightweight NLP tasks (sentiment, routing, classification). Fine-tune on PECH-specific data in Phase 2. Use **DeBERTa-v3-small** if DistilBERT accuracy is insufficient.

---

## 16. MODEL DEPLOYMENT SUMMARY

### Phase 1 — Starter Hardware (1× RTX 4090, 24 GB VRAM)

Deploy via **Ollama** (simplest management):

| Slot | Model | VRAM | Purpose |
|------|-------|------|---------|
| Primary LLM | Qwen2.5-7B (Q4) | 4.5 GB | General AI assistant |
| Code | Qwen2.5-Coder-7B (Q4) | 4.5 GB | Developer platform |
| Vision | Qwen2.5-VL-3B (Q4) | 2 GB | Image understanding |
| Embeddings | all-MiniLM-L6-v2 | 0.1 GB | RAG pipeline |
| STT | Faster-Whisper (Small) | 1 GB | Voice input |
| TTS | Piper TTS | CPU | Voice output |
| OCR | PaddleOCR v4 | CPU | Invoice/receipt processing |
| Detection | RT-DETR-L | 2 GB | Solar panel inspection |
| NLP | DistilBERT | CPU | Sentiment/classification |
| ML | XGBoost + Prophet | CPU | Pricing, forecasting |
| **Total GPU** | | **~14 GB** | Fits in 24 GB with headroom |

### Phase 2 — Production (2× RTX 4090 or cloud)

Migrate to **vLLM** (higher throughput, batching):

| Slot | Model | VRAM | Purpose |
|------|-------|------|---------|
| Primary LLM | Qwen2.5-14B (Q4) | 8 GB | Better quality assistant |
| Code | Qwen2.5-Coder-14B (Q4) | 8 GB | Full coding assistant |
| Vision | Qwen2.5-VL-7B (Q4) | 5 GB | Production vision |
| Embeddings | Nomic-Embed-Text-v1.5 | 0.5 GB | Better RAG quality |
| Reasoning | Qwen2.5-32B (Q4) | 18 GB | Complex analysis (GPU 2) |
| STT | Faster-Whisper (Large-v3) | 4 GB | Best accuracy |
| All others | Same as Phase 1 | | |

### Phase 3 — Scale (Cloud GPU cluster)

- Fine-tuned PECH models on business data
- Qwen2.5-72B (Q4) for premium tier
- Multiple model replicas for concurrency
- A/B testing between model versions

---

## 17. VRAM QUICK-REFERENCE

All measurements assume inference only (not training). Q4 = 4-bit quantization via GGUF/AWQ.

| Model | FP16 | Q8 | Q4 | Minimum GPU |
|-------|------|-----|-----|-------------|
| Qwen2.5-0.5B | 1 GB | 600 MB | 350 MB | Any GPU / CPU |
| Qwen2.5-1.5B | 3 GB | 1.7 GB | 1 GB | GTX 1060+ |
| Qwen2.5-7B | 14 GB | 8 GB | 4.5 GB | RTX 3060 12GB |
| Qwen2.5-14B | 28 GB | 16 GB | 8 GB | RTX 4090 24GB |
| Qwen2.5-32B | 64 GB | 36 GB | 18 GB | 2× RTX 4090 |
| Qwen2.5-72B | 144 GB | 80 GB | 40 GB | A100 80GB or 2× A6000 |
| Mixtral-8x7B | 93 GB | 52 GB | 26 GB | 2× RTX 4090 |
| Mistral-7B | 14 GB | 8 GB | 4.5 GB | RTX 3060 12GB |
| Phi-4 (14B) | 28 GB | 16 GB | 8 GB | RTX 4090 24GB |
| Phi-3-Mini (3.8B) | 7.6 GB | 4.3 GB | 2.3 GB | RTX 3060 12GB |
| SmolLM2-1.7B | 3.4 GB | 1.9 GB | 1 GB | Any GPU |
| Whisper Large-v3 | 4 GB | 2.5 GB | — | RTX 3060+ |
| DistilBERT | 260 MB | — | — | CPU |
| all-MiniLM-L6-v2 | 80 MB | — | — | CPU |

---

*This document is confidential to PECH Group Holdings Ltd. Last updated: March 2026.*
