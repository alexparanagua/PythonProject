def calcular_desconto(valor: float, cupom: str | None = None) -> float:
    if valor < 0:
        raise ValueError("valor não pode ser negativo")

    if cupom == "PROMO10" and valor >= 100:
        return round(valor * 0.90, 2)

    return round(valor, 2)