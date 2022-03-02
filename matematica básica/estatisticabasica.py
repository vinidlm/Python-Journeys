# -*- coding:  utf-8 -*-
import statistics

num1 = float(input ("Digite o primeiro número: "))
num2 = float(input ("Digite o segundo número: "))
num3 = float(input ("Digite o terceiro número: "))

items = [num1, num2, num3]

print("Mediana: %.0f" % statistics.median(items))