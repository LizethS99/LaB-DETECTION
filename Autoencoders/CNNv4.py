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



class CNN(models.Model):
    def __init__(self):
        super(CNN,self).__init__()
        #Capas para codificar
        self.convolucional = tf.keras.Sequential([
            layers.Conv2D(8, (3,3), activation='elu', padding="same", strides=2,input_shape=(128,128,3)),
            BatchNormalization(),
            layers.MaxPooling2D(2,2),
            layers.Conv2D(16, (3,3), activation='elu', padding="same", strides=2),
            layers.MaxPooling2D(2,2),
            layers.Conv2D(32, (3,3), activation='elu', padding="same", strides=2),
            layers.MaxPooling2D(2,2),
            #layers.Conv2D(64, (3,3), activation='elu', padding="same", strides=2),
            #layers.MaxPooling2D(2,2),
            layers.Flatten(),
            layers.Dense(32,activation='elu'), #Usamos relu o elu
            layers.Dense(16,activation='elu'),
            layers.Dense(8,activation='elu'),
            Dropout(0.5),
            layers.Dense(3,activation='softmax')
        ])
    
    def call(self,x):
        return self.convolucional(x)
    
def loadImages(carpeta):
    images = []
    for file in os.listdir(carpeta):
        img = Image.open(os.path.join(carpeta,file))
        img = img.resize((128,128))
        img_array = np.array(img)
        images.append(img_array)
    return np.array(images)

def loadDirectoryClass(carpeta,op):
    if op==1:
        tipo = "training"
    else:
        tipo = "validation"
    datasetClass = image_dataset_from_directory(
        directory=carpeta,
        validation_split=0.2,
        subset=tipo,
        seed=123,
        image_size=(128,128),
        color_mode="rgb",
        batch_size=16
    )
    return datasetClass

"""dataset = loadImages("./PH2")

dataset = dataset.astype('float32')/255.0

x_train,x_test = train_test_split(dataset, test_size=0.2)

train_dataset = tf.data.Dataset.from_tensor_slices(x_train).batch(16)
test_dataset = tf.data.Dataset.from_tensor_slices(x_test).batch(16)"""

train_dataset = loadDirectoryClass("PH2CNN",1)
normalization_layer = layers.experimental.preprocessing.Rescaling(1./255)
train_dataset = train_dataset.map(lambda x,y: (normalization_layer(x),y))
val_dataset = loadDirectoryClass("PH2CNN",2)
val_dataset = val_dataset.map(lambda x,y: (normalization_layer(x),y))
    
#------------Early Stopping---------------
early_stopping = EarlyStopping(
    monitor = "val_loss",
    patience=30,
    verbose=1,
    min_delta=0.001,
    mode='auto',
    baseline=None,
    restore_best_weights=True
)
#-----------------------------------------

#---------------------CNN......................................................................................
Convolutional = CNN()
Convolutional.compile(optimizer='adam', loss="sparse_categorical_crossentropy")
history = Convolutional.fit(train_dataset, epochs=100,validation_data=val_dataset, callbacks=[early_stopping])
Convolutional.save("LaB-CNN", save_format='tf')
#---------------------------------------------------------------------------------------------------------------

#---------------Ver resultados------------------------
plt.figure(figsize=(8,4))
plt.plot(history.history['loss'],label='Pérdida de entrenamiento')
if 'val_loss' in history.history:
    plt.plot(history.history['val_loss'], label='Pérdida de Validación')
plt.title('Pérdida Durante el Entrenamiento')
plt.xlabel('Epochs')
plt.ylabel('Pérdida')
plt.legend()
plt.show()

# Gráfico para la precisión, si está disponible
if 'accuracy' in history.history:
    plt.figure(figsize=(8, 4))
    plt.plot(history.history['accuracy'], label='Precisión de Entrenamiento')
    if 'val_accuracy' in history.history:
        plt.plot(history.history['val_accuracy'], label='Precisión de Validación')
    plt.title('Precisión Durante el Entrenamiento')
    plt.xlabel('Epochs')
    plt.ylabel('Precisión')
    plt.legend()
    plt.show()

#-----------------------------------------------------