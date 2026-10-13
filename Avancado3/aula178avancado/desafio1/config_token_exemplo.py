import os
from dotenv import load_dotenv

load_dotenv('.env.example')
V_EXEMPLO = os.environ.get("V_EXEMPLO")

print(V_EXEMPLO)