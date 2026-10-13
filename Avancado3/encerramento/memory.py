import json
import os

CAMINHO_PADRAO = os.path.join("data", "chat_history.json")


def carregar_historico(caminho=CAMINHO_PADRAO):
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_historico(mensagens, caminho=CAMINHO_PADRAO):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(mensagens, f, ensure_ascii=False, indent=2)