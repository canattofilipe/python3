#!/usr/bin/python3
from funcao_primeira_class import dobro, quadrado


def processar(titulo, lista, funcao):
    print(f'processando {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrados de 1 a 10', range(1, 11), quadrado)
