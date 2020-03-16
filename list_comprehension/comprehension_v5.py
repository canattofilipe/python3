#!/usr/bin/python3


dicionario = {i: i*2 for i in range(10) if i % 2 == 0}
print(dicionario)

dicionario2 = {f'Chave {i}': f'Valor {i*2}' for i in range(10) if i % 2 == 0}
print(dicionario2)
