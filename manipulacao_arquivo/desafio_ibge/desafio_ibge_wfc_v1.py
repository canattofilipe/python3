#!/usr/bin/python3

"""
Desafio:
Extrair o nono e o quarto campos do arquivo CSV sobre Região de influência das Cidades do IBGE,
"""

import csv

with open('desafio-ibge.csv', encoding='ISO-8859-1') as file:
    counter = 0
    for line in csv.reader(file):
        if counter == 0:
            pass
        else:
            print('{} , {}'.format(line[3], line[8]))
        counter += 1
