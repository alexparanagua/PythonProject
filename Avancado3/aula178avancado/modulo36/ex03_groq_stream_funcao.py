from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO

def gerar_texto_stream(prompt: str, *, max_saida: int = 256, temperatura: float = 0.7) -> str:
    if not V_GROQ:
        raise ValueError("Token ausente. Verifique o .env (GROQ_TOKEN) e o config_token.py.")

    client = Groq(api_key=V_GROQ)

    try:
        stream = client.chat.completions.create(
            model=V_MODELO,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            temperature=temperatura,
            max_tokens=max_saida
        )

        partes = []
        for chunk in stream:
            delta = None
            if chunk.choices and chunk.choices[0].delta:
                delta = chunk.choices[0].delta.content

            if delta:
                print(delta, end="", flush=True)
                partes.append(delta)

        print()
        return "".join(partes)

    except KeyboardInterrupt:
        print("\n\nExecução interrompida pelo usuário.")
        return "".join(partes) if "partes" in locals() else ""
    except Exception as e:
        raise RuntimeError(f"Falha ao gerar texto em streaming: {e}")


if __name__ == "__main__":
    saida = gerar_texto_stream("Resuma em 3 tópicos o que é uma API.", max_saida=120)
    print("\n---\nRetorno da função (string final):\n")
    print(saida)