#!/usr/bin/python3
import numpy as np

DELIMITER = ';'

# Mapa que armazena o conteudo + indice da primeira coluna da matriz.
FIRST_COLUMN_MAP = {}
# Mapa que armazena as configuracoes.
CONFIG = {'start_datetime': None, 'end_datetime': None,
          'axys_x_len': None, 'labels': {}}


def load():
    m = []
    with open('data/data.csv') as file:
        for i, raw_row in enumerate(file):
            if len(m) == 0:
                m = np.array([raw_row.split(DELIMITER)])
                FIRST_COLUMN_MAP.update({raw_row.split(DELIMITER)[0]: i})
                CONFIG['axys_x_len'] = len(raw_row.split(DELIMITER))
                continue
            row = raw_row.split(DELIMITER)
            FIRST_COLUMN_MAP.update({row[0]: i})
            m = np.append(m, [row], 0)
        load_labels(m)
        return m


# Verifica se as informacoes de entrada sao validas.
def check(m):
    start_datetime, end_datetime = False, False
    if FIRST_COLUMN_MAP[CONFIG['start_datetime']]:
        start_datetime = True
    if FIRST_COLUMN_MAP[CONFIG['end_datetime']]:
        end_datetime = True

    return start_datetime and end_datetime


def load_labels(m):
    for i in m:
        if i[0] == 'Scan Sweep Time (Sec)':
            for j, k in enumerate(i):
                CONFIG['labels'][j] = k


def find_hotter_point(m):
    begin = FIRST_COLUMN_MAP[CONFIG['start_datetime']]
    end = FIRST_COLUMN_MAP[CONFIG['end_datetime']]
    axys_x_len = CONFIG['axys_x_len']

    v = float(m[begin][2].replace(',', '.'))
    tag = {'l': 0, 'c': 0}

    for il, l in enumerate(m[begin:end+1], start=begin):
        for ic, c in enumerate(l[2:axys_x_len-4], start=2):
            aux = float(c.replace(',', '.'))
            if aux >= v:
                v = aux
                tag['l'] = il
                tag['c'] = ic
    return tag


if __name__ == '__main__':
    CONFIG['start_datetime'] = '2020-02-21 13:41:31,610'
    CONFIG['end_datetime'] = '2020-02-21 13:49:31,663'
    m = load()

    check(m)

    info = find_hotter_point(m)

    print(info)

    print(
        f"Ponto mais quente esta eh: {m[info['l']][info['c']]}, e esta no sensor: {CONFIG['labels'][info['c']]}")
