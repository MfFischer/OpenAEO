# 🌐 OpenAEO

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Standard: v0.1](https://img.shields.io/badge/OpenAEO_Standard-v0.1-green.svg)]()

**OpenAEO** is an open-source protocol that makes web content **AI-readable**, **verifiable**, and **structured** — enabling AI systems to reliably understand any website.

> Think of it as **`robots.txt` for AI understanding**: while `robots.txt` tells crawlers what they *can access*, OpenAEO tells AI agents what the content *means*.

---

## 🔍 The Problem

Current web standards (SEO, metadata, schema.org) were designed for search engines — not AI agents.

- **Invisibility:** Websites are not reliably understood by AI systems.
- **Hallucinations:** Content can be misinterpreted or fabricated by LLMs.
- **Trust Gap:** No standard exists for verifiable, AI-consumable content.
- **Lack of Control:** Website owners cannot control how AI represents their content.

---

## 💡 The Solution: OpenAEO Output Standard v0.1

OpenAEO defines a **structured JSON specification** that transforms any URL into AI-readable, verifiable output:

| Field              | Type   | Description                                           |
|--------------------|--------|-------------------------------------------------------|
| `title`            | string | Page title                                            |
| `summary`          | string | Concise content summary (max 300 chars)               |
| `entities`         | array  | Extracted named entities                               |
| `intent`           | string | Content classification: informational, commercial, navigational, transactional |
| `key_topics`       | array  | Primary content topics                                 |
| `ai_context_block` | string | Structured block for AI agents *(new web primitive)*  |
| `source_url`       | string | Original URL                                           |
| `content_hash`     | string | SHA-256 hash for content integrity verification       |

> 📄 Full specification: [`docs/openaeo_standard.md`](docs/openaeo_standard.md)

### The AI Context Block

The **AI Context Block** is a new web primitive. It provides AI systems with a pre-structured summary they can consume directly — giving website owners control over how AI represents their content:

```
OPENAEO_CONTEXT_v0.1
TITLE: Example Domain
INTENT: informational
TOPICS: domain, examples, documentation
ENTITIES: IANA, Internet Assigned Numbers Authority
SUMMARY: This domain is for use in illustrative examples...
END_CONTEXT
```

---

## 🛠️ Quick Start

### Installation

```bash
git clone https://github.com/MfFischer/OpenAEO.git
cd OpenAEO
pip install -r requirements.txt
```

### CLI Usage

Analyze any URL from the command line:

```bash
python main.py https://example.com
```

Output:

```json
{
  "title": "Example Domain",
  "summary": "This domain is for use in documentation examples...",
  "entities": ["Avoid", "Learn"],
  "intent": "informational",
  "key_topics": ["use", "domain", "documentation", "examples"],
  "ai_context_block": "OPENAEO_CONTEXT_v0.1\nTITLE: Example Domain\nINTENT: informational\n...\nEND_CONTEXT",
  "source_url": "https://example.com",
  "content_hash": "f7ced2eba2cef05c5f8948ae2b0f88db3ccea97cf999058d31265cbab453bb58",
  "openaeo_version": "0.1",
  "timestamp": "2026-05-01T17:51:28.370814+00:00"
}
```

Save output to file:

```bash
python main.py https://example.com > output.json
```

### API Usage

```bash
uvicorn api.main:app --reload
```

```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'
```

> 📁 See [`examples/`](examples/) for real-world generated outputs.

---

## 🏗️ Project Structure

```
openaeo/
├── core/
│   ├── parser.py         # HTML fetching & content extraction
│   ├── analyzer.py       # AI structuring engine (v0.1 protocol)
│   ├── extractor.py      # Content extraction module (API)
│   └── formatter.py      # AI-readable JSON formatting (API)
├── verification/
│   └── signer.py         # Content hashing & verification
├── api/
│   └── main.py           # FastAPI endpoints
├── docs/
│   └── openaeo_standard.md  # OpenAEO Output Standard v0.1
├── examples/
│   ├── blog.json         # Example: blog/documentation site
│   ├── company.json      # Example: organization website
│   └── docs.json         # Example: developer documentation
├── main.py               # CLI entry point
├── PROJECT_PLAN.md       # Detailed project roadmap
├── requirements.txt
└── LICENSE               # MIT
```

---

## 🎯 Roadmap

### ✅ Current Prototype

The current prototype parses a URL and converts web content into structured, machine-readable JSON including summary, entities, intent classification, and an AI Context Block — all verifiable via content hashing.

- [x] **OpenAEO Output Standard v0.1** — Formal specification
- [x] **AI Readability Engine** — URL → structured JSON
- [x] **AI Context Block** — Structured block for AI agents
- [x] **Content Verification** — SHA-256 hashing
- [x] **CLI Tool** — Command-line interface
- [x] **REST API** — FastAPI `/analyze` endpoint

### 🔜 Funded Phase (6 Months)

In the funded phase, OpenAEO will expand into:

- **Enhanced NLP**: Multilingual entity extraction and multi-label intent classification
- **Verification Layer v2**: Content versioning, change detection, and trust scoring
- **Developer SDK**: `pip install openaeo` + JavaScript SDK for web integration
- **CMS Plugins**: WordPress integration for automatic OpenAEO metadata
- **AI Context Block Standard**: Website-hosted `/.well-known/openaeo.json` proposal

> 📄 Full roadmap: [`PROJECT_PLAN.md`](PROJECT_PLAN.md)

### 🔭 Future Vision

Long-term, OpenAEO aims to become an **open standard for AI-readable web content**, similar to how `robots.txt` standardized crawler behavior and how `RSS` standardized content syndication.

---

## 🌍 Public Benefit

OpenAEO is **public-good infrastructure** for the open web:

- **Levels the playing field** — Small websites and independent publishers can be accurately represented by AI systems, reducing the dominance of large platforms.
- **Reduces AI misinformation** — Content verification through cryptographic hashing enables AI agents to distinguish authentic content from fabricated sources.
- **Gives publishers control** — The AI Context Block allows website owners to define how their content is understood by AI — not the other way around.
- **Privacy-aware by design** — Respects data ownership and enables GDPR-compliant content exposure for AI consumption.
- **Open and decentralized** — MIT-licensed, community-driven, no vendor lock-in.

---

## 🤝 Contributing

We welcome contributions from developers, researchers, and AI enthusiasts! Whether you want to improve the extraction logic, enhance the verification layer, or suggest new features, please feel free to open an issue or submit a pull request.

---

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<p align="center">
  Made with ❤️ for an Open Web
</p>
