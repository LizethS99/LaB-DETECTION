from ultralytics import YOLO
import cv2
def clasificacion_imagen():
    img = "IMD004.bmp" 
    model = YOLO('C:/Users/USER/OneDrive/Documentos/GitHub/LaB-DETECTION/runs/runs/classify/train6/weights/best.pt')
    result = model.predict(img, imgsz = 640)
    boxes = result[0].plot()
    cv2.imshow("DETECCIÓN", boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

 
clasificacion_imagen()