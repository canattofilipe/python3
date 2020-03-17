#!/usr/bin/python3

"""
Funcoes com parametros nomeados.
"""


# se nao for passado nada o valor padrao do argumento classe sera "success"
def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}"> {conteudo} </{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul{lista}></ul>'


if __name__ == '__main__':
    # Testes (assertions)
    print(tag_bloco('bloco'))
    print(tag_bloco('Inline e classe', 'Info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
