from functools import reduce

lista = [
    {'nome':'José','idade':17},
    {'nome':'Alex','idade':26},
    {'nome':'Brenanildes','idade':33},
    {'nome':'Alguem','idade':12}
]

menores_18 = list(filter(lambda p:p['idade']<18,lista))
print((menores_18))

so_idade =list(map(lambda p : p['idade'],list(menores_18)))
print((so_idade))

soma = reduce(lambda x,y : x+y,list(so_idade))

print(soma)