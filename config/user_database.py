# ============================================
# FILE: config/user_database.py
# DESCRIPTION:
# Loads user records from user_data/users.json file
# Makes it easy to update without changing code
# ============================================

import json
import os


# Resolve path to users.json in user_data folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USERS_JSON_PATH = os.path.join(BASE_DIR, "user_data", "users.json")


def load_users_database() -> dict:
    """
    Load user records from user_data/users.json file.
    
    Returns:
        Dictionary mapping phone numbers to user records
    """
    try:
        if not os.path.exists(USERS_JSON_PATH):
            print(f"[USER_DB] Warning: {USERS_JSON_PATH} not found")
            return {}
        
        with open(USERS_JSON_PATH, "r", encoding="utf-8") as f:
            users = json.load(f)
            print(f"[USER_DB]  Loaded {len(users)} users from database")
            return users
    
    except json.JSONDecodeError as e:
        print(f"[USER_DB]  Error reading JSON: {str(e)}")
        return {}
    
    except Exception as e:
        print(f"[USER_DB]  Error loading users: {str(e)}")
        return {}


# Load users on startup
USERS_DATABASE = load_users_database()


def get_user_profile(phone_number: str) -> dict | None:
    """
    Retrieve user profile from database using phone number.
    
    Args:
        phone_number: User's phone number (will be cleaned)
        
    Returns:
        User profile dict if found, None if not found
    """
    
    # Clean phone number
    cleaned_phone = phone_number.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    
    print(f"[USER_DB] Looking up phone: {cleaned_phone}")
    
    if cleaned_phone in USERS_DATABASE:
        user = USERS_DATABASE[cleaned_phone]
        print(f"[USER_DB] User found: {user.get('name', 'Unknown')}")
        return user
    else:
        print(f"[USER_DB]  User not found in database")
        return None


def format_user_profile(user_profile: dict) -> str:
    """
    Format user profile into readable string.
    
    Args:
        user_profile: User profile dictionary
        
    Returns:
        Formatted string of user profile
    """
    return f"""
Name: {user_profile.get('name', 'N/A')}
Age: {user_profile.get('age', 'N/A')}
Designation: {user_profile.get('designation', 'N/A')}
Health Status: {user_profile.get('health_status', 'N/A')}
Medical Conditions: {user_profile.get('medical_conditions', 'None')}
"""