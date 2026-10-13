dic={}
while True :
    try:
        sobrenome = input("Sobrenome: ")
        if(sobrenome==""):
            break
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))
    except:
        print("Dados invalidos")
        continue
    else:
        lista = [idade,altura,peso]
        dic.setdefault(sobrenome,lista)
soma_idade=0
soma_altura=0.0
soma_peso=0.0
dic_sort = sorted(dic)
for i in dic_sort:
    soma_idade += dic[i][0]
    soma_altura += dic[i][1]
    soma_peso += dic[i][2]
    print(f"{i} - {dic[i]}")
print(f"media idade = {soma_idade/2}")
print(f"media altura = {soma_altura/2}")
print(f"media peso = {soma_peso/2}")