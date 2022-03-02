# -*- coding:  utf-8 -*-

#coleta dados
num = int(input ("Digite um inteiro de 4 algarismos: "))

#metodo aplicado:
mil = num // 1000
cent = (num % 1000) // 100
dez = (num % 100) // 10
uni = num % 10

#metodo mais simples:
#numI = int(str(num)[::-1])

#exibindo o invertido
print("Valor invertido: %i%i%i%i " % (uni, dez, cent, mil))

