from datetime import datetime as data

def adicionar(compromissos,registro):
    if compromissos:
        chaves = []
        for comp in compromissos:
            chaves.extend(comp.keys())
        idmax =max(chaves)
    else :
        idmax=0
    novo_id=idmax+1
    compromisso = {int(novo_id): registro}
    compromissos.append(compromisso)

def remover(compromissos,chave):
    reg =pesquisar(compromissos,chave)
    if reg:
        compromissos[:] = [comp for comp in compromissos if int(chave) not in comp]
        print(f"Registro {chave} removido!")
    else:
        pass

def pesquisar(compromissos,chave):
    try:
        reg_p = next((comp for comp in compromissos if int(chave) in comp))
        return reg_p
    except:
        print(f"Registro {chave} não encontrado!")

def listar(compromissos):
    print("\n==== LISTA DE COMPROMISSOS ===")
    if not compromissos:
        print("Sem registros!")
        return
    comp_ordenados = sorted(compromissos, key=lambda comp: list(comp.values())[0][1])
    for comp in comp_ordenados:
        for id_comp, dados in comp.items():
            #print(f"ID: {id_comp} | Tipo do dado: {type(dados)} | Conteúdo: {dados}")
            print(f"ID: {id_comp} | Título: {dados[0]} | Agenda: {dados[1].strftime('%d/%m/%Y %H:%M:%S')}")
    print("=== === === === === === === ===\n")

def formatarData(value):
    return data.strptime(value, "%d/%m/%Y %H:%M:%S")

def listarFuturo(compromissos):
    print("\n==== LISTA DE COMPROMISSOS ===")
    if not compromissos:
        print("Sem registros!")
        return
    comp_ordenados = sorted(compromissos, key=lambda comp: list(comp.values())[0][1])
    for comp in comp_ordenados:
        for id_comp, dados in comp.items():
            if dados[1]>data.now():
                print(f"ID: {id_comp} | Título: {dados[0]} | Agenda: {dados[1].strftime('%d/%m/%Y %H:%M:%S')}")
    print("=== === === === === === === ===\n")