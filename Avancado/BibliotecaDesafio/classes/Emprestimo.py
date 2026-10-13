from datetime import datetime as dd
class Emprestimo:
    def __init__(self, id, idlivro, idusuario, dataemp, datadev, status):
        self.__id = id
        self.__idlivro = idlivro
        self.__idusuario = idusuario
        self.__dataemp = dataemp
        self.__datadev = datadev
        self.__status = status
    def __str__(self):
        return f'ID: {self.id} | ID Livro: {self.idlivro} | ID Usuario: {self.idusuario} | Data Emprestimo: {self.dataemp} | Data Devolucao: {self.datadev} | Status: {self.status}'
    @property
    def id(self):
        return self.__id
    @property
    def idlivro(self):
        return self.__idlivro
    @property
    def idusuario(self):
        return self.__idusuario
    @property
    def dataemp(self):
        if isinstance(self.__dataemp, dd):
            return self.__dataemp.strftime("%d/%m/%Y")
        return self.__dataemp
    @property
    def datadev(self):
        if isinstance(self.__datadev, dd):
            return self.__datadev.strftime("%d/%m/%Y")
        return self.__datadev
    @property
    def status(self):
        return self.__status

    @datadev.setter
    def datadev(self,datadev):
        self.__datadev = datadev
        self.__status = None

    # Método para transformar o objeto em dicionário (JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "idlivro": self.idlivro,
            "idusuario": self.idusuario,
            # Convertemos as datas para string aqui para o json.dump não quebrar
            "dataemp": self.__dataemp.strftime("%d/%m/%Y") if isinstance(self.__dataemp, dd) else self.__dataemp,
            "datadev": self.__datadev.strftime("%d/%m/%Y") if isinstance(self.__datadev, dd) else self.__datadev,
            "status": self.__status
        }

    # Método estático para recriar o objeto a partir de um dicionário
    @staticmethod
    def from_dict(dados):
        # Lê as chaves limpas ou as antigas com o prefixo privado se já existirem no arquivo
        dataemp_str = dados.get("dataemp")
        datadev_str = dados.get("datadev")

        # Converte as strings de volta para objetos datetime reais para o construtor
        dataemp_obj = dd.strptime(dataemp_str, "%d/%m/%Y") if dataemp_str else None
        datadev_obj = dd.strptime(datadev_str, "%d/%m/%Y") if datadev_str else None

        return Emprestimo(
            dados.get("id"),
            dados.get("idlivro"),
            dados.get("idusuario"),
            dataemp_obj,
            datadev_obj,
            dados.get("status")
        )