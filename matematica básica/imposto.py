# -*- coding:  utf-8 -*-

v = float(input ("Digite o valor do produto: "))
uf = str(input ('Digite o estado: '))

if uf == "MG":
    vf = v + ((7/100)*v)
    print("Valor final: %.2f" % vf)
elif uf == "SP" == "sp":
    vf = v + ((12/100)*v)
    print("Valor final: %.2f" % vf)
elif uf == "RJ" == "rj":
    vf = v + ((15/100)*v)
    print("Valor final: %.2f" % vf)
elif uf == "MS" == "ms":
    vf = v + ((8/100)*v)
    print("Valor final: %.2f" % vf)
else: 
    print("Estado inválido")