# ============================================
# FILE: advisor_app/risk_agent.py
# ============================================
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
    
    # Log received input
    print(f"[RISK] Received - Exercise: {exercise_frequency}, Smoking: {smoking_status}")
    print(f"[RISK] Hobbies: {high_risk_hobbies}, Stress: {stress_level}")
    
    # Initialize risk score
    risk_score = 0
    
    # ===== CALCULATE RISK FACTORS =====
    
    # Exercise factor (0-20 points)
    if "no" in exercise_frequency.lower() or "never" in exercise_frequency.lower():
        risk_score += 20
        print("[RISK] +20 points for no exercise")
    elif "rarely" in exercise_frequency.lower():
        risk_score += 10
        print("[RISK] +10 points for rarely exercising")
    
    # Smoking factor (0-25 points)
    if "yes" in smoking_status.lower():
        risk_score += 25
        print("[RISK] +25 points for smoking")
    
    # High-risk hobbies factor (0-20 points)
    if "yes" in high_risk_hobbies.lower():
        risk_score += 20
        print("[RISK] +20 points for high-risk hobbies")
    
    # Stress factor (0-15 points)
    try:
        stress = int(stress_level)
        if stress >= 8:
            risk_score += 15
            print("[RISK] +15 points for high stress (8-10)")
        elif stress >= 6:
            risk_score += 10
            print("[RISK] +10 points for moderate stress (6-7)")
        elif stress >= 4:
            risk_score += 5
            print("[RISK] +5 points for mild stress (4-5)")
    except:
        risk_score += 5
        print("[RISK] +5 points for invalid stress input")
    
    # ===== DETERMINE RISK LEVEL =====
    
    if risk_score <= 20:
        risk_level = "LOW"
        recommendation = "You qualify for the best rates and terms."
    elif risk_score <= 50:
        risk_level = "MEDIUM"
        recommendation = "You qualify for standard rates and coverage options."
    else:
        risk_level = "HIGH"
        recommendation = "You may have higher premiums, but suitable coverage is available."
    
    # Log final result
    print(f"[RISK]  FINAL - Score: {risk_score}/100, Level: {risk_level}")
    
    return f""" RISK ASSESSMENT COMPLETE
Exercise: {exercise_frequency}
Smoking: {smoking_status}
High-Risk Hobbies: {high_risk_hobbies}
Stress Level: {stress_level}/10

Risk Score: {risk_score}/100
Risk Level: {risk_level}
Recommendation: {recommendation}

Proceeding to personalized recommendations..."""