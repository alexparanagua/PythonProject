lista = [1,2,3,4,5,6,7]

print(tuple(reversed(lista)))

frase = 'frase qualquer para impressao'

for letra in reversed(frase):
    print(letra, end='')

#or
print("\n")
print(frase[::-1])