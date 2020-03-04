#!/usr/bin/python3

for i in range(1, 11):
    print('i = {}'.format(i))

# como nao foi passado um intervalo assume começar do 0.
for j in range(10):
    print('j = {}'.format(j))

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{ x } * { y } = { x * y }')
