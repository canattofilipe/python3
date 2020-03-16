#!/usr/bin/python3

# Versão "normal/classica"
dobros = []
for i in range(10):
    dobros.append(i*2)
print(dobros)


# [ empressão for item in list if condicional ]

dobros = [i*2 for i in range(10)]
print(dobros)
