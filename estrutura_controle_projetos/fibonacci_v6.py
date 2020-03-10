#!/usr/bin/python3

# sequencia fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21 ..


def fibonacci(quantidade):
    resultado = [0, 1]

    # "_" significa uma variavel nao utilizada, se fosse colocado outras como "i" ou "k" por exemplo o compilador apontaria um warning.
    for _ in range(2, quantidade+1):
        resultado.append(sum(resultado[-2:]))

    return resultado


if __name__ == "__main__":
    # lista os 21 primeiros da sequencia.
    print(fibonacci(5))
