def seja_educado(funcao):
    def sendo():
        print("Olá...")
        funcao()
        print("Foi um prazer conhecê-lo(a)!")
    return sendo

def saudacao():
    print("Seja bem-vendo(a) ao pyPRO!")

#saudacao()
saudacao_melhorada = seja_educado(saudacao)
saudacao_melhorada()
