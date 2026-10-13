lista_idade = []
while True :
    idade = int(input("Digite a idade: "))
    if(idade==-1) :
        break
    lista_idade.append(idade)
tupla_idade = tuple(lista_idade)
print(f"Quantidade de idades = {len(tupla_idade)}")
print(f"Média das idades = {sum(tupla_idade)/len(tupla_idade)}")