import requests

# Faz uma requisição (API pública, sem chave)
response = requests.get("https://api.agify.io?name=joao")

# Exibe o resultado em JSON
print(response.json())