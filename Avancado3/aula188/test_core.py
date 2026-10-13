from core import media, situacao, validar_aluno


def test_media():
    assert media([10, 0]) == 5.0
    assert media([]) == 0.0


def test_situacao():
    assert situacao(7.0) == "Aprovado"
    assert situacao(6.9) == "Recuperação"
    assert situacao(4.9) == "Reprovado"


def test_validar_aluno():
    ok, _ = validar_aluno({"nome": "Ana", "notas": [8, 9]})
    assert ok is True
    ok, _ = validar_aluno({"nome": "", "notas": [8]})
    assert ok is False
    ok, _ = validar_aluno({"nome": "Ana", "notas": [12]})
    assert ok is False


if __name__ == "__main__":
    test_media()
    test_situacao()
    test_validar_aluno()
    print("OK — testes do core passaram!")