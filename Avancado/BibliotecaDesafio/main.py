from logging import exception
from warnings import catch_warnings

import menu
import BibliotecaDesafio.acoes.livros as ll
import BibliotecaDesafio.acoes.usuarios as uu
import BibliotecaDesafio.acoes.emprestimos as ee

while True:
    acaoobj = menu.menu_objeto()
    if acaoobj == 0:
        break
    ff = menu.menu_acao(acaoobj)
    if acaoobj==1:
        ll.acoes(ff)
    if acaoobj==2:
        uu.acoes(ff)
    if acaoobj==3:
        ee.acoes(ff)

