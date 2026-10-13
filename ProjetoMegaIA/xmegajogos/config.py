from pathlib import Path

# Quantidade de jogos (volantes) a gerar apos carregar os concursos.
QUANTIDADE_JOGOS = 5

DEZENAS_POR_JOGO = 6
DEZENA_MINIMA = 1
DEZENA_MAXIMA = 60

URL_ULTIMO_CONCURSO = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"
URL_CONCURSO = "https://api.guidi.dev.br/loteria/megasena/{numero}"

PASTA_PROJETO = Path(__file__).resolve().parent
ARQUIVO_CONCURSOS = PASTA_PROJETO / "concursos.txt"

INTERVALO_REQUISICAO = 0.15
TENTATIVAS_HTTP = 4
