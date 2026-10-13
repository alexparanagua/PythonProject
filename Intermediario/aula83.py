from datetime import datetime as dd

hoje = dd.now()
natal = dd(2026,2,25,0)
#calcular o delta
espera = natal-hoje
print(type(espera))
print(repr(espera))
print(espera)

print(f"Faltam {espera.days} dias para o natal! ")

