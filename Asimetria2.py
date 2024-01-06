import cv2
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
    if asimetria_forma_horizontal > umbral_forma or asimetria_forma_vertical > umbral_forma:
        puntuacion += 1
    if asimetria_estructuras_horizontal > umbral_estructuras or asimetria_estructuras_vertical > umbral_estructuras:
        puntuacion += 1

    # Mostrar las regiones
    plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(region1, cv2.COLOR_BGR2RGB)), plt.title('Región 1'), plt.axis('off')
    plt.subplot(2, 2, 2), plt.imshow(cv2.cvtColor(region2, cv2.COLOR_BGR2RGB)), plt.title('Región 2'), plt.axis('off')
    plt.subplot(2, 2, 3), plt.imshow(cv2.cvtColor(region3, cv2.COLOR_BGR2RGB)), plt.title('Región 3'), plt.axis('off')
    plt.subplot(2, 2, 4), plt.imshow(cv2.cvtColor(region4, cv2.COLOR_BGR2RGB)), plt.title('Región 4'), plt.axis('off')
    plt.savefig("asimetry_analysis.png", bbox_inches='tight', pad_inches=0)

    #plt.show()
    return puntuacion

# Cargar la imagen
imagen = cv2.imread('Extract.png')  # Reemplaza 'tu_imagen.jpg' con la ruta de tu imagen
if imagen is None:
        print("No se pudo cargar la imagen.")
        exit()

    # Obtener las dimensiones de la imagen
alto, ancho = imagen.shape[:2]

# Dividir en dos ejes de 90 grados (horizontal y vertical)
mitad_horizontal = alto // 2
mitad_vertical = ancho // 2

# Verificar que la imagen se haya cargado correctamente
def main():
    
    # Calcular la puntuación de asimetría
    puntuacion_asimetria = calcular_asimetria(imagen)

    # Imprimir la puntuación
    return puntuacion_asimetria
