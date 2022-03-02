# -*- coding:  utf-8 -*-

#coleta os dados
speed = float(input ("Digite o valor da velocidade: "))
ace = float(input ("Digite o valor da aceleração: "))
time = float(input ("Digite o valor do tempo: "))

#formulas de velocidade final e distancia percorrida
v = speed + ace * time
d = speed * time + (ace*time**2)/2

#mostra os resultados
print("Velocidade final: %.2f" % v)
print("Distância percorrida: %.2f" % d)