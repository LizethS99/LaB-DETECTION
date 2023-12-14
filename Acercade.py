import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, messagebox
import sys
from claseCentrar import centerScreen
import LaB_DETECTION

def Acerca_de(imagen_logo2, img):

    color = '#003F79' # color menú lateral
    color2 = '#122E60' #Azul muy oscuro
    color3 = '#48F0FA' #Azul muy claro
    color4 = '#E8FBFC' #Letras en los botones
    color5 = '#0D2764'
    color6 = '#2E6FAC'
    app4 = customtkinter.CTk()
    centro = centerScreen()
    app4.geometry(centro.situarLaB(1200,700)) #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
    app4.minsize(1100,700)
    app4.maxsize(1400, 700)
    app4.config(bg=color5)
    app4.title('Acerca de')
    img_logo = imagen_logo2
    img_logo2 = Image.open(img_logo)
    ntam = (400, 180)
    imagen_redim = img_logo2.resize(ntam)
    imagen_logo = ImageTk.PhotoImage(imagen_redim)
    imagen_logo = PhotoImage(file='Images\Segundologo.png')
    app4.iconbitmap("Images\logo.ico")
    fondo = PhotoImage(file=img)
    lbl_fondo = Label(image=fondo).place(x=0, y=0.05)
    

    def menu():
        f1 = Frame(app4, width=150, height=900, bg=color)
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
        

        Botones(0, 50, 'Acerca de', color4,color2, 0, None)
        Botones(0, 90, 'Cáncer de piel', color4,color2, 1, None)
        Botones(0, 130, 'Redes neuronales', color4,color2, 1, None)
        Botones(0, 170, 'Nuevo análisis', color4,color2, 0, None)
        Botones(0, 210, 'Salir', color4,color2, 1, salir)
        Botones(0, 250, 'Home', color4,color2, 1, lambda: Home(app4))

    
        def dele():
            f1.destroy()
        global img2
        imagen = Image.open('Images\close.png')
        nuevo_tam = (30, 30)
        imagen_nueva = imagen.resize(nuevo_tam)
        img2 = ImageTk.PhotoImage(imagen_nueva)
        Button(f1, image=img2, command=dele, border=0, activebackground=color, bg=color, cursor="hand2").place(x=5, y=10)

    frame = Frame(app4, width=80, height=900, bg=color)
    frame.place(x=0, y=0)
    imagen2 = Image.open('Images\open.png')
    nuevo_tam2 = (35, 35)
    imagen_nueva2 = imagen2.resize(nuevo_tam2)
    img1 = ImageTk.PhotoImage(imagen_nueva2)
    Button(app4, image=img1, border=0, activebackground=color, bg=color, command=menu, cursor="hand2").place(x=15, y=15)

    def default_home():
        #tam = (70,30)
        #nimg = imagen_logo.resize(tam)
        label = CTkLabel(app4, image=imagen_logo, fg_color="#00042A", text='')
        label.pack()
        label.place(relx=0.067, rely=0)

    default_home()
    def AS():
        formulario_frame = tkinter.Frame(app4, background=color)
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
        nosotros = """ Hola, nosotros somos LaB-DETECTION e hicimos este software para apoyarte en el diagnóstico del cáncer de piel del tipo melanoma, decidimos hacer este proyecto para apoyar a médicos y pacientes, nosotros no pretendemos sustituir a médicos y mucho menos hacer autodiagnósticos, pretendemos que esta herramienta pueda darle al médico un panorama más detallado sobre la lesión. Esperamos sea de utilidad y seguir haciendo mejoras a este software. 
        Agradecemos mucho de tu colaboración para poder darle vida a este proyecto, en los paartado de 'Cáncer de piel' y 'Redes neuronales' podrás encontrar más sobre cómo se realizó este proyecto y cómo se obtienen los parametros que se muestran en el pdf de resultados. 
        Si tienes alguna duda, quejas o sugerencia, por favor no dudes en ponerte en contacto con alguno de nosotros por medio de nuestros correo electrónicos, nos encantará saber tu opinión."""
        label1 = tkinter.Label(canvas, text=nosotros, justify=tkinter.LEFT, wraplength=500, background=color, fg="white", font= ("Helvetica", 13), width=70)
        canvas.create_window((50, 100), window=label1, anchor='w')


        imagen_Liz = Image.open('./Images/fotoLiz.jpeg')
        ntam_liz = (150, 200)
        imagen_redim_liz = imagen_Liz.resize(ntam_liz)
        imagen_nueva_liz = ImageTk.PhotoImage(imagen_redim_liz)
        label2 = CTkLabel(canvas, image=imagen_nueva_liz, fg_color="#00042A", text='')
        canvas.create_window((160, 400), window=label2, anchor='w')
        label3 = tkinter.Label(canvas, text="Yeraldi Lizeth Sánchez Sandoval\n lizeth.sanchez1780.99@gmail.com", background=color, fg="white", font= ("Helvetica", 13), width=30)
        canvas.create_window((100, 520), window=label3, anchor='w')

        
        imagen_Brandon = Image.open('./Images/fotoBrandon.jpg')
        ntam_brandon = (140, 200)
        imagen_redim_brandon = imagen_Brandon.resize(ntam_brandon)
        imagen_nueva_brandon = ImageTk.PhotoImage(imagen_redim_brandon)
        label4 = CTkLabel(canvas, image=imagen_nueva_brandon, fg_color="#00042A", text='')
        canvas.create_window((450, 400), window=label4, anchor='w')
        label5 = tkinter.Label(canvas, text="Brandon de Jesús Bravo Mendoza\n1brandon.bravo.2101@hotmail.com", background=color, fg="white", font= ("Helvetica", 13), width=30)
        canvas.create_window((390, 520), window=label5, anchor='w')
        

    AS()

    Label6 = tkinter.Label(app4, text="Derechos de autor © 2023 LaB-DETECTION.", background=color5, fg="white", font= ("Helvetica", 13), width=50)
    Label6.place(relx=0.3, rely=0.96)

    app4.mainloop()

    return app4
#Acerca_de()