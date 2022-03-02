nome = input()
notas = []
while nome != '':
	nota1 = float(input())
	nota2 = float(input())
	media = (nota1 + nota2) / 2
	notas.append((media, nome))
	nome = input()
notas.sort(reverse=True)
for i in notas:
	print('%s - %.2f' % (i[1], i[0]))