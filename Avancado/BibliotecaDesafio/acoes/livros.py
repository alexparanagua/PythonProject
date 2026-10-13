from BibliotecaDesafio.classes.Livro import Livro
import json
from os import path as path

def add():
    print("** Incluir novo livro:")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    if len(listaLivro)>0:
        livroidmax = max(listaLivro, key=lambda x: x.id)
        id = livroidmax.id +1
    else:
        id =1
    listaLivro.append(Livro(id,titulo,autor,ano))
    print(f'Livro {titulo}({id}) incluido com sucesso!')

def rem():
    id = int(input("ID para remoção: "))
    livro = next(filter(lambda x : x.id==id,listaLivro),None)
    listaLivro.remove(livro)
    print(f'Livro {livro.titulo}({livro.id}) removido com sucesso!')

def list():
    if len(listaLivro)==0:
        print("Sem registros!")
    else :
        print("** Listar todos os livros:")
        for livro in listaLivro:
            print(livro)

def listId():
    id = int(input("ID para pesquisar: "))
    if len(listaLivro)==0:
        print("Sem registros!")
    else :
        print(f"** Listar livro {id}:")
        livro = next(filter(lambda x : x.id==id,listaLivro),None)
        print(livro)

def listId(id):
    if len(listaLivro)==0:
        return None
    else :
        livro = next(filter(lambda x : x.id==int(id),listaLivro),None)
        return livro

def validar_livro(idlivro):
    livro = listId(idlivro)
    if livro!=None:
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
    caminho_arquivo = path.join(pasta, "livros.txt")
    return caminho_arquivo

def gravarArquivo():
    with open(oarquivo(),'w',encoding='utf-8') as arquivo:
        json.dump([livro.__dict__ for livro in listaLivro],arquivo,ensure_ascii=False, indent=4)
    print("Gravado com sucesos em arquivo")

def lerArquivo():
    with open(oarquivo(),'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return [Livro.from_dict(dado) for dado in dados]

try:
    listaLivro = lerArquivo()
except FileNotFoundError:
    listaLivro=[]