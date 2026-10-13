lista = [1,2,3,4,5]
r= map(abs,lista)
print(list(r))
print(list(r))

#or
r= map(abs,lista)
l=list(r)
print(l)
print(l)

#or
r= map(abs,lista)
cubo = map(lambda x:x*x*x, lista)
print(list(cubo))
print(list(cubo))

lista2 = [11,12,13,14,15]

soma = map(lambda x, y : x+y, lista, lista2)
print(list(soma))

ll = map(lambda a,b,x:a*x+b, [1,3,5],[2,4,6],[1,1,1])
print(list(ll))
