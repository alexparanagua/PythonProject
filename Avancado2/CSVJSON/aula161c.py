from csv import DictReader

with open("exemplo.csv") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        print(f'C1: {linha["CotaMensal"]} C2: {linha["DataInicio"]} \
C3: {linha["NomeProprietario"]} C4: {linha["Usuario"]}')

with open("exemplo.csv") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        print(f'{linha["CotaMensal"]}   {linha["DataInicio"]} \
   {linha["NomeProprietario"]}   {linha["Usuario"]}')