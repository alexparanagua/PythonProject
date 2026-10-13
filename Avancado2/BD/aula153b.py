import sqlite3
con = sqlite3.connect('empresa.db')
cur = con.cursor()

exp_sql = 'INSERT INTO funcionarios values (?, ?, ?, ?, ?, ?, ?, ?)'

registros = [
    (1001, 'José da Silva', 20345231, 'M', 1, 'Rua Campos Filho, 234', 'Itu', 2895.12),
    (1002, 'Adriana Barros', 23123001, 'F', 2, 'Av. Sampaio Correia, 1234', 'Sorocaba', 15345.01),
    (1003, 'Ronny Sampaio', 11345123, 'M', 1, 'Alameda Itororó, 123', 'São Paulo', 4234.12),
    (2001, 'Marcelo Mapiado',25234678, 'M', 4, 'Rua Parco Vilela, 123', 'Salto', 23567.00),
    (2002, 'Luciana Leal', 30234567, 'F', 3, 'Av. Santo Antonio, 12', 'Campinas', 11678.90)
]

for registro in registros:
    cur.execute(exp_sql, registro)

con.commit()

con.close()