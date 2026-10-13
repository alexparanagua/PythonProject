#com lista
def fibonacci_l(final):
    f = []
    a, b = 0 ,1
    while len(f) < final:
        f.append(b)
        a,b = b, a+b
    return f

print(fibonacci_l(10))

def fibonacci_g(final):
    a, b, contador = 0, 1, 0
    while contador < final:
        a ,b = b,a+b
        yield a
        contador+=1
print('')
for n in fibonacci_g(10):
    print(n,end=' ')