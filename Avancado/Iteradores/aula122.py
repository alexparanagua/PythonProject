frase = "frase qualquer aparece"

numeros = [1,2,3,4,5]

for letra in frase:
    print(letra,end='')
print('')
for numero in numeros:
    print(numero,end='')


def meu_loop(itera):
    it = iter(itera)
    while True:
        try:
            ii = next(it)
            if isinstance(ii,(int,float)):
                ii+=10
            print(ii)
        except StopIteration:
            break

meu_loop(numeros)
meu_loop(frase)