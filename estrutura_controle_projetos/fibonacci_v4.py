#!/usr/bin/python3

# sequencia fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21 ..


def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == "__main__":
    print(fibonacci(21))
