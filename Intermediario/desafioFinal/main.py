import agenda as dd

compromissos = []

registro = ["Igreja", dd.formatarData('10/09/2026 10:30:45')]
dd.adicionar(compromissos,registro)
registro = ["Futebol", dd.formatarData('01/01/2001 12:30:43')]
dd.adicionar(compromissos,registro)
registro = ["Escola", dd.formatarData('01/03/2022 11:50:20')]
dd.adicionar(compromissos,registro)
registro = ["Banca", dd.formatarData('01/03/2022 08:50:20')]
dd.adicionar(compromissos,registro)

while True :
    try:
        print('--------------------SISTEMA DE AGENDAMENTO DE COMPROMISSOS *************')
        print(f"0 - Sair \n"
              f"1 - Adicionar \n"
              f"2 - Excluir \n"
              f"3 - Listar Todos \n"
              f"4 - Listar por Id \n"
              f"5 - Listar Futuro")
        acao = int(input("Informe a Ação desejada: :"))
        if(acao<0 or acao>5):
            continue
        elif acao==0:
            break
    except:
        continue
    print('--------------------')
    if(acao==1):
        titulo=input("Titulo: ")
        try:
            agenda=input("Data e Hora (dd/mm/yyyy 00:00:00): ")
        except:
            print("Data invalida!")
            continue
        dado = [titulo, dd.formatarData(agenda)]
        dd.adicionar(compromissos,dado)
    elif(acao==2):
        try:
            id = int(input("Informe a chave para exclusão: "))
        except:
            print("chave invalida!")
            continue
        dd.remover(compromissos,id)
    elif(acao==3):
        dd.listar(compromissos)
    elif(acao==4):
        try:
            id = int(input("Informe a chave: "))
        except:
            print("chave invalida!")
            continue
        print(dd.pesquisar(compromissos,id))
    elif(acao==5):
        dd.listarFuturo(compromissos)
    else:
        continue