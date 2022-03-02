# -*- coding:  utf-8 -*-

palavra = input('')
d = {}
for c in palavra:
	if c in "aeiou":
		d[c] = d.get(c, 0) + 1

letras = []
for k, v in d.items():
    letras.append((v, k))
letras.sort(reverse=True)
for item in letras:
	print(item[1])
	break