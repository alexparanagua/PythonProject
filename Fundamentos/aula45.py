letras = set()
while True :
    palavra = input("Digite: ")
    if(palavra == "") :
        break
    for i in palavra :
        letras.add(i)

print(letras)