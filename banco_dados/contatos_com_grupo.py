#!python3

from db import nova_conexao
from mysql.connector import ProgrammingError

sql = '''
SELECT
    grupos.descricao AS grupo,
    contatos.nome AS contatoNome
FROM contatos
INNER JOIN grupos ON contatos.grupo_id = grupos.id
ORDER BY grupo, contatoNome
'''
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro  : {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["contatoNome"]}')
