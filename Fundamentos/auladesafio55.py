import random
def motivacao() :
    msgs =["Vamos continue...", "Bela tentativa!", "Esta perto, continue...", "Está chegando perto...", "Isso ai, boa tentativa", "Gostei, vc consegue"]
    return " --- "+random.choice(msgs)+" --- "

def gerar_numero_secreto(modo_teste=False, numero_fixo=9):
    if(modo_teste):
        return numero_fixo
    else:
        return random.randint(1,100)

def ler_palpite(numero,segredo,palpites):
    retorno = False
    if (numero>segredo):
         print(f"numero {numero} maior que segredo")
         palpites.append(f"segrego<{numero}")
    elif (numero < segredo):
        print(f"numero {numero} menor que segredo")
        palpites.append(f"{numero}<segrego")
    else:
        print(f" *** O segredo foi encontrado = {numero}, Parabéns!!! ***")
        retorno = True
    print(palpites)
    return retorno

def jogar(segredo, tentativas):
    palpites =[]
    while tentativas!=0:
        numero = input("Digite o numero: ")
        if(numero.isdigit()) :
            if(ler_palpite(int(numero),segredo,palpites)):
                break
            else :
                print(motivacao())
        else:
            print(f" {numero} nao é um numero valido! tente novamente")
        tentativas-=1
        print(f"*ATENCAO: vc tem mais {tentativas} tentativas!")
        if(tentativas==0) :
            print(f"As tentativas chegaram ao fim, o segredo era {segredo}!")
            break

tentativas = 10
jogar_novamente = "S"
while jogar_novamente == "S" :
    segredo = int(gerar_numero_secreto())
    jogar(segredo, tentativas)
    jogar_novamente = input("Jogar novamente (S/N)?")
