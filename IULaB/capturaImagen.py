from tkinter import *
from PIL import Image, ImageTk
from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Inicializar el modelo YOLO
model = YOLO('./runs/segment/train8/weights/best.pt')

# Inicializar la cámara
video = cv2.VideoCapture(0)

# Crear una ventana de Tkinter
root = Tk()
root.title("Capturar Imagen")
root.geometry("700x600")
img = PhotoImage(file="./fondoCaptura.png")
fondo = Label(root, image=img)
fondo.place(x=0, y=0)
Label(root, text="Presione espacio para captura",bg="#050c2d", fg="white", font=("DaunPenh",15)).place(x=210, y=30)
captura = []
capturaR = []
contCap = 0
capturaCamera = PhotoImage(None)
tomarVideo=True

# Crear un lienzo para mostrar la imagen
canvas = Canvas(root, width=640, height=480)
canvas.place(x=30, y=70)
Label(root, text="Tome 4 imágenes",bg="#050c2d", fg="white", font=("DaunPenh",15)).place(x=270, y=555)
# Capturar un solo fotograma
def capturar_fotograma():
    global captura, contCap, capturaR
    ret, frame = video.read()

    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    img2 = img.resize((200,154))
    img_tk = ImageTk.PhotoImage(image=img)
    img_tk2 = ImageTk.PhotoImage(image=img2)
    # Mostrar la foto en una nueva ventana de Tkinter
    # Guardar el fotograma capturado en la variable
    captura.append(img_tk)
    capturaR.append(img_tk2)
    contCap += 1
    if contCap == 4:
        ventana_seleccion()

def ventana_seleccion():
    global captura, img, capturaR, tomarVideo
    tomarVideo=False
    ventana_foto = Toplevel(root)
    ventana_foto.geometry("700x600")
    fondo2 = Label(ventana_foto, image=img)
    fondo2.place(x=0, y=0)
    Label(ventana_foto, image=capturaR[0]).place(x=150, y=40)
    Button(ventana_foto, text="Seleccionar", command=lambda:bestPhoto(captura[0])).place(x=185,y=205)
    Label(ventana_foto, image=capturaR[1]).place(x=400, y=40)
    Button(ventana_foto, text="Seleccionar", command=lambda:bestPhoto(captura[1])).place(x=425,y=205)
    Label(ventana_foto, image=capturaR[2]).place(x=150, y=280)
    Button(ventana_foto, text="Seleccionar", command=lambda:bestPhoto(captura[2])).place(x=185,y=445)
    Label(ventana_foto, image=capturaR[3]).place(x=400, y=280)
    Button(ventana_foto, text="Seleccionar", command=lambda:bestPhoto(captura[3])).place(x=425,y=445)
    Button(ventana_foto, text="Nuevas capturas", command=lambda:cancelarCaptura(ventana_foto)).place(x=340,y=550)
    strLabel = str(type(captura[0]))
    Label(root, text="Seleccione la mejor captura",bg="#050c2d", fg="white", font=("DaunPenh",15)).place(x=210, y=30)
def cancelarCaptura(app):
    global contCap, tomarVideo, captura, capturaR
    capturaR=[]
    captura=[]
    contCap=0
    tomarVideo=True

    app.destroy()
    update_frame()
def bestPhoto(img):
    global capturaCamera
    capturaCamera = img

    """img1 = captura[0].subsample(200,154)
    img2 = captura[1].subsample(200,154)
    img3 = captura[2].subsample(200,154)
    img4 = captura[3].subsample(200,154)
    Label(ventana_foto,image=captura[0]).place(x=20,y=20)
    Label(ventana_foto,image=img2).place(x=240,y=20)
    Label(ventana_foto,image=img3).place(x=20,y=194)
    Label(ventana_foto,image=img4).place(x=240,y=194)
    lbl_confirm = Label(ventana_foto, text="¿Desea guardar estas capturas?", fg="black")
    lbl_confirm.place(x=100,y=650)"""

# Enlazar la función capturar_fotograma a la tecla "Espacio"
root.bind('<space>', lambda event: capturar_fotograma())

# Función para actualizar el fotograma en el lienzo
def update_frame():
    if tomarVideo == True:
        ret, frame = video.read()

        # Realizar predicción con YOLO
        resultado = model.predict(frame, imgsz=640, conf=0.3)
        boxes = resultado[0].plot()

        # Convertir la imagen de OpenCV a formato compatible con Tkinter
        img = Image.fromarray(cv2.cvtColor(boxes, cv2.COLOR_BGR2RGB))
        img_tk = ImageTk.PhotoImage(image=img)

        # Mostrar la imagen en el lienzo
        canvas.create_image(0, 0, anchor=NW, image=img_tk)
        canvas.img_tk = img_tk

        # Llamar a esta función cada 10 milisegundos para actualizar la imagen
        canvas.after(10, update_frame)

# Llamar a la función para actualizar la imagen
update_frame()

# Iniciar el bucle principal de Tkinter
root.mainloop()

# Liberar la cámara
video.release()
