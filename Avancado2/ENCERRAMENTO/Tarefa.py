from pydantic import BaseModel
from typing import Optional

class Tarefa(BaseModel):  # Certifique-se de que herda de BaseModel
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluida: bool = False
    criada: str