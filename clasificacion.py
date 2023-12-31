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
from keras.utils import plot_model
import time

#autoencoder=tf.keras.models.load_model('C:/Users/yeraldi.sanchez/OneDrive - Netlogistik/Documents/LaB-DETECTION/Modelo/autoencoder')
if os.path.exists("RutaKeras.txt"):
            # Leer las rutas desde el archivo
            with open("RutaKeras.txt", "r") as archivo:
                lineas = archivo.readlines()
            
            # Asegurarse de que hay al menos dos líneas en el archivo
            if len(lineas) >= 2:
                # Eliminar posibles espacios en blanco al principio y al final de cada línea
                ruta_autoencoder = lineas[0].strip()
                ruta_cnn = lineas[1].strip()

                # Cargar modelos Keras desde las rutas
                autoencoder = tf.keras.models.load_model(ruta_autoencoder)
                cnn = tf.keras.models.load_model(ruta_cnn)

#autoencoder=tf.keras.models.load_model('./Modelo/autoencoder_LaBCNN')
#cnn=tf.keras.models.load_model('./Modelo/LaB-CNN-fn')
def clasificacion_imagen(img):
    classify=[]
    classes = ["Atipica","Comun","Melanoma"]
    code = autoencoder.predict(img)
    result = cnn.predict(code)
    for i, val in np.ndenumerate(result):
        classify.append(val)
    classfy = "Imagen clasificada como: "+classes[classify.index(max(classify))]
    print(classfy)
    
    

image = Image.open("./IMD004.bmp")
image = image.resize((128,128))
img_array = np.array(image)
img_array = img_array.astype('float32')/255.0
if img_array.ndim==2:
    img_array=np.stack((img_array)*3,axis=-1)
elif img_array.shape[2]==1:
    img_array = np.repeat(img_array,3,axis=-1)
img_array=np.expand_dims(img_array,axis=0)


clasificacion_imagen(img_array)
