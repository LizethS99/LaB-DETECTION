import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, ttk, scrolledtext, messagebox
from tkinter import filedialog  as fd #Ventanas de dialogo
from tkinter import messagebox as mb
import os
import fitz  # PyMuPDF
from ultralytics import YOLO
from claseCentrar import centerScreen
import Forms 
import sys
import LaB_DETECTION
#from keras.models import load_model

def Res(file, pdf):
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green

    color = '#003F79' # color menú lateral
    color2 = '#122E60' #Azul muy oscuro
    color3 = '#48F0FA' #Azul muy claro
    color4 = '#E8FBFC' #Letras en los botones
    color5 = '#0D2764'
    color6 = '#2E6FAC'

    app5 = customtkinter.CTk()
    centro = centerScreen()
    app5.geometry(centro.situarLaB(1200,700)) #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
    app5.minsize(1100,700)
    app5.maxsize(1400, 700)
    app5.config(bg=color5)
    app5.title('LaB-DETECTION Historial')
    imagen_logo2 = Image.open('Images\Segundologo.png')
    ntam = (400, 180)
    imagen_redim = imagen_logo2.resize(ntam)
    imagen_logo = ImageTk.PhotoImage(imagen_redim)
    #app5.iconbitmap("Images\logo.ico")
    fondo = PhotoImage(file='Images\\fondo.png')
    lbl_fondo = CTkLabel(app5, image=fondo, text='').place(x=0, y=0)


    def menu():
        f1 = Frame(app5, width=150, height=900, bg=color)
        f1.place(x=0, y=0)
        def Botones(x,y,text,bcolor,fcolor, op, funcion):
            def on_enter(e):
                mybutton1['background'] = bcolor
                mybutton1['foreground'] = fcolor
            def on_leave(e):
                mybutton1['background'] = fcolor
                mybutton1['foreground'] = bcolor
            mybutton1 = Button(f1, width=22, height=2, text=text, fg=bcolor, border=2, bg=fcolor, activebackground=bcolor, activeforeground=fcolor, command=lambda: funcion(), cursor="hand2")
            if op ==1:
                mybutton1.configure(fg=bcolor)
                mybutton1.bind("<Enter>", on_enter)
                mybutton1.bind("<Leave>", on_leave)
            else:
                mybutton1.configure(fg="#595959", state="disabled")
            mybutton1.place(x=x, y=y)

        def salir():
            messagebox.showinfo("Salir", "Vuelva pronto")
            sys.exit(0)

        def NPantalla(screen):
            screen.destroy()
            nuevo_analisis = Forms.NewPantalla()

        def Home(screen):
            screen.destroy()
            pantalla_main = LaB_DETECTION.funcion_principal()
        
        Botones(0, 50, 'Acerca de', color4,color2, 1, None)
        Botones(0, 90, 'Cáncer de piel', color4,color2, 1, None)
        Botones(0, 130, 'Redes neuronales', color4,color2, 1, None)
        Botones(0, 170, 'Nuevo análisis', color4,color2, 1, lambda: NPantalla(app5))
        Botones(0, 210, 'Salir', color4,color2, 1, lambda: salir())
        Botones(0, 250, 'Inicio', color4,color2, 1, lambda: Home(app5))

        def dele():
            f1.destroy()
        global img2
        imagen = Image.open('Images\close.png')
        nuevo_tam = (30, 30)
        imagen_nueva = imagen.resize(nuevo_tam)
        img2 = ImageTk.PhotoImage(imagen_nueva)
        Button(f1, image=img2, command=dele, border=0, activebackground=color, bg=color, cursor="hand2").place(x=5, y=10)

    frame = Frame(app5, width=80, height=900, bg=color)
    frame.place(x=0, y=0)
    imagen2 = Image.open('Images\open.png')
    nuevo_tam2 = (35, 35)
    imagen_nueva2 = imagen2.resize(nuevo_tam2)
    img1 = ImageTk.PhotoImage(imagen_nueva2)
    Button(app5, image=img1, border=0, activebackground=color, bg=color, command=menu, cursor="hand2").place(x=15, y=15)

    texto = "Generando pdf, esto puede tardar unos minutos. La pantalla de resultados aparecerá cuando termine el proceso"   
    messagebox.showinfo("Cargando...", texto)

    def default_home():
        #tam = (70,30)
        #nimg = imagen_logo.resize(tam)
        label = CTkLabel(app5, image=imagen_logo, fg_color="#00042A", text='')
        label.pack()
        label.place(relx=0.067, rely=0)

    default_home()

    def Previ():
         # Mostrar previsualización de imagen
        canvas_imagen = tkinter.Canvas(app5, bg="white", width=300, height=250)
        canvas_imagen.place(relx=0.15, rely=0.35)


        # Mostrar previsualización del primer documento del PDF
        canvas_pdf = tkinter.Canvas(app5, bg="white", width=380, height=500)
        canvas_pdf.place(relx=0.6, rely=0.07)

        def cargar_imagen():
            imagen_path = file
            if imagen_path:
                imagen = Image.open(imagen_path)
                imagen = imagen.resize((300, 250), resample=Image.Resampling.LANCZOS)
                imagen_tk = ImageTk.PhotoImage(imagen)
                canvas_imagen.config(width=300, height=250)
                canvas_imagen.create_image(0, 0, anchor=tkinter.NW, image=imagen_tk)
                canvas_imagen.image = imagen_tk
        cargar_imagen()

        model = YOLO('./runs/runs/classify/train6/weights/best.pt')
        result = model.predict(file, imgsz = 640)
        boxes = result[0].plot()
        texto = "Los detalles del resultado puede encontrarlos en el PDF que se muestra a su derecha"
        Res = CTkLabel(app5,text=texto, bg_color='white', fg_color="#050c2d") 
        Res.place(relx=0.55, rely=0.07)

        def cargar_pdf():
            pdf_path = pdf
            if pdf_path:
                visor_pdf = fitz.open(pdf_path)
                primera_pagina = visor_pdf.load_page(0)
                pix = primera_pagina.get_pixmap(matrix=fitz.Matrix(1, 1))
                imagen = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                imagen = imagen.resize((380, 500), resample=Image.Resampling.LANCZOS)
                imagen_tk = ImageTk.PhotoImage(imagen)
                canvas_pdf.config(width=380, height=500)
                canvas_pdf.create_image(0, 0, anchor=tkinter.NW, image=imagen_tk)
                canvas_pdf.image = imagen_tk
                global visor_pdf_global
                visor_pdf_global = visor_pdf
        cargar_pdf()

    Previ()

    def guardar_Imagen():
        print("Push Button")
        ventana_guardar = CTk()
        centro = centerScreen()
        ventana_guardar.geometry(centro.situarLaB(600,200))
        #ventana_guardar.iconbitmap("Images\logo.ico")
        ventana_guardar.title("Ventana Guardar")
        ventana_guardar.config(bg=color5)

        def descargar():
            print(visor_pdf_global)
            if visor_pdf_global is not None and visor_pdf_global.page_count > 0:
                nomArchivo = fd.asksaveasfilename(initialdir="C:/Users/USER/OneDrive/Escritorio/AImages", title="Guardar como", defaultextension=".pdf")
                if nomArchivo != '':
                    visor_pdf_global.save(nomArchivo)
                    mb.showinfo("Información", "El PDF ha sido guardado correctamente.")
                    ventana_guardar.destroy()
                else:
                    mb.showwarning("Advertencia", "No hay un PDF cargado para descargar.")


        button_opcion1 = customtkinter.CTkButton(master=ventana_guardar, text="Descargar", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=descargar)
        button_opcion1.place(relx=0.30, rely=0.4, anchor= tkinter.CENTER) 

        button_opcion2 = customtkinter.CTkButton(master=ventana_guardar, text="Enviar", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=descargar)
        button_opcion2.place(relx=0.70, rely=0.4, anchor= tkinter.CENTER) 

        ventana_guardar.mainloop()


    button = customtkinter.CTkButton(master=app5, text="Guardar", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=guardar_Imagen)
    button.place(relx=0.50, rely=0.9, anchor= tkinter.CENTER) 

     

    app5.mainloop()
    return app5
#img = "IMD004.bmp" 
#Res(img)