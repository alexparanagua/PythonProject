from fastapi import FastAPI, Header, HTTPException, Depends
from typing import Optional

app = FastAPI(title="API Protegida por Token")

TOKEN_ESPERADO = "secreto123"  # didático


def validar_token(authorization: Optional[str] = Header(None)) -> str:
    print("\n--- DEBUG: CONTEÚDO DE AUTHORIZATION ---")
    print(f"Valor recebido: {authorization}")
    print(f"Tipo do dado: {type(authorization)}")
    print("---------------------------------------\n")
    if authorization is None:
        raise HTTPException(status_code=401, detail="Token ausente.")

    partes = authorization.split()
    if len(partes) != 2 or partes[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Formato de token inválido.")

    if partes[1] != TOKEN_ESPERADO:
        raise HTTPException(status_code=401, detail="Token inválido.")


@app.get("/publico")
def publico():
    return {"mensagem": "Este endpoint é público."}


@app.get("/privado")
def privado(authorization: Optional[str] = Header(default=None)):
    validar_token(authorization)
    return {"mensagem": "Acesso autorizado ao endpoint privado."}

@app.get("/sua-rota")
def minha_rota(token: str = Depends(validar_token)):
    return {"mensagem": "Se você chegou aqui, o token funcionou!"}