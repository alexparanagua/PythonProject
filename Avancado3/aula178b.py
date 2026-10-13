import requests

response = requests.get("https://api.agify.io?name=joao", timeout=10)
response.raise_for_status()  # lança erro se status != 200

data = response.json()

# Pega apenas o campo desejado
age = data.get("age")

if age is None:
    print("A API respondeu, mas não retornou 'age' (campo ausente ou nulo).")
else:
    print("Idade estimada:", age)