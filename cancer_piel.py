import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, messagebox
import sys
from claseCentrar import centerScreen
import LaB_DETECTION
import Acercade

def Cancer_piel(imagen_logo2, img):

    color = '#003F79' # color menú lateral
    color2 = '#122E60' #Azul muy oscuro
    color3 = '#48F0FA' #Azul muy claro
    color4 = '#E8FBFC' #Letras en los botones
    color5 = '#0D2764'
    color6 = '#2E6FAC'
    app_cancer_piel = customtkinter.CTk()
    centro = centerScreen()
    app_cancer_piel.geometry(centro.situarLaB(1200,700)) #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
    app_cancer_piel.minsize(1100,700)
    app_cancer_piel.maxsize(1400, 700)
    app_cancer_piel.config(bg=color5)
    app_cancer_piel.title('Cáncer d piel')
    img_logo = imagen_logo2
    img_logo3 = Image.open(img_logo)
    ntam = (245, 145)
    imagen_redim = img_logo3.resize(ntam)
    imagen_logo = ImageTk.PhotoImage(imagen_redim)
    imagen_log = PhotoImage(file='Images\Segundologo.png')
    app_cancer_piel.iconbitmap("Images\logo.ico")
    fondo = PhotoImage(file=img)
    lbl_fondo = Label(image=fondo).place(x=0, y=0.05)
    

    def menu():
        f1 = Frame(app_cancer_piel, width=150, height=900, bg=color)
        f1.place(x=0, y=0)
        def Botones(x,y,text,bcolor,fcolor, op, funcion):
            def on_enter(e):
                mybutton1['background'] = bcolor
                mybutton1['foreground'] = fcolor
            def on_leave(e):
                mybutton1['background'] = fcolor
                mybutton1['foreground'] = bcolor
            mybutton1 = Button(f1, width=22, height=2, text=text, border=2, bg=fcolor, activebackground=bcolor, activeforeground=fcolor, command=lambda: funcion(), cursor="hand2")
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
        
        def Home(screen):
            screen.destroy()
            back_home = LaB_DETECTION.funcion_principal()

        def Aboutus(screen, imagen1, imagen2):
            screen.destroy()

            pantallanueva3 = Acercade.Acerca_de(imagen1, imagen2)
        

        Botones(0, 50, 'Acerca de', color4,color2, 1, lambda: Aboutus(app_cancer_piel, imagen_logo2, img))
        Botones(0, 90, 'Cáncer de piel', color4,color2, 0, None)
        Botones(0, 130, 'Redes neuronales', color4,color2, 1, None)
        Botones(0, 170, 'Nuevo análisis', color4,color2, 0, None)
        Botones(0, 210, 'Salir', color4,color2, 1, lambda: salir())
        Botones(0, 250, 'Home', color4,color2, 1, lambda: Home(app_cancer_piel))

    
        def dele():
            f1.destroy()
        global img2
        imagen = Image.open('Images\close.png')
        nuevo_tam = (30, 30)
        imagen_nueva = imagen.resize(nuevo_tam)
        img2 = ImageTk.PhotoImage(imagen_nueva)
        Button(f1, image=img2, command=dele, border=0, activebackground=color, bg=color, cursor="hand2").place(x=5, y=10)

    frame = Frame(app_cancer_piel, width=80, height=900, bg=color)
    frame.place(x=0, y=0)
    imagen2 = Image.open('Images\open.png')
    nuevo_tam2 = (35, 35)
    imagen_nueva2 = imagen2.resize(nuevo_tam2)
    img1 = ImageTk.PhotoImage(imagen_nueva2)
    Button(app_cancer_piel, image=img1, border=0, activebackground=color, bg=color, command=menu, cursor="hand2").place(x=15, y=15)

    def default_home():
        label = CTkLabel(app_cancer_piel, image=imagen_logo, fg_color="#00042A", text='')
        label.pack()
        label.place(relx=0.067, rely=0)

    default_home()
    def AS():
        formulario_frame = tkinter.Frame(app_cancer_piel, background=color)
        formulario_frame.pack(fill='both', expand=True)
        formulario_frame.place(relx=0.2, rely=0.2)

        canvas = tkinter.Canvas(formulario_frame, background=color)
        scrollbar = tkinter.Scrollbar(formulario_frame, orient='vertical', command=canvas.yview, activebackground=color6, troughcolor="#D222D8", background=color6)
        
        canvas.config(yscrollcommand=scrollbar.set, width= 750, height=450, scrollregion=canvas.bbox("all"))
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        subformulario_frame = tkinter.Frame(canvas, background=color)
        subformulario_frame.config(width= 750, height=450)
        canvas.create_window((0,0), window=subformulario_frame, anchor='nw')
        subformulario_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        # Agregar los términos y condiciones al área de desplazamiento
        nosotros = """Puesto que el melanoma es uno de los canceres de piel que son más agresivos, puesto que si no es detectado a tiempo puede ser potencialmente mortal. 
        Por este motivo es que LaB-DETECTION fue creado con la finalidad de que a través de una imagen se haga un análisis por medio de redes neuronales convolucionales, en donde nos muestre un resultado donde la imagen quede clasificada como típica, común o melanoma.
        Además se hará uso del método ABCD en donde se tomará en cuenta la asímetria, el borde, el color y otras carcateristicas relevantes que proporcionen la información más amplia posible para el médico.
        Para entender un poco más cómo funciona este software debemos indagar un poco más sobre redes neuronales, estas funcionan mediante aprendizaje, ya que tratan de emular la forma en la que aprendemos los humanos. 
        En especifico la que usamos en LaB-DETECTION se entrenó, es decir, aprendió por medio de un DataSet proveniente de PH2 en el que que cada imagen es categorizada en 'común', 'típica' y 'melanoma', por lo que aprendió a diferenciar una imagen."""
        label1 = tkinter.Label(canvas, text=nosotros, justify=tkinter.LEFT, wraplength=500, background=color, fg="white", font= ("Helvetica", 13), width=70)
        canvas.create_window((50, 230), window=label1, anchor='w')     

    AS()

    Label6 = tkinter.Label(app_cancer_piel, text="Derechos de autor © 2023 LaB-DETECTION.", background=color5, fg="white", font= ("Helvetica", 13), width=50)
    Label6.place(relx=0.3, rely=0.96)

    app_cancer_piel.mainloop()
    return app_cancer_piel

"""ruta = 'Images\Segundologo.png'
ruta2 = 'Images\\fondo.png'    
Cancer_piel(ruta, ruta2)"""