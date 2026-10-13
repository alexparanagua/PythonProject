import os
os.remove('empresa.db') if os.path.exists('empresa.db') else None

import sqlite3

con = sqlite3.connect('empresa.db')

cur = con.cursor()

exp_sql = """
   CREATE TABLE departamentos(
     id    integer     NOT NULL PRIMARY KEY,
     nome  varchar(20) NOT NULL
   )
"""
cur.execute(exp_sql)

exp_sql = """
   CREATE TABLE funcionarios( 
     matricula decimal(5) NOT NULL PRIMARY KEY,
     nome      varchar(30) NOT NULL,
     rg        decimal(9) NOT NULL UNIQUE,
     sexo      char(1) CHECK(sexo in ("M", "F")),
     depto     integer,
     endereco  varchar(50),
     cidade    varchar(20) DEFAULT "São Paulo",
     salario   decimal(10, 2),
     FOREIGN KEY (depto) REFERENCES departamentos(id)
   );
"""
cur.execute(exp_sql)

exp_sql = """
   CREATE TABLE IF NOT EXISTS competencias(
     id       integer      NOT NULL,
     nome     varchar(30)  NOT NULL,
     area     varchar(20) CHECK (area in 
         ("ENGENHARIA", "PRODUÇÃO", "MARKETING", "VENDAS", "OUTRA")
     ),
     PRIMARY KEY (id AUTOINCREMENT)
   );
"""
cur.execute(exp_sql)

exp_sql = """
   CREATE TABLE funcionarios_competencias(
     matricula     decimal(5)  REFERENCES funcionarios(matricula),
     id            integer     REFERENCES competencias(id),
     data          DATE        NO NULL
   )
"""
cur.execute(exp_sql)

