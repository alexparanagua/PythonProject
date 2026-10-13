def contador(max):
    cont =1
    while cont <= max:
        yield cont
        cont+=1

gen = contador(10)

print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(list(contador(3)))