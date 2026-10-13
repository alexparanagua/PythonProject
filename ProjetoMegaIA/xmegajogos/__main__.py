from coletor import coletar_todos_concursos
from config import ARQUIVO_CONCURSOS, QUANTIDADE_JOGOS
from gerador import formatar_jogo, gerar_jogos


def main() -> None:
    print("Coletando concursos da Mega-Sena...")
    concursos = coletar_todos_concursos()
    print("%s concursos em %s" % (len(concursos), ARQUIVO_CONCURSOS))

    print("Gerando %s jogo(s)..." % QUANTIDADE_JOGOS)
    jogos = gerar_jogos(concursos, QUANTIDADE_JOGOS)
    for indice, jogo in enumerate(jogos, start=1):
        print("Jogo %s: %s" % (indice, formatar_jogo(jogo)))


if __name__ == "__main__":
    main()
