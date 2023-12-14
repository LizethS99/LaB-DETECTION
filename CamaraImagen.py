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
from claseCentrar import centerScreen

def Camara_Imagen():
    color = '#003F79' # color menú lateral
    color2 = '#001E6F' #Azul muy oscuro
    color3 = '#48F0FA' #Azul muy claro
    color4 = '#E8FBFC' #Letras en los botones
    color5 = '#0D2764'
    centro = centerScreen()
    # Inicializar el modelo YOLO
    global model, video, app_camera, img, fondo,captura, capturaR, contCap, capturaCamera, tomarVideo, label_inst
    model = YOLO('./runsSegmentation/train8/weights/best.pt')

    # Inicializar la cámara
    video = cv2.VideoCapture(0)
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green
    # Crear una ventana de Tkinter
    app_camera = customtkinter.CTk()
    app_camera.iconbitmap("Images\logo.ico")
    app_camera.title("Capturar Imagen")
    app_camera.geometry(centro.situarLaB(700,600))
    img = PhotoImage(file="./images/fondoCaptura.png")
    fondo = Label(app_camera, image=img)
    fondo.place(x=0, y=0)
    Label(app_camera, text="Presione espacio para captura",bg="#050c2d", fg="white", font=("DaunPenh",15)).place(x=210, y=30)
    captura = []
    capturaR = []
    contCap = 0
    capturaCamera = PhotoImage(None)
    tomarVideo=True

    # Crear un lienzo para mostrar la imagen
    canvas = Canvas(app_camera, width=640, height=480)
    canvas.place(x=30, y=70)
    instructions = f"Tome {4-contCap} imágenes"
    label_inst=Label(app_camera, text=instructions,bg="#050c2d", fg="white", font=("DaunPenh",15)).place(x=270, y=555)
    # Capturar un solo fotograma
    def capturar_fotograma():
        global captura, contCap, capturaR, label_inst
        ret, frame = video.read()
        resultado = model.predict(frame,imgsz=640,conf=0.5)
        boxes = resultado[0].plot()
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        img2 = Image.fromarray(cv2.cvtColor(boxes, cv2.COLOR_BGR2RGB))
        img2 = img2.resize((200,154))
        img_tk = ImageTk.PhotoImage(image=img)
        img_tk2 = ImageTk.PhotoImage(image=img2)
        
        # Mostrar la foto en una nueva ventana de Tkinter
        # Guardar el fotograma capturado en la variable
        captura.append(img_tk)
        capturaR.append(img_tk2)
        contCap += 1
        if contCap == 4:
            video.release()
            ventana_seleccion()
    def cancelarCaptura(app):
        global contCap, tomarVideo, captura, capturaR,video
        capturaR=[]
        captura=[]
        contCap=0
        tomarVideo=True
        video = cv2.VideoCapture(0)
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
        app_camera.destroy()
        
        global Gfile
        file = "\image_select.bmp"
        Gfile = os.path.dirname(__file__)+file
        nextStep = confirmar.confirmar_imagen(Gfile)
    def ventana_seleccion():
        global captura, img, capturaR, tomarVideo
        tomarVideo=False
        video.release()
        ventana_foto = Toplevel(app_camera)
        ventana_foto.geometry(centro.situarLaB(700,600))
        ventana_foto.iconbitmap("Images\logo.ico")
        fondo2 = Label(ventana_foto, image=img)
        fondo2.place(x=0, y=0)
        Label(ventana_foto, image=capturaR[0]).place(x=150, y=70)
        customtkinter.CTkButton(master=ventana_foto, text="Imagen 1", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:bestPhoto(captura[0],ventana_foto)).place(relx=0.36, rely=0.41, anchor= tkinter.CENTER)
        Label(ventana_foto, image=capturaR[1]).place(x=400, y=70)
        customtkinter.CTkButton(master=ventana_foto, text="Imagen 2", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:bestPhoto(captura[1],ventana_foto)).place(relx=0.7, rely=0.41, anchor= tkinter.CENTER)
        Label(ventana_foto, image=capturaR[2]).place(x=150, y=310)
        customtkinter.CTkButton(master=ventana_foto, text="Imagen 3", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:bestPhoto(captura[2],ventana_foto)).place(relx=0.36, rely=0.81, anchor= tkinter.CENTER)
        Label(ventana_foto, image=capturaR[3]).place(x=400, y=310)
        customtkinter.CTkButton(master=ventana_foto, text="Imagen 4", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:bestPhoto(captura[3],ventana_foto)).place(relx=0.7, rely=0.81, anchor= tkinter.CENTER)
        customtkinter.CTkButton(master=ventana_foto, text="Nuevas Capturas", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=5, command=lambda:cancelarCaptura(ventana_foto)).place(relx=0.55, rely=0.95, anchor= tkinter.CENTER)
        strLabel = str(type(captura[0]))
        Label(ventana_foto, text="Seleccione la mejor captura",bg="#050c2d", fg="white", font=("DaunPenh",15)).place(x=240, y=30)
    

    # Enlazar la función capturar_fotograma a la tecla "Espacio"
    app_camera.bind('<space>', lambda event: capturar_fotograma())

    # Función para actualizar el fotograma en el lienzo
    def update_frame():
        if tomarVideo == True:
            ret, frame = video.read()

            # Realizar predicción con YOLO
            """resultado = model.predict(frame, imgsz=640, conf=0.3)
            boxes = resultado[0].plot()"""

            # Convertir la imagen de OpenCV a formato compatible con Tkinter
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img_tk = ImageTk.PhotoImage(image=img)

            # Mostrar la imagen en el lienzo
            canvas.create_image(0, 0, anchor=NW, image=img_tk)
            canvas.img_tk = img_tk

            # Llamar a esta función cada 10 milisegundos para actualizar la imagen
            canvas.after(1, update_frame)

        # Llamar a la función para actualizar la imagen
    update_frame()

    # Iniciar el bucle principal de Tkinter
    app_camera.mainloop()

    # Liberar la cámara
    video.release()

    #return app_camera

if __name__ == "__main__":
    # Llama a la función principal si se ejecuta este script directamente
    Camara_Imagen()