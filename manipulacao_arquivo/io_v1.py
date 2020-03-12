#!/usr/bin/python3

registros = open('pessoas.csv')
dados = registros.read()
registros.close()

for registro in dados.splitlines():
    print('Nome {}, Idade {}'.format(*registro.split(',')))
