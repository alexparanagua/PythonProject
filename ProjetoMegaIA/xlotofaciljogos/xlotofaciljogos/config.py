from pathlib import Path

# Quantidade de jogos (volantes) a gerar apos carregar os concursos.
QUANTIDADE_JOGOS = 10

DEZENAS_POR_JOGO = 15
# Quantidade de dezenas extras alem das 15 (0 = padrao; ex.: 1 -> 16 numeros).
NUMEROS_EXTRAS = 1
DEZENA_MINIMA = 1
DEZENA_MAXIMA = 25

URL_ULTIMO_CONCURSO = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil"
URL_CONCURSO = "https://api.guidi.dev.br/loteria/lotofacil/{numero}"

PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_CONCURSOS = PASTA_PROJETO / "concursos.txt"

INTERVALO_REQUISICAO = 0.15
TENTATIVAS_HTTP = 4
