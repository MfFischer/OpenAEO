import requests
from bs4 import BeautifulSoup
from typing import Optional

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
