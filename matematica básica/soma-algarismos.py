# -*- coding:  utf-8 -*-

num = float(input ("Digite um inteiro de 4 algarismos: "))
mil = num // 1000
cent = (num % 1000) // 100
dez = (num % 100) // 10
uni = num % 10
soma = uni+mil+dez+cent
print("Resultado: %i" % soma)