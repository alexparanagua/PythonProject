def falar_alto(funcao):
    def maiusculas(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return maiusculas

@falar_alto
def saudacao(palavra):
    return f'Olá. {palavra}'

@falar_alto
def pedido(bola1, bola2):
    return f'Olá quero sorvete de {bola1} com {bola2}'

@falar_alto
def mensagem():
    return f'Bom te conhecer!!'

print(saudacao("Bom dia!!"))
print(pedido('Morango', 'Chocolate'))
print(mensagem())