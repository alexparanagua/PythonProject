lista_produtos = {"geladeira":2500,"microondas":350,"fogao":1300,"liquidificador":220}

com_desconto = {cc:vv*0.95 for cc, vv in lista_produtos.items()}

print(lista_produtos)

print(com_desconto)