from dataclasses import dataclass
from typing import Protocol


class RepositorioPedidos(Protocol):
    def salvar(self, pedido_id: str, total: float) -> None: ...

    def buscar_total(self, pedido_id: str) -> float | None: ...


@dataclass
class ServicoPedidos:
    repo: RepositorioPedidos

    def registrar_total(self, pedido_id: str, total: float) -> None:
        self.repo.salvar(pedido_id, total)

    def obter_total(self, pedido_id: str) -> float:
        total = self.repo.buscar_total(pedido_id)
        if total is None:
            raise ValueError("Pedido não encontrado")
        return total

    def total_carrinho(itens, cupom=None):
        total = 0
        for i in itens:
            total += i["preco"] * i["qtd"]
        if cupom:
            total *= 0.9
        return total

#Rodando mypy nesses exemplos:

# mypy src