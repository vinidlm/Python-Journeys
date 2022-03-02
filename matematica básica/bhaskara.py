# -*- coding:  utf-8 -*-
import math

a = float(input ("Digite o valor de a: "))
b = float(input ("Digite o valor de b: "))
c = float(input ("Digite o valor de c: "))

d = (b**2) - (4*a*c)
if d < 0:
    print("Não existe raiz real")

if d == 0:
 x1 = (-b + (math.sqrt(d)))/(2*a)
 a*(x1**2) + (b*x1) + c == 0
 print ("Raiz única")
 print("Raiz: %.2f" % x1)


if d > 0:
 x1 = (-b + (math.sqrt(d)))/(2*a)
 x2 = (-b - (math.sqrt(d)))/(2*a)
 a*(x1**2) + (b*x1) + c == 0
 a*(x2**2) + (b*x2) + c == 0
 print("Raiz 1: %.2f" % x1)
 print("Raiz 2: %.2f" % x2)