import requests
from PIL import Image
import numpy as np
from IPython.display import display

URL_imagem = 'https://as2.ftcdn.net/v2/jpg/04/38/99/23/1000_F_438992315_tPBkKloXvfQ2bPzcmZ3pgTBlIbo4fEmP.jpg'

# Realiza a leitura da imagem retornado-a na forma de matriz de inteiros
def le_imagem(imagem_URL):
    file_name = 'sample_image.jpg'
    response = requests.get(imagem_URL, allow_redirects=True)
    file = open(file_name, "wb")
    file.write(response.content)
    file.close()

    I = Image.open(file_name).copy()
    imagem_matriz = np.array(I, dtype=np.uint8)
    return imagem_matriz

# Exibe a matriz de inteiros na forma de imagem
def imprime_imagem(imagem_matriz):
    I = Image.fromarray(imagem_matriz)
    display(I)

# Execução 
img_matriz = le_imagem(URL_imagem) # img_matriz é a imagem como uma matriz de inteiros
imprime_imagem(img_matriz) # Exibe a imagem na tela
print('\nDimensões da imagem: {}'.format(img_matriz.shape))

def converte_bin(txt):
  if type(txt) == str:
    return ''.join([format(ord(i), "08b") for i in txt])
  elif type(txt) == bytes or type(txt) == np.ndarray:
    return [format(i, "08b") for i in txt]

def codificador(mensagem, img_matriz):

  #separador de palavras
  mensagem += "$$"

  data_index = 0
  #converte a mensagem em código binário
  codificada_bin = converte_bin(mensagem)

#acha o tamanho da mensagem a ser encondida
  tam_mensagem = len(codificada_bin)
  for val in img_matriz: 
      for pixel in val:
          #converte rgb para binário
          r, g, b = converte_bin(pixel)
          #modifica o ultimo bit
          if data_index < tam_mensagem:
              #esconde no pixel vermelho
              pixel[0] = int(r[:-1] + codificada_bin[data_index], 2)
              data_index += 1
          if data_index < tam_mensagem:
              #esconde no pixel verde
              pixel[1] = int(g[:-1] + codificada_bin[data_index], 2)
              data_index += 1
          if data_index < tam_mensagem:
              #esconde no pixel azul 
              pixel[2] = int(b[:-1] + codificada_bin[data_index], 2)
              data_index += 1
          #para o processo após codificar
          if data_index >= tam_mensagem:
              break

mensagem = "The moon is cool."
img_matriz_codificada = img_matriz.copy() # Vamos fazer uma cópia da imagem original

#Codificando a mensagem na imagem
codificador(mensagem, img_matriz_codificada)

# Imprimindo imagem codificada para comparação
print('Imagem codificada:\n')
imprime_imagem(img_matriz_codificada)

def decodificador(img_matriz):

  binario = ""
  for val in img_matriz:
      for pixel in val:
        #converte os valores dos pixels para binario
          r, g, b = converte_bin(pixel) 
          #extrai info do pixel vermelho
          binario += r[-1] 
          #extrai info do pixel verde
          binario += g[-1] 
          #extrai info do pixel azul
          binario += b[-1] 
  #divide em 8-bits
  dividido = [binario[i: i+8] for i in range(0, len(binario), 8) ]
  #converte bits para letras/num
  decodificado = ""
  for b in dividido:
      decodificado += chr(int(b, 2))
      #verifica se chegamos ao separador
      if decodificado[-2:] == "$$": 
          break
  #tira o separador para mostrar a mensagem original
  return decodificado[:-2]

mensagem_decodificada = decodificador(img_matriz_codificada)

# Imprimindo mensagem original
print('Mensagem original:', mensagem)
# Imprimindo mensagem extraída da imagem
print('Mensagem extraída:', mensagem_decodificada)