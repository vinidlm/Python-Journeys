# -*- coding:  utf-8 -*-

def criptografar(mensagem, chave):
    Mi, Mf, mi, mf = ord('A'), ord('Z'), ord('a'), ord('z')

    nova_mensagem = ""
    for letra in mensagem:
        crp = ord(letra)
        '''
        caso crp+chave seja menor que Mf (número de Z) então se pode prosseguir normalmente
        caso crp+chave for maior que Mf então precisamos calcular o resto desse número com Mf+1 e somar com Mi (numero de A)
        para que possamos retornar ao ciclo de letras
        assim, para letra maiusculas temos que:
        '''
        if Mi <= crp <= Mf:
            if (crp+chave) <= Mf: 
                nletra = chr(crp+chave)
            else:
                nletra = chr((crp+chave)%(Mf+1) + Mi)
            nova_mensagem = nova_mensagem + nletra
        #para minusculas a mesma lógica se aplica
        elif mi <= crp <= mf:
            if (crp+chave) <= mf:
               nletra = chr(crp+chave)
            else:
                nletra = chr((crp+chave)%(mf+1) + mi)
            nova_mensagem = nova_mensagem + nletra
        #para não-letras:
        else:
            nova_mensagem = nova_mensagem + letra
    #exibe a mensagem critografada:
    return nova_mensagem



palavra = input('Digite uma palavra:')
chave = int(input('Digite o valor da chave:'))
cripto = criptografar(palavra,chave)
print("Resultado: %s" % cripto)
