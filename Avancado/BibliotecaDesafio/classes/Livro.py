class Livro:
    def __init__(self, id, titulo, autor, ano):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
    def __str__(self):
        return f'ID: {self.__id} | Título: {self.__titulo} | Autor: {self.__autor} | Ano: {self.__ano}'
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

    # Método para transformar o objeto em dicionário (JSON)
    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "autor": self.autor, "ano" : self.ano}

    # Método estático para recriar o objeto a partir de um dicionário
    @staticmethod
    def from_dict(dados):
        return Livro(dados.get("_Livro__id"), dados.get("_Livro__titulo"),
                     dados.get("_Livro__autor"), dados.get("_Livro__ano"))
