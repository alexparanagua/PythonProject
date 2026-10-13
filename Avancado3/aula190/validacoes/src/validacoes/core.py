def cpf_limpo(cpf:str) -> str:
    return "".join(caractere for caractere in cpf if caractere.isdigit())