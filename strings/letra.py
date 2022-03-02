# -*- coding:  utf-8 -*-
# identifica e imprime na tela a letra que mais se repete
palavra = str(input(''))
npal = str.lower(palavra)
lista = []
num = []
letras = []
for i in range (1, len(npal)+1):
    lista.append(npal[i-1:i])
for item in lista:
    qt = lista.count(item)
    num.append(qt)
    if qt == max(num):
        letras.append(item)
    
print('Letra que mais se repete:',letras[-1])