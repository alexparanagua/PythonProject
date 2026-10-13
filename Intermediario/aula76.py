arquivo = open("texto.txt",'r',encoding="utf-8")
texto = arquivo.read()
i=1
for linha in texto.splitlines():
    print(i, linha)
    i+=1
arquivo.close()

