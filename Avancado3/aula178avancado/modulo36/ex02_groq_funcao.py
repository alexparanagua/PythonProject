from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO

MODELO_PADRAO = V_MODELO
MAX_SAIDA_PADRAO = 128


def gerar_texto(texto_entrada, *, temperatura=0.7, max_saida=MAX_SAIDA_PADRAO, modelo=MODELO_PADRAO):
    if not V_GROQ:
        raise ValueError("Token ausente. Verifique o arquivo .env e a variável GROQ_TOKEN.")

    client = Groq(api_key=V_GROQ)

    resp = client.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": texto_entrada}],
        temperature=temperatura,
        max_tokens=max_saida,
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    saida = gerar_texto("Liste 3 boas práticas ao consumir serviços web em Python.", max_saida=120)
    print(saida)