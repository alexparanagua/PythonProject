from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO

client = Groq(api_key=V_GROQ)

prompt = "Crie uma lista com 5 boas práticas ao consumir APIs em Python."

stream = client.chat.completions.create(
    model=V_MODELO,
    messages=[{"role": "user", "content": prompt}],
    stream=True,
    max_tokens=300
)

texto_final = []

for chunk in stream:
    delta = None
    if chunk.choices and chunk.choices[0].delta:
        delta = chunk.choices[0].delta.content

    if delta:
        print(delta, end="", flush=True)
        texto_final.append(delta)

print()

texto_completo = "".join(texto_final)
print("\n---\nTexto completo (para uso posterior):\n")
print(texto_completo)