#!/usr/bin/python3


class Data:

    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # my function impl.
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    # built-in function impl.
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2013)
print(d1.to_str())

d2 = Data(7, 11, 2020)
print(d2)
