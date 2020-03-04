#!/usr/bin/python3

# while True:
#     print('Loop infinito')

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe um número: '))

print('Número secreto {} foi encontrado.'.format(numero_informado))
