from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="API de Tarefas com Token")

TOKEN_ESPERADO = "secreto123"


def autenticar(authorization: Optional[str] = Header(default=None)) -> None:
    if not authorization:
        raise HTTPException(status_code=401, detail="Token ausente.")
    partes = authorization.split()
    if len(partes) != 2 or partes[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Formato de token inválido.")
    if partes[1] != TOKEN_ESPERADO:
        raise HTTPException(status_code=401, detail="Token inválido.")


class TarefaIn(BaseModel):
    titulo: str
    feita: bool = False


class TarefaOut(TarefaIn):
    id: int


tarefas: List[TarefaOut] = []
proximo_id = 1


@app.get("/tarefas", response_model=List[TarefaOut])
def listar_tarefas():
    return tarefas


@app.post("/tarefas", response_model=TarefaOut, status_code=201, dependencies=[Depends(autenticar)])
def criar_tarefa(tarefa: TarefaIn):
    global proximo_id
    nova = TarefaOut(id=proximo_id, titulo=tarefa.titulo, feita=tarefa.feita)
    tarefas.append(nova)
    proximo_id += 1
    return nova


@app.delete("/tarefas/{tarefa_id}", status_code=204, dependencies=[Depends(autenticar)])
def remover_tarefa(tarefa_id: int):
    for i, t in enumerate(tarefas):
        if t.id == tarefa_id:
            tarefas.pop(i)
            return None
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")