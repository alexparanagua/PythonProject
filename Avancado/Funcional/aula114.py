from functools import reduce

r =reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9,10])

print(r)

r2 =reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9,10],1000)

print(r2)

#fatorial

f = lambda n: reduce(lambda  x, y: x*y, range(1, n+1))

print(f(5))