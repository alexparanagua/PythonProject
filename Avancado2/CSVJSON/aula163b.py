import json
from dados import *

dados_json = json.dumps(pessoas_dicionario, indent=4)
print(dados_json)
print(type(dados_json))