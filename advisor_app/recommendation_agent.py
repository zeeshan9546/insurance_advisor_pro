# ============================================
# FILE: advisor_app/recommendation_agent.py
# ============================================


from config.gemini_client import ask_gemini
from config.rag_service import ask_rag

def recommendation_tool(policy_selection: str) -> str:
    """
    Recommendation tool that fetches policy details dynamically from documents.

    Args:
        policy_selection: User's selected policy (e.g., 'Basic Health', 'Premium Life')

    Returns:
        A formatted string containing confirmation and detailed policy info
    """

    # 1.Log the received selection for debugging
    print(f"[RECOMMENDATION] User selected: {policy_selection}")

    # 2️.Query the RAG service for the selected policy details
    #    - This replaces the previous static dictionaries
    #    - Gemini will read the /docs folder and return context-aware info
    policy_info = ask_rag(
        f"Provide complete details for the {policy_selection} insurance policy, "
        "including coverage, premium, deductible, or term as applicable."
    )

    # 3️.Log successful retrieval
    print("[RECOMMENDATION] RAG result fetched successfully")

    # 4️.Return the confirmation and policy details
    return f""" POLICY RECOMMENDATION RECORDED
Selected Policy: {policy_selection}

Policy Details:
{policy_info}

Your recommendation has been noted. Proceeding to final confirmation..."""