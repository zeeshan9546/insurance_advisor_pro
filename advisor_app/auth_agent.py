#============================================
# FILE: advisor_app/auth_agent.py
# ============================================
from google.adk.agents import LlmAgent
from config.gemini_client import ask_gemini


def validate_phone_number(phone: str) -> bool:
    """Simple phone number validation."""
    cleaned = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    return cleaned.isdigit() and len(cleaned) >= 10


def authentication_tool(phone_number: str) -> str:
    """
    Authentication tool that validates phone number.
    
    Args:
        phone_number: User's phone number
        
    Returns:
        Authentication result message
    """
    if validate_phone_number(phone_number):
        return f"""✓ AUTHENTICATION SUCCESSFUL
Phone Number: {phone_number}
Status: Verified

Your phone number has been verified. Proceeding to next step..."""
    else:
        return f"""✗ AUTHENTICATION FAILED
Phone Number: {phone_number}
Status: Invalid

Please provide a valid phone number with at least 10 digits."""


# Keep the LlmAgent for reference/backward compatibility
authentication_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="authentication_agent",
    description="Authenticates users by verifying their phone number.",
    instruction="""You are the Authentication Agent.

Your job:
1. Ask for phone number
2. Validate it (10+ digits)
3. Confirm authentication

Do NOT proceed to any other stages.""",
    tools=[],
)