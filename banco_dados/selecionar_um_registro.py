#!python3

from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'SELECT nome, tel FROM contatos'

with nova_conexao() as conexao:

    cursor = conexao.cursor()
    cursor.execute(sql)

    print(cursor.fetchone())
