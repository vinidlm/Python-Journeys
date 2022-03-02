# -*- coding:  utf-8 -*-

ht = float(input ("Digite o valor da hora de trabalho: "))
sal = float(input ("Digite a quantidade de horas trabalhadas no mês: "))

salbruto = ht * sal
if sal <= 900:
    ir = 0
    if 901 < salbruto <= 1500:
      ir = salbruto * (5/100)
    elif 1501 < salbruto <= 2500:
      ir = salbruto * (10/100)
    elif salbruto > 2500:
      ir = salbruto * (20/100)
 
inss = (10/100) * salbruto
fgts = (11/100) * salbruto
td = ir + inss
salq = salbruto - td

print("Salário Bruto: R$ %.2f" % salbruto)
print("IR: R$ %.2f" % ir)
print("INSS: R$ %.2f" % inss)
print("FGTS: R$ %.2f" % fgts)
print("Total de descontos: R$ %.2f" % td)
print("Salário líquido: %.2f" % salq)