#!/usr/bin/python3

"""
Programa que le um arquivo .csv e salva seu conteudo
formatado em um arquivo .txt
"""

with open('pessoas.csv') as arquivo:

    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome {}, Idade {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('o arquivo de leitura foi fechado.')
if saida.closed:
    print('o arquivo de escrita foi fechado.')
