import json
from dados import *

dados_dict = json.loads(pessoas_json)
for chave, valor in dados_dict.items():
    print(chave)
    print(valor)
