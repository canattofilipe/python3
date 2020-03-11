#!/usr/bin/python3

# sequencia fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21 ..


def fibonacci(lista, limite):
    if len(lista) < limite:
        lista.append(sum(lista[-2:]))
        fibonacci(lista, limite)


if __name__ == "__main__":
    # lista os 9 primeiros da sequencia.
    lista = [0, 1]
    fibonacci(lista, 9)
    print(lista)
