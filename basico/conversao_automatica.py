"""
Exemplos de conversão automática em Python3.
"""

"""
O resultado de uma divisao sem arredondamento é sempre um float.
"""
x = 10 / 2
print(type(x))

"""
O resultado de uma divisao com arredondamento forçado com 2
operandos inteiros é sempre um inteiro.
"""
k = 10 // 3
print(type(k))

"""
O resultado de uma divisao com arredondamento forçado com
pelo menos 1 operando float é sempre um float.
"""
j = 10 // 2.5
print(type(j))
