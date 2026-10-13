#sem separar responsabilidade, separando com livros e emprestimos
class LivroComEmprestino:
    def __init__(self, id, titulo, autor, ano, dataemp, usuarioemp):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__dataemp= dataemp
        self.__usuarioemp = usuarioemp
    def __str__(self):
        def emprestimo():
            if self.__dataemp != None:
                return f'\n*{self.emprestimo}'
            else:
                return ''
        return f'ID: {self.__id} | Título: {self.__titulo} | Autor: {self.__autor} | Ano: {self.__ano} {emprestimo()}'
    @property
    def id(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def ano(self):
        return self.__ano

    @property
    def emprestimo(self):
        return f'Emprestado em {self.__dataemp} para {self.__usuarioemp}'
    @emprestimo.setter
    def emprestimo(self,data,usuario):
        self.__dataemp=data
        self.__usuarioemp=usuario
