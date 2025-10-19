# ============================================
# FILE: advisor_app/storage_agent.py
# ============================================
from google.adk.agents import LlmAgent
from config.gemini_client import ask_gemini
from datetime import datetime
import json
import os


USER_DATA_DIR = "user_data"
POLICIES_FILE = "user_policies.json"


def ensure_storage_directory():
    """Ensure the user data directory exists."""
    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)


def storage_tool(confirmation: str) -> str:
    """
    Storage tool that saves user data and policy.
    
    Args:
        confirmation: User's confirmation (Yes/No)
        
    Returns:
        Storage confirmation or error message
    """
    if "yes" in confirmation.lower():
        ensure_storage_directory()
        
        try:
            # Generate policy ID
            policy_id = f"POL_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            # Create policy record
            policy_record = {
                "policy_id": policy_id,
                "created_at": datetime.now().isoformat(),
                "status": "Active"
            }
            
            # Save to file
            policies_file = os.path.join(USER_DATA_DIR, POLICIES_FILE)
            existing_policies = []
            
            if os.path.exists(policies_file):
                with open(policies_file, 'r') as f:
                    existing_policies = json.load(f)
            
            existing_policies.append(policy_record)
            
            with open(policies_file, 'w') as f:
                json.dump(existing_policies, f, indent=2)
            
            return f"""✓ SUCCESS! POLICY SAVED
Policy ID: {policy_id}
Status: Active
Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Your policy has been successfully saved!
You will receive confirmation via email/SMS.
Your coverage begins immediately.

Thank you for using Insurance Advisor!"""
            
        except Exception as e:
            return f"""✗ ERROR SAVING POLICY
Error: {str(e)}

Please try again or contact support."""
    
    else:
        return f"""No problem! Would you like to:
1. Review and change your selection
2. Start over with different options
3. Speak with an agent

Let us know how we can help!"""


data_storage_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="data_storage_agent",
    description="Saves user data and confirms policy enrollment.",
    instruction="""You are the Storage Agent. FINAL STEP.

Your job:
1. Summarize all collected information
2. Ask for confirmation (Yes/No)
3. Save if confirmed
4. Provide policy ID

This is the end of the workflow.""",
    tools=[],
)