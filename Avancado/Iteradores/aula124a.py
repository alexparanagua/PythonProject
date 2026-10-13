def notas_musicais():
    yield 'Dó'
    yield 'Ré'
    yield 'Mi'
    yield 'Fá'
    yield 'Sol'
    yield 'Lá'
    yield 'Si'

gen = notas_musicais()

for n in gen:
    print(n)