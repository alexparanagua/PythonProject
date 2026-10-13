from csv import DictWriter

with open("filmes2.csv", "w", newline="", encoding="utf-8") as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input("Nome do filme: ")
        if filme != 'sair':
            genero = input("Gênero: ")
            duracao = input("Duração: ")
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
