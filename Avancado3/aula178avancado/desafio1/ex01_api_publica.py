import requests

response = requests.get("https://api.agify.io?name=alex lima", timeout=10)
response.raise_for_status()

data = response.json()
campo = data['name']
try:
    campo = data['endereco']
except KeyError:
    print("campo endereco nao existe")

print(campo)

print(data)