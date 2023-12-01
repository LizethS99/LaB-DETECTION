from screeninfo import get_monitors
import tkinter as tk
from math import cos, sin, radians
import threading
import time
from PIL import Image, ImageTk
import customtkinter 
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel

colors = ["#00f9c4", "#00ff00", "#ff1844", "#100b79", "#50e910", "#ffb250"]

class PantallaCarga:
    def situarLaB(self, AnchoLaB, AltoLaB):
        monitors = get_monitors()
        halfSx, halfSy = monitors[0].width, monitors[0].height
        Lx = AnchoLaB
        Ly = AltoLaB

        x = halfSx/2 - AnchoLaB/2
        y = halfSy/2 - AltoLaB/2

        return f"{AnchoLaB}x{AltoLaB}+{int(x)}+{int(y)}" #700x500
    
    def __init__(self, texto):
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green
        global image, photo
        self.root = customtkinter.CTk()
        #self.root.overrideredirect(1)
        self.root.attributes('-toolwindow',-3)
        self.root.title("Pantalla de Carga")
        self.root.geometry(self.situarLaB(300,235))
        self.root.iconbitmap("Images\logo.ico")

        # Cargar la imagen de fondo
        image = Image.open("./Images/fondoCarga.png")
        photo = ImageTk.PhotoImage(image)
        # Crear un widget Canvas para la animación y establecer la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=300, height=235, bg="#000c5d")
        self.canvas.create_image(0, 0, anchor="nw", image=photo)
        self.canvas.pack()
        self.label=tk.Label(self.canvas, text=texto,font=("Arial",15), fg="white",bg="#000c5d", highlightcolor="yellow1").place(x=70, y=194)
        
        # Variables para la animación
        self.radio_circunferencia = 80
        self.radio_circulo_pequeno = 7
        self.centro_x, self.centro_y = 150, 100

        # Variable para indicar si la carga ha finalizado
        self.carga_completa = False

        # Simular la carga en un hilo
        self.hilo_carga = threading.Thread(target=self.simular_carga)
        self.hilo_carga.start()

        # Configurar la función de cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.root.mainloop()
    
    

    def simular_carga(self):
        changeColors = 0
        for i in range(36):
            if changeColors > 5:
                changeColors = 0
            angulo = i * 10
            x = self.centro_x + self.radio_circunferencia * cos(radians(angulo))
            y = self.centro_y + self.radio_circunferencia * sin(radians(angulo))
            self.canvas.create_oval(x - self.radio_circulo_pequeno, y - self.radio_circulo_pequeno,
                                     x + self.radio_circulo_pequeno, y + self.radio_circulo_pequeno, fill=colors[changeColors], outline="cyan")
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

# Crear la aplicación

for i in range(2):
    screen = PantallaCarga("Iniciando Cámara...")
# Aquí puedes continuar con el código principal de tu aplicación después de que la carga ha terminado
print("Proceso de carga completado. Continuar con el resto del código.")