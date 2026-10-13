from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO_AUDIO

client = Groq(api_key=V_GROQ)

# Certifique-se de que o arquivo existe no mesmo diretório!
with open("audioteste.mp3", "rb") as audio:
    transcription = client.audio.transcriptions.create(
        # Modelo padrão de alta qualidade.
        # DICA: Para maior velocidade, use "whisper-large-v3-turbo"
        model=V_MODELO_AUDIO,
        file=audio,
        # Opcional, mas recomendado para melhor precisão em PT-BR
        language="pt"
    )

print("Transcrição:", transcription.text)