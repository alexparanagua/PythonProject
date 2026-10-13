z = zip([1,2,3,4,5],[0,1,2,3,4])

print(list(z))

#funcao integrada zip /juntar

tupla = (1,2,3,4,5,6,7)
lista = [11,12,13,14,15,16]
dicionario = {'a':21, 'b':22, 'c':23, 'd':24, 'e':25}

zp = zip(tupla,lista,dicionario.values())

print(list(zp))

#juntar
v1 = [1200,234,2345,1560]
v2 = [1245,300,2103,1434]
p = ['fogao', 'liquidificador', 'geladeira','tv']
lista = {venda[0]:max(venda[1],venda[2]) for venda in zip(p,v1,v2)}

print(lista)