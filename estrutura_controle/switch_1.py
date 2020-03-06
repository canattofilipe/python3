#!/usr/bin/python3

# python não oferece suporte nativo a switch, esse exemplo mostra como simular um.


def get_dia_semana(dia):
    dias = {
        1: 'Domindo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado'
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    for dia in range(1, 9):
        print(f' {dia}: {get_dia_semana(dia)}')
