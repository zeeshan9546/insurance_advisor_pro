# Insurance Advisor Application

Interactive insurance advisor built with Google Agent Development Kit (ADK). Guides users through a 6-step consultation to find the right insurance policy.

## Quick Start

### 1. Setup

```bash
git clone <repo-url>
cd insurance_advisor_pro
python -m venv venv

# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
```

### 2. Configure

1. Get API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Create .env
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

### 3. Run

```bash
adk web
```

Open http://127.0.0.1:8000 and select `advisor_app`

## Workflow

1. Authentication - Validate phone number
2. Profile - Collect age, occupation, health info
3. Policy - Choose Health, Life, or Vehicle
4. Risk - System calculates risk score
5. Recommendations - Get top 3 personalized policies
6. Confirmation - Save policy data

## How It Works

Root agent calls tool functions in sequence. Each tool in respective agent file handles that step.

## Customization

Change Model: Edit all `agent.py` files, replace `gemini-2.0-flash-exp`

Edit Policies: Update policy databases in `recommendation_agent.py`

Adjust Risk Scoring: Modify `risk_analysis_tool()` in `risk_agent.py`

## Troubleshooting

| Issue | Solution |
|-------|----------|
| App not in dropdown | Run `adk web` from project root |
| API key error | Check `.env` in `advisor_app/` folder |
| Quota exceeded | Wait 24h or upgrade API plan |
| Port 8000 in use | Run `adk web --port 8001` |

## Requirements

- Python 3.9+
- Google Gemini API key

## Security

Add to `.gitignore`:
```
.env
venv/
user_data/
__pycache__/
```

## Resources

- [Google ADK Docs](https://docs.google.com/document/d/1jqzxOJ5-cWGLQQp6JLN-lTg3_bvCEyRXDVYrKHaATVE/)
- [Gemini API](https://ai.google.dev/)