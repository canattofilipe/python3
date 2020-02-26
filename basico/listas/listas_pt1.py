"""
Exemplos de listas em Python3.
"""

# cria uma lista.
lista = []
print(type(lista))  # <class 'list'>

# pedindo ajuda.
print(dir(lista))
print(help(lista))

# verifica o tamanho da lista.
print(len(lista))

# adiciona elementos.
lista.append(1)
lista.append(5)
print(lista)
print(len(lista))

# cria uma nova lista com valores.
nova_lista = [1, 2, 'Ana', 'Bia']
print(nova_lista)

# remove um elemento.
nova_lista.remove(2)
print(nova_lista)

# inverte a lista.
nova_lista.reverse()
print(nova_lista)
