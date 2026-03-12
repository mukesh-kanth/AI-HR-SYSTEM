import requests
from .knowledge_loader import load_company_knowledge

company_context = load_company_knowledge()

def generate_ai_response(message):

    prompt = f"""
You are an HR recruitment assistant.

Company knowledge:
{company_context}

Candidate question:
{message}
"""

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()
        return data.get("response", "AI did not return a response")

    except Exception as e:
        return f"AI server error: {str(e)}"