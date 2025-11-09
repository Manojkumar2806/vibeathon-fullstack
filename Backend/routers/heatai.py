# backend/routers/query.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import requests
import chromadb
from dotenv import load_dotenv
from typing import Any, Optional
import logging

router = APIRouter()
logger = logging.getLogger("heatx.query")
logger.setLevel(logging.INFO)

# Load environment variables
load_dotenv()
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
CHROMA_API_KEY = os.getenv("CHROMA_CLOUD_API_KEY")
CHROMA_TENANT = os.getenv("CHROMA_CLOUD_TENANT")
CHROMA_DB = "HeatX Software"
CHROMA_COLLECTION = "Heatx"

if not PERPLEXITY_API_KEY or not CHROMA_API_KEY or not CHROMA_TENANT:
    raise RuntimeError("Missing required API keys/tenant in environment variables.")

# Initialize Chroma Cloud client
try:
    client = chromadb.CloudClient(
        api_key=CHROMA_API_KEY,
        tenant=CHROMA_TENANT,
        database=CHROMA_DB,
    )
except Exception as e:
    raise RuntimeError(f"Failed to initialize Chroma Cloud client: {e}")

try:
    knowledge_collection = client.get_collection(CHROMA_COLLECTION)
except Exception as e:
    raise RuntimeError(f"Failed to access ChromaDB collection '{CHROMA_COLLECTION}': {e}")

# Request / Response models
class QueryRequest(BaseModel):
    query: str
    n_results: int = 3

class QueryResponse(BaseModel):
    answer: str

# Prompt template instructing Perplexity to return short HTML
PROMPT_TEMPLATE = """
You are an expert assistant in industrial sustainability and heat-to-energy systems.
Answer the user's question **clearly, concisely, and in HTML format**. Keep the response short (<= 150 words).

Formatting rules:
- Start with a single <h3> title summarizing the answer.
- Use <ul> / <li> for 2–5 bullet points.
- Highlight key terms with <b>...</b>.
- End with a one-line italic insight: <p><i>Insight:</i> ...</p>

Context:
{context}

User Question:
{query}

Produce only the HTML answer (no additional commentary).
"""

def query_chroma_collection(query: str, n_results: int = 3) -> str:
    """
    Query the Chroma collection and return concatenated document text for context.
    """
    try:
        results = knowledge_collection.query(query_texts=[query], n_results=n_results)
        # results structure may vary — handle safely
        docs = results.get("documents", [[]])[0] if isinstance(results, dict) else []
        if not docs:
            return ""
        return "\n\n".join(docs)
    except Exception as e:
        logger.exception("ChromaDB query failed")
        raise RuntimeError(f"ChromaDB query failed: {e}")

def call_perplexity_api(query: str, context: str) -> str:
    """
    Call Perplexity chat completions API with an instruction to return HTML formatted output.
    """
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = PROMPT_TEMPLATE.format(context=context, query=query)

    payload = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Answer using the provided context and the formatting rules."}
        ],
        "temperature": 0.4,
        "max_tokens": 1024,
        "stream": False,
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
    except requests.RequestException as e:
        logger.exception("Request to Perplexity API failed")
        raise RuntimeError(f"Perplexity API request failed: {e}")

    if response.status_code != 200:
        logger.error("Perplexity API error: %s %s", response.status_code, response.text)
        raise RuntimeError(f"Perplexity API error: {response.status_code} {response.text}")

    data = response.json()
    # defensive extraction
    try:
        content = data["choices"][0]["message"]["content"]
        return content.strip()
    except Exception as e:
        logger.exception("Unexpected Perplexity response format")
        raise RuntimeError(f"Unexpected Perplexity response format: {e}")

@router.post("/", response_model=QueryResponse)
async def query_docs(request: QueryRequest):
    """
    Endpoint: POST /backend/routers/query (mounted path depends on your app)
    Body: { "query": "...", "n_results": 3 }

    Returns: HTML formatted short answer based on Chroma context and Perplexity completion.
    """
    try:
        if not request.query or not request.query.strip():
            raise HTTPException(status_code=400, detail="Query text is empty.")

        context = query_chroma_collection(request.query, request.n_results)
        if not context.strip():
            return QueryResponse(answer="<h3>No results</h3><p>No relevant information found in the knowledge base.</p>")

        response_text = call_perplexity_api(request.query, context)
        # ensure we return a short HTML string
        return QueryResponse(answer=response_text)
    except HTTPException:
        # re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.exception("Internal server error in query_docs")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
