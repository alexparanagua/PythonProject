import json
from BibliotecaDesafio.classes.Livro import Livro

def gravarArquivoLivro(lista):
    lista_json = [Livro.to_dict() for Livro in lista]
    with open('Livros.txt','w',encoding='utf-8') as arquivo:
        json.dump(lista,arquivo,ensure_ascii=False, indent=4)
    print("Gravado com sucesos em arquivo")

def lerArquivoLivro(lista):
    with open('Livros.txt','r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return [Livro.from_dict(dado) for dado in dados]
