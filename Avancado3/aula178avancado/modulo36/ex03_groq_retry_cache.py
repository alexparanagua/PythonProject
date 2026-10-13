from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO
import time

_cache = {}


def gerar_texto_com_retry(texto_entrada, *, max_saida=128, temperatura=0.7, tentativas=3):
    if not V_GROQ:
        raise ValueError("Token ausente. Verifique o arquivo .env e a variável GROQ_TOKEN.")

    # Cache simples: se a mesma entrada foi usada, não chama de novo
    chave_cache = (texto_entrada, max_saida, temperatura)
    if chave_cache in _cache:
        return _cache[chave_cache]

    client = Groq(api_key=V_GROQ)

    for tentativa in range(1, tentativas + 1):
        try:
            resp = client.chat.completions.create(
                model=V_MODELO,
                messages=[{"role": "user", "content": texto_entrada}],
                temperature=temperatura,
                max_tokens=max_saida,
            )
            saida = resp.choices[0].message.content
            _cache[chave_cache] = saida
            return saida
        except Exception as e:
            # Backoff simples: espera um pouco mais a cada tentativa
            if tentativa == tentativas:
                raise RuntimeError(f"Falha após {tentativas} tentativas: {e}")
            time.sleep(0.5 * tentativa)


if __name__ == "__main__":
    texto = "Explique em 3 tópicos o que é uma API."
    print(gerar_texto_com_retry(texto, max_saida=120))