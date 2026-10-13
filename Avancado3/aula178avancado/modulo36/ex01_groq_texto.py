from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO

if not V_GROQ:
    raise ValueError("Token ausente. Verifique o arquivo .env e a variável GROQ_TOKEN.")

client = Groq(api_key=V_GROQ)

texto_entrada = "Explique em no máximo duas frases o que é uma API."

response = client.chat.completions.create(
    model=V_MODELO,
    messages=[{"role": "user", "content": texto_entrada}],
    temperature=0.7,
    max_tokens=128,
)

print(response.choices[0].message.content)