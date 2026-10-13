def falar_alto(funcao):
    def maiusculas(palavra):
        return funcao(palavra).upper()
    return maiusculas

@falar_alto
def saudacao(palavra):
    return f'Olá. {palavra}'


print(saudacao("Bom dia!!"))