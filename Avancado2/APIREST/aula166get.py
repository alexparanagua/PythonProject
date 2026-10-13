import requests


def buscar_endereco_por_cep(cep: str) -> dict:
    cep = "".join(ch for ch in cep if ch.isdigit())

    if len(cep) != 8:
        raise ValueError("CEP inválido. Use 8 dígitos.")

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    dados = response.json()
    if dados.get("erro"):
        raise ValueError("CEP não encontrado.")

    return {
        "cep": dados.get("cep"),
        "logradouro": dados.get("logradouro"),
        "bairro": dados.get("bairro"),
        "cidade": dados.get("localidade"),
        "uf": dados.get("uf"),
    }


try:
    endereco = buscar_endereco_por_cep("41720-020")
    print(endereco)
except (ValueError, requests.RequestException) as e:
    print("Erro:", e)