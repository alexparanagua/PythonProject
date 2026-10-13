from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO


def gerar_texto(texto_entrada: str, *, temperatura: float = 0.7, limite_saida: int = 228) -> str:
    """
    Adapter simples: hoje usa Groq, amanhã pode ser outro provedor.
    A assinatura fica estável para o restante do projeto.
    """
    if not V_GROQ:
        raise ValueError("Token ausente. Verifique o .env (GROQ_TOKEN).")

    client = Groq(api_key=V_GROQ)

    resp = client.chat.completions.create(
        model=V_MODELO,
        messages=[{"role": "user", "content": texto_entrada}],
        temperature=temperatura,
        max_tokens=limite_saida,
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    saida = gerar_texto("Liste 3 boas práticas ao consumir um serviço web em Python.")
    print(saida)