class Casa:
    def __init__(self,preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self,new):
        if new > 0 and isinstance(new,float):
            self.__preco=new
        else:
            print("valor invalido")

    @preco.deleter
    def preco(self):
        self.__preco =0

minha_casa = Casa(450000)

print("r= ",minha_casa.preco)

minha_casa.preco = (500000.0)

print("r= ",minha_casa.preco)

del minha_casa.preco

print("r= ",minha_casa.preco)
