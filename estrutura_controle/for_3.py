#!/usr/bin/python3

# iterando sobre um dicionario.
produto = {'Nome': 'Caneta Chic', 'preco': 14.99,
           'Importada': True, 'estoque': 739}

# iterando sobre as chaves de um dicionario.
for chave in produto:
    print(chave)

# iterando sobre os valores de um dicionario.
for valor in produto.values():
    print(valor)

# iterando sobre as chaves e valores de um dicionario.
for chave, valor in produto.items():
    print(f'{chave} = {valor}')