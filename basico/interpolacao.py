"""
Exemplos de interpolação em Python3.
"""

from string import Template

nome, idade, altura = 'Ana', 30, 1.6587

# 1. interpolação de variável (jeito mais antigo).
print('Nome: %s, Idade %d, %.2f' % (nome, idade, altura))

# 2. interpolação de variável (python < 3.6).
print('Nome: {0}, Idade {1}, Altura {2}'.format(nome, idade, altura))

# 3. interpolação de variável (python >= 3.6).
print(f'Nome: {nome}, Idade: {idade}, Altura: {altura}')

# 3.1 interpolação de sentença matematica (python >= 3.6).
print(f'{2 ** 2 + 5}')

# 4. interpolação usando o template.
s = Template('Nome: $nome, Idade: $idade, Altura: $altura')
print(s.substitute(nome=nome, idade=idade, altura=altura))
