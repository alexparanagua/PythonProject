def dobro(x):
    return x*2
def quadrado(x):
    return x * x
def calcular(operacao, lista, funcao):
    print(f'Calculando: {operacao}')
    for y in lista:
        print(y,'',funcao(y))

calcular('Dobro de 1 a 5 ', range(1,6), dobro)
calcular('Quadrado de 1 a 5 ', range(1,6), quadrado)

