import os
from dotenv import load_dotenv

load_dotenv()
V_GROQ = os.environ.get('GROQ_API_TOKEN')
V_REPLICATE = os.environ.get('REPLICATE_API_TOKEN')
V_MODELO = os.environ.get('MODELO_AI')
V_MODELO_AUDIO = os.environ.get('MODELO_AI_AUDIO')
V_MODELO_TO_AUDIO = os.environ.get('MODELO_AI_TOAUDIO')
REPLICATE_API_TOKEN = os.environ.get('REPLICATE_API_TOKEN')
#print(f'g={V_GROQ} | r={V_REPLICATE}')