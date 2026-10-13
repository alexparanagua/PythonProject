from __future__ import annotations

import time
from typing import Any

import requests

from xlotofaciljogos.config import (
    ARQUIVO_CONCURSOS,
    INTERVALO_REQUISICAO,
    TENTATIVAS_HTTP,
    URL_CONCURSO,
    URL_ULTIMO_CONCURSO,
)

CABECALHOS = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
}


def _get_json(url: str) -> dict[str, Any]:
    ultimo_erro: Exception | None = None
    for tentativa in range(1, TENTATIVAS_HTTP + 1):
        try:
            resposta = requests.get(url, headers=CABECALHOS, timeout=30)
            resposta.raise_for_status()
            dados = resposta.json()
            if not isinstance(dados, dict):
                raise ValueError("Resposta inesperada em %s" % url)
            return dados
        except (requests.RequestException, ValueError) as erro:
            ultimo_erro = erro
            time.sleep(min(2**tentativa, 8))
    raise RuntimeError("Falha ao consultar %s: %s" % (url, ultimo_erro)) from ultimo_erro


def _dezenas(dados: dict[str, Any]) -> list[int]:
    lista = dados.get("listaDezenas") or []
    dezenas = sorted(int(item) for item in lista)
    if len(dezenas) != 15:
        raise ValueError("Concurso sem 15 dezenas: %s" % dados.get("numero"))
    return dezenas


def _numero_anterior(dados: dict[str, Any]) -> int | None:
    valor = dados.get("numeroConcursoAnterior")
    if valor in (None, "", 0, "0"):
        return None
    numero = int(valor)
    return numero if numero > 0 else None


def carregar_concursos_salvos() -> dict[int, list[int]]:
    concursos: dict[int, list[int]] = {}
    if not ARQUIVO_CONCURSOS.exists():
        return concursos
    for linha in ARQUIVO_CONCURSOS.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        numero_txt, dezenas_txt = linha.split(None, 1)
        dezenas = [int(item) for item in dezenas_txt.split(",")]
        concursos[int(numero_txt)] = dezenas
    return concursos


def gravar_concursos(concursos: dict[int, list[int]]) -> None:
    linhas = [
        "%s %s" % (numero, ",".join("%02d" % dezena for dezena in concursos[numero]))
        for numero in sorted(concursos)
    ]
    ARQUIVO_CONCURSOS.write_text(
        "\n".join(linhas) + ("\n" if linhas else ""),
        encoding="utf-8",
    )


def _registrar(concursos: dict[int, list[int]], dados: dict[str, Any]) -> int:
    numero = int(dados["numero"])
    if numero in concursos:
        print("Concurso %s ja existe no arquivo. Pulando." % numero)
        return numero
    concursos[numero] = _dezenas(dados)
    gravar_concursos(concursos)
    print("Concurso %s salvo. Total: %s" % (numero, len(concursos)))
    return numero


def coletar_todos_concursos() -> dict[int, list[int]]:
    concursos = carregar_concursos_salvos()
    ultimo_salvo = max(concursos) if concursos else 0
    print(
        "Ultimo concurso no arquivo: %s (%s registro(s))"
        % (ultimo_salvo or "nenhum", len(concursos))
    )

    ultimo = _get_json(URL_ULTIMO_CONCURSO)
    numero_oficial = int(ultimo["numero"])
    print("Ultimo concurso na API da Caixa: %s" % numero_oficial)

    if numero_oficial <= ultimo_salvo and set(range(1, numero_oficial + 1)) <= set(concursos):
        print("Nenhum concurso novo para baixar.")
        return concursos

    _registrar(concursos, ultimo)

    proximo = _numero_anterior(ultimo)
    while proximo is not None:
        if proximo in concursos:
            print("Parando a coleta: concurso %s ja estava salvo." % proximo)
            break
        dados = _get_json(URL_CONCURSO.format(numero=proximo))
        _registrar(concursos, dados)
        proximo = _numero_anterior(dados)
        time.sleep(INTERVALO_REQUISICAO)

    faltantes = [n for n in range(1, numero_oficial + 1) if n not in concursos]
    for numero in reversed(faltantes):
        dados = _get_json(URL_CONCURSO.format(numero=numero))
        _registrar(concursos, dados)
        time.sleep(INTERVALO_REQUISICAO)

    return concursos
