try:
    with open("frutas2.txt", "x") as arquivo:
        while True:
            fruta = input("Digite uma fruta: ")
            if fruta == "sair":
                break
            else:
                arquivo.write(fruta)
                arquivo.write("\n")
except:
    print("Arquivo já existe! ")