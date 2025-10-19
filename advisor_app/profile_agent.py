# ============================================
# FILE: advisor_app/profile_agent.py
# ============================================
from config.gemini_client import ask_gemini


def profile_tool(age: str, occupation: str, health_status: str, medical_conditions: str) -> str:
    """
    Profile tool that collects and validates user profile.
    
    Args:
        age: User's age
        occupation: User's occupation
        health_status: Health status (Excellent/Good/Fair/Poor)
        medical_conditions: Medical conditions or 'None'
        
    Returns:
        Profile summary
    """
    print(f"[PROFILE] Received - Age: {age}, Occupation: {occupation}")
    print(f"[PROFILE] Health: {health_status}, Conditions: {medical_conditions}")
    
    print("[PROFILE] Profile saved successfully")
    
    return f""" PROFILE COLLECTED
Age: {age}
Occupation: {occupation}
Health Status: {health_status}
Medical Conditions: {medical_conditions if medical_conditions.lower() != 'none' else 'None'}

Your profile has been recorded. Proceeding to next step..."""