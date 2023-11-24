from ultralytics import YOLO
import cv2
import os

model = YOLO('./runs/classify/train6/weights/best.pt')
comun=0
atipyc=0

#PRUEBAS con imagenes
for img in os.listdir('C:/Users/Brandon Bravo/Desktop/RedNeuronalMelanoma/Data/train/images/'):
    image = cv2.imread('C:/Users/Brandon Bravo/Desktop/RedNeuronalMelanoma/Data/train/images/'+img)
    resultado = model.predict(image, imgsz=640, conf = 0.3)
    boxes = resultado[0].plot()
    cv2.imshow("Deteccion",boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""if 'Commons' in str(resultado):
        comun+=1
    elif 'Atypicals' in str(resultado):
        atipyc+=1
print("Atypical".ljust(10)+str(atipyc))
print("Comun".ljust(10)+str(comun))
print("Perdida".ljust(10)+str((25-atipyc-comun)))""" 

#Pruebas con video
"""video = cv2.VideoCapture(0)

while True:

    ret, frame = video.read()
    resultado = model.predict(frame, imgsz=640, conf = 0.3)
    boxes = resultado[0].plot()
    cv2.imshow("Detection and segmentation", boxes)

    if cv2.waitKey(1) == 27:
        break
video.release()
cv2.destroyAllWindows()"""