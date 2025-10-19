# ============================================
# FILE: advisor_app/auth_agent.py
# ============================================
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
    print(f"[AUTH] Received phone: {phone_number}")
    
    if validate_phone_number(phone_number):
        print(f"[AUTH] VALID - Phone verified")
        return f"""AUTHENTICATION SUCCESSFUL
Phone Number: {phone_number}
Status: Verified

Your phone number has been verified. Proceeding to next step..."""
    else:
        print(f"[AUTH] INVALID - Invalid phone format")
        return f""" AUTHENTICATION FAILED
Phone Number: {phone_number}
Status: Invalid

Please provide a valid phone number with at least 10 digits."""