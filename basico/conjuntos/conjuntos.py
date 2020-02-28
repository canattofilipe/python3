"""
Exemplos de conjuntos em Python3.
"""

# criando um conjunto.
a = {1, 2, 3, 3}
print(type(a))  # <class 'set'>
print(a)

# criando um conjunto usando a funcao set().
a = set('cod3r')
print(a)

# usando operadores de membro em conjuntos.
print('c' in a, 't' not in a)

# verica se um conjunto pertence ao outro.
{1, 2, 3} == {3, 2, 1, 3}  # True

# Operações.

c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))  # {1, 2, 3}
print(c1.intersection(c2))  # {2}

# incorpora os elementos de "c2" em "c1".
c1.update(c2)
print(c1)  # {1, 2, 3}

# verifica se "c2" é um subconjunto de "c1".
print(c2 <= c1)  # True

# verifica se "c1" é um superconjunto de "c2".
print(c1 >= c2)

# mostra a diferença entre os conjuntos (isso é o contrario da interseção)
print({1, 2, 3} - {2})
print(c1 - c2)
