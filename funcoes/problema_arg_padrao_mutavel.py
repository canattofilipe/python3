#!/usr/bin/python3

'''
Esse exemplo mostra o perigo de se usar objetos mutaveis
com valor padrao em funcoes (exemplo lista/[]), nesse caso a o valor padrao
e alterado em tempo de execuçao e engana o programador
pois usa um valor diferente do que esta escrito.

Resolve-se esse problema trocando a lista por um objeto imutavel,
a tupla/()

Exemplo: def fibonacci(sequencia=(0, 1)):

'''


def fibonacci(sequencia=[0, 1]):
    # Uso de mutaveis com valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    # agora o valor padrao eh [0, 1, 1]
    inicio = fibonacci()
    print(inicio, id(inicio))
    # agora o valor padrao eh [0, 1, 1, 2]
    print(fibonacci(inicio))

    restart = fibonacci()
    print(restart, id(restart))
