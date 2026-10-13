def saudacao(nome: str) -> str:
    nome_limpo = " ".join(nome.strip().split())
    return f"Olá, {nome_limpo}!"