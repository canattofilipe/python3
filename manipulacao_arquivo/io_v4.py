#!/usr/bin/python3


try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome {}, Idade {}'.format(registro.strip().split(',')))

except IndexError:
    print('capturando uma excessao do tipo \'IndexError\'.')
finally:
    print('fechando stream.')
    arquivo.close()

if arquivo.closed:
    print('o arquivo foi fechado.')
