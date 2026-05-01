"""
OpenAEO Analyzer — AI Content Structuring Engine

Transforms raw text content into the OpenAEO Output Standard v0.1 format.
This module is the core of the protocol: it takes unstructured web content
and produces structured, machine-readable, verifiable JSON for AI agents.
"""

import hashlib
import re
from collections import Counter
from datetime import datetime, timezone
from typing import Dict, List, Any

from core.parser import fetch_html, extract_main_content


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def classify_intent(text: str) -> str:
    """Classify the intent of web content using keyword heuristics.

    Categories:
        - commercial: product pages, shops, pricing
        - navigational: login, signup, account pages
        - transactional: checkout, purchase, order pages
        - informational: articles, blogs, docs (default)

    Args:
        text: The extracted text content.

    Returns:
        One of: "commercial", "navigational", "transactional", "informational".
    """
    text_lower = text.lower()

    commercial_signals = ["buy", "price", "shop", "product", "discount",
                          "sale", "offer", "cart", "order", "subscribe"]
    navigational_signals = ["login", "sign in", "sign up", "register",
                            "my account", "dashboard", "profile"]
    transactional_signals = ["checkout", "payment", "purchase", "billing",
                             "shipping", "confirm order"]

    scores = {
        "commercial": sum(1 for s in commercial_signals if s in text_lower),
        "navigational": sum(1 for s in navigational_signals if s in text_lower),
        "transactional": sum(1 for s in transactional_signals if s in text_lower),
    }

    best = max(scores, key=scores.get)
    if scores[best] >= 2:
        return best
    return "informational"


def extract_entities(text: str) -> List[str]:
    """Extract likely named entities from text using capitalization heuristics.

    Identifies capitalized multi-word phrases that are likely proper nouns,
    organization names, or product names.

    Args:
        text: The extracted text content.

    Returns:
        A deduplicated list of entity strings (max 15).
    """
    # Find capitalized word sequences (2+ words or single long capitalized words)
    patterns = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b', text)

    # Also grab standalone capitalized words that are long enough (likely proper nouns)
    single_caps = re.findall(r'\b([A-Z][a-z]{3,})\b', text)

    # Common words to exclude
    stop_words = {"The", "This", "That", "These", "Those", "There", "Here",
                  "What", "When", "Where", "Which", "While", "After", "Before",
                  "About", "With", "From", "Into", "Through", "During", "Since",
                  "However", "Although", "Because", "Also", "Many", "Some",
                  "Other", "Each", "Every", "Most", "More", "Such"}

    entities = []
    seen = set()
    for entity in patterns + single_caps:
        entity_clean = entity.strip()
        if entity_clean not in stop_words and entity_clean not in seen:
            seen.add(entity_clean)
            entities.append(entity_clean)

    return entities[:15]


def extract_topics(text: str) -> List[str]:
    """Extract key topics from text using word frequency analysis.

    Filters out common stop words and returns the most frequently occurring
    meaningful words as topic indicators.

    Args:
        text: The extracted text content.

    Returns:
        A list of top topic words (max 10).
    """
    stop_words = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
        "being", "have", "has", "had", "do", "does", "did", "will", "would",
        "could", "should", "may", "might", "shall", "can", "it", "its",
        "this", "that", "these", "those", "not", "no", "nor", "as", "if",
        "then", "than", "so", "up", "out", "about", "into", "over", "after",
        "we", "our", "us", "you", "your", "they", "them", "their", "he",
        "she", "his", "her", "who", "which", "what", "when", "where", "how",
        "all", "each", "every", "both", "few", "more", "most", "other",
        "some", "such", "only", "own", "same", "also", "very", "just",
    }

    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    filtered = [w for w in words if w not in stop_words]

    counter = Counter(filtered)
    return [word for word, _ in counter.most_common(10)]


def generate_context_block(title: str, content: str, intent: str,
                           entities: List[str], topics: List[str]) -> str:
    """Generate an AI Context Block — a structured text block for AI agents.

    The AI Context Block is a new web primitive, analogous to robots.txt but
    for content understanding. It provides AI systems with a pre-structured
    summary they can consume without parsing the full page.

    Args:
        title: The page title.
        content: The extracted text content.
        intent: The classified intent.
        entities: Extracted entities.
        topics: Extracted topics.

    Returns:
        A formatted context block string.
    """
    summary = content[:300].strip()
    if len(content) > 300:
        # Try to break at a sentence boundary
        last_period = summary.rfind(".")
        if last_period > 100:
            summary = summary[:last_period + 1]

    block = (
        f"OPENAEO_CONTEXT_v0.1\n"
        f"TITLE: {title}\n"
        f"INTENT: {intent}\n"
        f"TOPICS: {', '.join(topics[:5])}\n"
        f"ENTITIES: {', '.join(entities[:5])}\n"
        f"SUMMARY: {summary}\n"
        f"END_CONTEXT"
    )
    return block


def generate_hash(content: str) -> str:
    """Generate a SHA-256 content hash for verification and trust.

    This hash enables content integrity verification — AI agents can check
    whether the content they received matches the original source.

    Args:
        content: The text content to hash.

    Returns:
        The hex-encoded SHA-256 hash string.
    """
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Main Analysis Pipeline
# ---------------------------------------------------------------------------

def analyze_content(title: str, content: str) -> Dict[str, Any]:
    """Analyze extracted content and produce a structured OpenAEO result.

    This is the core structuring function that transforms raw title + content
    into the fields defined by the OpenAEO Output Standard v0.1.

    Args:
        title: The page title.
        content: The extracted text content.

    Returns:
        A dictionary matching the OpenAEO Output Standard v0.1 schema.
    """
    intent = classify_intent(content)
    entities = extract_entities(content)
    topics = extract_topics(content)
    context_block = generate_context_block(title, content, intent,
                                           entities, topics)

    return {
        "title": title,
        "summary": content[:300] if content else "",
        "entities": entities,
        "intent": intent,
        "key_topics": topics,
        "ai_context_block": context_block,
    }


def build_openaeo_output(url: str) -> Dict[str, Any]:
    """Full OpenAEO v0.1 pipeline: URL → structured, verifiable JSON.

    This is the primary entry point for the protocol. It fetches a URL,
    extracts content, analyzes it, and produces a complete OpenAEO output
    including verification metadata.

    Args:
        url: The target URL to analyze.

    Returns:
        A complete OpenAEO Output Standard v0.1 dictionary.
    """
    html = fetch_html(url)
    title, content = extract_main_content(html)

    data = analyze_content(title, content)

    return {
        **data,
        "source_url": url,
        "content_hash": generate_hash(content),
        "openaeo_version": "0.1",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
