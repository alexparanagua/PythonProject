from __future__ import annotations

import random

from config import DEZENA_MAXIMA, DEZENA_MINIMA, DEZENAS_POR_JOGO, QUANTIDADE_JOGOS


def _colunas(concursos: dict[int, list[int]]) -> list[list[int]]:
    colunas: list[list[int]] = [[] for _ in range(DEZENAS_POR_JOGO)]
    for numero in sorted(concursos):
        dezenas = concursos[numero]
        for indice, dezena in enumerate(dezenas):
            colunas[indice].append(dezena)
    return colunas


def gerar_jogo(colunas: list[list[int]]) -> list[int]:
    jogo: list[int] = []
    for coluna in colunas:
        candidatos = [n for n in coluna if n not in jogo]
        if not candidatos:
            candidatos = [
                n for n in range(DEZENA_MINIMA, DEZENA_MAXIMA + 1) if n not in jogo
            ]
        jogo.append(random.choice(candidatos))
    return sorted(jogo)


def gerar_jogos(
    concursos: dict[int, list[int]],
    quantidade: int = QUANTIDADE_JOGOS,
) -> list[list[int]]:
    if not concursos:
        raise ValueError("Nao ha concursos para gerar jogos.")
    colunas = _colunas(concursos)
    return [gerar_jogo(colunas) for _ in range(quantidade)]


def formatar_jogo(dezenas: list[int]) -> str:
    return ",".join("%02d" % dezena for dezena in dezenas)
