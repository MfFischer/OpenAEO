"""
OpenAEO Core Parser — HTML Fetching & Content Extraction

Provides both a functional API (for the v0.1 protocol CLI) and a class-based
API (for the FastAPI backend). The functional API is the primary interface
for the OpenAEO Output Standard v0.1.
"""

import requests
from bs4 import BeautifulSoup
from typing import Optional, Tuple


# ---------------------------------------------------------------------------
# Functional API — OpenAEO Output Standard v0.1
# ---------------------------------------------------------------------------

def fetch_html(url: str) -> str:
    """Fetch raw HTML content from a URL.

    Args:
        url: The target URL to fetch.

    Returns:
        The raw HTML string.

    Raises:
        requests.RequestException: If the HTTP request fails.
    """
    headers = {
        "User-Agent": "OpenAEO/0.1 (+https://github.com/MfFischer/OpenAEO)"
    }
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.text


def extract_main_content(html: str) -> Tuple[str, str]:
    """Extract the title and main textual content from raw HTML.

    Focuses on paragraph (<p>) tags to capture the primary readable content,
    filtering out navigation, scripts, and other non-content elements.

    Args:
        html: Raw HTML string.

    Returns:
        A tuple of (title, content) where content is the joined paragraph text.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Extract title
    title = soup.title.string.strip() if soup.title and soup.title.string else ""

    # Remove non-content elements
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    # Extract paragraph text as the main content signal
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    content = " ".join(p for p in paragraphs if p)

    return title, content


# ---------------------------------------------------------------------------
# Class-based API — backward compatibility with api/main.py
# ---------------------------------------------------------------------------

class HTMLParser:
    """
    Core HTML Parsing utility for OpenAEO.
    """
    def __init__(self, url: Optional[str] = None):
        self.url = url
        self.soup = None

    def fetch_content(self, url: Optional[str] = None) -> str:
        target_url = url or self.url
        if not target_url:
            raise ValueError("No URL provided for parsing.")
        
        response = requests.get(target_url, timeout=10)
        response.raise_for_status()
        return response.text

    def parse(self, html_content: str):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        return self.soup

    def get_title(self) -> str:
        if self.soup:
            title_tag = self.soup.find('title')
            return title_tag.get_text().strip() if title_tag else ""
        return ""

    def get_text_content(self) -> str:
        if self.soup:
            # Remove script and style elements
            for script_or_style in self.soup(["script", "style"]):
                script_or_style.decompose()
            return self.soup.get_text(separator=' ', strip=True)
        return ""
