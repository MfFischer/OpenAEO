# OpenAEO — Project Plan

## 1. Current Prototype

The current prototype parses a URL and converts web content into structured, machine-readable JSON following the **OpenAEO Output Standard v0.1**. It includes:

- **HTML Parsing**: Fetches and parses web pages using BeautifulSoup.
- **Content Extraction**: Extracts title, paragraph text, and filters non-content elements.
- **AI Structuring**: Classifies intent, extracts entities and topics, generates summaries.
- **AI Context Block**: Produces a structured text block that AI agents can consume directly — a new web primitive analogous to `robots.txt` but for content understanding.
- **Verification**: Generates SHA-256 content hashes for integrity verification.
- **CLI Tool**: `python main.py <url>` outputs the full OpenAEO JSON.
- **REST API**: FastAPI endpoint at `/analyze` for programmatic access.

### What exists today:

| Component | Status | Description |
|-----------|--------|-------------|
| Core Parser | ✅ Complete | HTML fetching + content extraction |
| AI Analyzer | ✅ Complete | Intent, entities, topics, context block |
| Verification | ✅ Complete | SHA-256 content hashing |
| CLI | ✅ Complete | URL → JSON via command line |
| API | ✅ Complete | FastAPI `/analyze` endpoint |
| Output Standard | ✅ v0.1 | Formal specification defined |
| Examples | ✅ Complete | Real-world generated outputs |

---

## 2. Funded Phase — 6-Month Roadmap

In the funded phase, OpenAEO will expand from a working prototype into production-grade infrastructure:

### Month 1–2: Enhanced Extraction & NLP

- Integrate lightweight NLP models for better entity recognition
- Improve intent classification with multi-label support
- Add support for non-English content (multilingual extraction)
- Handle JavaScript-rendered pages (Playwright integration)

### Month 3: Verification Layer v2

- Content hashing with change detection (diff tracking)
- Timestamp-based content versioning
- Publisher identity verification (optional digital signatures)
- Trust score calculation based on content consistency

### Month 4: Developer SDK

- Python SDK: `pip install openaeo`
- JavaScript/Node.js SDK for web integration
- WordPress plugin for automatic OpenAEO metadata generation
- Documentation site with interactive examples

### Month 5: AI Context Block Standard

- Formal specification for the AI Context Block format
- Website-hosted `/.well-known/openaeo.json` endpoint proposal
- Integration guides for CMS platforms
- Outreach to AI agent developers (LangChain, AutoGPT, etc.)

### Month 6: Testing, Documentation & Community

- Comprehensive test suite (100+ websites across categories)
- Performance benchmarking and optimization
- Community contribution guidelines
- Conference paper / technical report for academic credibility

### Deliverables at end of funded phase:

1. Production-ready AI readability engine
2. Standardized AI Context Block specification
3. Content verification and trust scoring system
4. Developer SDKs (Python + JavaScript)
5. CMS integration (WordPress plugin)
6. Public documentation site
7. Technical report / white paper

---

## 3. Future Vision

Long-term, OpenAEO aims to become an **open standard for AI-readable web content**, similar to how `robots.txt` standardized crawler behavior and how `RSS` standardized content syndication. By providing a universal protocol for AI-web interaction, OpenAEO reduces dependence on centralized AI platforms and ensures that every website — regardless of size — can be accurately understood, verified, and fairly represented by AI systems.

---

## 4. Public Benefit

OpenAEO is designed as **public-good infrastructure** for the open web:

- **Levels the playing field**: Small websites and independent publishers can be accurately represented by AI systems, reducing the dominance of large platforms.
- **Reduces AI misinformation**: Content verification through cryptographic hashing enables AI agents to distinguish authentic content from fabricated or modified sources.
- **Gives publishers control**: The AI Context Block allows website owners to define how their content is understood by AI — not the other way around.
- **Privacy-aware by design**: OpenAEO respects data ownership and enables GDPR-compliant content exposure for AI consumption.
- **Open and decentralized**: MIT-licensed, community-driven, no vendor lock-in.

---

## 5. Technical Architecture

```
Input (URL)
    │
    ▼
┌──────────────┐
│  HTML Parser  │  ← Fetch + parse web content
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Extractor   │  ← Title, content, metadata
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Analyzer    │  ← Intent, entities, topics, context block
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Verifier    │  ← SHA-256 hash, timestamp
└──────┬───────┘
       │
       ▼
Output (OpenAEO v0.1 JSON)
```

---

## 6. Tech Stack

- **Language**: Python 3.9+
- **Web Framework**: FastAPI
- **HTML Parsing**: BeautifulSoup4
- **HTTP Client**: Requests
- **Hashing**: hashlib (SHA-256)
- **Future**: Playwright (JS rendering), spaCy (NLP), Node.js SDK

---

## 7. Risks & Mitigation

| Risk | Mitigation |
|------|-----------|
| Inconsistent content extraction across sites | Start with paragraph-based extraction; iteratively improve with heuristics |
| JavaScript-heavy pages not rendered | Playwright integration planned for Month 1-2 |
| LLM dependency for advanced features | Keep rule-based fallbacks for all core functions |
| Adoption challenges | Focus on developer experience; provide SDKs and plugins |
| Scope creep | Strictly follow 6-month roadmap; defer post-prototype features |

---

## 8. Team

**Lead Developer**: Open-source contributor with experience in AI infrastructure, web development, and developer tools.

**Community**: Open to contributors from the AI, web standards, and open-source communities.

---

*OpenAEO Project Plan — May 2026*
