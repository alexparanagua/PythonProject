numero = int(input("Digite um numero: "))
soma = 0
for i in str(numero) :
    soma += int(i)

print(f"Soma em for = {soma}")

soma2 =0
idx =0
while(idx < len(str(numero))) :
    soma2 += int(str(numero)[idx])
    print(f"letra {str(numero)[idx]} posicao {idx}")
    idx+=1

print(f"Soma while = {soma2}")

soma3 =0
resta =0
while numero !=0 :
    resta = numero%10
    print(f"resta > {resta}")
    soma3 += resta
    print(f"{numero/10} or {int(numero/10)}")
    numero = int(numero/10)
print(f"Soma do resta = {soma3}")