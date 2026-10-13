rr= filter(lambda x: x % 2, [1,2,3,4,5,6,7])

print(rr)
print(list(rr))

lista = [
    {'nome':'José','idade':'17'},
    {'nome':'Alex','idade':'26'},
    {'nome':'Brenanildes','idade':'33'},
    {'nome':'Alguem','idade':'12'}
]

menores_18 = filter(lambda p: int(p['idade'])<18,lista)
print(list(menores_18))

nomes_max_5letras = filter(lambda p : len(p['nome'])>5,lista)
print(list(nomes_max_5letras))