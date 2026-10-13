import requests
from config_token_exemplo import MINHA_API_KEY


class ApiClient:
    def __init__(self, base_url: str, api_key: str):
        if not api_key:
            raise ValueError("API key ausente. Verifique o .env e as variáveis de ambiente.")
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def get(self, path: str, params: dict | None = None, timeout: int = 15) -> dict:
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            resp = self.session.get(url, params=params, timeout=timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.Timeout:
            raise RuntimeError("Timeout: a API demorou demais para responder.")
        except requests.exceptions.HTTPError as e:
            # Evite imprimir headers; nunca exponha a chave
            raise RuntimeError(f"Erro HTTP: {resp.status_code} - {resp.text[:200]}") from e
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Falha de rede/HTTP: {e}") from e

# Uso (exemplo de base_url fictícia)
client = ApiClient("https://httpbin.org", MINHA_API_KEY)
data = client.get("/get")
print(data)