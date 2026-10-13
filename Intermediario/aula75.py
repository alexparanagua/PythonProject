arquivo = open("texto2.txt",'w')
print(type(arquivo))
texto = input("Digite um texto: ")
arquivo.write(texto)
arquivo.close()

#ler
arquivo = open("texto2.txt",'r')
print(type(arquivo))
texto = arquivo.read()
print(type(texto))
print(texto)
arquivo.close()