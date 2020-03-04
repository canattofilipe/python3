#!/usr/bin/python3

import sys


def nota_conceito(nota):
    if nota <= 1 and nota >= 0:
        return 'E-'
    elif nota <= 2:
        return 'E'
    elif nota <= 3:
        return 'D-'
    elif nota <= 4:
        return 'D'
    elif nota <= 5:
        return 'C-'
    elif nota <= 6:
        return 'C-'
    elif nota <= 7:
        return 'B-'
    elif nota <= 8:
        return 'B'
    elif nota <= 9:
        return 'A-'
    elif nota <= 10:
        return 'A'
    else:
        return 'Nota invalida'


if __name__ == '__main__':
    nota = input('Informe uma nota: ')
    conceito = nota_conceito(float(nota))
    print(conceito)
