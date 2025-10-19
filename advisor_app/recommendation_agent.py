# ============================================
# FILE: advisor_app/recommendation_agent.py
# ============================================
from google.adk.agents import LlmAgent
from config.gemini_client import ask_gemini


HEALTH_POLICIES = {
    "basic": {"name": "Basic Health", "coverage": "$5K annual", "premium": "$50/mo", "deductible": "$500"},
    "standard": {"name": "Standard Plus", "coverage": "$25K annual", "premium": "$120/mo", "deductible": "$250"},
    "premium": {"name": "Premium Comprehensive", "coverage": "$100K annual", "premium": "$250/mo", "deductible": "$0"}
}

LIFE_POLICIES = {
    "basic": {"name": "Term Life Basic", "coverage": "$100K", "premium": "$20/mo", "term": "20 years"},
    "standard": {"name": "Term Life Standard", "coverage": "$500K", "premium": "$50/mo", "term": "30 years"},
    "premium": {"name": "Whole Life Premium", "coverage": "$1M", "premium": "$180/mo", "term": "Lifetime"}
}

VEHICLE_POLICIES = {
    "basic": {"name": "Basic Liability", "coverage": "Liability only", "premium": "$70/mo", "deductible": "$1000"},
    "standard": {"name": "Comprehensive", "coverage": "Full coverage", "premium": "$150/mo", "deductible": "$500"},
    "premium": {"name": "Premium Plus", "coverage": "Full + extras", "premium": "$250/mo", "deductible": "$250"}
}


def recommendation_tool(policy_selection: str) -> str:
    """
    Recommendation tool that provides top 3 policies and handles selection.
    
    Args:
        policy_selection: User's selected policy from recommendations
        
    Returns:
        Confirmation of selected policy
    """
    return f"""✓ POLICY RECOMMENDATION RECORDED
Selected Policy: {policy_selection}

Your recommendation has been noted. Proceeding to final confirmation..."""


policy_recommendation_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="policy_recommendation_agent",
    description="Provides personalized policy recommendations.",
    instruction="""You are the Recommendation Agent.

Your job:
1. Based on all collected info, provide TOP 3 personalized policies
2. Show for each: Name, Coverage, Premium, Why it fits them
3. Ask which one interests them
4. Record their choice

Do NOT save data - that's the next step.""",
    tools=[],
)