#!/usr/bin/python3

'''
Como visto em "problema_arg_padrao_mutavel.py" usar argumentos padroes
mutaveis em funcoes eh um perigo, porem caso seja necessario existe
uma tecnica para evitar armadilhas, esse exemplo mostra essa tecninca.
'''


def fibonacci(sequencia=None):
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))

    assert restart == [0, 1, 1]
