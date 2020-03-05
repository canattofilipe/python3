#!/usr/bin/python3

# iterando sobre uma string.
palavra = 'paralelepipado'
for letra in palavra:
    print(letra, end=',')
print('Fim')

# iterando sobre uma lista.
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(posicao+1, nome)

# iterando sobre uma tupla.
dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sabado')

for dia in dias_semana:
    print(f'Hoje é dia {dia}')

# iterando sobre um conjunto de string.
for letra in set('Muito Legal'):
    print(letra)

# iterando sobre um conjunto de numeros.
for numero in {1, 2, 3, 4, 5}:
    print(numero)
