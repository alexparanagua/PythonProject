import json
from dados import *

with open("pessoas.json", "r") as arquivo:
    dados_dict = json.load(arquivo)

for chave, valor in dados_dict.items():
    print(chave)
    print(valor)