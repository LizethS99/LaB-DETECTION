from tkinter import *
import tkinter
from PIL import Image, ImageTk
from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt
import confirmar
import os 
import customtkinter 

def Camara_Imagen():
    color = '#003F79' # color menú lateral
    color2 = '#001E6F' #Azul muy oscuro
    color3 = '#48F0FA' #Azul muy claro
    color4 = '#E8FBFC' #Letras en los botones
    color5 = '#0D2764'
    # Inicializar el modelo YOLO
    global model, video, root, img, fondo,captura, capturaR, contCap, capturaCamera, tomarVideo 
    model = YOLO('./runsSegmentation/train8/weights/best.pt')

    # Inicializar la cámara
    video = cv2.VideoCapture(0)
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green
    # Crear una ventana de Tkinter
    root = customtkinter.CTk()
    root.title("Capturar Imagen")
    root.geometry("700x600")
    img = PhotoImage(file="./images/fondoCaptura.png")
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
    def cancelarCaptura(app):
        global contCap, tomarVideo, captura, capturaR
        capturaR=[]
        captura=[]
        contCap=0
        tomarVideo=True

        app.destroy()
        update_frame()
    def bestPhoto(img,app):
        global capturaCamera, captura, capturaR, contCap, tomarVideo
        capturaR=[]
        captura=[]
        contCap=0
        tomarVideo=True
        capturaCamera = img
        image_selec = ImageTk.getimage(img)
        #eliminar si ya existe
        image_selec.save("./IULaB/image_select.bmp")
        app.destroy()
        root.destroy()
        
        global Gfile
        file = "\image_select.bmp"
        Gfile = os.path.dirname(__file__)+file
        nextStep = confirmar.confirmar_imagen(Gfile)
    def ventana_seleccion():
        global captura, img, capturaR, tomarVideo
        tomarVideo=False
        ventana_foto = Toplevel(root)
        ventana_foto.geometry("700x600")
        fondo2 = Label(ventana_foto, image=img)
        fondo2.place(x=0, y=0)
        Label(ventana_foto, image=capturaR[0]).place(x=150, y=40)
        customtkinter.CTkButton(master=ventana_foto, text="Imagen 1", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:bestPhoto(captura[0],ventana_foto)).place(relx=0.36, rely=0.375, anchor= tkinter.CENTER)
        Label(ventana_foto, image=capturaR[1]).place(x=400, y=40)
        customtkinter.CTkButton(master=ventana_foto, text="Imagen 2", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:bestPhoto(captura[1],ventana_foto)).place(relx=0.7, rely=0.375, anchor= tkinter.CENTER)
        Label(ventana_foto, image=capturaR[2]).place(x=150, y=280)
        customtkinter.CTkButton(master=ventana_foto, text="Imagen 3", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:bestPhoto(captura[2],ventana_foto)).place(relx=0.36, rely=0.77, anchor= tkinter.CENTER)
        Label(ventana_foto, image=capturaR[3]).place(x=400, y=280)
        customtkinter.CTkButton(master=ventana_foto, text="Imagen 4", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:bestPhoto(captura[3],ventana_foto)).place(relx=0.7, rely=0.77, anchor= tkinter.CENTER)
        customtkinter.CTkButton(master=ventana_foto, text="Nuevas Capturas", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:cancelarCaptura(ventana_foto)).place(relx=0.55, rely=0.93, anchor= tkinter.CENTER)
        strLabel = str(type(captura[0]))
        Label(root, text="Seleccione la mejor captura",bg="#050c2d", fg="white", font=("DaunPenh",15)).place(x=210, y=30)
    

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

    #return root

if __name__ == "__main__":
    # Llama a la función principal si se ejecuta este script directamente
    Camara_Imagen()