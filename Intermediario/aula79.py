
with open("frutas79.txt", "w") as arquivo:
    while True:
        fruta = input("Digite uma fruta: ")
        if fruta == "sair":
            break
        else:
            arquivo.write(fruta)
            arquivo.write("\n")