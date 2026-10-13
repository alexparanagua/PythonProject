class Automovel:
    def __init__(self,placa, velocidade_max):
        self.placa = placa
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def __str__(self):
        return f"{self.velocidade_atual} km/h"

    def get_placa(self):
        return self.placa

    def dirigir(self,velocidade):
        print(f"Estou dirigindo({self.placa}) a {self.velocidade_max} km/h")

    def acelerar(self):
        maxima = int(self.velocidade_max)
        nova = self.velocidade_atual+10
        self.velocidade_atual = nova if nova < maxima else maxima

    def frear(self):
        nova = self.velocidade_atual -10
        self.velocidade_atual = nova if nova >=0 else 0

meuCarro = Automovel('XYZ-1234','180')
outroCarro = Automovel('ABC-3333','230')

print(meuCarro.get_placa())
print(outroCarro.get_placa())

meuCarro.dirigir(100)
print(meuCarro)
outroCarro.dirigir(120)
print(outroCarro)

print("----------------------------")
print(meuCarro.__str__())
print(meuCarro.__repr__())

print(f"----{meuCarro.get_placa()} - {meuCarro}")
for _ in range(20):
    meuCarro.acelerar()
    print("A ",meuCarro)

for _ in range(20):
    meuCarro.frear()
    print("F ",meuCarro)

print(f"----{outroCarro.get_placa()} - {outroCarro}")
for _ in range(20):
    outroCarro.acelerar()
    print("A ",outroCarro)

for _ in range(20):
    outroCarro.frear()
    print("F ",outroCarro)