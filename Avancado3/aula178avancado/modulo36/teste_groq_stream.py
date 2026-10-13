from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO
import time

client = Groq(api_key=V_GROQ)

prompt = "Descreva em detalhes as três principais funções de uma API."

stream = client.chat.completions.create(
    model=V_MODELO,
    messages=[{"role": "user", "content": prompt}],
    stream=True,
    max_tokens=512
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
        time.sleep(0.05)

print()