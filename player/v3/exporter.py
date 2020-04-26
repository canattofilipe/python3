#!/usr/bin/python3

from prettytable import PrettyTable
import jinja2

x1 = PrettyTable()


def export(l):
    x1.add_column('Sensor', ['Minima', 'Máxima', 'Média'])
    for key, value in l.items():
        value_aux = sorted(value)
        min = "{:.2f}".format(value_aux[0]).replace('.', ',')
        max = "{:.2f}".format(value_aux[-1]).replace('.', ',')
        avg = sum(value)/len(value)
        avg = "{:.2f}".format(avg).replace('.', ',')
        x1.add_column(key, [min, max, avg])
    table = x1.get_html_string(attributes={"id": "customers"})

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(table=table)
    print(outputText)
