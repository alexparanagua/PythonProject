import util
from Forca.util import palco


def main():
    jogo = util.Forca(util.palavra_aleatoria())
    tentativas = len(util.palco)-2
    tentativa =0
    while True:
        if int(tentativa) > 0:
            print(f"Palavras ja digitadas = {jogo.letra_erradas}")
        print(f'Tentativa {tentativa} / {tentativas} >> {util.palco[tentativa]}')
        letra = input("Digite a letra:")
        jogo.advinhar(letra)
        jogo.mostra_status_jogo()
        if not jogo.get_acertou():
            tentativa+=1
        if(tentativa==tentativas+1):
            print(palco[tentativa])
            jogo.forca_acabou()
            break
        if(set(jogo.letra_certas).issuperset(set(jogo.palavra_escondida()))):
            jogo.forca_venceu()
            break
        continue
main()