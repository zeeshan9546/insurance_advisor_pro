# ============================================
# FILE: config/rag_service.py
# DESCRIPTION:
# Lightweight RAG service for insurance policies.
# Reads documents from /docs and queries Gemini
# to get context-aware answers.
# ============================================

import os
from config.gemini_client import ask_gemini  


# Dynamically resolve absolute path to /docs

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_PATH = os.path.join(BASE_DIR, "docs")


# Load all text documents from /docs folder

def load_documents():
    """
    Reads all .txt files from the docs directory and returns
    combined text for Gemini to reference.
    """
    docs = []
    for file in os.listdir(DOCS_PATH):
        if file.endswith(".txt"):
            path = os.path.join(DOCS_PATH, file)
            with open(path, "r", encoding="utf-8") as f:
                # Add filename as header for clarity in prompt
                docs.append(f"### {file}\n{f.read()}\n")
    return "\n".join(docs)


DOCUMENT_CONTEXT = load_documents()


# Main RAG function — ask Gemini with context

def ask_rag(query: str) -> str:
    """
    Sends user's query along with all document text to Gemini,
    letting the model infer which policy text is relevant.
    """
    prompt = f"""
You are an insurance advisor AI.

Use the below policy documents to answer accurately:

--- POLICY DOCUMENTS ---
{DOCUMENT_CONTEXT}

--- USER QUERY ---
{query}

Answer based only on the provided documents.
"""

    # Ask Gemini and return the result
    response = ask_gemini(prompt)
    return response
