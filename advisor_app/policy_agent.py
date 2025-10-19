# ============================================
# FILE: advisor_app/policy_agent.py
# ============================================
from google.adk.agents import LlmAgent
from config.gemini_client import ask_gemini


VALID_POLICY_TYPES = ["health", "life", "vehicle"]


def policy_selection_tool(policy_type: str, additional_detail: str) -> str:
    """
    Policy selection tool that validates and confirms policy choice.
    
    Args:
        policy_type: Type of policy (Health/Life/Vehicle)
        additional_detail: Budget/Coverage/Vehicle type
        
    Returns:
        Policy selection confirmation
    """
    policy_type_lower = policy_type.lower().strip()
    
    if policy_type_lower not in VALID_POLICY_TYPES:
        return f"""✗ INVALID POLICY TYPE
Selected: {policy_type}
Valid options: Health, Life, Vehicle

Please select one of the three policy types."""
    
    return f"""✓ POLICY SELECTED
Policy Type: {policy_type}
Details: {additional_detail}

Your policy preference has been recorded. Proceeding to risk analysis..."""


policy_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="policy_selection_agent",
    description="Handles policy type selection.",
    instruction="""You are the Policy Selection Agent.

Your job:
1. Ask for policy type (Health/Life/Vehicle)
2. Ask follow-up based on type
3. Confirm selection

Do NOT do risk analysis.""",
    tools=[],
)