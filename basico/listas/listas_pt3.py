"""
Exemplos de listas em Python3.
"""

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']

# acessando intervalos da lista.

print(lista[1:3])  # ['Lia', 'Rui']
print(lista[1:-1])  # ['Lia', 'Rui', 'Paulo']
print(lista[1:])  # ['Lia', 'Rui', 'Paulo', 'Dani']
print(lista[:-1])  # ['Ana', 'Lia', 'Rui', 'Paulo']
print(lista[:])  # ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']

print(lista[::2])  # ['Ana', 'Rui', 'Dani']
print(lista[::-1])  # ['Dani', 'Paulo', 'Rui', 'Lia', 'Ana']

# deleta um elemento pelo indice.
del lista[2]
print(lista)

# deleta um grupo de elementos.
del lista[1:]
print(lista)
