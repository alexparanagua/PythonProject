from Tarefa import Tarefa
from typing import List, Optional
import db

def inserir(lista: List[Tarefa]):
    con = db.reconnectdb(db.con)
    cur = con.cursor()
    exp_sql = f'INSERT INTO {db.NOME_TABELA} values (?, ?, ?, ?, ?)'
    for obj in lista:
        cur.execute(exp_sql, (obj.id, obj.titulo, obj.descricao, obj.concluida, obj.criada))
    con.commit()
    con.close()


def excluir(lista: List[Tarefa]):
    con = db.reconnectdb(db.con)
    cur = con.cursor()
    # Expressão SQL baseada no ID do objeto
    exp_sql = f'DELETE FROM {db.NOME_TABELA} WHERE id = ?'
    for obj in lista:
        # Passamos apenas o obj.id para a query de exclusão
        cur.execute(exp_sql, (obj.id,))
    con.commit()
    con.close()

def excluir_por_ids(lista_ids: List[int]):
    con = db.reconnectdb(db.con)
    cur = con.cursor()
    # Expressão SQL utilizando o ID como filtro
    exp_sql = f'DELETE FROM {db.NOME_TABELA} WHERE id = ?'
    for tarefa_id in lista_ids:
        cur.execute(exp_sql, (tarefa_id,))
    con.commit()
    con.close()


def atualizar(lista: List[Tarefa]):
    con = db.reconnectdb(db.con)
    cur = con.cursor()
    # Monta a expressão SQL especificando quais colunas serão alteradas
    exp_sql = f'''
        UPDATE {db.NOME_TABELA} 
        SET titulo = ?, descricao = ?, concluida = ?, criada = ? 
        WHERE id = ?
    '''
    for obj in lista:
        # Passamos os novos valores dos atributos e, por último, o ID para o WHERE
        cur.execute(exp_sql, (
            obj.titulo,
            obj.descricao,
            obj.concluida,
            obj.criada,
            obj.id
        ))
    con.commit()
    con.close()


def buscar_todos(pagina: int = 1, tamanho_pagina: int = 10) -> List[Tarefa]:
    con = db.reconnectdb(db.con)
    cur = con.cursor()
    # Cálculo de quantos registros pular com base na página atual
    # Se pagina=1, offset=0. Se pagina=2, offset=10 (pula os primeiros 10)
    offset = (pagina - 1) * tamanho_pagina
    exp_sql = f'SELECT id, titulo, descricao, concluida, criada FROM {db.NOME_TABELA} LIMIT ? OFFSET ?'
    cur.execute(exp_sql, (tamanho_pagina, offset))
    linhas = cur.fetchall()
    con.close()

    lista_tarefas = []
    for linha in linhas:
        # Monta o objeto Tarefa com os dados vindos da tupla do banco
        tarefa = Tarefa(
            id=linha[0],
            titulo=linha[1],
            descricao=linha[2],
            concluida=int(linha[3])==1,  # SQLite guarda boolean como 0 ou 1, convertemos de volta
            criada=linha[4]  # String de data ISO (Ex: 2026-01-13T08:30:00)
        )
        lista_tarefas.append(tarefa)

    return lista_tarefas


def buscar_por_id(tarefa_id: int) -> Optional[Tarefa]:
    con = db.reconnectdb(db.con)
    cur = con.cursor()
    exp_sql = f'SELECT id, titulo, descricao, concluida, criada FROM {db.NOME_TABELA} WHERE id = ?'
    cur.execute(exp_sql, (tarefa_id,))
    linha = cur.fetchone()  # Traz apenas uma linha (ou None se não existir)
    con.close()
    if linha:
        return Tarefa(
            id=linha[0],
            titulo=linha[1],
            descricao=linha[2],
            concluida=bool(linha[3]),
            criada=linha[4]
        )
    return None