import requests

url = "https://httpbin.org/headers"
token = "MEU_TOKEN_DE_TESTE"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

print(response.json())