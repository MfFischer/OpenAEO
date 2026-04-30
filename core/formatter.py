import json
from typing import Dict, Any, List

class AIFormatter:
    """
    Formats extracted data into the OpenAEO AI-readable standard.
    """
    @staticmethod
    def to_ai_json(
        title: str,
        summary: str,
        entities: List[str],
        intent: str,
        key_facts: List[str],
        verification_metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        return {
            "title": title,
            "summary": summary,
            "entities": entities,
            "intent": intent,
            "key_facts": key_facts,
            "ai_context_block": f"Title: {title}. Intent: {intent}. Summary: {summary}",
            "verification": verification_metadata
        }
