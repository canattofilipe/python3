#!/usr/bin/python3

'''
Exemplo com *kwargs (key word arguments), diferente da *args
o *kwargs gera um dicionario ao inves de tupla.

Nesse exemplo faço o packing, onde transformo parametros
nomeados em um dicionario.
'''


def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')
