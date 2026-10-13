soma = 0
for i in range(1,3) :
    idade = int(input(f"/Digite a idade {i} : "))
    soma += idade
media = soma/2

print(f"A média é {media}")

numero = int(input("Entre com o numero: "))
fatorial=1
if(numero<0) :
    print(f"Não existe fatorial para {numero}")
elif numero ==0 :
    print(f"O fatorial de {numero} é 1")
else :
    for i in range(1,numero+1) :
        fatorial = fatorial * i
    print(f"O fatorial de {i} é {fatorial}")
