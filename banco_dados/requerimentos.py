#!python3

try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL não instalado!')
else:
    print('MySQL connector esta instalado e pronto!')
