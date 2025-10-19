# ============================================
# FILE: advisor_app/profile_agent.py
# DESCRIPTION:
# Updated to handle conditional profile collection
# based on existing user data from user_data/users.json
# ============================================

from typing import Optional  
from config.gemini_client import ask_gemini


def profile_tool(
    phone_number: str,
    policy_for_self: bool,
    profile_found: bool,
    existing_profile: Optional[dict] = None,  
    name: Optional[str] = None,
    age: Optional[str] = None,
    occupation: Optional[str] = None,
    health_status: Optional[str] = None,
    medical_conditions: Optional[str] = None
) -> str:
    """
    Profile collection tool with conditional logic.
    Handles three scenarios:
    1. Policy for self + profile found → merge existing + new data
    2. Policy for self + profile NOT found → collect all manually
    3. Policy for someone else → collect all info
    """

    print(f"[PROFILE] Processing profile...")
    print(f"[PROFILE] For self: {policy_for_self}, Profile found: {profile_found}")

    # ===== SCENARIO 1: POLICY FOR SELF + PROFILE FOUND =====
    if policy_for_self and profile_found and existing_profile:
        print("[PROFILE] Scenario 1: Merging existing profile with new inputs")

        final_name = existing_profile.get("name", name)
        final_age = existing_profile.get("age", age)
        final_occupation = existing_profile.get("designation", occupation)
        final_health = health_status or existing_profile.get("health_status", "Good")
        final_conditions = medical_conditions or existing_profile.get("medical_conditions", "None")

        print("[PROFILE]  Profile successfully merged")
        print(f"[PROFILE] Final - Name: {final_name}, Age: {final_age}, Health: {final_health}")

        return f"""PROFILE COMPLETE (Partially Retrieved)

Retrieved from System:
- Name: {final_name}
- Age: {final_age}
- Occupation: {final_occupation}

Your Additional Information:
- Health Status: {final_health}
- Medical Conditions: {final_conditions}

Profile updated successfully. Proceeding to policy selection..."""

    # ===== SCENARIO 2: POLICY FOR SELF + NO PROFILE FOUND =====
    elif policy_for_self and not profile_found:
        print("[PROFILE] Scenario 2: Collecting all information manually")
        print(f"[PROFILE] Collected - Name: {name}, Age: {age}, Occupation: {occupation}")
        print(f"[PROFILE] Health: {health_status}, Conditions: {medical_conditions}")

        return f"""PROFILE COMPLETE (Manual Entry)

Your Information:
- Name: {name}
- Age: {age}
- Occupation: {occupation}
- Health Status: {health_status}
- Medical Conditions: {medical_conditions}

Profile recorded successfully. Proceeding to policy selection..."""

    # ===== SCENARIO 3: POLICY FOR SOMEONE ELSE =====
    else:
        print("[PROFILE] Scenario 3: Collecting information for another person")
        print(f"[PROFILE] Collected for: {name}, Age: {age}, Occupation: {occupation}")

        return f"""PROFILE COMPLETE (For Another Person)

{name}'s Information:
- Age: {age}
- Occupation: {occupation}
- Health Status: {health_status}
- Medical Conditions: {medical_conditions}

Profile recorded successfully. Proceeding to policy selection..."""
