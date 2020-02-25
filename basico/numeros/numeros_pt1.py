"""
Exemplos de números em Python3.
"""

print(dir(int))
print(dir(float))

a = 5
b = 2.5
print(a / b)
print(a + b)
print(a * b)

print(type(a))
print(type(b))
print(type(a - b))

print(b.is_integer())  # False
print(5.0.is_integer())  # True

# operando com funcoes dentro do modulo int
print(int.__add__(2, 3))
print((-2).__abs__())

# operando com builtin function.
print(abs(-2))

"""
A funcao abs() referencia/mapeia a funcao int.__abs__()
"""

# operando com funcoes dentro do modulo float
print(float.__add__(2.5, 3))
print((-2.9).__abs__())

# operando com builtin function.
print(abs(-2.9))

"""
A funcao abs() referencia/mapeia a funcao float.__abs__()
"""
