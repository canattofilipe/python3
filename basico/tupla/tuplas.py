"""
Exemplos de tuplas em Python3.
"""

# cria uma tupla.
tupla = tuple()

# cria uma tupla.
tupla = ()

print(type(tupla))  # <class 'tuple'>

# lista as funcionalidades e pedindo ajuda.
print(dir(tuple))
print(help(tuple))

tupla = ('um',)
print(type(tupla))

# acessa um elemento pelo indicie.
print(tupla[0])

# tuple[0] = 'novo'
# TypeError: 'type' object does not support item assignment

cores = ('verde', 'amarelo', 'azul', 'azul', 'branco')
print(cores[0])
print(cores[-1])  # ultimo elemento.

# acessa um grupo de elementos.
print(cores[1:])  # ('amarelo', 'azul', 'branco')

# acessa um index pelo elemento.
print(cores.index('amarelo'))

# responde quantos elementos existem na tupla.
print(cores.count('azul'))

# mostra o tamanho da tupla.
print(len(cores))
