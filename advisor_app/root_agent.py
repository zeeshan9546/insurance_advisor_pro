# ============================================
# FILE: advisor_app/root_agent.py
# ============================================

from google.adk.agents import Agent

# Import tools
from .auth_agent import authentication_tool
from .policy_owner_agent import policy_owner_tool
from .profile_agent import profile_tool
from .policy_agent import policy_selection_tool
from .risk_agent import risk_analysis_tool
from .recommendation_agent import recommendation_tool
from .storage_agent import storage_tool

print("[ROOT AGENT]  Initializing Insurance Advisor")


# Root agent with updated flow
root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash-exp",
    description="Insurance policy advisor that retrieves existing user profiles and asks conditional questions",
    instruction="""You are an insurance advisor. Guide users through 7 steps:

1. Authenticate: Ask phone number, use authentication_tool
2. Policy Owner: Ask "for yourself or someone else?", use policy_owner_tool
3. Profile: Show retrieved data if found, ask missing info, use profile_tool
4. Policy Type: Ask Health/Life/Vehicle, use policy_selection_tool
5. Risk: Ask exercise, smoking, hobbies, stress level, use risk_analysis_tool
6. Recommendations: Get policies from RAG, show top 3, use recommendation_tool
7. Confirmation: Summarize, confirm, save, use storage_tool

Rules:
- Ask ONE question per message
- Wait for response before next step
- If profile found: acknowledge + show data + ask missing fields only
- If profile not found: ask all fields
- If for someone else: skip database lookup, ask all fields
- Be conversational and clear""",
    tools=[
        authentication_tool,
        policy_owner_tool,
        profile_tool,
        policy_selection_tool,
        risk_analysis_tool,
        recommendation_tool,
        storage_tool,
    ],
)

print("[ROOT AGENT]  Agent initialized with 7 tools")


if __name__ == "__main__":
    print("[ROOT AGENT] Starting Insurance Advisor application...")
    root_agent.run()