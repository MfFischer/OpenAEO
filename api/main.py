from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from core.parser import HTMLParser
from core.extractor import ContentExtractor
from core.formatter import AIFormatter
from verification.signer import ContentSigner

app = FastAPI(title="OpenAEO API", version="0.1.0")

class AnalyzeRequest(BaseModel):
    url: Optional[str] = None
    html: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to OpenAEO API - The infrastructure layer for AI-readable websites."}

@app.post("/analyze")
def analyze_content(request: AnalyzeRequest):
    if not request.url and not request.html:
        raise HTTPException(status_code=400, detail="Either 'url' or 'html' must be provided.")
    
    try:
        parser = HTMLParser()
        if request.url:
            html_content = parser.fetch_content(request.url)
        else:
            html_content = request.html
            
        parser.parse(html_content)
        text_content = parser.get_text_content()
        title = parser.get_title()
        
        extractor = ContentExtractor(text_content)
        summary = extractor.extract_summary()
        entities = extractor.extract_entities()
        intent = extractor.extract_intent()
        key_facts = extractor.extract_key_facts()
        
        # Verification
        content_hash = ContentSigner.generate_hash(text_content)
        verification = ContentSigner.sign_content(content_hash)
        
        # Formatting
        result = AIFormatter.to_ai_json(
            title=title,
            summary=summary,
            entities=entities,
            intent=intent,
            key_facts=key_facts,
            verification_metadata=verification
        )
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
