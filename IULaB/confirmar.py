import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, ttk, scrolledtext, filedialog, messagebox
import os
import numpy as np
import cv2
import CapturarImagen
import crearpdf
def confirmar_imagen(nfile):
    color3 = '#48F0FA'
    color5 = '#0D2764'
    ventana_confirmar = CTk()
    ventana_confirmar.geometry('700x500+400+210') #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
    ventana_confirmar.config(bg=color5)
    ventana_confirmar.title('Confirmar')
    
    lbl_text= Label(ventana_confirmar, text= "¿Esta es la imagen que desea análizar?", background=color5, fg='white', font= ("Helvetica", 20)).place(x=100, y=30)

    # Mostrar previsualización de imagen
    #label_imagen = Label(ventana_confirmar, bg="white", width=50, height=20)
    #label_imagen.place(relx=0.25, rely=0.17)

    
    # Mostrar previsualización de imagen
    #global nfile
    #nfile = 'E:/TT2/gato.jpeg'
    def Previ():
         # Mostrar previsualización de imagen
        canvas_imagen = tkinter.Canvas(ventana_confirmar, bg="white", width=300, height=250)
        canvas_imagen.place(relx=0.27, rely=0.25)

        def cargar_imagen():
            imagen_path = nfile
            if imagen_path:
                imagen = Image.open(imagen_path)
                imagen = imagen.resize((300, 250), resample=Image.Resampling.LANCZOS)
                imagen_tk = ImageTk.PhotoImage(imagen)
                canvas_imagen.config(width=300, height=250)
                canvas_imagen.create_image(0, 0, anchor=tkinter.NW, image=imagen_tk)
                canvas_imagen.image = imagen_tk
        cargar_imagen()
    Previ()
    def NImage():
        print("Push Button")
        ventana_confirmar.destroy()
        nuevo_analisis = CapturarImagen.capturar()

    def Continuar():
        print("Push Button")
        ventana_confirmar.destroy()
        #clasific = clasificacion.clasificacion_imagen()
        file_path = ".\Resultados_LaB_DETECTION.pdf"
        generar_pdf = crearpdf.crear_pdf(file_path, nfile)

    button_nuevo = CTkButton(master=ventana_confirmar, text="Nueva Imagen", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=lambda:NImage())
    button_nuevo.place(relx=0.28, rely=0.88, anchor= tkinter.CENTER) 

    button_continuar = CTkButton(master=ventana_confirmar, text="Continuar", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=lambda:Continuar())
    button_continuar.place(relx=0.78, rely=0.88, anchor= tkinter.CENTER) 
    
    ventana_confirmar.mainloop()
    return ventana_confirmar
#nfile = 'E:/TT2/gato.jpeg'
#confirmar_imagen(nfile)