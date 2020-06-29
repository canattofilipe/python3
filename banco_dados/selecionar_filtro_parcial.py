#!python3

from db import nova_conexao
from mysql.connector import ProgrammingError

sql = "SELECT * FROM contatos WHERE nome like '%a%'"

with nova_conexao() as conexao:

    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
