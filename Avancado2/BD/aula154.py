import sqlite3
con = sqlite3.connect('empresa.db')
cur = con.cursor()

exp_sql = """
   SELECT matricula, nome FROM funcionarios
   WHERE sexo = "M"
"""
cur.execute(exp_sql)
#Recupera os registros e guarda em uma variável
dados = cur.fetchall()
for linha in dados:
    print(f'Matrícula: {linha[0]:5d} - Nome: {linha[1]:10s}')

con.close()