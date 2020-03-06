#!/usr/bin/python3


def get_dias_semana(dia):
    dias = {
        1: 'Domindo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado'
    }

    return dias.get(dia)


if __name__ == '__main__':

    dias_feriados = {1, 7}
    dias_normais = {2, 3, 4, 5, 6}

    for dia in range(1, 9):
        if dia in dias_feriados.union(dias_normais):
            print(
                f'{get_dias_semana(dia)} é {"feriado" if dia in dias_feriados else "dia normal"}')
        else:
            print('Dia inválido')
