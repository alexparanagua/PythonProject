from xlotofaciljogos.coletor import coletar_todos_concursos
from xlotofaciljogos.config import ARQUIVO_CONCURSOS, DEZENAS_POR_JOGO, NUMEROS_EXTRAS, QUANTIDADE_JOGOS
from xlotofaciljogos.gerador import formatar_jogo, gerar_jogos


def main() -> None:
    print("Coletando concursos da Lotofacil...")
    concursos = coletar_todos_concursos()
    print("%s concursos em %s" % (len(concursos), ARQUIVO_CONCURSOS))

    total_dezenas = DEZENAS_POR_JOGO + NUMEROS_EXTRAS
    print(
        "Gerando %s jogo(s) com %s dezena(s) (%s + %s extra(s))..."
        % (QUANTIDADE_JOGOS, total_dezenas, DEZENAS_POR_JOGO, NUMEROS_EXTRAS)
    )
    jogos = gerar_jogos(concursos, QUANTIDADE_JOGOS, NUMEROS_EXTRAS)
    for indice, jogo in enumerate(jogos, start=1):
        print("Jogo %s: %s" % (indice, formatar_jogo(jogo)))


if __name__ == "__main__":
    main()
