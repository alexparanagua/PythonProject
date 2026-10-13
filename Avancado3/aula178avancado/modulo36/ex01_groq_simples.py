from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO

# 1) Inicializa o cliente com o token
client = Groq(api_key=V_GROQ)

# 2) Texto de entrada
texto_entrada = "Explique em no máximo duas frases o que é uma API."

# 3) Chamada
response = client.chat.completions.create(
    model=V_MODELO,
    messages=[{"role": "user", "content": texto_entrada}],
    temperature=0.7,
    max_tokens=128,
)

# 4) Saída
print(response.choices[0].message.content)