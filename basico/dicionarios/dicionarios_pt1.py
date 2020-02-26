"""
Exemplos de dicionários em Python3.
"""

# criando um dicionario.
pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': [
    'Inglês', 'Português']}

# verifica o tipo.
print(type(pessoa))  # <class 'dict'>

# mostra as operações disponiveis para um dicionario.
print(dir(dict))

"""
mostra a quantidade de pares (chave e valor) contidas
no dicionario.
"""
print(len(pessoa))

# acessando valor pela chave.
print(pessoa['nome'])
print(pessoa.get('idade'))

"""
acessa o valor pela chave e
devolve um valor customizado quando nao encontra a chave.
"""
print(pessoa.get('valor invalido'), ['lista vazia'])

# acessando um valor do tipo lista
print(pessoa['cursos'][1])

# mostra todas as chaves de um dicionario.
print(pessoa.keys())

# mostra todos os valores de um dicionario.
print(pessoa.values())

# mostra todos os items (chave e valor) de um dicionario.
print(pessoa.items())
