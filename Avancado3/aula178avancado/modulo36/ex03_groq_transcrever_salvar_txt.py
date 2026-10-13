from pathlib import Path
from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO_AUDIO


def transcrever_e_salvar(arquivo_audio: str, saida_txt: str, *, idioma: str = "pt") -> Path:
    if not V_GROQ:
        raise ValueError("Token ausente. Verifique o .env (GROQ_TOKEN).")

    audio_path = Path(arquivo_audio)
    if not audio_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {audio_path.resolve()}")

    client = Groq(api_key=V_GROQ)

    with audio_path.open("rb") as audio:
        transcription = client.audio.transcriptions.create(
            model=V_MODELO_AUDIO,
            file=audio,
            language=idioma
        )

    texto = transcription.text.strip()

    out_path = Path(saida_txt)
    out_path.write_text(texto, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    destino = transcrever_e_salvar("audioteste.mp3", "transcricao_teste.txt")
    print(f"Transcrição salva em: {destino.resolve()}")