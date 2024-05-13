import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as skl
from skimage.io import imread

x = np.arange(-1000, 1000, 2)
"""
#y = x**2

# Relação dos dados
# plt.plot(x, y)

# Mostrar grafico
plt.show()
"""

# Configurando o tamanho da figura
figura = plt.figure(figsize=(5, 5))

###############################################################

# Grafico 1
y1 = x**2

#Sub Plot
plt.subplot(2, 2, 1)
# Separado por (2 Linhas, 2 Colunas, No 1° Quadrante)

# Plot
plt.plot(x, y1)

##############################################################

# Grafico 2
y2 = x**3

#Sub Plot
plt.subplot(2, 2, 2)

# Plot
plt.plot(x, y2)

##############################################################

# Grafico 3
y3 = x+82

#Sub Plot
plt.subplot(2, 2, 3)

# Plot
plt.plot(x, y3)

##############################################################

# Grafico 4
y4 = -x**3

#Sub Plot
plt.subplot(2, 2, 4)

# Plot
plt.plot(x, y4)

##############################################################

# Carregar imagem para os Gráficos
imagem1 = imread('https://dynamic-media-cdn.tripadvisor.com/media/photo-o/03/8c/0f/a3/playa-paraiso.jpg?w=1200&h=1200&s=1')
plt.imshow(imagem1)

##############################################################

# Endereço de Imagens Salvas
enderecoUrl = 'C:/Users/vinic/OneDrive/Área de Trabalho/Python/TESTE EVOLUE/imag/'
imagens = []

# For para pegar cada imagem e guardar no array 'imagens'
for i in range(5):
    imagem = imread(enderecoUrl+'imagem'+str(i+1)+'.jpg')
    imagens.append(imagem)

# Configurando tamanho das imagens
figuras1 = plt.figure(figsize=(5, 8))

# Configurando as linhas e as colunas atraves do For
for i in range(5):
    figuras1.add_subplot(3, 2, i+1)
    plt.imshow(imagens[i])

##############################################################

# Mostrar grafico
plt.show()

