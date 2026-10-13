def frutas(n) :
    lista = ['abacaxi','pera','maca','banana']
    if n>3 :
        raise IndexError("valor excedido")
    else :
        return lista[n]

print(frutas(5))