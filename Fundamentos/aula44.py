imoveis = {}
while True :
     apto = int(input("Digite o Apto: "))
     if(apto==-1) :
         break
     dono = input("Digite o Proprietario: ")
     imoveis.setdefault(apto,dono)
ordem = {}
ordenado = sorted(imoveis)
print(ordenado)
for i in range(1,len(ordenado)+1) :
    ordem.setdefault(ordenado[i-1],imoveis.get(ordenado[i-1]))

print(imoveis)
print(ordem)

''' or'''

lista = dict(sorted(imoveis.items()))

for chave, valor in lista.items() :
    print(f"{chave} - {valor}")

print(f"Total de apartamentos = {len(imoveis)}")