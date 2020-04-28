#!/usr/bin/python3

from prettytable import PrettyTable
import jinja2
import config
import pdfkit


def create_table(l, labels, s_index):
    x1 = PrettyTable()
    x1.add_column('Sensor', ['Minima', 'Máxima', 'Média'])
    for i, value in enumerate(l, start=s_index):
        value_aux = sorted(value)
        min = "{:.2f}".format(value_aux[0]).replace('.', ',')
        max = "{:.2f}".format(value_aux[-1]).replace('.', ',')
        avg = sum(value)/len(value)
        avg = "{:.2f}".format(avg).replace('.', ',')
        x1.add_column(labels[i], [min, max, avg])

    return x1.get_html_string(attributes={"id": "customers"})


def export(l, labels):

    chunks = [l[x:x+4] for x in range(0, len(l), 4)]

    table = ''

    inic = config.sensors_range[0]

    for i in chunks:
        table = table + create_table(i, labels, inic)
        table = table+'<br>'
        inic = inic + len(i)

    print(table)

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(table=table)
    # print(outputText)
    pdfkit.from_string(outputText, 'sensor_list.pdf')
