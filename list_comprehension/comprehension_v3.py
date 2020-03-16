#!/usr/bin/python3

"""
Um generator é muito semelhante a um comprehension, porem faz um
uso mais intelegente da memoria, criando uma estrtura dinamica, que
cresce sob demanda.
"""

generator = (i**2 for i in range(10) if i % 2 == 0)
print(next(generator))  # 0
print(next(generator))  # 4
print(next(generator))  # 16
print(next(generator))  # 32
print(next(generator))  # 64
print(next(generator))  # Erro
