def primo(n) :
    """Retorna True se n for primo e False caso contratio
    n tem que ser um numero interio maior que 1 """
    ehprimo = True
    qtd_div = 0
    for i in range(1,n):
        if(n % i) == 0:
            qtd_div +=1
    if qtd_div>1:
        ehprimo=False
    return ehprimo