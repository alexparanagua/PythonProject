from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, Query, Header, status

from Tarefa import Tarefa
from crud import inserir, excluir, atualizar, buscar_todos, buscar_por_id

app = FastAPI(title="API de Gerenciamento de Tarefas")

# Token usado na validação do cabeçalho
TOKEN_ESPERADO = "meutoken"


# token
def validar_token(authorization: Optional[str] = Header(None)) -> str:
    print("\n--- DEBUG: CONTEÚDO DE AUTHORIZATION ---")
    print(f"Valor recebido: {authorization}")
    print(f"Tipo do dado: {type(authorization)}")
    print("---------------------------------------\n")

    if authorization is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token ausente.")

    partes = authorization.split()
    if len(partes) != 2 or partes[0].lower() != "bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Formato de token inválido.")

    if partes[1] != TOKEN_ESPERADO:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido.")

    return partes[1]


# ==========================================
# ROTAS DO FASTAPI (EndPoints)
# ==========================================

# 1. CADASTRAR (Inserir lote) - Protegido
@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def cadastrar_tarefas(lista: List[Tarefa], token: str = Depends(validar_token)):
    inserir(lista)  # Chama o seu método do crud.py
    return {"status": "Sucesso", "mensagem": f"{len(lista)} tarefa(s) inserida(s)."}


# 2. EXCLUIR (Deletar lote) - Protegido
@app.delete("/tarefas")
def deletar_tarefas(lista: List[Tarefa], token: str = Depends(validar_token)):
    excluir(lista)  # Chama o seu método do crud.py
    return {"status": "Sucesso", "mensagem": "Exclusão concluída com sucesso."}


# 3. ATUALIZAR (Editar lote) - Protegido
@app.put("/tarefas")
def atualizar_tarefas(lista: List[Tarefa], token: str = Depends(validar_token)):
    atualizar(lista)  # Chama o seu método do crud.py
    return {"status": "Sucesso", "mensagem": "Atualização concluída com sucesso."}


# 4. LISTAR TODOS OU POR PÁGINA (Público)
# Aceita parâmetros opcionais na URL. Ex: /tarefas?pagina=2&tamanho=5
@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas(
        pagina: Optional[int] = Query(None, description="Número da página", ge=1),
        tamanho: Optional[int] = Query(None, description="Quantidade de itens por página", ge=1, le=100)
):
    # Se você não passar parâmetros, certifique-se de que seu buscar_todos aceita None ou tem valores padrão
    return buscar_todos(pagina=pagina, tamanho_pagina=tamanho)


# 5. LISTAR POR ID ÚNICO (Público)
# Exemplo: /tarefas/5
@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
def obter_tarefa_por_id(tarefa_id: int):
    tt = buscar_por_id(tarefa_id)
    if not tt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada.")
    return tt
