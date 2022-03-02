# -*- coding:  utf-8 -*-

inv = float(input ("Digite o valor do investimento inicial: "))
juro = float(input ("Digite a taxa de juros anual: "))
temp = float(input ("Digite o período do investimento em anos: "))

fut = inv * (1+(juro * 0.01))**temp

print("Valor futuro: %.2f" % fut)