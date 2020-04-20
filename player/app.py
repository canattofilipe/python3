#!/usr/bin/python3
import numpy as np

DELIMITER = ';'

i = {}
sensors = {}
begin = None
end = None
axys_x_len = 0


def load():
    m = []
    count = 0
    with open('data/data.csv') as file:
        for raw_row in file:
            if len(m) == 0:
                m = np.array([raw_row.split(DELIMITER)])
                i.update({raw_row.split(DELIMITER)[0]: count})
                count += 1
                continue
            row = raw_row.split(DELIMITER)
            i.update({row[0]: count})
            m = np.append(m, [row], 0)
            count += 1
        return m


def from_string_to_float(m):
    for i in (range(begin, end+1)):
        for j in range(2, axys_x_len):
            m[i][j] = float(m[i][j].replace(',', '.'))


def new(m):
    new_m = []
    for i in (range(begin, end+1)):
        if i == begin:
            new_m = np.array([m[i]])
            continue
        new_m = np.append(new_m, [m[i]], 0)
    return new_m


def get_higher_value(m):
    v = {'value': float(m[0][2]), 'sensor_index': 2}
    for i in m:
        for idx, j in enumerate(i[2:], start=2):
            aux = {'value': float(j), 'sensor_index': idx}
            v = aux if aux['value'] > v['value'] else v
    return v


def get_min_value(m):
    v = float(m[0][2])
    for i in m:
        for j in i[2:axys_x_len-4]:
            aux = float(j)
            v = aux if aux < v else v
    return v


def get_sensors_hash(m):
    for i in m:
        if i[0] == 'Scan Sweep Time (Sec)':
            for idx, j in enumerate(i[2:axys_x_len-4], start=2):
                sensors[idx] = j


if __name__ == '__main__':
    m = load()
    axys_x_len = len(m[0])
    begin = i['2020-02-21 13:40:31,610']
    end = i['2020-02-21 13:40:31,610']
    from_string_to_float(m)
    # for i in (range(begin, end+1)):
    #    print(m[i])
    new_m = new(m)
    print(get_higher_value(new_m))
    print(get_min_value(new_m))
    get_sensors_hash(m)
    print(sensors)
    print(sensors[9])
