import sqlite3
con = sqlite3.connect('empresa.db')
cur = con.cursor()

exp_sql = 'INSERT INTO competencias (nome, area) values (?, ?)'

registros = [
    ('Configurar linha de Produção', 'PRODUÇÃO'),
    ('Elaborar Plano de Marketing', 'MARKETING'),
    ('Vender para Mercosul', 'VENDAS'),
    ('Realizar a manutenção da LP', 'PRODUÇÃO'),
    ('Operar CAD e CAM', 'ENGENHARIA')
]

for registro in registros:
    cur.execute(exp_sql, registro)

con.commit()

con.close()