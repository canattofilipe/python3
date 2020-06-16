#!/usr/bin/python3
from functools import reduce
from operator import add

# forçando a imutabilidade através do uso de estruturas de dados imutaveis
valores = (30, 10, 25, 100, 94)

# não altera a lista
print(sorted(valores))
print(valores)

# altera a lista
# valores.sort()
# print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))

# soma via reduce
print(reduce(add, valores))

print(tuple(reversed(valores)))

print(valores)
