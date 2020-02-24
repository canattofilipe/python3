"""
Exemplos de operadores ternarios em Python3.
"""

esta_chovendo = False
print('Hoje estou com as roupas ' + ('molhadas', 'secas')[esta_chovendo])
print('Hoje estou com as roupas ' + ('molhadas' if esta_chovendo else 'secas'))
