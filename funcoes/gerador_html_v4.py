#!/usr/bin/python3


''' 
Quando se coloca um argumento do tipo *(star) todos os seguintes
argumentos devem ser nomeados na chamada da funcao. Perde-se a 
possibilidade de usar argumentos posicionais.
'''


def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}"> {html} </{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul{lista}></ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('Inline e classe', 'Info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
