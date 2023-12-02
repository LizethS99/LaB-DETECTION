import cv2
import numpy as np
from PIL import Image

image = Image.open("IMD004.bmp")
flip_1 =image.transpose(Image.ROTATE_270) 

image.show("original Image")
flip_1.show("Rotated Image")