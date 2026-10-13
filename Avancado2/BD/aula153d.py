import sqlite3
con = sqlite3.connect('empresa.db')
cur = con.cursor()

exp_sql = 'INSERT INTO funcionarios_competencias values (?, ?, ?)'

registros = [
    (1001, 1, "10/10/2022"),
    (1002, 3, "20/11/2021"),
    (1003, 1, "24/03/2021"),
    (2001, 2, "27/04/2022"),
    (2002, 3, "22/01/2021"),
    (1001, 4, "15/07/2022"),
    (1003, 4, "21/11/2022")
]

for registro in registros:
    cur.execute(exp_sql, registro)

con.commit()

con.close()