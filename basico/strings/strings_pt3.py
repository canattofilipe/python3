"""
Exemplos de strings em Python3.
"""

"""
Verifica se trechos estão presentes na
string atraves do usu do operador membro (in).
"""

frase = 'Python é uma linguagem excelente.'

print('py' in frase)  # False
print('ing' in frase)  # True
print('py' not in frase)  # True

# imprimi o tamanho da string.
print(len(frase))

# imprimi todos os caracteres em letras minusculas.
print(frase.lower())
print('py' in frase.lower())  # True

# imprimi todos os caracteres em letras maiusculas.
print(frase.upper())

# imprimi a string "quebrada"(delimitador padrao é o caractere de espaço).
print(frase.split())

# imprimi a string "quebrada" usando o caractere passado como argumento.
print(frase.split('a'))
