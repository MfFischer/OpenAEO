# 🌐 OpenAEO

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Status: Prototype](https://img.shields.io/badge/Status-Prototype-orange.svg)]()

**OpenAEO** is an open-source infrastructure layer that bridges the gap between the human-centric web and the world of AI agents. It enables websites to become **AI-readable**, **verifiable**, and **privacy-aware**.

---

## 🚀 The Vision

As AI systems increasingly act as intermediaries between users and the web, most websites remain invisible, misrepresented, or unverifiable. **OpenAEO** addresses this by providing a modular toolkit that transforms web content into structured, machine-readable formats while maintaining trust and privacy.

### 🔍 The Problem
Current web standards (SEO, metadata, schema.org) were designed for search engines—not AI agents.
- **Invisibility:** Websites are not reliably understood by AI systems.
- **Hallucinations:** Content can be misinterpreted or fabricated by LLMs.
- **Trust Gap:** No standard exists for verifiable AI-consumable content.
- **Lack of Control:** Website owners cannot control how AI accesses their data.

### 💡 The Solution
OpenAEO introduces an open and extensible framework:
- **AI Readability Engine:** Converts unstructured HTML into high-fidelity AI-friendly JSON.
- **Verification Layer:** Content signing and trust scoring using cryptographic hashing.
- **Privacy Layer:** Fine-grained, GDPR-aware exposure rules for AI access.
- **Developer SDK:** Seamless integration into any CMS, API, or web stack.

---

## 🏗️ Project Structure

```bash
openaeo/
├── api/                # FastAPI Application Layer
│   └── main.py         # Primary API endpoints
├── core/               # Transformation Engine
│   ├── parser.py       # HTML parsing (BS4/Playwright)
│   ├── extractor.py    # Content & Entity extraction
│   └── formatter.py    # AI-readable JSON formatting
├── verification/       # Trust & Integrity Layer
│   └── signer.py       # Hashing and digital signatures
├── examples/           # Implementation examples
│   └── sample_output.json
├── LICENSE             # MIT License
├── README.md           # Project Documentation
└── requirements.txt    # Python dependencies
```

---

## 🛠️ Quick Start (MVP Prototype)

### 1. Installation
```bash
git clone https://github.com/MfFischer/OpenAEO.git
cd OpenAEO
pip install -r requirements.txt
```

### 2. Run the API
```bash
uvicorn api.main:app --reload
```

### 3. Analyze a Webpage
Send a POST request to `/analyze` with a URL:
```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'
```

---

## 🎯 Roadmap (Prototype Phase)

- [x] **Core AI-readability engine** (Transformation layer)
- [x] **Basic content verification** (Hashing + Signatures)
- [x] **JSON-based output standard** for AI agents
- [ ] **Developer CLI** for local analysis
- [ ] **LLM Integration** for advanced entity extraction

---

## 🌍 Public Benefit

OpenAEO contributes to a more transparent and trustworthy AI ecosystem by:
- Reducing dependence on centralized AI platforms.
- Empowering small and independent websites with equal visibility.
- Establishing open standards for AI-web interaction.

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
