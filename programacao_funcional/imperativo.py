#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name


'''
Programacao imperativa é quando você escreve como algo
deve ser feito.
Programação declarativa é quando você pede para algo ser feito
sem a necessidade de saber como é feito (exemplo: instrucao SQL)
'''

# Usa locale padrão do OS
setlocale(LC_ALL, '')

# Meses com 31 dias
for i in range(1, 13):
    if mdays[i] == 31:
        print(f'- {month_name[i]}')
