#!/usr/bin/python3


def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a+b+c


# *numeros se tranforma em um tupla dentro da funcao.
def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(1, 2))
    print(soma_3(1, 2, 3))

    # packing
    print(soma_n(1, 2, 3, 4, 5))

    # unpacking
    tupla = (6, 7, 8)
    print(soma_n(*tupla))

    lista = [6, 7, 8]
    print(soma_n(*lista))
