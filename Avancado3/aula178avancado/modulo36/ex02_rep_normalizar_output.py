import json
import replicate
from config_token import V_REPLICATE
from config_token import V_MODELO_TO_AUDIO


def normalizar_output(output):
    # Caso 1: lista (ex.: vários pedaços ou várias saídas)
    if isinstance(output, list):
        # Se houver URLs, pega a primeira URL encontrada
        for item in output:
            if isinstance(item, str) and item.startswith("http"):
                return item
        # Caso contrário, junta como texto
        return "".join(str(x) for x in output)

    # Caso 2: dicionário (alguns modelos retornam campos específicos)
    if isinstance(output, dict):
        for chave in ("audio", "output", "url"):
            if chave in output:
                return output[chave]
        return json.dumps(output, ensure_ascii=False)

    # Caso 3: string ou outro tipo simples
    return output


prompt = "Gere uma narração curta: 'Bem-vindo ao módulo 36. Vamos praticar integrações por API. Teste de Alex Paranaguá Neves de Lima'"

output = replicate.run(
    V_MODELO_TO_AUDIO,
    input={"prompt": prompt, "max_new_tokens": 148, "temperature": 0.7}
)

resultado = normalizar_output(output)
print("Resultado normalizado:")
print(resultado)