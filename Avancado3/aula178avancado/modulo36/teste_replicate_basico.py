import replicate
from config_token import V_REPLICATE
from config_token import V_MODELO_TO_AUDIO

# O cliente lê o token via variável de ambiente.
# Se preferir setar aqui (evite versionar!): os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

prompt = "Olá! Este é um exemplo de conversão de texto para voz usando uma API Gratuita."

output = replicate.run(
    V_MODELO_TO_AUDIO,
    input={
        "prompt": prompt,  # alguns modelos usam "prompt"
        "max_new_tokens": 128,
        "temperature": 0.7
    }
)

# Muitos modelos retornam um iterável de pedaços (strings). Junte se necessário:
print("".join(output) if isinstance(output, list) else output)