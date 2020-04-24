#!/usr/bin/python3
import numpy as np
import constants

y_axis = {}
config = {'start_datetime': None, 'end_datetime': None,
          'start_datetime_index': None, 'end_datetime_index': None,
          'x_axis_len': None, 'labels': {}}


def load():
    m = []
    with open('data/data.csv', encoding='iso-8859-1') as file:
        for i, l in enumerate(file):
            a = l.split(constants.DELIMITER)
            if len(m) == 0:
                m = np.array([a])
                continue
            m = np.append(m, [a], 0)
        load_config(m)
        return m


def load_config(m):
    load_labels(m)

    config['x_axis_len'] = len(m[0])

    for i, a in enumerate(m):
        y_axis.update({a[0]: i})


def load_labels(m):
    for i in m:
        if i[0] == constants.LABEL_COLUMN_HINT:
            for j, k in enumerate(i):
                config['labels'][j] = k


def find_hotspot(m, interval, mode=1):
    x_axis_len = config['x_axis_len']

    v = float(m[interval[0]][2].replace(',', '.'))
    tag = {'l': 0, 'c': 0}

    for il, l in enumerate(m[interval[0]:interval[1]+1], start=interval[0]):
        for ic, c in enumerate(l[2:x_axis_len-4], start=2):
            aux = float(c.replace(',', '.'))
            if mode == 1 and aux >= v:
                v = aux
                tag['l'] = il
                tag['c'] = ic
            elif mode == 2 and aux <= v:
                v = aux
                tag['l'] = il
                tag['c'] = ic
    return tag


if __name__ == '__main__':
    m = load()
    config['start_datetime'] = '2020-02-21 13:41:31,610'
    config['end_datetime'] = '2020-02-21 13:49:31,663'

    config['start_datetime_index'] = y_axis['2020-02-21 13:41:31,610']
    config['end_datetime_index'] = y_axis['2020-02-21 13:49:31,663']

    interval = (config['start_datetime_index'], config['end_datetime_index'])
    info = find_hotspot(m, interval, 2)

    print(info)

    print(
        f"Ponto mais quente esta eh: {m[info['l']][info['c']]}, e esta no sensor: {config['labels'][info['c']]}")
