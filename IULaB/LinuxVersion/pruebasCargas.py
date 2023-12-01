import concurrent.futures
import threading
import time
from tkinter import ttk
import tkinter as tk
from math import cos, sin, radians
from PIL import Image, ImageTk
import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from win32api import GetSystemMetrics
from ultralytics import YOLO
import cv2

colors = ["#00f9c4", "#00ff00", "#ff1844", "#100b79", "#50e910", "#ffb250"]

class PantallaCarga:
    def situarLaB(self, AnchoLaB, AltoLaB):
        halfSx, halfSy = GetSystemMetrics(0), GetSystemMetrics(1)

        x = halfSx/2 - AnchoLaB/2
        y = halfSy/2 - AltoLaB/2

        return f"{AnchoLaB}x{AltoLaB}+{int(x)}+{int(y)}"  # 700x500

    def __init__(self, texto):
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        global image, photo
        self.root = customtkinter.CTk()
        self.root.title(texto)
        self.root.geometry(self.situarLaB(300, 235))
        #self.root.iconbitmap("Images\logo.ico")

        # Cargar la imagen de fondo
        image = Image.open("./Images/fondoCarga.png")
        photo = ImageTk.PhotoImage(image)
        # Crear un widget Canvas para la animación y establecer la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=300, height=235, bg="#000c5d")
        self.canvas.create_image(0, 0, anchor="nw", image=photo)
        self.canvas.pack()
        self.label = tk.Label(self.canvas, text=texto, font=("Arial", 15), fg="white", bg="#000c5d",
                              highlightcolor="yellow1").place(x=70, y=194)

        # Variables para la animación
        self.radio_circunferencia = 80
        self.radio_circulo_pequeno = 7
        self.centro_x, self.centro_y = 150, 100

        # Variable para indicar si la carga ha finalizado
        self.carga_completa = False

        # Configurar la función de cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        self.simular_carga()
        self.root.mainloop()
        # Ejecutar la tarea en segundo plano
        

        print("Procesos han terminado.")

    def simular_carga(self):
        changeColors = 0
        chLoading = 0
        for i in range(36):
            if changeColors > 5:
                changeColors = 0
            angulo = i * 10
            x = self.centro_x + self.radio_circunferencia * cos(radians(angulo))
            y = self.centro_y + self.radio_circunferencia * sin(radians(angulo))
            self.canvas.create_oval(x - self.radio_circulo_pequeno, y - self.radio_circulo_pequeno,
                                     x + self.radio_circulo_pequeno, y + self.radio_circulo_pequeno,
                                     fill=colors[changeColors], outline="cyan")
            self.root.update()
            time.sleep(0.1)
            changeColors += 1

        # Indicar que la carga ha finalizado
        self.carga_completa = True

        # Cerrar la ventana de carga después de un breve retraso
        self.root.after(1000, self.cerrar_ventana)

    def cerrar_ventana(self):
        # Verificar si la carga ha finalizado antes de cerrar la ventana
        if not self.carga_completa:
            print("Espera a que el proceso de carga termine.")
        else:
            self.root.destroy()

def imprimir():
    print("Hola")
screen = PantallaCarga("Hola",imprimir)
