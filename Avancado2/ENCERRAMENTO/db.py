import sqlite3
import os

NOME_BANCO = 'todo.db'
NOME_TABELA = 'TAREFA'
con = sqlite3.connect(NOME_BANCO, check_same_thread=False)

def reconnectdb(cc):
    cc = sqlite3.connect(NOME_BANCO, check_same_thread=False)
    return cc

def closedb():
    con.close()

def criarTabelas():
    reconnectdb(con)
    cur = con.cursor()
    exp_sql = """
        create table TAREFA(
        id INTEGER not null primary key,
        titulo varchar(20) not null,
        descricao varchar(20) ,
        concluida char(1) ,
        criada varchar(20)
        )
        """
    cur.execute(exp_sql)
    closedb()

def tabelaExiste():
    reconnectdb(con)
    cur = con.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (NOME_TABELA,)
    )
    tabela_existe = cur.fetchone()
    closedb()
    return tabela_existe!=None

if tabelaExiste():
    print(f"tabela '{NOME_TABELA}' já existe.")
else:
    criarTabelas()

con.close()