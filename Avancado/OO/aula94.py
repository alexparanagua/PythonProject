class Automovel:
    contador = 0
    precisao = 0.95
    def __init__(self,placa, velocidade_max):
        self.__id = Automovel.contador+1
        self.__placa = placa
        self.__velocidade_max = int(velocidade_max) * Automovel.precisao
        self.__velocidade_atual = 0
        Automovel.contador = self.__id


    def __str__(self):
        return f"{self.__id} - {self.__velocidade_atual} km/h"

    def get_placa(self):
        return self.__placa

    def get_velocidade_max(self):
        return self.__velocidade_max

    def set_velocidade_max(self, nova):
        self.__velocidade_max = nova
        print(f"A nova velocidade maxima é {nova} Km/h! ")

    def dirigir(self,velocidade):
        print(f"Estou dirigindo({self.__placa}) a {self.__velocidade_max} km/h")

    def acelerar(self):
        maxima = int(self.__velocidade_max)
        nova = self.__velocidade_atual+10
        self.__velocidade_atual = nova if nova < maxima else maxima

    def frear(self):
        nova = self.__velocidade_atual -10
        self.__velocidade_atual = nova if nova >=0 else 0

meuCarro = Automovel('XYZ-1234','180')
outroCarro = Automovel('ABC-3333','230')

print(meuCarro.get_placa())
print(meuCarro.get_velocidade_max())
print(outroCarro.get_placa())
print(outroCarro.get_velocidade_max())

meuCarro.dirigir(100)
print(meuCarro)
outroCarro.dirigir(120)
print(outroCarro)

