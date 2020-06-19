#!/usr/bin/python3
from functools import reduce


def mdc(l):
    div = 2
    div_com = set()
    aux = l
    while True:
        v = list(map(lambda e: int(e/div)
                     if e % div == 0
                     else e,
                     aux))

        if v == aux:
            div += 1
            continue

        if not any(aux[i] == v[i] for i in range(len(l))):
            div_com.add(div)

        aux = v

        if len(list(filter(lambda e: e == 1, aux))) == len(l):
            break

    return reduce(lambda d, f: d * f, div_com, 1)


if __name__ == '__main__':
    print(mdc([21, 7]))
    print(mdc([125, 40]))
    print(mdc([9, 564, 66, 3]))
    print(mdc([55, 22]))
    print(mdc([15, 150]))
    print(mdc([7, 9]))
