tupla = (3,4,8,9,1,3,4,3,0,1)

print(sorted(tupla))

print(sorted(tupla, reverse=True))

dicionario = [
    {'Titulo': 'Amigo', 'Tocou': 4},
    {'Titulo': 'Liberdade', 'Tocou': 45},
    {'Titulo': 'Para Sempre', 'Tocou': 12},
    {'Titulo': 'Nuvem de Lagrimas', 'Tocou': 23},
    {'Titulo': 'Papel Mache', 'Tocou': 14},
]

#ordenacao mais tocada

r= sorted(dicionario, key=lambda musica : musica['Tocou'], reverse=True)
print(r)