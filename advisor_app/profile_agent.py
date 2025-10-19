# ============================================
# FILE: advisor_app/profile_agent.py
# ============================================
from google.adk.agents import LlmAgent
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
    return f"""✓ PROFILE COLLECTED
Age: {age}
Occupation: {occupation}
Health Status: {health_status}
Medical Conditions: {medical_conditions if medical_conditions.lower() != 'none' else 'None'}

Your profile has been recorded. Proceeding to next step..."""


user_profile_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="user_profile_agent",
    description="Collects user profile information.",
    instruction="""You are the Profile Agent.

Your job is to ask these questions ONE AT A TIME:
1. Age
2. Occupation
3. Health Status
4. Medical Conditions

Do NOT ask about policy type - that's the next step.""",
    tools=[],
)