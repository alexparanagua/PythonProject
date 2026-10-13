from pathlib import Path
from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO_AUDIO


def transcrever_audio(caminho_audio: str, *, idioma: str = "pt", rapido: bool = False) -> str:
    if not V_GROQ:
        raise ValueError("Token ausente. Verifique o .env (GROQ_TOKEN) e o config_token.py.")

    arquivo = Path(caminho_audio)
    if not arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo.resolve()}")

    modelo = V_MODELO_AUDIO+"-turbo" if rapido else V_MODELO_AUDIO

    client = Groq(api_key=V_GROQ)

    with arquivo.open("rb") as audio:
        transcription = client.audio.transcriptions.create(
            model=modelo,
            file=audio,
            language=idioma
        )

    return transcription.text


if __name__ == "__main__":
    texto = transcrever_audio("audioteste.mp3", rapido=True)  # rápido=True usa o turbo
    print("Transcrição:\n")
    print(texto)