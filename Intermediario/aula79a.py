from io import StringIO

frutas = ""
arquivo = StringIO(frutas)
while True:
    fruta = input("Digite uma fruta: ")
    if fruta == "sair":
        break
    else:
        arquivo.write(fruta)
        arquivo.write("\n")

arquivo.seek(0)
with open('frutas79_2.txt','w') as arq_fisico:
    for fruta in arquivo.readlines():
        arq_fisico.write(fruta)