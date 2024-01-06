from PIL import ImageEnhance, Image
from pylab import *
import cv2
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu as otsu
from skimage import io, morphology, exposure
import numpy as np
import matplotlib.pyplot as plt



def calcular_asimetria(imagen):
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Calcular el perfil de intensidad horizontal y vertical
    perfil_horizontal = np.sum(gris, axis=1)
    perfil_vertical = np.sum(gris, axis=0)

    # Asegurarse de que las regiones tengan la misma forma
    region1 = imagen[:mitad_horizontal, :mitad_vertical, :]
    region2 = imagen[:mitad_horizontal, -mitad_vertical:, :]
    region3 = imagen[-mitad_horizontal:, :mitad_vertical, :]
    region4 = imagen[-mitad_horizontal:, -mitad_vertical:, :]

    # Calcular la asimetría en color
    asimetria_color = np.mean(np.abs(region1 - region2))

    # Calcular la asimetría en forma (perfil de intensidad)
    asimetria_forma_horizontal = np.mean(np.abs(perfil_horizontal[:mitad_horizontal] - perfil_horizontal[-mitad_horizontal:]))
    asimetria_forma_vertical = np.mean(np.abs(perfil_vertical[:mitad_vertical] - perfil_vertical[-mitad_vertical:]))

    # Calcular la asimetría en estructuras (usando Canny como ejemplo)
    bordes_horizontal = cv2.Canny(gris[:mitad_horizontal, :], 50, 150)
    bordes_vertical = cv2.Canny(gris[:, :mitad_vertical], 50, 150)
    asimetria_estructuras_horizontal = np.mean(bordes_horizontal)
    asimetria_estructuras_vertical = np.mean(bordes_vertical)

    # Definir umbrales para cada métrica
    umbral_color = 150  # Si hay pequeñas variaciones pueden depender de la luz, por lo que es mejor tener un rango intermedio
    umbral_forma = 500  # Este nivel es adecuado para tener un balance entre la detectar asimetrías que realmente no sean tan pequeñas
    umbral_estructuras = 200  # Detección de bordes que son más evidentes en una imagen

    # Calcular puntuación total
    puntuacion = 0
    if asimetria_color > umbral_color:
        puntuacion += 1
        print("En color")
    if asimetria_forma_horizontal > umbral_forma or asimetria_forma_vertical > umbral_forma:
        puntuacion += 1
        print("En forma")
    if asimetria_estructuras_horizontal > umbral_estructuras or asimetria_estructuras_vertical > umbral_estructuras:
        puntuacion += 1
        print("En Estuctura")

    # Mostrar las regiones
    plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(region1, cv2.COLOR_BGR2RGB)), plt.title('Región 1'), plt.axis('off')
    plt.subplot(2, 2, 2), plt.imshow(cv2.cvtColor(region2, cv2.COLOR_BGR2RGB)), plt.title('Región 2'), plt.axis('off')
    plt.subplot(2, 2, 3), plt.imshow(cv2.cvtColor(region3, cv2.COLOR_BGR2RGB)), plt.title('Región 3'), plt.axis('off')
    plt.subplot(2, 2, 4), plt.imshow(cv2.cvtColor(region4, cv2.COLOR_BGR2RGB)), plt.title('Región 4'), plt.axis('off')

    plt.show()
    return puntuacion

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
    #cv2.imshow("Resultado",img)
    return img
def mayorPixel(img):
    y = img.shape[0]
    x = img.shape[1]
    valores=[]
    for i in range(y):
        for j in range(x):
            if img[i,j] not in valores:
                valores.append(img[i,j])
    valores.sort()
    return valores[len(valores)-1]

def extraerLesion(image,file):
    image = contrasteImg(image, factor_contraste)
    img_gray = image.convert('L')
    #img_gray.save("tmp.jpg")
    imagen_np = np.array(img_gray)
    imagen_cv2 = cv2.cvtColor(imagen_np, cv2.COLOR_RGB2BGR)
    for i in range(8):
        imagen_cv2 = cv2.GaussianBlur(imagen_cv2, (5, 5), sigmaX=0, sigmaY=0)
    cv2.imwrite("tmp.jpg",imagen_cv2)
    
    newImg = imread('tmp.jpg')
    newImg = np.mean(newImg, axis=2)
    newImg = newImg/255
    U = otsu(newImg)
    binary_nevus = newImg < U
    binary_nevus_cv2 = (binary_nevus * 255).astype(np.uint8)
    binary_nevus_cv2 = cv2.erode(binary_nevus_cv2,(4,4),iterations=6)
    binary_nevus_cv2 = cv2.dilate(binary_nevus_cv2,(4,4),iterations=14)
    imagen2 = cv2.imread(file)
    cv2.imwrite("mask.png",binary_nevus_cv2)
    imagen3 = cv2.imread("mask.png")
    
    sub2 = cv2.bitwise_or(cv2.bitwise_not(imagen3),imagen2)
    sub3 = cv2.bitwise_or(imagen2,imagen3)
    cv2.imwrite("Extract.png",sub2)
    
    puntaje=[]
    num = extractColor(imagen2)
    import Asimetria2
    import Bordes2
    
    puntaje.append(Asimetria2.main())
    puntaje.append(Bordes2.main())
    puntaje.append(num)
    return puntaje
    
    

def extractColor(extract):
    extract2 = cv2.cvtColor(extract, cv2.COLOR_BGR2RGB)
    img_hsv=cv2.cvtColor(extract2,cv2.COLOR_RGB2HSV)
    light_brown_hue_range = (8, 13)
    light_brown_sat_range = (135, 199)
    light_brown_val_range = (148, 204)

    dark_brown_hue_range = (0, 12)
    dark_brown_sat_range = (56, 146)
    dark_brown_val_range = (79, 145)

    blue_gray_hue_range=(111,170)
    blue_gray_sat_range=(10,66)
    blue_gray_val_range=(102,189)
    
    black_hue_range = (0,180)
    black_sat_range = (0,255)
    black_val_range = (0,50)
    
    white_hue_range = (0,180)
    white_sat_range = (0,20)
    white_val_range = (200,255)

    red_hue_range=(0,175)
    red_sat_range=(100,255)
    red_val_range=(20,255)

    red_mask=cv2.inRange(
        img_hsv, (red_hue_range[0],red_sat_range[0],red_val_range[0]),
        (red_hue_range[1],red_sat_range[1],red_val_range[1])
    )
    blue_gray_mask=cv2.inRange(
        img_hsv, (blue_gray_hue_range[0],blue_gray_sat_range[0],blue_gray_val_range[0]),
        (blue_gray_hue_range[1],blue_gray_sat_range[1],blue_gray_val_range[1])
    )
    # Crear máscaras para cada rango de café
    light_brown_mask = cv2.inRange(img_hsv, (light_brown_hue_range[0],light_brown_sat_range[0],light_brown_val_range[0]),
        (light_brown_hue_range[1],light_brown_sat_range[1],light_brown_val_range[1])
    )
    dark_brown_mask = cv2.inRange(img_hsv, (dark_brown_hue_range[0],dark_brown_sat_range[0],dark_brown_val_range[0]),
        (dark_brown_hue_range[1],dark_brown_sat_range[1],dark_brown_val_range[1])
    )
    black_mask=cv2.inRange(
        img_hsv, (black_hue_range[0],black_sat_range[0],black_val_range[0]),
        (black_hue_range[1],black_sat_range[1],black_val_range[1])
    )
    white_mask=cv2.inRange(
        img_hsv, (white_hue_range[0],white_sat_range[0],white_val_range[0]),
        (white_hue_range[1],white_sat_range[1],white_val_range[1])
    )
    # Contamos los píxeles de cada máscara
    red_mask_pixel = np.sum(red_mask > 0)
    blue_gray_pixel = np.sum(blue_gray_mask > 0)
    light_brown_pixels = np.sum(light_brown_mask > 0)
    dark_brown_pixels = np.sum(dark_brown_mask > 0)
    black_pixels = np.sum(black_mask > 0)
    white_pixels = np.sum(white_mask > 0)

    # Visualizamos los resultados
    import matplotlib.gridspec as gridspec

    # Crear una figura
    fig = plt.figure(figsize=(10, 5))

    # Configurar la disposición de los subplots
    gs = gridspec.GridSpec(2, 4)

    # Añadir la "Imagen Original" en el centro
    ax0 = fig.add_subplot(gs[:, 0])
    ax0.imshow(extract2)
    ax0.set_title('Imagen original')
    ax0.axis('off')

    # Configurar los otros subplots alrededor de la imagen central
    ax1 = fig.add_subplot(gs[0, 1])
    ax1.imshow(light_brown_mask, cmap='gray')
    ax1.set_title('Café claro')
    ax1.axis('off')

    ax2 = fig.add_subplot(gs[0, 2])
    ax2.imshow(dark_brown_mask, cmap='gray')
    ax2.set_title('Café oscuro')
    ax2.axis('off')

    ax3 = fig.add_subplot(gs[0, 3])
    ax3.imshow(blue_gray_mask, cmap='gray')
    ax3.set_title('Azul-Gris')
    ax3.axis('off')

    ax4 = fig.add_subplot(gs[1, 1])
    ax4.imshow(red_mask, cmap='gray')
    ax4.set_title('Rojo')
    ax4.axis('off')
    
    ax5 = fig.add_subplot(gs[1, 2])
    ax5.imshow(black_mask, cmap='gray')
    ax5.set_title('Negro')
    ax5.axis('off')
    
    ax6 = fig.add_subplot(gs[1, 3])
    ax6.imshow(white_mask, cmap='gray')
    ax6.set_title('Blanco')
    ax6.axis('off')

    # Dejar los espacios restantes en blanco
    ax5 = fig.add_subplot(gs[1, 2])
    ax5.axis('off')
    ax6 = fig.add_subplot(gs[1, 3])
    ax6.axis('off')


    plt.savefig("color_analysis.png", bbox_inches='tight', pad_inches=0)
    #plt.show()
    color_count = {
        'Cafe claro':light_brown_pixels,
        'Cafe oscuro':dark_brown_pixels,
        'Azul-Gris':blue_gray_pixel,
        'Rojo':red_mask_pixel,
        'Negro':black_pixels,
        'Blanco': white_pixels,
        
    }
    suma=0
    for i in color_count.values():
        if i > 2000:
            suma+=1  
        
    return suma

def halfImage(imagen):
    
    height,width = imagen.shape
    leftHalf = imagen[:,:width//2]
    rightHalf = imagen[:,width//2:]

    cv2.imshow('Left',leftHalf)
    cv2.imshow('Right',rightHalf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



    # Convertir la imagen al espacio de color LAB
    
def main(file):
    image = Image.open(file)
    return extraerLesion(image,file)