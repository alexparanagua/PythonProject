def media(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def situacao(m):
    if m >= 7.0:
        return "Aprovado"
    if m >= 5.0:
        return "Recuperação"
    return "Reprovado"

def validar_aluno(aluno):
    nome = aluno.get("nome")
    if not nome or not isinstance(nome, str):
        return False, "Aluno sem nome válido"
    notas = aluno.get("notas", [])
    if not isinstance(notas, list):
        return False, "Notas deve ser uma lista"
    for n in notas:
        if not isinstance(n, (int, float)):
            return False, "Nota deve ser numérica"
        if n < 0 or n > 10:
            return False, "Nota fora do intervalo 0..10"
    return True, ""