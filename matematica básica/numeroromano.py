# -*- coding: utf-8 -*-
num = int(input("Digite um número:"))

if 0 > num or num > 999:
    print(" Erro: número deve estar entre 1 e 999")

cent = (num // 100)
dez = ((num % 100) // 10)
uni = (num % 10)

unidades = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
dezenas = {0:"", 1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
centenas = {0:"", 1:"C", 2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC", 9:"CM"}

romano = []
romano.append(unidades)
romano.append(dezenas)
romano.append(centenas)

print("Número Romano:",romano[2][cent] + romano[1][dez] + romano[0][uni])