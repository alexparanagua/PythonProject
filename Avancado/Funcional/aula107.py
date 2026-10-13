
def multiplicar(x):
    def calcular(y):
        return x*y
    return calcular

print('dobro',multiplicar(2)(33))
print('triplo',multiplicar(3)(5))