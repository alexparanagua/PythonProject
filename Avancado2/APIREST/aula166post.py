import requests

url = "https://httpbin.org/post"  # endpoint de teste

payload = {
    "titulo": "Estudar requests",
    "prioridade": "alta",
    "feita": False
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "PythonProfissional/1.0"
}

with requests.Session() as session:
    session.headers.update(headers)

    response = session.post(url, json=payload, timeout=10)
    response.raise_for_status()

    retorno = response.json()
    print("JSON enviado:", retorno["json"])