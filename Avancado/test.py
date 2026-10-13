import BibliotecaDesafio.classes.Livro as ll
livro = ll.Livro(1,'a','x',2000)
lista = []
lista.append(livro)

livro = next(filter(lambda x : x.id==1,lista),None)
print(livro)
