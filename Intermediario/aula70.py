listas = [[1,2,3],[4,5,6],[7,8,9]]


print(f"unico numero {listas[0][2]}")

print("todos")
for lista in listas:
    for num in lista:
        print(num)

#list comprehension
[print(lista) for lista in listas]

[[print(num) for num in lista] for lista in listas]

matriz = [[num for num in range(1,4)] for lista in range(1,4)]
print(matriz)