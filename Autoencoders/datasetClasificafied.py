#Creación de autoencoder para clasificación de imagenes, empezamos con el dataset
#Primero probamos PH2 sin data aumentation

from PIL import Image
import numpy as np
import os 
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras import layers, models 
from keras.preprocessing import image_dataset_from_directory
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
from keras.layers import Dropout, BatchNormalization
import cv2 

image = Image.open("./PH2Class/Melanoma/IMD063_19.bmp")
image.show()
image = image.resize((128,128))
img_array = np.array(image)
img_array = img_array.astype('float32')/255.0
if img_array.ndim==2:
    img_array=np.stack((img_array)*3,axis=-1)
elif img_array.shape[2]==1:
    img_array = np.repeat(img_array,3,axis=-1)
img_array=np.expand_dims(img_array,axis=0)
autoencoder=tf.keras.models.load_model('./autoencoder')

cnn=tf.keras.models.load_model('./LaB-CNN')

code = autoencoder.predict(img_array)

result = cnn.predict(code)
classify = []
classes = ["Atipica","Comun","Melanoma"]
for i, val in np.ndenumerate(result):
    print(f"index: {i}, Valor: {val}")
    classify.append(val)
print(classes[classify.index(max(classify))])
plt.subplot(1,2,1)
plt.imshow(img_array[0])
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(code[0])
plt.title("Reconstrucción")
plt.axis("off")
plt.show()