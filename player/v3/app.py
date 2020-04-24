#!/usr/bin/python3

import config
import input

y_axis = {}
labels = {}


def load():
    m = []
    with open('data/data.csv', encoding='iso-8859-1') as file:
        for l in file:
            a = l.split(config.DELIMITER)
            m.append(a)
        load_config(m)
        return m


def load_config(m):
    load_labels(m)

    for i, a in enumerate(m):
        y_axis.update({a[0]: i})


def load_labels(m):
    for i in m:
        if i[0] == config.LABEL_COLUMN_HINT:
            for j, k in enumerate(i):
                labels[j] = k


def find_hot_spots_in_interval(m, interval, mode=1):

    interval_from = interval[0]
    interval_to = interval[1]

    interval_sensor_from = config.sensors_range[0]
    interval_sensor_to = config.sensors_range[1]

    tag = {'l': None, 'r': None}
    v = float(m[interval_from][interval_sensor_from].replace(',', '.'))

    for il, l in enumerate(m[interval_from:interval_to+1], start=interval_from):
        for ic, c in enumerate(l[interval_sensor_from:interval_sensor_to], start=interval_sensor_from):
            aux = float(c.replace(',', '.'))
            if mode == 1 and aux >= v:
                v = aux
                tag['l'] = il
                tag['r'] = ic
            elif mode == 2 and aux <= v:
                v = aux
                tag['l'] = il
                tag['r'] = ic
    return tag


def find_hot_spots_in_interval_for_each_sensor(m, interval, mode=1):

    interval_from = interval[0]
    interval_to = interval[1]

    interval_sensor_from = config.sensors_range[0]
    interval_sensor_to = config.sensors_range[1]

    dici = {}

    for i in range(interval_sensor_from, interval_sensor_to):
        aux_lista = []
        for j in (range(interval_from, interval_to+1)):
            aux_lista.append(float(m[j][i].replace(',', '.')))
        dici.update({labels[i]: aux_lista})

    return dici


if __name__ == '__main__':
    m = load()
    interval = (y_axis[input.datetime_inicio], y_axis[input.datetime_fim])

    hotter_point_location = find_hot_spots_in_interval(m, interval)
    colder_point_location = find_hot_spots_in_interval(m, interval, 2)
    print(
        f"ponto mais quente do periodo: {m[hotter_point_location['l']][hotter_point_location['r']]} | sensor: {labels[hotter_point_location['r']]} | horario: {m[hotter_point_location['l']][0]}")
    print(
        f"ponto mais frio do periodo: {m[colder_point_location['l']][colder_point_location['r']]} | sensor: {labels[colder_point_location['r']]} |  horario: {m[colder_point_location['l']][0]}")

    x = find_hot_spots_in_interval_for_each_sensor(m, interval)
