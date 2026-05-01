#!/usr/bin/env python3
"""
OpenAEO CLI — URL → AI-readable JSON

Usage:
    python main.py <url>
    python main.py https://example.com
    python main.py https://example.com > examples/output.json

Part of the OpenAEO Output Standard v0.1.
See: docs/openaeo_standard.md
"""

import sys
import json

from core.analyzer import build_openaeo_output


def main():
    if len(sys.argv) < 2:
        print("OpenAEO CLI v0.1 — AI-readable web content protocol")
        print()
        print("Usage: python main.py <url>")
        print()
        print("Example:")
        print("  python main.py https://example.com")
        print("  python main.py https://example.com > output.json")
        sys.exit(1)

    url = sys.argv[1]

    try:
        result = build_openaeo_output(url)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({
            "error": str(e),
            "source_url": url,
            "openaeo_version": "0.1"
        }, indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
