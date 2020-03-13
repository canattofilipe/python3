#!/usr/bin/python3

"""
Programa que le um arquivo .csv e salva seu conteudo
formatado em um arquivo .txt usando uma lib do python.
"""

import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome {}, Idade {}'.format(*pessoa))
