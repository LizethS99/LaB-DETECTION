import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, ttk, scrolledtext, filedialog
import os
from keras.models import load_model

def PantallaImagen():
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
    app3.title('LaB-DETECTION Historial')
    imagen_logo2 = Image.open('Images\Segundologo.png')
    ntam = (400, 180)
    imagen_redim = imagen_logo2.resize(ntam)
    imagen_logo = ImageTk.PhotoImage(imagen_redim)
    app3.iconbitmap("Images\logo.ico")
    fondo = PhotoImage(file='Images\\fondo.png')
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

    def Seleccionar_Imagen(label):
        #melanoma_model = load_model('Melanoma_model\MelanomaModelV1.h5')
        print("Push Button")
        file_path = filedialog.askopenfilename()
        print(file_path)
        label.configure(text=file_path)


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
    lbl = Label(text='', fg="white", background=color)
    lbl.place(relx=0.48, rely=0.8) 
    imagen_galeria = Image.open('Images\galeria.png')
    ntam_galeria = (180, 205)
    imagen_redim_galeria = imagen_galeria.resize(ntam_galeria)
    img_galeria = ImageTk.PhotoImage(imagen_redim_galeria)
    labelButton = CTkLabel(app3, image=img_galeria, text='', bg_color="#00042A")
    labelButton.pack()
    labelButton.place(relx=0.6, rely=0.35)
    button = customtkinter.CTkButton(master=app3, text="Seleccionar Imagen", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=lambda:Seleccionar_Imagen(lbl))
    button.place(relx=0.68, rely=0.7, anchor= tkinter.CENTER) 

     

    app3.mainloop()

PantallaImagen()