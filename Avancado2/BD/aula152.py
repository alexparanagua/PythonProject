#import os

#os.remove('empresa.db') if os.path.exists('empresa.db') else None

import sqlite3
con = sqlite3.connect('empresa.db')

cur = con.cursor()
exp_sql = """
    create table departamentos(
    id INTEGER not null primary key,
    nome varchar(20) not null
    )
    """

exp_sql = """
    create table funcionarios(
    id INTEGER not null primary key,
    nome varchar(20) not null
    )
    """
cur.execute(exp_sql)

