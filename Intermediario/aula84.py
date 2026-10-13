
from datetime import datetime as dt
from datetime import timedelta as dl
from datetime import time as tt

dia_semana =["Segunda","Terça","Quarta","Quinta","Sexta","Sabado","Domingo"]

hoje = dt.now()
amanha = hoje + dl(days=1)

meianoite= tt()
tarefa = dt.combine(amanha, meianoite)

print(tarefa)
print(type(tarefa))
print(repr(tarefa))
print(tarefa.weekday())
print(dia_semana[tarefa.weekday()])

print("-----------")
print(hoje)
print(hoje.strftime('%d/%m/%Y %I:%M:%S %p - %B/%y'))

def retorna_dataf(hoje):
    meses = ['','Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Outubro','Novembro', 'Dezembro']
    return meses[hoje.month]

print(retorna_dataf(hoje))