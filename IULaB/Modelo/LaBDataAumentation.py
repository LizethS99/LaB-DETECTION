import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image, ImageEnhance
import os, random, cv2
import matplotlib.pyplot as plt


#imagen = Image.open('./Data/train/images/IMD002.png')

# Ajustar el contraste (cambiar el factor según sea necesario)
factor_contraste = 1.5
#Contraste con PILL
def contrasteImg(img, contrasteFact):
    ajustador_contraste = ImageEnhance.Contrast(imagen)
    imagen_contrastada = ajustador_contraste.enhance(contrasteFact)
    return imagen_contrastada

def ruido(imagenMain, porcentaje):

    numPixeles=imagenMain.size[0]*imagenMain.size[1]
    img_res = imagenMain
    pixels=(numPixeles*porcentaje)//800
    if imagenMain.mode=='RGB':
        dato_minimo=(0, 0, 0)
        dato_maximo=(255, 255, 255)
 
    elif imagenMain.mode=='L':
        dato_minimo=0
        dato_maximo=255
 
    #pixeles blancos
    for x in range(pixels):
 
        coordenada_x=random.randrange(2, img_res.width-2)
        coordenada_y=random.randrange(2, img_res.height-2)
 
        img_res.putpixel((coordenada_x, coordenada_y), dato_maximo)
        img_res.putpixel((coordenada_x+1, coordenada_y), dato_maximo)
        img_res.putpixel((coordenada_x, coordenada_y+1), dato_maximo)
        img_res.putpixel((coordenada_x+1, coordenada_y+1), dato_maximo)
 
    #pixeles negros
    for x in range(pixels):
 
        coordenada_x=random.randrange(2, img_res.width-2)
        coordenada_y=random.randrange(2, img_res.height-2)
 
        img_res.putpixel((coordenada_x, coordenada_y), dato_minimo)
        img_res.putpixel((coordenada_x+1, coordenada_y), dato_minimo)
        img_res.putpixel((coordenada_x, coordenada_y+1), dato_minimo)
        img_res.putpixel((coordenada_x+1, coordenada_y+1), dato_minimo)
    return img_res
    
def dataAumentation(imagen,path,file,aux):
    global contImag
    plusAumentation = 1.0
    for i in range(4):
        contImag+=1
        plusAumentation+=0.5
        img2 = contrasteImg(imagen,plusAumentation)
        img2.save(path+"NewAumentation/"+file[:len(file)-4]+"_"+str(contImag)+file[6:])
    for i in range(4):
        contImag+=1
        img2=ruido(imagen,i+1)
        img2.save(path+"NewAumentation/"+file[:len(file)-4]+"_"+str(contImag)+file[6:])
    
    cv_image = np.array(aux)
    cv_image = cv_image[:,:,::-1].copy()
    cv2.imshow("Blur",cv_image)
    for i in range(8):
        cv_image=cv2.blur(cv_image,(3,3))
        if i%2==1:
            contImag+=1
            #cv2.imshow(f"Iteracion: {i+1}",cv_image)
            cv2.imwrite(path+"NewAumentation/"+file[:len(file)-4]+"_"+str(contImag)+file[6:],cv_image)

images=[]
for img in os.listdir('C:/Users/brandon.bravo-ext/OneDrive - Eutelsat SA/Desktop/ESCOM/PruebasAu'): #Ruta del proyecto: ./Images/Dataset/train/Melanoma/
    if img.endswith('.bmp'):
        
        contImag=0
        imagen = Image.open('C:/Users/brandon.bravo-ext/OneDrive - Eutelsat SA/Desktop/ESCOM/PruebasAu/'+img)
        cv_file = cv2.imread('C:/Users/brandon.bravo-ext/OneDrive - Eutelsat SA/Desktop/ESCOM/PruebasAu/'+img)
        inv1 = cv2.flip(cv_file,0)
        inv1 = cv2.cvtColor(inv1,cv2.COLOR_BGR2RGB)
        inv2 = cv2.flip(cv_file,1)        
        inv2 = cv2.cvtColor(inv2,cv2.COLOR_BGR2RGB)
        inv3 = cv2.flip(cv_file,-1)
        inv3 = cv2.cvtColor(inv3,cv2.COLOR_BGR2RGB)
        inv1 = Image.fromarray(inv1)
        inv2 = Image.fromarray(inv2)
        inv3 = Image.fromarray(inv3)
        images.append(imagen)
        images.append(imagen.transpose(Image.ROTATE_270))
        images.append(imagen.transpose(Image.ROTATE_90))
        images.append(inv1)
        images.append(inv2)
        images.append(inv3)
        #imagen.save("C:/Users/brandon.bravo-ext/OneDrive - Eutelsat SA/Desktop/ESCOM/NewAumentation/"+img) #Ruta de guardado en el proyecto: ./Images/Dataset/train/MelanomaAumentation/
        
        for i in images:
            i.save("C:/Users/brandon.bravo-ext/OneDrive - Eutelsat SA/Desktop/ESCOM/NewAumentation/"+img[:len(img)-4]+"_"+str(contImag)+img[6:])
            dataAumentation(i,'C:/Users/brandon.bravo-ext/OneDrive - Eutelsat SA/Desktop/ESCOM/',img, i)
            contImag+=1

cv2.waitKey()

        