def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def original(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto. O primeiro argumento tem que ser {valor}'
            return funcao(*args, **kwargs)
        return original
    return interna

@verifica_primeiro_argumento(20)
def calcula(num1, num2):
    return num1+num2

print(calcula(20, 30))
print(calcula(10, 40))