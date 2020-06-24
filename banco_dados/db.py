#!python3

from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='cpqdcpqd',
    database='agenda'
)

# Utilitario para ser usado com o bloco with


@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    # sera chamado quando o bloco with terminar
    finally:
        print('finally...')
        if (conexao and conexao.is_connected()):
            conexao.close()
