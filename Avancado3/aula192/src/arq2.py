from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    nome: str
    preco: float
    quantidade: int


def total_carrinho(itens: list[Item], cupom: str | None = None) -> float:
    total = sum(i.preco * i.quantidade for i in itens)
    return round(total * 0.90, 2) if cupom == "PROMO10" and total >= 100 else round(total, 2)