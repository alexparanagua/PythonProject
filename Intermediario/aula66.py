from funcao import primo

numero = int(input("Digite o numero: "))

if primo(numero):
    print(f"O numero {numero} é primo! ")
else:
    print(f"O numero {numero} nao é primo! ")