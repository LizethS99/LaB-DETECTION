import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, ttk, scrolledtext, filedialog, messagebox
import os
import numpy as np
import cv2
import Resultados
#from keras.models import load_model


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green

color = '#003F79' # color menú lateral
color2 = '#122E60' #Azul muy oscuro
color3 = '#48F0FA' #Azul muy claro
color4 = '#E8FBFC' #Letras en los botones
color5 = '#0D2764'
color6 = '#2E6FAC'

app3 = customtkinter.CTk()
app3.geometry('1200x700+250+110') #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
app3.minsize(1100,700)
app3.maxsize(1400, 700)
app3.config(bg=color5)
ruta = 'Images\Segundologo.png'
ruta2 = 'Images\\fondo.png'
app3.title('LaB-DETECTION Historial')
imagen_logo2 = Image.open(ruta)
ntam = (400, 180)
imagen_redim = imagen_logo2.resize(ntam)
imagen_logo = ImageTk.PhotoImage(imagen_redim)
app3.iconbitmap("Images\logo.ico")
fondo = PhotoImage(file=ruta2)
lbl_fondo = CTkLabel(app3, image=fondo, text='').place(x=0, y=0)



def menu():
    f1 = Frame(app3, width=150, height=900, bg=color)
    f1.place(x=0, y=0)
    def Botones(x,y,text,bcolor,fcolor):
        def on_enter(e):
            mybutton1['background'] = bcolor
            mybutton1['foreground'] = fcolor
        def on_leave(e):
            mybutton1['background'] = fcolor
            mybutton1['foreground'] = bcolor
        mybutton1 = Button(f1, width=22, height=2, text=text, fg=bcolor, border=2, bg=fcolor, activebackground=bcolor, activeforeground=fcolor, command=None)
        mybutton1.bind("<Enter>", on_enter)
        mybutton1.bind("<Leave>", on_leave)
        mybutton1.place(x=x, y=y)
    Botones(0, 50, 'Acerca de', color4,color2)
    Botones(0, 90, 'Cáncer de piel', color4,color2)
    Botones(0, 130, 'Redes neuronales', color4,color2)
    Botones(0, 170, 'Nuevo análisis', color4,color2)
    Botones(0, 210, 'Salir', color4,color2)

    def dele():
        f1.destroy()
    global img2
    imagen = Image.open('Images\close.png')
    nuevo_tam = (30, 30)
    imagen_nueva = imagen.resize(nuevo_tam)
    img2 = ImageTk.PhotoImage(imagen_nueva)
    Button(f1, image=img2, command=dele, border=0, activebackground=color, bg=color, cursor="hand2").place(x=5, y=10)

frame = Frame(app3, width=80, height=900, bg=color)
frame.place(x=0, y=0)
imagen2 = Image.open('Images\open.png')
nuevo_tam2 = (35, 35)
imagen_nueva2 = imagen2.resize(nuevo_tam2)
img1 = ImageTk.PhotoImage(imagen_nueva2)
Button(app3, image=img1, border=0, activebackground=color, bg=color, command=menu, cursor="hand2").place(x=15, y=15)

def default_home():
    #tam = (70,30)
    #nimg = imagen_logo.resize(tam)
    label = CTkLabel(app3, image=imagen_logo, fg_color="#00042A", text='')
    label.pack()
    label.place(relx=0.067, rely=0)

default_home()

def Captura_Imagen():
    print("Push Button")

def Seleccionar_Imagen():
    print("Push Button")
    """file_path = filedialog.askopenfilename()
    global file
    file = file_path
    print(file_path)"""

    confirmar_imagen()

def confirmar_imagen():
    ventana_confirmar = CTk()
    ventana_confirmar.geometry('700x500+400+210') #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
    ventana_confirmar.config(bg=color5)
    ventana_confirmar.title('Confirmar')
    
    lbl_text= Label(ventana_confirmar, text= "¿Esta es la imagen que desea análizar?", background=color5, fg='white', font= ("Helvetica", 20)).place(x=100, y=30)

    # Mostrar previsualización de imagen
    #label_imagen = Label(ventana_confirmar, bg="white", width=50, height=20)
    #label_imagen.place(relx=0.25, rely=0.17)

    
    # Mostrar previsualización de imagen
    imagen_tk = None
    nfile = 'E:/TT2/gato.jpeg'
    imagen = Image.open(nfile)
    nueva_imagen_tk = PhotoImage(nfile)

    new_label = Label(ventana_confirmar, width=300, height=250, image=nueva_imagen_tk)
    new_label.place(relx=0.5, rely=0.17)
    """canvas_imagen_confir.config(width=300, height=250)
    canvas_imagen_confir.create_image(0, 0, anchor=tkinter.NW, image=nueva_imagen_tk)
    canvas_imagen_confir.image = nueva_imagen_tk

    if file:
        imagen = Image.open(file)
        canvas_imagen_confir.configure(bg="red")
        n_imagen = imagen.resize((300, 250), resample=Image.Resampling.LANCZOS)
        nueva_imagen_tk = ImageTk.PhotoImage(n_imagen)
        canvas_imagen_confir.config(width=300, height=250)
        canvas_imagen_confir.create_image(0, 0, anchor=tkinter.NW, image=imagen_tk)
        canvas_imagen_confir.image = nueva_imagen_tk
        imagen_tk = nueva_imagen_tk
    imagen_tk = None"""

    """def cargar_imagen(imagen_tk):
            
            if file:
                imagen = Image.open(file)
                imagen_res = imagen.resize((50, 20), resample=Image.Resampling.LANCZOS)
                nueva_imagen_tk = ImageTk.PhotoImage(imagen_res)
                label_imagen.config(width=50, height=20, image=imagen_tk)
                label_imagen.image = imagen_tk
                imagen_tk = nueva_imagen_tk
    cargar_imagen(imagen_tk)"""

    def NImage():
        print("Push Button")
        ventana_confirmar.destroy()

    def Continuar():
        print("Push Button")
        texto = "Espere un momento, los resultados se están obteniendo."    
        messagebox.showinfo("Cargando...", texto)
        ventana_confirmar.destroy()
        def Pantalla(screen):
            screen.destroy()
            #pantallanueva = Resultados.Res(file)
        Pantalla(app3) 

    button_nuevo = CTkButton(master=ventana_confirmar, text="Nueva Imagen", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=lambda:NImage())
    button_nuevo.place(relx=0.28, rely=0.88, anchor= tkinter.CENTER) 

    button_continuar = CTkButton(master=ventana_confirmar, text="Continuar", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=lambda:Continuar())
    button_continuar.place(relx=0.78, rely=0.88, anchor= tkinter.CENTER) 
    
    ventana_confirmar.mainloop()




imagen_camara = Image.open('Images\camara-2.png')
ntam_camara = (190, 215)
imagen_redim_camara = imagen_camara.resize(ntam_camara)
img_camara = ImageTk.PhotoImage(imagen_redim_camara)
labelButton = CTkLabel(app3, image=img_camara, text='', bg_color="#00042A")
labelButton.pack()
labelButton.place(relx=0.3, rely=0.35)
button = customtkinter.CTkButton(master=app3, text="Capturar Imagen", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=Captura_Imagen)
button.place(relx=0.38, rely=0.7, anchor= tkinter.CENTER) 

############################################################
lbl = Label(text='', fg="white", background="#00042a")
lbl.place(relx=0.48, rely=0.8) 

imagen_galeria = Image.open('Images\galeria.png')
ntam_galeria = (180, 205)
imagen_redim_galeria = imagen_galeria.resize(ntam_galeria)
img_galeria = ImageTk.PhotoImage(imagen_redim_galeria)
labelButton = CTkLabel(app3, image=img_galeria, text='', bg_color="#00042A")
labelButton.pack()
labelButton.place(relx=0.6, rely=0.35)
button = customtkinter.CTkButton(master=app3, text="Seleccionar Imagen", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=lambda:Seleccionar_Imagen())
button.place(relx=0.68, rely=0.7, anchor= tkinter.CENTER) 

    

app3.mainloop()

    #return app3