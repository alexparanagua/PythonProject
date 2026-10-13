from csv import writer

with open("filmes.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input("Nome do filme: ")
        if filme != 'sair':
            genero = input("Gênero: ")
            duracao = input("Duração: ")
            escritor_csv.writerow([filme, genero, duracao])