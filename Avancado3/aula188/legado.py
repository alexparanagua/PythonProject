# legado.py (exemplo didático)
# Problemas: tudo junto, validação fraca, duplicação, difícil de testar.

def relatorio():
    alunos = [
        {"nome": "Ana", "notas": [8.0, 7.5, 9.0]},
        {"nome": "Bruno", "notas": [5.0, 6.0, 5.5]},
        {"nome": "Carla", "notas": [3.0, 4.0, 2.5]},
        {"nome": "Diego", "notas": [9.5, 9.0, 10.0]},
    ]

    texto = "RELATÓRIO DA TURMA\n"
    texto += "-" * 40 + "\n"
    texto += "Alunos: " + str(len(alunos)) + "\n"

    soma_medias = 0
    for a in alunos:
        notas = a.get("notas", [])
        if len(notas) == 0:
            m = 0
        else:
            m = sum(notas) / len(notas)
        soma_medias += m

    if len(alunos) == 0:
        media_geral = 0
    else:
        media_geral = soma_medias / len(alunos)

    texto += "Média geral: " + str(round(media_geral, 2)) + "\n\n"
    texto += "Por aluno:\n"

    for a in alunos:
        notas = a.get("notas", [])
        if len(notas) == 0:
            m = 0
        else:
            m = sum(notas) / len(notas)
        if m >= 7:
            sit = "Aprovado"
        elif m >= 5:
            sit = "Recuperação"
        else:
            sit = "Reprovado"
        texto += "- " + a.get("nome", "SemNome") + ": " + str(round(m, 2)) + " (" + sit + ")\n"

    texto += "-" * 40 + "\n"
    return texto


if __name__ == "__main__":
    print(relatorio())