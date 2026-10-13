print("======== Desafio 1 ========")
print(" ")
numero = int(input("Digite o numero: "))
if(numero<=0) :
    print("Numero negativo ou igual a zero")
elif(numero % 2 ==0):
    print("Numero par")
else :
    print("Numero impar")

print("======== Desafio 2 ========")
print(" ")
altura = float(input("Digite sua altura(Exemplo: 1.84) : "))
sexo = input("Digite seu sexo (Exemplo: M ou F): ")

if(sexo == "M") :
    print((72.7*altura)-58)
else :
    print((62.1 * altura) - 44.7)

