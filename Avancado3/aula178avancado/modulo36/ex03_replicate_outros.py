import replicate
import os
from config_token import REPLICATE_API_TOKEN
from config_token import V_MODELO_TO_AUDIO

if not REPLICATE_API_TOKEN:
    raise ValueError("Token ausente. Verifique o arquivo .env e a variável REPLICATE_API_TOKEN.")

# O cliente do Replicate lê o token pela variável de ambiente.
# Se necessário, você pode garantir isso manualmente (mas evite versionar!):

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

texto_entrada = "Olá! Gere uma saída em texto bem curta a partir deste texto."

output = replicate.run(
    V_MODELO_TO_AUDIO,
    input={
        "prompt": texto_entrada,
        "max_new_tokens": 128,
        "temperature": 0.1
    },
    token=REPLICATE_API_TOKEN
)

print("".join(output) if isinstance(output, list) else output)