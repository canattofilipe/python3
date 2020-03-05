#!/usr/bin/python3

from random import randint

# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')


def sortear():
    return randint(1, 7)


if __name__ == '__main__':

    numero_sorteado = sortear()

    for i in range(1, 7):
        if i % 2 != 0:
            continue
        if i == numero_sorteado:
            print('ACERTOU', i)
            break
    else:
        print('Não acertou o numero')
