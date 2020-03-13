#!/usr/bin/python3

"""
Esse exemplo diferente de io_v1.py só fecha o stream (arquivo.close()) no fim do 
programa, dessa maneira o python consegue ler o arquivo gradualmente sendo 
desnecessario carrega-lo completamente em memória. Essa técnica é chamada de streaming.
"""

arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome {}, Idade {}'.format(*registro.split(',')))

arquivo.close()
