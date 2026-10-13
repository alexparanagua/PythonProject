import math
def area_circulo(r):
    return math.pi * (r**2)

raios = [3.4,1.2,11.3,2.5,5]

areas = list(map(area_circulo,raios))
#or
areas2 = list(map(lambda r: math.pi * (r ** 2),raios))

print(areas)
print(areas2)

print(math.pi)