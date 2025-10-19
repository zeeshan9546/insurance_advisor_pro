# ============================================
# FILE: advisor_app/storage_agent.py
# ============================================
from config.gemini_client import ask_gemini
from datetime import datetime
import json
import os


# ===== CONFIGURATION =====

USER_DATA_DIR = "user_data"
POLICIES_FILE = "user_policies.json"


# ===== HELPER FUNCTIONS =====

def ensure_storage_directory():
    """Ensure the user data directory exists."""
    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)
        print(f"[STORAGE] Created directory: {USER_DATA_DIR}")


# ===== MAIN TOOL FUNCTION =====

def storage_tool(confirmation: str) -> str:
    """
    Storage tool that saves user data and policy.
    
    Args:
        confirmation: User's confirmation (Yes/No)
        
    Returns:
        Storage confirmation or error message
    """
    
    # Log received confirmation
    print(f"[STORAGE] Received confirmation: {confirmation}")
    
    # Check if user confirmed
    if "yes" in confirmation.lower():
        print("[STORAGE]  User confirmed - proceeding with save")
        
        # Create storage directory
        ensure_storage_directory()
        
        try:
            # ===== GENERATE POLICY ID =====
            policy_id = f"POL_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            print(f"[STORAGE] Generated Policy ID: {policy_id}")
            
            # ===== CREATE POLICY RECORD =====
            policy_record = {
                "policy_id": policy_id,
                "created_at": datetime.now().isoformat(),
                "status": "Active"
            }
            print(f"[STORAGE] Created policy record: {policy_id}")
            
            # ===== LOAD EXISTING POLICIES =====
            policies_file = os.path.join(USER_DATA_DIR, POLICIES_FILE)
            existing_policies = []
            
            if os.path.exists(policies_file):
                with open(policies_file, 'r') as f:
                    existing_policies = json.load(f)
                print(f"[STORAGE] Loaded {len(existing_policies)} existing policies")
            
            # ===== ADD NEW POLICY =====
            existing_policies.append(policy_record)
            print(f"[STORAGE] Total policies now: {len(existing_policies)}")
            
            # ===== SAVE TO FILE =====
            with open(policies_file, 'w') as f:
                json.dump(existing_policies, f, indent=2)
            
            print(f"[STORAGE]  Successfully saved to {policies_file}")
            
            return f""" SUCCESS! POLICY SAVED
Policy ID: {policy_id}
Status: Active
Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Your policy has been successfully saved!
You will receive confirmation via email/SMS.
Your coverage begins immediately.

Thank you for using Insurance Advisor!"""
            
        except Exception as e:
            print(f"[STORAGE]  ERROR during save: {str(e)}")
            
            return f""" ERROR SAVING POLICY
Error: {str(e)}

Please try again or contact support."""
    
    else:
        print("[STORAGE]  User did not confirm - policy not saved")
        
        return f"""No problem! Would you like to:
1. Review and change your selection
2. Start over with different options
3. Speak with an agent

Let us know how we can help!"""