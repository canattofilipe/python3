"""
Exemplos de strings em Python3.
"""

nome = 'Kamily Canatto'

# acessando indices.
print(nome[0])
print(nome[5])

# acessando indices reversamente (de traz pra frente).
print(nome[-7])

# acessando intervalos.
print(nome[7:])  # imprimi o indice 7 em diante.
print(nome[-7:])  # imprimi o indice -7 em diante.
print(nome[:6])  # imprimi até o indice 5.
print(nome[2:6])  # imprimi do indice 2 ao 6.

numeros = '1234567890'
print(numeros)
print(numeros[::])  # imprimi completamente / sem intervalos.
print(numeros[::2])  # imprimi um index e pula outro.
print(numeros[1::2])  # imprimi um index e pula outro partindo do index 1.
print(numeros[::-1])  # imprimi uma string reversamente.
print(numeros[::-2])  # imprimi uma string reversamente pulando um indice.
