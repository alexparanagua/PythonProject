from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Tarefas2")


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


@app.post("/tarefas", response_model=TarefaOut, status_code=201)
def criar_tarefa(tarefa: TarefaIn):
    global proximo_id
    nova = TarefaOut(id=proximo_id, titulo=tarefa.titulo, feita=tarefa.feita)
    tarefas.append(nova)
    proximo_id += 1
    return nova


def encontrar_indice_por_id(tarefa_id: int) -> int:
    for i, t in enumerate(tarefas):
        if t.id == tarefa_id:
            return i
    return -1


@app.get("/tarefas/{tarefa_id}", response_model=TarefaOut)
def obter_tarefa(tarefa_id: int = Path(..., ge=1)):
    idx = encontrar_indice_por_id(tarefa_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return tarefas[idx]


@app.put("/tarefas/{tarefa_id}", response_model=TarefaOut)
def atualizar_tarefa(tarefa_id: int, dados: TarefaIn):
    idx = encontrar_indice_por_id(tarefa_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    atualizada = TarefaOut(id=tarefa_id, titulo=dados.titulo, feita=dados.feita)
    tarefas[idx] = atualizada
    return atualizada


@app.delete("/tarefas/{tarefa_id}", status_code=204)
def remover_tarefa(tarefa_id: int):
    idx = encontrar_indice_por_id(tarefa_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    tarefas.pop(idx)
    return None