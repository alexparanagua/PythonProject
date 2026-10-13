def main():
    alunos = [
        {"nome": "Ana", "notas": [8.0, 7.5, 9.0]},
        {"nome": "Bruno", "notas": [5.0, 6.0, 5.5]},
        {"nome": "Carla", "notas": [3.0, 4.0, 2.5]},
        {"nome": "Diego", "notas": [9.5, 9.0, 10.0]},
    ]
    print("MVP Relatório de Turma — OK (esqueleto)")
def media(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)
def situacao(media_aluno):
    if media_aluno >= 7.0:
        return "Aprovado"
    if media_aluno >= 5.0:
        return "Recuperação"
    return "Reprovado"
def avaliar_alunos(alunos):
    avaliados = []
    for a in alunos:
        m = media(a["notas"])
        avaliados.append({
            "nome": a["nome"],
            "notas": a["notas"],
            "media": round(m, 2),
            "situacao": situacao(m),
        })
    return avaliados


def media_turma(avaliados):
    if not avaliados:
        return 0.0
    return round(sum(a["media"] for a in avaliados) / len(avaliados), 2)


def top_n(avaliados, n=3):
    ordenados = sorted(avaliados, key=lambda x: x["media"], reverse=True)
    return ordenados[:n]


def gerar_relatorio(avaliados):
    linhas = []
    linhas.append("RELATÓRIO DA TURMA")
    linhas.append("-" * 40)

    linhas.append(f"Quantidade de alunos: {len(avaliados)}")
    linhas.append(f"Média geral da turma: {media_turma(avaliados)}")
    linhas.append("")

    linhas.append("Desempenho por aluno:")
    for a in avaliados:
        linhas.append(f"- {a['nome']}: média {a['media']} ({a['situacao']})")

    linhas.append("")
    linhas.append("Top 3 médias:")
    for i, a in enumerate(top_n(avaliados, 3), start=1):
        linhas.append(f"{i}) {a['nome']} — {a['media']}")

    linhas.append("-" * 40)
    return "\n".join(linhas)

def salvar_relatorio(texto, caminho="relatorio.txt"):
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)


def main():
    alunos = [
        {"nome": "Ana", "notas": [8.0, 7.5, 9.0]},
        {"nome": "Bruno", "notas": [5.0, 6.0, 5.5]},
        {"nome": "Carla", "notas": [3.0, 4.0, 2.5]},
        {"nome": "Diego", "notas": [9.5, 9.0, 10.0]},
    ]

    avaliados = avaliar_alunos(alunos)
    relatorio = gerar_relatorio(avaliados)

    print(relatorio)
    salvar_relatorio(relatorio)
    
if __name__ == "__main__":
    main()