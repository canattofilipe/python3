#!/usr/bin/python3

'''
Tipos de método:
- método de instancia:
    Recebe a instancia como parametro
- método de classe:
    Recebe a classe como parametro
- método estatico:
    Não recebe parametro
'''


class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido ? {HomoSapiens.is_evoluido()}')
    print(f'Homo Sapiens evoluido ? {Neanderthal.is_evoluido()}')
    print(f'Jose evoluido ? {jose.is_evoluido()}')
    print(f'Grokn evoluido ? {grokn.is_evoluido()}')
