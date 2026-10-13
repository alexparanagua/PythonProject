def soma(*args):
    return sum(args)
print(soma(1,2,3,4,5,6,7,8,8,9,9,9,9,9,9))

def dic(**kwargs):
    print(kwargs)

dic(ana="1", alguem="44")

def dic2(**kwargs):
    for indice in kwargs:
        print(f"{indice} é igual a {kwargs[indice]}")

dic2(analice="ana2", fulano="alguem2")