from core import media, situacao


def relatorio():
    alunos = [
        {"nome": "Ana", "notas": [8.0, 7.5, 9.0]},
        {"nome": "Bruno", "notas": [5.0, 6.0, 5.5]},
        {"nome": "Carla", "notas": [3.0, 4.0, 2.5]},
        {"nome": "Diego", "notas": [9.5, 9.0, 10.0]},
    ]

    linhas = []
    linhas.append("RELATÓRIO DA TURMA")
    linhas.append("-" * 40)
    linhas.append(f"Alunos: {len(alunos)}")

    medias = [media(a.get("notas", [])) for a in alunos]
    media_geral = (sum(medias) / len(medias)) if medias else 0.0
    linhas.append(f"Média geral: {round(media_geral, 2)}")
    linhas.append("")
    linhas.append("Por aluno:")

    for a in alunos:
        nome = a.get("nome", "SemNome")
        m = media(a.get("notas", []))
        linhas.append(f"- {nome}: {round(m, 2)} ({situacao(m)})")

    linhas.append("-" * 40)
    return "\n".join(linhas)


if __name__ == "__main__":
    print(relatorio())