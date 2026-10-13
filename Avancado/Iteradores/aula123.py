class Contador:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim=fim
    def __iter__(self):
        return self
    def __next__(self):
        if self.inicio<self.fim:
            numero = self.inicio
            self.inicio+=1
            return numero
        else:
            raise StopIteration

numeros = Contador(1,6)

print(type(numeros))

it=iter(numeros)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except:
    print("erro do stop")


for i in Contador(1,11):
    print(i)

