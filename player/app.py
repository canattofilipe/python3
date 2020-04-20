#!/usr/bin/python3
import numpy as np

DELIMITER = ';'

i = {}
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


if __name__ == '__main__':
    m = load()
    axys_x_len = len(m[0])
    begin = i['2020-02-21 13:42:31,648']
    end = i['2020-02-21 14:03:31,643']
    from_string_to_float(m)
    for i in (range(begin, end+1)):
        print(m[i])
