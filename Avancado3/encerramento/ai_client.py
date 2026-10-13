import os
import requests
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_ENDPOINT = os.getenv("GROQ_ENDPOINT", "https://api.groq.com/openai/v1/chat/completions")


class GroqAPIError(Exception):
    pass


def chat_completions(messages, model='openai/gpt-oss-20b', temperature=0.4, max_tokens=400):
    if not GROQ_API_KEY:
        raise GroqAPIError("Chave da API não encontrada. Defina a variável de ambiente GROQ_API_KEY.")

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    resp = requests.post(GROQ_ENDPOINT, json=payload, headers=headers, timeout=60)
    if resp.status_code >= 400:
        raise GroqAPIError(f"Erro {resp.status_code}: {resp.text}")

    data = resp.json()
    return data["choices"][0]["message"]["content"]