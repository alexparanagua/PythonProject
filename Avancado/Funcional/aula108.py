
'''def dobro(x):
    return x*2'''

d = lambda x : x * 2

print(d(4))

s = lambda x,y,z : x+y+z
print(s(1,2,3))
#or
print((lambda x,y,z : x+y+z)(5,2,5))


def cumprimento():
    titulo = 'Sr(a) '
    acao = lambda x : titulo + x
    return acao

print(cumprimento())

print(cumprimento()('Fulana'))