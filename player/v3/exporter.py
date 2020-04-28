#!/usr/bin/python3

from prettytable import PrettyTable
import jinja2
import pdfkit


def create_html_table_for_each_sensor(l):
    pt = PrettyTable()
    pt.add_column('Sensor', ['Mínima', 'Máxima', 'Média'])
    for value in l:
        value_aux = sorted(value.values)
        min = "{:.2f}".format(value_aux[0]).replace('.', ',')
        max = "{:.2f}".format(value_aux[-1]).replace('.', ',')
        avg = sum(value_aux)/len(value_aux)
        avg = "{:.2f}".format(avg).replace('.', ',')
        pt.add_column(value.label, [min, max, avg])

    return pt.get_html_string(attributes={"id": "customers"})


def export_for_each_sensor(l):

    chunks = [l[x:x+5] for x in range(0, len(l), 5)]

    table = ''
    for i in chunks:
        table = table + create_html_table_for_each_sensor(i)
        table = table+'<br>'

    to_pdf('template_for_each_sensor.html', {
           'attr': 'table', 'value': table})


def to_pdf(template_name, map):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = template_name
    template = templateEnv.get_template(TEMPLATE_FILE)
    for k, v in map.items():
        outputText = template.render(k=v)
    pdfkit.from_string(outputText, 'sensor_list.pdf')
