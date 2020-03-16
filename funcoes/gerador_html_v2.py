#!/usr/bin/python3

"""
Funcoes com parametros nomeados.
"""


# se nao for passado nada o valor padrao do argumento classe sera "success"
def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}"> {texto} </{tag}>'


if __name__ == '__main__':
    # Testes (assertions)
    print(tag_bloco('bloco'))
    print(tag_bloco('Inline e classe', 'Info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
