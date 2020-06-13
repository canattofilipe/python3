#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Usa locale padrão do OS
setlocale(LC_ALL, '')

# Listar todos os meses do ano com  dias
meses_31 = filter(lambda m: mdays[m] == 31, range(1, 12))
meses_nome = map(lambda m: month_name[m], meses_31)
juntar_meses = reduce(
    lambda todos, mes: f'{todos}:\n - {mes}', meses_nome, 'Meses com 31 dias')
print(juntar_meses)
