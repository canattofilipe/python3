#!/usr/bin/python3


def get_dividendo():
    inic = 1
    while True:
        inic += 1
        yield inic


def doIt(dividendo, divisor):
    return int(dividendo/divisor) if dividendo % divisor == 0 else dividendo


def entra_na_conta(divs, divisor):
    r = True
    for x in divs:
        if x % divisor != 0:
            r = False
            break
    return r


def mdc(dividendos):
    print(dividendos)
    div = get_dividendo()
    r = dividendos
    y = next(div)
    ld = []
    while True:
        before = r
        r = [doIt(x, y) for x in r]
        if before != r:
            print(r)
            if entra_na_conta(before, y) is True:
                ld.append(y)
        else:
            y = next(div)

        dec = True
        for x in r:
            if x != 1:
                dec = False

        if dec is True:
            break

    print(ld)


if __name__ == '__main__':
    print(mdc([6, 12, 15]))
