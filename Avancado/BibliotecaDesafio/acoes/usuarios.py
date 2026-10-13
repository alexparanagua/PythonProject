from BibliotecaDesafio.classes.Usuario import Usuario
import json
from os import path as path

def add():
    print("** Incluir novo usuario:")
    nome = input("Nome: ")
    tel = input("Telefone: ")
    if len(listaUsuario)>0:
        usuarioidmax = max(listaUsuario, key=lambda x: x.id)
        id = usuarioidmax.id +1
    else:
        id =1
    listaUsuario.append(Usuario(id,nome,tel))
    print(f'Usuario {nome}({id}) incluido com sucesso!')

def rem():
    id = int(input("ID para remoção: "))
    usuario = next(filter(lambda x : x.id==id,listaUsuario),None)
    listaUsuario.remove(usuario)
    print(f'Usuario {usuario.nome}({usuario.id}) removido com sucesso!')

def list():
    if len(listaUsuario)==0:
        print("Sem registros!")
    else :
        print("** Listar todos os Usuarios:")
        for usuario in listaUsuario:
            print(usuario)

def listId():
    id = int(input("ID para pesquisar: "))
    if len(listaUsuario)==0:
        print("Sem registros!")
    else :
        print(f"** Listar Usuario {id}:")
        usuario = next(filter(lambda x : x.id==id,listaUsuario),None)
        print(usuario)

def listId(id):
    if len(listaUsuario)==0:
        return None
    else :
        usuario = next(filter(lambda x : x.id==int(id),listaUsuario),None)
        return usuario

def validar_usuario(idusuario):
    usuario = listId(idusuario)
    if usuario:
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
    caminho_arquivo = path.join(pasta, "usuarios.txt")
    return caminho_arquivo

def gravarArquivo():
    with open(oarquivo(),'w',encoding='utf-8') as arquivo:
        json.dump([Usuario.__dict__ for Usuario in listaUsuario],arquivo,ensure_ascii=False, indent=4)
    print("Gravado com sucesos em arquivo")

def lerArquivo():
    with open(oarquivo(),'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return [Usuario.from_dict(dado) for dado in dados]

try:
    listaUsuario = lerArquivo()
except FileNotFoundError:
    listaUsuario = []