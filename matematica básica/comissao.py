# -*- coding:  utf-8 -*-

valor = float(input ("Digite o valor da compra: "))
parcela = valor/6
desconto = valor*(90/100)
cav = (5/100)*desconto
cp = (5/100)*valor

print("Valor com desconto: %.2f" % desconto)
print("Valor da parcela: %.2f" % parcela)
print("Comissão do vendedor(á vista): %.2f" % cav)
print("Comissão do vendedor(parcelado): %.2f" % cp)