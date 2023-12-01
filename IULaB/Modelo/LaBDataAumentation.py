import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image, ImageEnhance
import os


#imagen = Image.open('./Data/train/images/IMD002.png')

# Ajustar el contraste (cambiar el factor según sea necesario)
factor_contraste = 1.5

def contrasteImg(img, contrasteFact):
    ajustador_contraste = ImageEnhance.Contrast(imagen)
    imagen_contrastada = ajustador_contraste.enhance(contrasteFact)
    return imagen_contrastada

for img in os.listdir('./Images/Dataset/train/Melanoma/'):
    if img.endswith('.bmp'):
        contImag=0
        imagen = Image.open('./Images/Dataset/train/Melanoma/'+img)
        imagen.save("./Images/Dataset/train/MelanomaAumentation/"+img)
        plusAumentation = 1.0
        for i in range(4):
            contImag+=1
            plusAumentation+=0.5
            img2 = contrasteImg(imagen,plusAumentation)
            #print(img[:len(img)-4]+"_"+str(i)+img[6:])
            img2.save("./Images/Dataset/train/MelanomaAumentation/"+img[:len(img)-4]+"_"+str(contImag)+img[6:])
            
        