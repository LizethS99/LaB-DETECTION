import pandas as pd 
import tensorflow as tf
from keras.layers import Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam,RMSprop
from keras.callbacks import EarlyStopping
import time 
labelsTrain_df = pd.read_excel("PH2_Train.xlsx")
labelsEvaluate_df = pd.read_excel("PH2_Evaluate.xlsx")

image_generator = ImageDataGenerator(rescale=1./255, validation_split=0.2)

pathTrain="./MelanomaTrain"
pathEvaluate ="./MelanomaEvaluate"
dataTrain_generator = image_generator.flow_from_directory(
    directory="C:/Users/Brandon Bravo/Desktop/RedNeuronalMelanoma/DataAumentation/Dataset",
    
)


"""LOOK!
    LABELS: COMMON NEVUS: [0,1,0] ATYPICAL NEVUS: [1,0,0] MELANOMA: [0,0,1]"""
modelMelanoma = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(8, (3,3), activation='elu', padding="same", input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(16, (3,3), activation='elu', padding="same"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3,3), activation='elu', padding="same"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='elu', padding="same"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32,activation='elu'), #Usamos relu o elu 
    tf.keras.layers.Dense(16,activation='elu'),
    tf.keras.layers.Dense(8,activation='elu'),
    Dropout(0.5),
    tf.keras.layers.Dense(3,activation='softmax')
])
inicio = time.time()
modelMelanoma.compile(optimizer=Adam(learning_rate=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
modelMelanoma.summary()
early_stop = EarlyStopping(monitor="val_loss", mode='min', min_delta=0.01,verbose=1, patience=15, restore_best_weights=True)
modelMelanoma.fit(dataTrain_generator,epochs=50, batch_size=32, validation_data=dataEvaluate_generator, callbacks=[early_stop])
test_loss,test_acc = modelMelanoma.evaluate(dataTrain_generator)
test_loss2,test_acc2 = modelMelanoma.evaluate(dataEvaluate_generator)

fin = time.time()
print("Time: "+str(int((fin-inicio)/60))+":"+str(int((fin-inicio)%60)))
tf.saved_model.save(modelMelanoma,"modeloMelanoma")
print(test_acc, test_acc2)
