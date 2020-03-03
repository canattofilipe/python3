#!/usr/bin/python3

# import math
from math import pi
import sys

"""
Calcula a area do circulo.
"""


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""\
É necessário informar o raio do círculo.
Sintaxe: {} <raio>""".format(sys.argv[0][2:]))
    else:
        print(sys.argv[0])  # uri do script.
        print(sys.argv[1])  # uri do script.
        area = circulo(sys.argv[1])
        print('Área do círculo', area)
