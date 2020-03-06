#!/usr/bin/python3

PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'politica'}
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida'
]

if __name__ == '__main__':
    for texto in textos:
        intersecao = PALAVRAS_PROIBIDAS.intersection(
            set(texto.lower().split()))
        if intersecao:
            print(f'Texto possui {len(intersecao)} palavras repetidas', intersecao)
        else:
            print('Texto autorizado:', texto)
