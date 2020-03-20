#!/usr/bin/python3

palavras_reservadas = ('class')


def filtro_palavras_reservadas(palavra):
    return palavra.split('_')[-1]


def tag(tag, *args, **kwargs):
    miolo = ''.join(f' {conteudo}' for conteudo in args)
    params = ''.join(
        f'{filtro_palavras_reservadas(k)}="{v}"' for k, v in kwargs.items())
    return ''.join(f'<{tag} {params}> {miolo} </{tag}>')


if __name__ == '__main__':
    print(tag('p',
              tag('span', 'Curso de Python 3 por '),
              tag('strong', 'Juracy Filho', id='jf'),
              tag('span', ' e '),
              tag('strong', 'Leonardo Leitão', id='ll'),
              tag('span', '.'),
              html_class='alert'
              )
          )
