# ============================================
# FILE: advisor_app/policy_agent.py
# ============================================
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
    # Log received input
    print(f"[POLICY] Received - Type: {policy_type}, Detail: {additional_detail}")
    
    # Normalize input
    policy_type_lower = policy_type.lower().strip()
    
    # Validate policy type
    if policy_type_lower not in VALID_POLICY_TYPES:
        print(f"[POLICY]  INVALID - Not in {VALID_POLICY_TYPES}")
        
        return f""" INVALID POLICY TYPE
Selected: {policy_type}
Valid options: Health, Life, Vehicle

Please select one of the three policy types."""
    
    # Log success
    print(f"[POLICY]  VALID - Policy type accepted")
    
    return f""" POLICY SELECTED
Policy Type: {policy_type}
Details: {additional_detail}

Your policy preference has been recorded. Proceeding to risk analysis..."""