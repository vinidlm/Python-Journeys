# -*- coding:  utf-8 -*-
import math

def soma_divisores(x):
    soma = 0
    for n in range(1, x):
        if x % n == 0:
            soma += n
    return soma

y = (int(input('Digite o número:')))
soma_divisores(y)
print("", soma_divisores(y))