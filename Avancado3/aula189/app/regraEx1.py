def eh_email_valido(email:str):
    if ('@' in email) and ('.' in email) and not(' ' in email):
        print('Parece email VALIDO! rs')
        return True
    elif ' ' in email:
        print('Email invalido, contem espacos!')
    else :
        print('Email invalido!')
    return False

def calcular_frete(peso_kg:float, uf:str, cotacao_combustivel) -> float:
    if peso_kg <=0:
        print('Valor negativo ou zero, nao permitido!')
        raise ValueError
    uf = uf.upper()#padronizar uf
    cotacao = cotacao_combustivel()
    if(str(cotacao).isdigit()):
        cotacao = int(0)
        if uf == 'SP':
            return (2 * peso_kg)+10+cotacao
        else:
            return (3 * peso_kg)+15+cotacao


