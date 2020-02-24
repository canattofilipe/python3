"""
Exemplos de números em Python3.
"""

from decimal import Decimal, getcontext

print(Decimal(1) / Decimal(7))  # 0.1428571428571428571428571429

getcontext().prec = 4

print(Decimal(1) / Decimal(7))  # 0.1429

print(Decimal.max(Decimal(1), Decimal(7)))

print(dir(Decimal))

print(1.1 + 2.2)  # 3.3000000000000003
print(Decimal(1.1) + Decimal(2.2))  # 3.300
