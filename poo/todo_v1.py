#!/usr/bin/python3
from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Passar pano'))
    casa.append(Tarefa('Tirar Pó'))
    casa.append(Tarefa('Lavar louça'))

    [t.concluir() for t in casa if t.descricao == 'Lavar louça']

    for t in casa:
        print(f'- {t}')


if __name__ == '__main__':
    main()
