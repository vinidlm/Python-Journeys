# -*- coding:  utf-8 -*-

#coleta o dado
seg = int(input ("Digite o valor do tempo em segundos: "))

horas = seg // 3600
seg = seg % 3600
min = seg // 60
seg = seg % 60 

#mostra o resultado
print("Valor convertido: %i h %i m %i s" % (horas, min, seg))

