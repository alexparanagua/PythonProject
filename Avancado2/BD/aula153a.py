import sqlite3
con = sqlite3.connect('empresa.db')
cur = con.cursor()

exp_sql = 'INSERT INTO departamentos values (?, ?)'

registros = [ (1, 'PRODUÇÃO'),
              (2, 'VENDAS'),
              (3, 'COMPRAS'),
              (4, 'MARKETING'),
              (5, 'INFORMÁTICA')]

for registro in registros:
    cur.execute(exp_sql, registro)

con.commit()

con.close()