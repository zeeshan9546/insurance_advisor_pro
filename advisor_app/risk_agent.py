# ============================================
# FILE: advisor_app/risk_agent.py
# ============================================
from google.adk.agents import LlmAgent
from config.gemini_client import ask_gemini


def risk_analysis_tool(exercise_frequency: str, smoking_status: str, high_risk_hobbies: str, stress_level: str) -> str:
    """
    Risk analysis tool that calculates user's risk profile.
    
    Args:
        exercise_frequency: How often user exercises
        smoking_status: Smoking status (Yes/No)
        high_risk_hobbies: High-risk hobbies (Yes/No)
        stress_level: Stress level 1-10
        
    Returns:
        Risk assessment result
    """
    # Calculate risk score
    risk_score = 0
    
    # Exercise factor
    if "no" in exercise_frequency.lower() or "never" in exercise_frequency.lower():
        risk_score += 20
    elif "rarely" in exercise_frequency.lower():
        risk_score += 10
    
    # Smoking factor
    if "yes" in smoking_status.lower():
        risk_score += 25
    
    # High-risk hobbies factor
    if "yes" in high_risk_hobbies.lower():
        risk_score += 20
    
    # Stress factor
    try:
        stress = int(stress_level)
        if stress >= 8:
            risk_score += 15
        elif stress >= 6:
            risk_score += 10
        elif stress >= 4:
            risk_score += 5
    except:
        risk_score += 5
    
    # Determine risk level
    if risk_score <= 20:
        risk_level = "LOW"
        recommendation = "You qualify for the best rates and terms."
    elif risk_score <= 50:
        risk_level = "MEDIUM"
        recommendation = "You qualify for standard rates and coverage options."
    else:
        risk_level = "HIGH"
        recommendation = "You may have higher premiums, but suitable coverage is available."
    
    return f"""✓ RISK ASSESSMENT COMPLETE
Exercise: {exercise_frequency}
Smoking: {smoking_status}
High-Risk Hobbies: {high_risk_hobbies}
Stress Level: {stress_level}/10

Risk Score: {risk_score}/100
Risk Level: {risk_level}
Recommendation: {recommendation}

Proceeding to personalized recommendations..."""


risk_analysis_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="risk_analysis_agent",
    description="Analyzes user's risk profile.",
    instruction="""You are the Risk Analysis Agent.

Your job is to ask these questions ONE AT A TIME:
1. Exercise frequency
2. Smoking status
3. High-risk hobbies
4. Stress level (1-10)

Then calculate risk assessment.
Do NOT provide recommendations.""",
    tools=[],
)