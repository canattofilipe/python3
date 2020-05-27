#!/usr/bin/python3


class ClasseSimples:
    contador = 0

    def __init__(self):
        self.incrementa_contador()
        # solucao alternativa (sem o uso do metodo incrementa_contador)
        # self.__class__.contador += 1

    @classmethod
    def incrementa_contador(cls):
        cls.contador += 1


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)
