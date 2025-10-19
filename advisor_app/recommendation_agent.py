# ============================================
# FILE: advisor_app/recommendation_agent.py
# ============================================
from config.gemini_client import ask_gemini


# ===== POLICY DATABASES =====

HEALTH_POLICIES = {
    "basic": {
        "name": "Basic Health",
        "coverage": "$5K annual",
        "premium": "$50/mo",
        "deductible": "$500"
    },
    "standard": {
        "name": "Standard Plus",
        "coverage": "$25K annual",
        "premium": "$120/mo",
        "deductible": "$250"
    },
    "premium": {
        "name": "Premium Comprehensive",
        "coverage": "$100K annual",
        "premium": "$250/mo",
        "deductible": "$0"
    }
}

LIFE_POLICIES = {
    "basic": {
        "name": "Term Life Basic",
        "coverage": "$100K",
        "premium": "$20/mo",
        "term": "20 years"
    },
    "standard": {
        "name": "Term Life Standard",
        "coverage": "$500K",
        "premium": "$50/mo",
        "term": "30 years"
    },
    "premium": {
        "name": "Whole Life Premium",
        "coverage": "$1M",
        "premium": "$180/mo",
        "term": "Lifetime"
    }
}

VEHICLE_POLICIES = {
    "basic": {
        "name": "Basic Liability",
        "coverage": "Liability only",
        "premium": "$70/mo",
        "deductible": "$1000"
    },
    "standard": {
        "name": "Comprehensive",
        "coverage": "Full coverage",
        "premium": "$150/mo",
        "deductible": "$500"
    },
    "premium": {
        "name": "Premium Plus",
        "coverage": "Full + extras",
        "premium": "$250/mo",
        "deductible": "$250"
    }
}


def recommendation_tool(policy_selection: str) -> str:
    """
    Recommendation tool that records policy selection.
    
    Args:
        policy_selection: User's selected policy from recommendations
        
    Returns:
        Confirmation of selected policy
    """
    
    # Log received selection
    print(f"[RECOMMENDATION] User selected: {policy_selection}")
    
    # Record the selection
    print("[RECOMMENDATION] ✓ Selection recorded successfully")
    
    return f"""✓ POLICY RECOMMENDATION RECORDED
Selected Policy: {policy_selection}

Your recommendation has been noted. Proceeding to final confirmation..."""