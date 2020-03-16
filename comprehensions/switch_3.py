#!/usr/bin/python3


def get_dias_semana(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana'
    }
    dias_escolhido = (v for k, v in dias.items() if dia in k)
    return next(dias_escolhido, '** dia inválido')


if __name__ == '__main__':
    for i in range(0, 8):
        print(f'Dia {i}: {get_dias_semana(i)}')
