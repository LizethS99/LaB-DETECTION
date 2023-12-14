import cv2
import numpy as np
import time 

model = cv2.ddn.readNet("yolov3-tiny.weights","yolo3-tiny.cfg")
classes = []
with open("coco.names","r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = model.getLayerNames()
output_layers = [layer_names[i[0]-1] for i in model.getUnconnectedOutLayers()]
colors = np.random.uniform(0,255,size=(len(classes),3))

camera = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
starting_time = time.time()
frame_id = 0
while True:
    _, frame = camera.read()
    frame_id += 1
    height, width, channels = frame.shape
    while True:
        _, frame = camera.read()
        frame_id +=1
        height, width, channels = frame.shape
        #deteccion de objetos 
