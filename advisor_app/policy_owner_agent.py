# ============================================
# FILE: advisor_app/policy_owner_agent.py
# DESCRIPTION:
# Determines if policy is for the user or someone else
# Retrieves profile from user_data/users.json if applicable
# ============================================

from config.user_database import get_user_profile, format_user_profile


def policy_owner_tool(phone_number: str, owner_choice: str) -> dict:
    """
    Determines policy owner and retrieves existing profile if applicable.
    
    Args:
        phone_number: User's authenticated phone number
        owner_choice: "self" or "other" (from user response)
        
    Returns:
        Dict with owner info and profile data if available
    """
    
    print(f"[POLICY_OWNER] Owner choice: {owner_choice}")
    print(f"[POLICY_OWNER] Phone: {phone_number}")
    
    result = {
        "policy_for_self": "self" in owner_choice.lower(),
        "phone_number": phone_number,
        "existing_profile": None,
        "profile_found": False,
        "message": ""
    }
    
    # ===== IF POLICY IS FOR SELF =====
    if result["policy_for_self"]:
        print("[POLICY_OWNER] Policy is for self - attempting profile retrieval")
        
        # Try to retrieve existing profile from users.json
        profile = get_user_profile(phone_number)
        
        if profile:
            result["existing_profile"] = profile
            result["profile_found"] = True
            
            print("[POLICY_OWNER] Existing profile found in database")
            
            result["message"] = f""" PROFILE FOUND IN SYSTEM

I found your details:
{format_user_profile(profile)}

I'll need just a few more details:
- What type of insurance? (Health/Life/Vehicle)
- Any lifestyle details? (exercise, smoking, stress level)
"""
        
        else:
            print("[POLICY_OWNER]  No profile found - will collect all details")
            
            result["message"] = """ PROFILE NOT FOUND

I couldn't find your details in our system.
No problem! I'll collect your information now:
- Your Name
- Your Age
- Your Occupation
- Your Health Status
- Your Medical Conditions
"""
    
    # ===== IF POLICY IS FOR SOMEONE ELSE =====
    else:
        print("[POLICY_OWNER] Policy is for someone else - skipping retrieval")
        
        result["message"] = """ POLICY FOR SOMEONE ELSE

I'll collect complete information for them:
- Their Name
- Their Age
- Their Occupation
- Their Health Status
- Their Medical Conditions
"""
    
    print(f"[POLICY_OWNER] Profile found: {result['profile_found']}")
    
    return result