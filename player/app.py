#!/usr/bin/python3
import numpy as np

DELIMITER = ';'


def load():
    m = []
    with open('data/data.csv') as file:
        for raw_row in file:
            if len(m) == 0:
                m = np.array([raw_row.split(DELIMITER)])
                continue
            row = raw_row.split(DELIMITER)
            m = np.append(m, [row], 0)
        return m


if __name__ == '__main__':
    m = load()
    print(m[9][2])
