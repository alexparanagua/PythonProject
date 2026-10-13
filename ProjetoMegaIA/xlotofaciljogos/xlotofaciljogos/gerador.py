from __future__ import annotations

import random

from xlotofaciljogos.config import (
    DEZENA_MAXIMA,
    DEZENA_MINIMA,
    DEZENAS_POR_JOGO,
    NUMEROS_EXTRAS,
    QUANTIDADE_JOGOS,
)


def _colunas(concursos: dict[int, list[int]]) -> list[list[int]]:
    colunas: list[list[int]] = [[] for _ in range(DEZENAS_POR_JOGO)]
    for numero in sorted(concursos):
        dezenas = concursos[numero]
        for indice, dezena in enumerate(dezenas):
            colunas[indice].append(dezena)
    return colunas


def _pool_historico(concursos: dict[int, list[int]]) -> list[int]:
    pool: set[int] = set()
    for dezenas in concursos.values():
        pool.update(dezenas)
    return sorted(pool)


def _completar_com_extras(jogo: list[int], pool: list[int], extras: int) -> list[int]:
    if extras <= 0:
        return jogo

    escolhidos = set(jogo)
    candidatos = [n for n in pool if n not in escolhidos]
    if len(candidatos) < extras:
        candidatos = [
            n for n in range(DEZENA_MINIMA, DEZENA_MAXIMA + 1) if n not in escolhidos
        ]
    if len(candidatos) < extras:
        raise ValueError(
            "Nao ha dezenas suficientes para adicionar %s numero(s) extra(s)." % extras
        )

    adicionais = random.sample(candidatos, extras)
    return sorted(jogo + adicionais)


def gerar_jogo(colunas: list[list[int]], pool: list[int], extras: int = NUMEROS_EXTRAS) -> list[int]:
    jogo: list[int] = []
    for coluna in colunas:
        candidatos = [n for n in coluna if n not in jogo]
        if not candidatos:
            candidatos = [
                n for n in range(DEZENA_MINIMA, DEZENA_MAXIMA + 1) if n not in jogo
            ]
        jogo.append(random.choice(candidatos))
    return _completar_com_extras(sorted(jogo), pool, extras)


def gerar_jogos(
    concursos: dict[int, list[int]],
    quantidade: int = QUANTIDADE_JOGOS,
    extras: int = NUMEROS_EXTRAS,
) -> list[list[int]]:
    if not concursos:
        raise ValueError("Nao ha concursos para gerar jogos.")
    if extras < 0:
        raise ValueError("NUMEROS_EXTRAS nao pode ser negativo.")
    colunas = _colunas(concursos)
    pool = _pool_historico(concursos)
    return [gerar_jogo(colunas, pool, extras) for _ in range(quantidade)]


def formatar_jogo(dezenas: list[int]) -> str:
    return ",".join("%02d" % dezena for dezena in dezenas)
