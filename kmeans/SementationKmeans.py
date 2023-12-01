import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image, ImageEnhance
import os

#imagen = Image.open('./Data/train/images/IMD002.png')

# Ajustar el contraste (cambiar el factor según sea necesario)
factor_contraste = 1.5
def contrasteImg(img):
    print(factor_contraste)
    ajustador_contraste = ImageEnhance.Contrast(imagen)
    imagen_contrastada = ajustador_contraste.enhance(factor_contraste)
    imagen_contrastada.show()
    return imagen_contrastada
imagen = Image.open("IMD004.bmp")
imagen2 = contrasteImg(imagen)


 
# Mostrar la imagen original y la imagen con contraste





"""I1 = imagen_contrastada.convert('L')
I2 = np.asarray(I1,dtype=np.float64)


X = I2.reshape((-1, 1))
k_means = KMeans(n_clusters=2, algorithm="elkan")
k_means.fit(X)

centroides = k_means.cluster_centers_
etiquetas = k_means.labels_
I2_compressed = np.choose(etiquetas, centroides)
I2_compressed.shape = I2.shape

plt.figure(figsize=(8,8))
plt.imshow(I2_compressed,cmap='gray')
plt.axis('off')
plt.show()
I2 = (I2_compressed-np.min(I2_compressed))/(np.max(I2_compressed)-np.min(I2_compressed))*255
I2 = Image.fromarray(I2.astype(np.uint8))
w, h =I2.size
colors = I2.getcolors(w * h)
print (colors)
print (u'Área = ',  float(210000)*float(colors[0][0])/float(w*h), 'km2')"""