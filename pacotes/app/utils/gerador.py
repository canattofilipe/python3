import random
nomes = ['Jose', 'João', 'Marcio', 'Enzo']


def novo_nome():
    return nomes[random.randint(0, len(nomes)-1)]

