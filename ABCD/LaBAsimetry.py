from PIL import ImageEnhance, Image
from pylab import *
import cv2
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu as otsu
from skimage import io, morphology, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt

factor_contraste = 3.5
#Contraste con PILL
def contrasteImg(img, contrasteFact):
    ajustador_contraste = ImageEnhance.Contrast(img)
    imagen_contrastada = ajustador_contraste.enhance(contrasteFact)
    
    return imagen_contrastada
def suavizarImagen(image_cv):
    if len(image_cv.shape) == 3 and image_cv.shape[2] == 3:
        # Convert to grayscale
        image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Threshold the image to get a binary image
    # Here we use Otsu's binarization which automatically determines the threshold value
    _, binary_image_cv = cv2.threshold(image_cv, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Create a larger structuring element for more aggressive smoothing
    kernel_size = 3  # Increase the size for more smoothing
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))

    # Apply morphological opening with the larger kernel to remove more noise
    opened_image_cv = cv2.morphologyEx(binary_image_cv, cv2.MORPH_OPEN, kernel)
    opened_image_cv = cv2.cvtColor(opened_image_cv, cv2.COLOR_GRAY2BGR)
    return opened_image_cv

def rellenarMask(img):
    img = cv2.bitwise_not(img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    w,h = img.shape[:2]
    for i in range(1,w-1):
        for y in range(1,h-1):
            setPixel = 0
            if img[i,y]==255:
                if img[i+1,y]==0:
                    setPixel+=1
                if img[i-1,y]==0:
                    setPixel+=1
                if img[i,y+1]==0:
                    setPixel+=1
                if img[i,y-1]==0:
                    setPixel+=1
                if img[i+1,y-1]==0: 
                    setPixel+=1
                if img[i+1,y+1]==0: 
                    setPixel+=1
                if img[i-1,y-1]==0:
                    setPixel+=1
                if img[i-1,y+1]==0:
                    setPixel+=1
                if setPixel>4:
                    img[i,y]=0
                    setPixel=0
    for i in range(1,w-1):
        for y in range(1,h-1):
            setPixel = 0
            coordenates = []
            if img[i,y]==255:
                deltaI = i
                if img[i+1,y]==0:
                    setPixel+=1
                if img[i-1,y]==0:
                    setPixel+=1
                if img[i,y+1]==0:
                    setPixel+=1
                if img[i,y-1]==0:
                    setPixel+=1
                if img[i+1,y-1]==0: 
                    setPixel+=1
                if img[i+1,y+1]==0: 
                    setPixel+=1
                if img[i-1,y-1]==0:
                    setPixel+=1
                if img[i-1,y+1]==0:
                    setPixel+=1
                """coordenates.append(img[i+1,y-1])
                coordenates.append(img[i+1,y])
                coordenates.append(img[i+1,y+1])
                coordenates.append(img[i-1,y])
                coordenates.append(img[i-1,y+1])
                coordenates.append(img[i-1,y-1])
                coordenates.append(img[i,y+1])
                coordenates.append(img[i,y-1])
                coordenates.append(img[i+1,y])
                coordenates.append(img[i+1,y])"""

                if setPixel>4:
                    img[i,y]=0
                    setPixel=0
    img = cv2.erode(img,(4,4),iterations=10)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    cv2.imshow("Resultado",img)
    return img


def extraerLesion(image,file):
    image = contrasteImg(image, factor_contraste)
    img_arr = np.array(image)
    cvim = cv2.cvtColor(img_arr, cv2.COLOR_RGB2BGR)
    for i in range(5):
        cvim = cv2.GaussianBlur(cvim,(3,3),1)
    cvim = cv2.cvtColor(cvim, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("tmp.jpg",cvim)
    cv2.imshow("Gauss",cvim)
    newImg = imread('tmp.jpg')
    newImg = newImg/255
    U = otsu(newImg)+.1
    print(U)
    binary_nevus = newImg < U
    binary_nevus_cv2 = (binary_nevus * 255).astype(np.uint8)
    binary_nevus_cv2 = cv2.erode(binary_nevus_cv2,(4,4),iterations=8)
    binary_nevus_cv2 = cv2.dilate(binary_nevus_cv2,(4,4),iterations=14)
    imagen2 = cv2.imread(file)
    cv2.imwrite("mask.png",binary_nevus_cv2)
    imagen3 = cv2.imread("mask.png")
    imagen4=rellenarMask(imagen3)
    cv2.imshow("Antes de poda", imagen4)
    for i in range(3):
        imagen4=suavizarImagen(imagen4)
    cv2.imshow("Después de poda", imagen4)
    sub2 = cv2.bitwise_or(imagen4,imagen2)
    cv2.imwrite("Extract.png",sub2)
    #halfImage(cv2.bitwise_not(binary_nevus_cv2))
    imgEx = cv2.imread("Extract.png")
    extractColor(imgEx)
    

def extractColor(extract):
    extract2 = cv2.cvtColor(extract, cv2.COLOR_BGR2RGB)
    img_hsv=cv2.cvtColor(extract2,cv2.COLOR_RGB2HSV)
    light_brown_hue_range = (10, 30)
    dark_brown_hue_range = (0, 10)
    blue_gray_hue_range=(98,180)
    blue_gray_sat_range=(51,255)
    blue_gray_val_range=(194,255)
    blue_gray_mask=cv2.inRange(
        img_hsv, (blue_gray_hue_range[0],blue_gray_sat_range[0],blue_gray_val_range[0]),
        (blue_gray_hue_range[1],blue_gray_sat_range[1],blue_gray_val_range[1])
    )
    # Crear máscaras para cada rango de café
    light_brown_mask = cv2.inRange(img_hsv, (light_brown_hue_range[0], 50, 50), (light_brown_hue_range[1], 255, 255))
    dark_brown_mask = cv2.inRange(img_hsv, (dark_brown_hue_range[0], 50, 50), (dark_brown_hue_range[1], 255, 255))

    # Contamos los píxeles de cada máscara
    blue_gray_pixel = np.sum(blue_gray_mask > 0)
    light_brown_pixels = np.sum(light_brown_mask > 0)
    dark_brown_pixels = np.sum(dark_brown_mask > 0)

    # Visualizamos los resultados
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))

    axs[0].imshow(extract2)
    axs[0].set_title('Original Image')
    axs[0].axis('off')

    axs[1].imshow(light_brown_mask, cmap='gray')
    axs[1].set_title('Light Brown Mask')
    axs[1].axis('off')

    axs[2].imshow(dark_brown_mask, cmap='gray')
    axs[2].set_title('Dark Brown Mask')
    axs[2].axis('off')

    axs[3].imshow(blue_gray_mask, cmap='gray')
    axs[3].set_title('Blue-gray')
    axs[3].axis('off')

    plt.show()
    color_count = {
        'Cafe claro':light_brown_pixels,
        'Cafe oscuro':dark_brown_pixels,
        'Azul-gricesaceo':blue_gray_pixel,
    }
    print(color_count)

def halfImage(imagen):
    
    height,width = imagen.shape
    leftHalf = imagen[:,:width//2]
    rightHalf = imagen[:,width//2:]

    cv2.imshow('Left',leftHalf)
    cv2.imshow('Right',rightHalf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



    # Convertir la imagen al espacio de color LAB
    
file = "IMD078.png"
image = Image.open(file)
extraerLesion(image,file)