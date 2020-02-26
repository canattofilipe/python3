"""
Exemplos de listas em Python3.
"""

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]

# recupera o index atraves do elemento.
print(lista.index('Guilherme'))

# recupera o elemento atraves do index.
print(lista[2])

"""
Usa o operador membro para identificar se determinado
elemento esta presente na lista.
"""
print(1 in lista)  # True
print('Rebeca' in lista)  # True
print('Pedro' in lista)  # False

# recupera elementos pelo indice negativo.
print(lista[-1])  # ultimo elemento da lista.
print(lista[-5])  # primeiro elemento da lista.
