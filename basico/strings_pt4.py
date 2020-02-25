"""
Exemplos de strings em Python3.
"""

# ref: https://www.python-course.eu/python3_magic_methods.php

a = '123'
b = ' de Oliveira 4'

print(a + b)
print(a.__add__(b))
print(str.__add__(a, b))

print(dir(str))
len(a)
a.__len__()
'a' in a
a.__contains__('1')
