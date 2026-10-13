from random import randint as rr

def palavra_aleatoria():
    with open("palavras.txt", "rt") as f :
        banco = f.readlines()
    return banco[rr(0, len(banco))].strip()

palco = ['','O','O-', 'O-|','O-|-', 'O-|-<']

class Forca:
    def __init__(self,palavra):
        self.__palavra=palavra
        self.letra_certas = []
        self.letra_erradas = []
        self.acertou = False
    def advinhar(self,letra):
        self.acertou = False
        for p in self.__palavra:
            if p == letra:
                self.acertou=True
        if self.acertou:
            self.letra_certas.append(letra)
        else:
            if letra not in self.letra_erradas:
                self.letra_erradas.append(letra)
    def forca_acabou(self):
        print("Tentativas esgotadas!")
    def get_acertou(self):
        return self.acertou
    def forca_venceu(self):
        print("Voce acertou a palavra! Parabens!!")
    def palavra_escondida(self):
        return self.__palavra
    def mostra_status_jogo(self):
        escondida = ""
        for i in self.__palavra:
            #print("se", i)
            achou =False
            for l in self.letra_certas:
                #print("essa",l)
                if i==l:
                    achou= True
            escondida += f' {i} ' if achou else " _ "
        print(escondida)