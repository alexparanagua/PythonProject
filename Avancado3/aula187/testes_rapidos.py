from relatorio_turma import media, situacao, avaliar_alunos, media_turma, top_n

# 1) média
assert media([10, 0]) == 5.0
assert media([]) == 0.0

# 2) situação
assert situacao(7.0) == "Aprovado"
assert situacao(6.9) == "Recuperação"
assert situacao(4.9) == "Reprovado"

# 3) avaliar alunos
alunos = [{"nome": "X", "notas": [10, 10, 10]}]
avaliados = avaliar_alunos(alunos)
assert avaliados[0]["media"] == 10.0
assert avaliados[0]["situacao"] == "Aprovado"

# 4) média turma e top_n
alunos2 = [
    {"nome": "A", "notas": [10]},
    {"nome": "B", "notas": [5]},
    {"nome": "C", "notas": [7]},
]
avaliados2 = avaliar_alunos(alunos2)
assert media_turma(avaliados2) == round((10 + 5 + 7) / 3, 2)
assert top_n(avaliados2, 1)[0]["nome"] == "A"

print("OK — testes rápidos passaram!")