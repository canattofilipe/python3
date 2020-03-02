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
    print(sys.argv[0])  # uri do script.
    print(sys.argv[1])  # uri do script.
    area = circulo(sys.argv[1])
    print('Área do círculo', area)
