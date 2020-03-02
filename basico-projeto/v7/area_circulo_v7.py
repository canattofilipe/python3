#!/usr/bin/python3

# import math
from math import pi

"""
Calcula a area do circulo.
"""


def circulo(raio):
    print('Área do circulo =', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
