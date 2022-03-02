# -*- coding:  utf-8 -*-
import math

lista = []
y = int(input('Digite um número:'))
lista.append(y)
while y >= 0:
    y = int(input('Digite um número:'))
    if y < 0:
        break
    lista.append(y)

print('Maior:', max(lista))
print('Menor:', min(lista))
