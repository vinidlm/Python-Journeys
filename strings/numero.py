#le uma sequencia de numeros até que -1 seja digitado e após imprime na tela 
#o numero com maior ocorrencia

d = {}
numero = int(input())
while numero != -1:
	d[numero] = d.get(numero, 0) + 1
	numero = int(input())

numeros = []
for k, v in d.items():
    numeros.append((v, k))
numeros.sort(reverse=True)
for item in numeros:
	print(item[1])
	break