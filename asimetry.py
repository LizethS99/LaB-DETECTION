import cv2
import numpy as np

image = cv2.imread("IMD004.bmp")
flip_1 = cv2.flip(image,0)

cv2.imshow("original Image", image)
cv2.imshow("Rotated Image", flip_1)
cv2.waitKey(0)
cv2.destroyAllWindows()