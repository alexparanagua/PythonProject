import json
from dados import *

with open("pessoas.json", "w") as arquivo:
    json.dump(pessoas_dicionario, arquivo, indent=4)