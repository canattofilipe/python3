
print('operadores de membro')

lista = [1, 2, 3, 'Ana', 'Carla']

# verifica se "2" esta presente na lista
print(2 in lista)

# verifica se "Ana" NAO esta presente na lista
print('Ana' not in lista)


print('operadores de identidade')
x = 3
y = x

print(x is y)

z = 3

print(y is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]
print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)
