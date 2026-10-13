cidade = ""
cidades = []
while cidade != "sair" :
    cidade = input("Digite a cidade: ")
    if(cidade!="sair"):
        cidades.append(cidade)
if(len(cidades)==0) :
    print("nao foram inseridas cidades")
cidades.sort()
for i in range(1,len(cidades)+1) :
    print(f"Cidade {i} = {cidades[i-1]}")