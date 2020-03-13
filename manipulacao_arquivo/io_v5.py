#!/usr/bin/python3

"""
Usando o "with" dizemos o seguinte para o compilador:
abra um stream para o arquivo 'pessoas.csv' e quando o bloco
terminar feche o stream.
"""

with open('pessoas.csv') as arquivo:

    for registro in arquivo:
        print('Nome {}, Idade {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('o arquivo foi fechado.')
