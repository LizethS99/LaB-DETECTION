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




class AutoEncoderCNN(models.Model):
    def __init__(self):
        super(AutoEncoderCNN,self).__init__()
        #Capas para codificar
        self.encoder = tf.keras.Sequential([
            layers.Input(shape=(128,128,3)),
            layers.Conv2D(32,(3,3),activation='relu',padding='same',strides=2),
            layers.Conv2D(16,(3,3),activation='relu',padding='same',strides=2),
            layers.Conv2D(8,(3,3),activation='relu',padding='same',strides=2)
        ])
        self.decoder = tf.keras.Sequential([
            layers.Conv2DTranspose(8, kernel_size=3,strides=2,activation='relu', padding='same'),
            layers.Conv2DTranspose(16, kernel_size=3, strides=2,activation='relu',padding='same'),
            layers.Conv2DTranspose(32, kernel_size=3, strides=2,activation='relu',padding='same'),
            layers.Conv2D(3,kernel_size=(3,3), activation='sigmoid', padding='same',)
        ])
    
    def call(self,x):
        encode = self.encoder(x)
        decode = self.decoder(encode)
        return decode
    
def loadImages(carpeta):
    images = []
    for file in os.listdir(carpeta):
        img = Image.open(os.path.join(carpeta,file))
        img = img.resize((128,128))
        img_array = np.array(img)
        images.append(img_array)
    return np.array(images)



dataset = loadImages("./PH2Extend")

dataset = dataset.astype('float32')/255.0

x_train,x_test = train_test_split(dataset, test_size=0.2)

train_dataset = tf.data.Dataset.from_tensor_slices(x_train).batch(16)
test_dataset = tf.data.Dataset.from_tensor_slices(x_test).batch(16)
    
autoencoder = AutoEncoderCNN()
autoencoder.compile(optimizer='adam', loss="mean_squared_error")

autoencoder.fit(x_train,x_train, epochs=25,shuffle=True,validation_data=(x_test,x_test))
autoencoder.save("autoencoder", save_format='tf')

#Los predicts regresan valores tipo np.array
decoded_imgs = autoencoder.predict(x_test)

n = 10
plt.figure(figsize=(20,4))
for i in range(n):
    ax = plt.subplot(2,n,i+1)
    plt.imshow(x_test[i].reshape(128,128,3))
    plt.axis('off')

    ax = plt.subplot(2,n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(128,128,3))
    plt.axis('off')
plt.show()