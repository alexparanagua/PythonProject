musicas = [
    {'titulo': 'Amigo', 'tocou': 4},
    {'titulo': 'Ai se eu te pego', 'tocou': 45},
    {'titulo': 'Para Sempre', 'tocou': 12},
    {'titulo': 'Nuvem de Lágrimas', 'tocou': 23},
    {'titulo': 'Papel Machê', 'tocou': 14},
]

print(min(musicas, key=lambda musica: musica['tocou']))
print(max(musicas, key=lambda musica: musica['tocou']))