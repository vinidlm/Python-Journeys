# -*- coding:  utf-8 -*-

num1 = float(input ("Digite o comprimento do primeiro lado: "))
num2 = float(input ("Digite o comprimento do segundo lado: "))
num3 = float(input ("Digite o comprimento do terceiro lado: "))

if num1 < num2+num3 and num2 < num1+num3 and num3 < num1+num2:
    print("Triângulo ", end='')
    if num1 == num2 == num3:
        print("Equilátero")
    elif num1 != num2 != num3 != num1:
        print("Escaleno")
    elif num1 == num2 or num2 == num3 or num1 == num3:
         print("Isósceles")
else: 
    print("Não é um triângulo")