#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name

# Usa locale padrão do OS
setlocale(LC_ALL, '')

# Listar todos os meses do ano com  dias
meses_com_31_dias = list(map(lambda m: m[0], list(
    filter(lambda m: m[1] == 31, enumerate(mdays)))))

for i in meses_com_31_dias:
    print(month_name[i])
