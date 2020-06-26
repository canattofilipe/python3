#!python3

from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Lucas', '98761-4321'),
    ('Bia', '98762-4321'),
    ('Jose', '98735-4321'),
    ('Joao', '98745-4321'),
    ('Ricardo', '58765-4321'),
    ('Rafael', '96765-4321'),
)
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro  : {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
