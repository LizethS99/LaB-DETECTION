#Seleccionar imagen o tomarla desde la cámara
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, ttk, scrolledtext
import os
def NewPantalla():
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green

    color = '#003F79' # color menú lateral
    color2 = '#122E60' #Azul muy oscuro
    #color3 = '#48F0FA' #Azul muy claro
    color4 = '#E8FBFC' #Letras en los botones
    color5 = '#0D2764'
    color6 = '#2E6FAC'

    app2 = customtkinter.CTk()
    app2.geometry('1200x700+250+110') #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
    app2.minsize(1100,700)
    app2.maxsize(1400, 700)
    app2.config(bg=color5)
    app2.title('LaB-DETECTION Historial')
    imagen_logo2 = Image.open('Images\Segundologo.png')
    ntam = (400, 180)
    imagen_redim = imagen_logo2.resize(ntam)
    imagen_logo = ImageTk.PhotoImage(imagen_redim)
    app2.iconbitmap("Images\logo.ico")
    fondo = PhotoImage(file='Images\\fondo.png')
    lbl_fondo = CTkLabel(app2, image=fondo, text='').place(x=0, y=0)

    def formularios():
        #Pestañas para los formularios
        style = ttk.Style()

        style.configure('TNotebook', background="#00042A", borderwidth=5)
        style.map('TNotebook.Tab', background=[('selected', 'blue'), ('active', 'lightblue')])

        notebook = ttk.Notebook(app2, width= 800, height=480)
        notebook.place(relx=0.2, rely=0.14)
        
        tab1 = Frame(notebook, background=color6, border=10)
        tab2 = Frame(notebook, background="#7683F7", border=10)
        tab3 = Frame(notebook, background="#CDFA9F", border=10)

        notebook.add(tab1, text='       HEREDOFAMILIAR       ')
        notebook.add(tab2, text='       PATOLOGICO       ')
        notebook.add(tab3, text='       NO PATOLOGICO       ')

        # Formulario 1
        formulario_frame = tkinter.Frame(tab1, background=color)
        formulario_frame.pack(fill='both', expand=True)
        formulario_frame.place(relx=0, rely=0)

        canvas = tkinter.Canvas(formulario_frame, background=color)
        scrollbar = tkinter.Scrollbar(formulario_frame, orient='vertical', command=canvas.yview, activebackground=color6, troughcolor="#D222D8", background=color6)
        
        canvas.config(yscrollcommand=scrollbar.set, width= 750, height=450)

        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        subformulario_frame = tkinter.Frame(canvas, background="#F78876")
        #canvas.create_window((0,0), window=subformulario_frame, width=750)#, anchor='nw')
        

        # Configura el widget Canvas para actualizar su vista cuando cambia el contenido
        #subformulario_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        label1 = tkinter.Label(canvas, text='Nombre completo:', background=color, fg="white", font= ("Helvetica", 13), width=15) 
        entry1 = tkinter.Entry(canvas, width=60)
        canvas.create_window((10, 30), window=label1, anchor='w')
        canvas.create_window((170, 30), window=entry1, anchor='w')
       
        label2 = tkinter.Label(canvas, text='Edad:', background=color, fg="white", font= ("Helvetica", 13), width=15) 
        entry2 = tkinter.Entry(canvas, width=10)
        canvas.create_window((5, 80), window=label2, anchor='w')
        canvas.create_window((170, 80), window=entry2, anchor='w')
    

        label3 = tkinter.Label(canvas, text='Sexo:', background=color, fg="white", font= ("Helvetica", 13), width=15) 
        canvas.create_window((5, 130), window=label3, anchor='w')
        #Radiobuttons
        options = ["Femenino", "Masculino", "Otro"]
        select_option = tkinter.StringVar(value=options[0])

        # Crear estilo para los Radiobuttons sin resaltado en estado 'hover'
        style.configure('TRadiobutton', background=color, foreground="black")

        for i, option in enumerate(options):
            radio = tkinter.Radiobutton(canvas, text=option, variable=select_option, value=option, background=color, fg="black", activebackground="black", font= ("Helvetica", 13), width=7)
            #radio.grid(row=2+i, column=1, padx=3, pady=5, sticky='w')
            canvas.create_window((170+(i*130), 130+i), window=radio, anchor='w')
        entry3 = tkinter.Entry(canvas)
        canvas.create_window((550, 130), window=entry3, anchor='w')

        label4 = tkinter.Label(canvas, text='¿Algún miembro de la familia ha sido diagnósticado previamente con melanoma?', background=color, fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((35, 190), window=label4, anchor='w')
        
        #Radiobuttons
        options = ["Si", "No"]
        select_option = tkinter.StringVar(value=options[0])
        style.configure('TRadiobutton', background=color, foreground="black")

        for i, option in enumerate(options):
            radio = tkinter.Radiobutton(canvas, text=option, variable=select_option, value=option, background=color, font= ("Helvetica", 13))
            canvas.create_window((170+(i*130), 240+i), window=radio, anchor='w')

        label5 = tkinter.Label(canvas, text='Si la respuesta es "Sí" en la pregunta anterior, ¿cuál es la relación familiar \ny cuándo fue el diagnóstico?', background=color, fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 290), window=label5, anchor='w')
        scroll_area = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 380), window=scroll_area, anchor='w', width=620, height=100)

        label6 = tkinter.Label(canvas, text='Hay antecendentes en usted o en su familia que haya llevado a cambios en el \ncomportamiento, como una mayor conciencia de protección solar', background=color, fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 450), window=label6, anchor='w')
        #############################################################################################################################

        # Formulario 2
        formulario_frame2 = tkinter.Frame(tab2, background="#2E3BAC")
        formulario_frame2.pack(fill='both', expand=True)
        formulario_frame2.place(relx=0, rely=0)

        canvas = tkinter.Canvas(formulario_frame2)
        scrollbar = tkinter.Scrollbar(formulario_frame2, orient='vertical', command=canvas.yview)

        canvas.config(yscrollcommand=scrollbar.set, width= 750, height=450)

        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        subformulario_frame2 = tkinter.Frame(canvas, background="#2E3BAC")
        subformulario_frame2.config(width= 750, height=450)
        canvas.create_window((0,0), window=subformulario_frame2, anchor='nw')
        subformulario_frame2.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        label4 = tkinter.Label(canvas, text='¿Algún miembro de la familia ha sido diagnósticado previamente con melanoma?', background="#2E3BAC", fg="white", font= ("Helvetica", 14)) 
        canvas.create_window((5, 190), window=label4, anchor='w')
       
        

    def menu():
        f1 = Frame(app2, width=150, height=900, bg=color)
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

    frame = Frame(app2, width=80, height=900, bg=color)
    frame.place(x=0, y=0)
    imagen2 = Image.open('Images\open.png')
    nuevo_tam2 = (35, 35)
    imagen_nueva2 = imagen2.resize(nuevo_tam2)
    img1 = ImageTk.PhotoImage(imagen_nueva2)
    Button(app2, image=img1, border=0, activebackground=color, bg=color, command=menu, cursor="hand2").place(x=15, y=15)

    def default_home():
        #tam = (70,30)
        #nimg = imagen_logo.resize(tam)
        label = CTkLabel(app2, image=imagen_logo, fg_color="#00042A", text='')
        label.pack()
        label.place(relx=0.067, rely=0)

    default_home()
    formularios()
    app2.mainloop()

    return app2

#NewPantalla()
