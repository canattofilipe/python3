"""
Exemplos de dicionários em Python3.
"""

# criando um dicionario.
pessoa = {'nome': 'Alberto', 'idade': 43, 'cursos': [
    'React', 'Python']}

# sobreescreve um valor da lista.
pessoa['idade'] = 44

# adiciona um elemento a valor do tipo lista.
pessoa['cursos'].append('Angular')
print(pessoa)

# le um valor do dicionario e remove do dicionario.
print(pessoa.pop('idade'))
print(pessoa)

# adiciona pares no dicionario.
pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)

# remove um par de chave ({ }) do dicionario.
del pessoa['cursos']
print(pessoa)
