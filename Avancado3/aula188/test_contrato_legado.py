from legado import relatorio


def test_contrato_basico():
    texto = relatorio()
    assert "RELATÓRIO DA TURMA" in texto
    assert "Alunos: 4" in texto
    assert "Média geral:" in texto
    assert "Ana" in texto and "Diego" in texto
    assert "Aprovado" in texto and "Reprovado" in texto


if __name__ == "__main__":
    test_contrato_basico()
    print("OK — contrato mínimo preservado!")