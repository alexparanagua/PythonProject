# Livros, Usuários, Empréstimos, Relatórios, Sair
def menu_acao(obj):
    print("SISTEMA DE BIBLIOTECA DIGITAL")
    if obj ==3:
        print("1- Emprestar")
        print("2- Devolver")
    else:
        print("1- Incluir")
        print("2- Remover")
    print("3- Listar todos")
    print("4- Listar por ID")
    print("0 - Sair")
    x = int(input("Digite a acao: "))
    return x

def menu_objeto():
    print("SISTEMA DE BIBLIOTECA DIGITAL")
    print("1- Livro")
    print("2- Usuario")
    print("3- Emprestimo")
    print("0 - Sair")
    x = int(input("Digite a acao: "))
    return x

