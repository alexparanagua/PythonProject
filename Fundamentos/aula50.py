def com_retorno(um,dois=0):
    """soma de numeros onde nao informado o segundo ele deixa o valor zero"""
    return um + dois

uu = int(input("valor 1 = "))
dd = int(input("valor 2 = "))

media = com_retorno(dois=dd,um=uu)/2
media2 = com_retorno(um=uu)/2
print(f"media = {media} or {media2}")

help(com_retorno)