# -*- coding:  utf-8 -*-

nome = input()
d = nome.rindex(' ')
s = nome[d+1:]
p = nome[0:d]
print ('%s, %s' % (s,p)) 
