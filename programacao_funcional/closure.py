#!//usr/bin/python3


def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    # provando de dobro e triplo são funcoes
    print(dobro)
    print(triplo)
    print(f'O dobro de 7 é {dobro(7)}')
    print(f'O triplo de 3 é {triplo(3)}')
