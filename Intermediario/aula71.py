dicio = {'a':1,'b':2,'c':3, 'd':4}

quadrado = {cc:vv**2 for cc, vv in dicio.items()}

print(dicio)
print(quadrado)

quadrado2 = {cc:vv**2 for cc, vv in dicio.items() if not (vv%2)}

print(quadrado2)