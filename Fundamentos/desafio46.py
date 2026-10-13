pessoas = {}
count = 0
while count<5 :
    print(f"Pessoa {count+1}")
    nome = input(f"Digite o nome: ")
    idade = int(input("Digite a idade: "))
    tam = int(input("Digite o N.do calçado: "))
    pessoas.setdefault(nome,(idade,tam))
    count+=1
print(pessoas)
ordenar = dict(sorted(pessoas.items()))
print(ordenar)
total_idade = 0
total_calcado = 0
for pessoa in pessoas.values():
    print(pessoa[0])
    total_idade +=pessoa[0]
    print(pessoa[1])
    total_calcado+=pessoa[1]
print(total_idade)
print(total_calcado)
print(len(pessoas))
if(len(pessoas)>0) :
    print(f"Media idade = {int(total_idade/len(pessoas))}")
    print(f"Media calcado = {int(total_calcado/len(pessoas))}")