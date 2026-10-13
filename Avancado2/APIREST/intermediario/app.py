from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Tarefas")


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

