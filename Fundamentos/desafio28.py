numero = int(input("Digite o valor inteiro(>0): "))
texto = input("Digite a frase: ")
print("numero é: ", numero, " e o texto:", texto)

x = float(numero)
print(" a conversao ficou assim: " , x)

texto = texto.upper()
print("texto em maisculo: ", texto)

y = 10
if x > y :
    print("valor ",x," maior que ", y)
elif (x==y):
    print("valores iguais")
else :
    print("Valor ",x," menor que ", y)

