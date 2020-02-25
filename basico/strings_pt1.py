"""
Exemplos de strings em Python3.
"""

print(dir(str))

nome = 'Saulo de Tarso'

# a instrucao abaixo gera erro, como em java uma string é imutavel.
# print(nome[0])

# strings com "aspas duplas" e 'aspas simples' no meio.
print("exemplo de texto com aspas duplas que contem 'aspas' simples.")
print('exemplo de texto com aspas simples que contem \'aspas\' simples.')
print("exemplo de texto com aspas duplas que contem \"aspas\" duplas.")

doc = """ Texto com múltiplas
... linhas"""
print(doc)

doc2 = ''' Texto com múltiplas
... linhas'''
print(doc2)
