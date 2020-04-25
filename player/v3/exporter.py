#!/usr/bin/python3

from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
x = PrettyTable()
x1 = PrettyTable()

x1.set_style(MSWORD_FRIENDLY)


x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])


#mystring = x.get_html_string()
# print(mystring)


def export(l):
    x1.add_column('Sensor', ['Minima', 'Máxima', 'Média'])
    for key, value in l.items():
        value_aux = sorted(value)
        min = "{:.2f}".format(value_aux[0]).replace('.', ',')
        max = "{:.2f}".format(value_aux[-1]).replace('.', ',')
        avg = sum(value)/len(value)
        avg = "{:.2f}".format(avg).replace('.', ',')
        x1.add_column(key, [min, max, avg])
    print(x1.get_html_string(format=True))
