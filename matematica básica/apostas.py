# -*- coding:  utf-8 -*-

p = float(input ("Digite o valor que o Pedro apostou: "))
j = float(input ("Digite o valor que o João apostou: "))
m = float(input ("Digite o valor que a Marcela apostou: "))
vp = float(input ("Digite o valor do prêmio: "))

aux = p+j+m

pp = (p/aux) * vp
pj = (j/aux) * vp
pm = (m/aux) * vp


print("Prêmio do Pedro: %.2f" % pp)
print("Prêmio do João: %.2f" % pj)
print("Prêmio da Marcela: %.2f" % pm)
