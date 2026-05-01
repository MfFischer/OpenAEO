# OpenAEO Output Standard v0.1

> A specification for structured, AI-readable, and verifiable web content.

## Overview

The OpenAEO Output Standard defines a machine-readable JSON format that enables AI systems to reliably consume, understand, and verify web content. It is designed to be:

- **Open**: Free to implement, extend, and integrate.
- **Minimal**: A small, well-defined set of fields — easy to adopt.
- **Verifiable**: Every output includes a content hash for integrity checking.
- **AI-native**: Structured specifically for LLMs and AI agents, not search engine crawlers.

---

## Schema Definition

| Field              | Type     | Required | Description                                                                 |
|--------------------|----------|----------|-----------------------------------------------------------------------------|
| `title`            | string   | ✅       | The title of the web page.                                                  |
| `summary`          | string   | ✅       | A concise summary of the page content (max 300 characters).                 |
| `entities`         | array    | ✅       | Named entities extracted from the content (people, organizations, products).|
| `intent`           | string   | ✅       | Content intent: `informational`, `commercial`, `navigational`, or `transactional`. |
| `key_topics`       | array    | ✅       | Primary topics/themes of the content, ordered by relevance.                 |
| `ai_context_block` | string   | ✅       | A structured text block for AI agents (see below).                          |
| `source_url`       | string   | ✅       | The original URL of the analyzed content.                                   |
| `content_hash`     | string   | ✅       | SHA-256 hash of the extracted content for integrity verification.           |
| `openaeo_version`  | string   | ✅       | The version of the standard used (e.g., `"0.1"`).                           |
| `timestamp`        | string   | ✅       | ISO 8601 UTC timestamp of when the analysis was performed.                  |

---

## AI Context Block

The **AI Context Block** is a new web primitive — analogous to `robots.txt` but for content understanding.

While `robots.txt` tells crawlers what they *can access*, the AI Context Block tells AI agents what the content *means*.

### Format

```
OPENAEO_CONTEXT_v0.1
TITLE: <page title>
INTENT: <intent classification>
TOPICS: <comma-separated topics>
ENTITIES: <comma-separated entities>
SUMMARY: <content summary>
END_CONTEXT
```

### Purpose

- Provides AI systems with a **pre-structured summary** without requiring full page parsing.
- Enables websites to **control their AI representation** — what AI agents "see" about them.
- Creates a **verifiable, standardized layer** between human web content and AI consumption.

---

## Example Output

```json
{
  "title": "Example Domain",
  "summary": "This domain is for use in illustrative examples in documents...",
  "entities": ["Internet Assigned Numbers Authority", "IANA"],
  "intent": "informational",
  "key_topics": ["domain", "examples", "documentation", "illustrative"],
  "ai_context_block": "OPENAEO_CONTEXT_v0.1\nTITLE: Example Domain\nINTENT: informational\nTOPICS: domain, examples, documentation\nENTITIES: IANA\nSUMMARY: This domain is for use in illustrative examples...\nEND_CONTEXT",
  "source_url": "https://example.com",
  "content_hash": "a1b2c3d4e5f6...",
  "openaeo_version": "0.1",
  "timestamp": "2026-05-01T17:48:00+00:00"
}
```

---

## Verification

Every OpenAEO output includes a `content_hash` field — a SHA-256 hash of the extracted text content.

This enables:
- **Content integrity**: AI agents can verify that content hasn't been tampered with.
- **Change detection**: Re-analyzing a URL and comparing hashes detects content updates.
- **Trust signaling**: A verifiable hash chain builds trust between content publishers and AI systems.

---

## Intent Classification

| Intent          | Description                                      | Example                          |
|-----------------|--------------------------------------------------|----------------------------------|
| `informational` | Educational, news, blog, or documentation content | Wikipedia article, blog post     |
| `commercial`    | Product, pricing, or sales-oriented content       | Product page, pricing table      |
| `navigational`  | Login, account, or navigation-oriented content    | Login page, dashboard            |
| `transactional` | Purchase, checkout, or order-oriented content     | Checkout page, payment form      |

---

## Conformance

An implementation is **conformant** with OpenAEO Output Standard v0.1 if:

1. All required fields are present in the output.
2. The `content_hash` is a valid SHA-256 hex digest of the extracted content.
3. The `ai_context_block` follows the specified format.
4. The `openaeo_version` field is set to `"0.1"`.
5. The `timestamp` is a valid ISO 8601 UTC string.

---

## License

This specification is released under the MIT License as part of the OpenAEO project.

---

*OpenAEO Output Standard v0.1 — May 2026*
