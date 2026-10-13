import datetime

from BibliotecaDesafio.classes.Emprestimo import Emprestimo
import BibliotecaDesafio.acoes.livros as livros
import BibliotecaDesafio.acoes.usuarios as usuarios
import json
from os import path as path

def add():
    while True :
        print("** Incluir novo emprestimo:")
        idlivro = input("Id Livro: ")
        if not livros.validar_livro(idlivro):
            print(" ** Livro nao encontrado! **")
            continue
        if validar_emprestimo_livro(idlivro):
            print("** Livro já emprestado **")
            continue
        idusuario = input("Id Usuario: ")
        if not usuarios.validar_usuario(idusuario):
            print(" ** Usuario nao encontrado! **")
            continue
        if len(listaEmprestimo)>0:
            empidmax = max(listaEmprestimo, key=lambda x: x.id)
            id = empidmax.id +1
        else:
            id =1
        listaEmprestimo.append(Emprestimo(id,idlivro,idusuario,datetime.datetime.now(),None,'E'))
        print(f'Emprestimo ({id}) incluido com sucesso!')
        break

def rem():
    id = int(input("ID para devolução: "))
    emp = next(filter(lambda x : x.id==id,listaEmprestimo),None)
    emp.datadev = datetime.datetime.now()
    print(f'Emprestimo {emp.id} devolvido!')

def list():
    if len(listaEmprestimo)==0:
        print("Sem registros!")
    else :
        print("** Listar todos os Emprestimos:")
        for emp in listaEmprestimo:
            print(emp)

def listId():
    id = int(input("ID para pesquisar: "))
    if len(listaEmprestimo)==0:
        print("Sem registros!")
    else :
        print(f"** Listar Emprestimo {id}:")
        emp = next(filter(lambda x : x.id==id,listaEmprestimo),None)
        print(emp)

def listIdEmp(idlivro):
    if len(listaEmprestimo)==0:
        return None
    else :
        emp = next(filter(lambda x : int(x.idlivro)==int(idlivro) and str(x.status)=='E' ,listaEmprestimo),None)
        return emp

def validar_emprestimo_livro(idlivro):
    livro = listIdEmp(idlivro)
    if livro:
        return True
    return False

def acoes(acao):
    if acao==1:
        add()
        gravarArquivo()
    elif acao==2:
        rem()
        gravarArquivo()
    elif acao==3:
        list()
    elif acao==4:
        listId()
    else:
        pass

def oarquivo():
    pasta = "dados"
    caminho_arquivo = path.join(pasta, "emps.txt")
    return caminho_arquivo

def gravarArquivo():
    with open(oarquivo(),'w',encoding='utf-8') as arquivo:
        json.dump([emp.to_dict() for emp in listaEmprestimo],arquivo,ensure_ascii=False, indent=4)
    print("Gravado com sucesos em arquivo")

def lerArquivo():
    with open(oarquivo(),'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return [Emprestimo.from_dict(dado) for dado in dados]

try:
    listaEmprestimo = lerArquivo()
except FileNotFoundError:
    listaEmprestimo = []