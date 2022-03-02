# -*- coding:  utf-8 -*-
#adiciona acentuação no codigo 

PI = 3.1415

#define o raio
raio = float(input ("Digite o valor do raio da circunferência: "))

#formulas
p = 2 * PI * raio
a = PI * (raio**2)
v = 4 * PI * (raio**3)/3

#imprimindo os resultados
print ("Perímetro: %.2f" % p)
print("Área: %.2f" % a)
print("Volume: %.2f" % v)