#!/usr/bin/python3

generator = (i**2 for i in range(10) if i % 2 == 0)

"""
Usando um generator dentro do laço for a chamada ao
método next é implicita.
"""
for numero in generator:
    print(numero)
