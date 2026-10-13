class Usuario:
    def __init__(self, id, nome, tel):
        self.__id = id
        self.__nome = nome
        self.__tel = tel
    def __str__(self):
        return f'ID: {self.__id} | Nome: {self.__nome} | Telefone: {self.__tel}'
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def tel(self):
        return self.__tel

    # Método para transformar o objeto em dicionário (JSON)
    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "tel": self.tel}

    # Método estático para recriar o objeto a partir de um dicionário
    @staticmethod
    def from_dict(dados):
        return Usuario(dados.get("_Usuario__id"), dados.get("_Usuario__nome"),
                     dados.get("_Usuario__tel"))
