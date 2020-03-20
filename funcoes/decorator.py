#!/usr/bin/python3

'''
Esse exemplo mostra as faciliades que o python oferece
para usar o padrao de projeto "decorator".
'''


def log(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {args}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x+y


@log
def sub(x, y):
    return x-y


if __name__ == '__main__':
    soma(5, 7)
    sub(7, 5)
