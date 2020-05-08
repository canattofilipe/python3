'''
Esse exemplo usa o padrao de projeto facade para
permitir  a importacao de n modulos apartir de
um unico pacote, ou seja, quem importar o
pacote calc tera acesso aos modulos modulo1 e modulo2
presentes nos pacotes pacote1 e pacote2.
'''
from pacote1.modulo1 import soma
from pacote2.modulo1 import subtracao

__all__ = ['soma', 'subtracao']
