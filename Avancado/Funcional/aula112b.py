produtos = [('tv',2500), ('fogao',1240),('radio',234)]

#novo_preco = preco * 1.05

novo_preco = lambda produto : (produto[0],[produto[1]*1.05])

print(list(map(novo_preco,produtos)))

#lista dict

lista = [
    {'nome':'José','idade':'28'},
    {'nome':'Alex','idade':'45'},
    {'nome':'Brena','idade':'33'},
    {'nome':'Alguem','idade':'12'}
]

so_nomes = lambda pessoa : pessoa['nome']

so_idades = lambda pessoa : int(pessoa['idade'])

print(list(map(so_nomes,lista))) #so nomes
print(list(map(so_idades,lista))) #so idades

print(sum(list(map(so_idades,lista)))) #soma das idades