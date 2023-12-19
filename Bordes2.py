from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

def bordes(path_image):
    # Cargar la imagen desde el archivo
    image_path = path_image
    image = Image.open(image_path)
    
    # Convertir la imagen a escala de grises para el análisis de bordes
    gray_image = image.convert("L")
    
    # Preparar el gráfico para mostrar la imagen con las líneas de división de segmentos
    plt.figure(figsize=(8, 8))
    
    # Mostrar la imagen original
    plt.imshow(image, cmap='gray')
    
    # Calcular el centro de la imagen
    width, height = image.size
    center_x, center_y = width // 2, height // 2
    
    # Dibujar las líneas para dividir la imagen en 8 segmentos
    # Línea horizontal y vertical para dividir en cuadrantes
    plt.axline((center_x, 0), (center_x, height), color="red", linewidth=2)
    plt.axline((0, center_y), (width, center_y), color="red", linewidth=2)
    
    # Líneas diagonales para dividir los cuadrantes en segmentos
    plt.axline((center_x, center_y), (width, 0), color="red", linewidth=2)
    plt.axline((center_x, center_y), (0, 0), color="red", linewidth=2)
    plt.axline((center_x, center_y), (0, height), color="red", linewidth=2)
    plt.axline((center_x, center_y), (width, height), color="red", linewidth=2)
    
    # Eliminar ejes para una mejor visualización
    plt.axis('off')
    
    # Guardar la imagen con las líneas de división
    output_path = 'image_with_segments.png'
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    
    # Mostrar el gráfico
    plt.show()
    
    # Devolver la ruta del archivo para acceder desde el sistema de archivos
    output_path
    
    # Convertir la imagen a un arreglo de numpy y aplicar escala de grises
    image_np = np.array(gray_image, dtype=np.uint8)
    
    # Aplicar el detector de bordes de Canny
    edges = cv2.Canny(image_np, 100, 200)
    """edges_sobel_x = cv2.Sobel(image_np, cv2.CV_64F, 1, 0, ksize=3)
    edges_sobel_y = cv2.Sobel(image_np, cv2.CV_64F, 0, 1, ksize=3)
    edges = np.sqrt(edges_sobel_x**2 + edges_sobel_y**2)"""


    
    # Función para calcular la puntuación de un segmento
    def calculate_segment_score(segment, min_edge_pixels=800):
        # Detectar los bordes en el segmento utilizando Canny
        edges_segment = cv2.Canny(segment, 100, 200)
        total_edge_pixels = np.sum(edges_segment > 0)
        # Calcular la puntuación como la presencia de bordes (valor > 0)
        score = 1 if total_edge_pixels >= min_edge_pixels else 0
        return score
    
    # Dividir la imagen en 8 segmentos y calcular la puntuación para cada uno
    segment_scores = np.zeros(8, dtype=int)
    height_segment = edges.shape[0] // 2
    width_segment = edges.shape[1] // 2
    
    # Coordenadas de los segmentos en sentido horario, comenzando desde la esquina superior derecha
    segments_coords = [
        (0, width_segment, center_y, width),  # Superior derecho
        (center_y, width_segment, height, width),  # Inferior derecho
        (center_y, 0, height, width_segment),  # Inferior izquierdo
        (0, 0, center_y, width_segment),  # Superior izquierdo
        # Diagonales - se toman triángulos aproximados para simplificar
        (0, center_x, center_y, width),  # Superior derecho diagonal
        (center_y, center_x, height, width),  # Inferior derecho diagonal
        (center_y, 0, height, center_x),  # Inferior izquierdo diagonal
        (0, 0, center_y, center_x),  # Superior izquierdo diagonal
    ]
    
    # Calcular la puntuación para cada segmento
    for i, (y_start, x_start, y_end, x_end) in enumerate(segments_coords):
        segment_edges = edges[y_start:y_end, x_start:x_end]
        segment_scores[i] = calculate_segment_score(segment_edges)
    
    # Calcular la puntuación total
    total_score = np.sum(segment_scores)
    return total_score

    
    
    