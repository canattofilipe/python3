"""
Exemplos de membros em Python3.
"""

lista = [1, 2, 3, 'Ana', 'Carla']

# verifica se "2" esta presente na lista
print(2 in lista)

# verifica se "Ana" NAO esta presente na lista
print('Ana' not in lista)

"""
Exemplos de identidade em Python3.
"""

x = 3
y = x

print(x is y)  # True

z = 3

print(y is not z)  # False

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]
print(lista_a is lista_b)  # True
print(lista_b is lista_c)  # False
print(lista_a is not lista_c)  # True
