#!/usr/bin/python3

"""
Desafio:
Extrair o nono e o quarto campos do arquivo CSV sobre Região de influência das Cidades do IBGE,
"""

import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'https://raw.githubusercontent.com/canattofilipe/python3/master/manipulacao_arquivo/desafio_ibge/desafio-ibge.csv')
