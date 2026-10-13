from datetime import datetime as dd
from datetime import timedelta as dd2

hoje = dd.now()
regra = dd2(days=3)

#calcular data do boleto
data_boleto= hoje+regra
print(hoje)
print(regra)
print(data_boleto)