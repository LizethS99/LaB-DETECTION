#FORMULARIO
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, ttk, scrolledtext, messagebox
import sys
import os
import CapturarImagen 
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
        
        canvas.config(yscrollcommand=scrollbar.set, width= 750, height=450, scrollregion=canvas.bbox("all"))
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        subformulario_frame = tkinter.Frame(canvas, background=color)
        subformulario_frame.config(width= 750, height=450)
        canvas.create_window((0,0), window=subformulario_frame, anchor='nw')
        subformulario_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

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
        options2 = ["Si", "No"]
        select_option2 = tkinter.StringVar(value=options2[0])
        style.configure('TRadiobutton', background=color, foreground="black")

        for i, option in enumerate(options2):
            radio2 = tkinter.Radiobutton(canvas, text=option, variable=select_option2, value=option, background=color, font= ("Helvetica", 13))
            canvas.create_window((170+(i*130), 240+i), window=radio2, anchor='w')

        label5 = tkinter.Label(canvas, text='Si la respuesta es "Sí" en la pregunta anterior, ¿cuál es la relación familiar \ny cuándo fue el diagnóstico?', background=color, fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 290), window=label5, anchor='w')
        scroll_area = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 380), window=scroll_area, anchor='w', width=620, height=100)

        label6 = tkinter.Label(canvas, text='¿Hay antecendentes en usted o en su familia que haya llevado a cambios en el \ncomportamiento, como una mayor conciencia de protección solar?', background=color, fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 470), window=label6, anchor='w')

        #Radiobuttons
        options3 = ["Si", "No"]
        select_option3 = tkinter.StringVar(value=options3[0])
        style.configure('TRadiobutton', background=color, foreground="black")

        for i, option in enumerate(options3):
            radio3 = tkinter.Radiobutton(canvas, text=option, variable=select_option3, value=option, background=color, font= ("Helvetica", 13))
            canvas.create_window((170+(i*130), 520+i), window=radio3, anchor='w')
        
        label7 = tkinter.Label(canvas, text='¿Existen otros tipos de cáncer en la familia que podrían estar relacionados con un \nmayor riesgo de melanoma? (Por ejemplo, cáncer de piel no melanoma,\n cáncer de mama, cáncer de páncreas, etc.)', background=color, fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 570), window=label7, anchor='w')
        #Radiobuttons
        options4 = ["Si", "No"]
        select_option4 = tkinter.StringVar(value=options4[0])
        style.configure('TRadiobutton', background=color, foreground="black")

        for i, option in enumerate(options4):
            radio4 = tkinter.Radiobutton(canvas, text=option, variable=select_option4, value=option, background=color, font= ("Helvetica", 13))
            canvas.create_window((170+(i*130), 620+i), window=radio4, anchor='w')
        
        label8 = tkinter.Label(canvas, text='¿Cuál?', background=color, fg="white", font= ("Helvetica", 13), width=20) 
        canvas.create_window((0, 660), window=label8, anchor='w')
        entry8 = tkinter.Entry(canvas, width=30)
        canvas.create_window((145, 660), window=entry8, anchor='w')

        label9 = tkinter.Label(canvas, text='¿Se han realizado pruebas genéticas dentro de su familia para detectar mutaciones \nrelacionadas con el melanoma u otros cánceres?', background=color, fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 720), window=label9, anchor='w')
        #Radiobuttons
        options5 = ["Si", "No"]
        select_option5 = tkinter.StringVar(value=options5[0])
        style.configure('TRadiobutton', background=color, foreground="black")

        for i, option in enumerate(options5):
            radio4 = tkinter.Radiobutton(canvas, text=option, variable=select_option5, value=option, background=color, font= ("Helvetica", 13))
            canvas.create_window((170+(i*130), 770+i), window=radio4, anchor='w')
        
        label10 = tkinter.Label(canvas, text='Si es así, ¿cuáles fueron los resultados?', background=color, fg="white", font= ("Helvetica", 13), width=40) 
        canvas.create_window((40, 820), window=label10, anchor='w')
        scroll_area2 = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 900), window=scroll_area2, anchor='w', width=620, height=60)

        label10 = tkinter.Label(canvas, text='¿Se conocen otros factores hereditarios que puedan aumentar el riesgo de melanona, \ncomo una predisposición genética a la sensibilidad solar o a la pigmentación de la piel?', background=color, fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 980), window=label10, anchor='w')
        scroll_area3 = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 1060), window=scroll_area3, anchor='w', width=620, height=60)
        #############################################################################################################################

        # Formulario 2
        formulario_frame2 = tkinter.Frame(tab2, background="#2E3BAC")
        formulario_frame2.pack(fill='both', expand=True)
        formulario_frame2.place(relx=0, rely=0)

        canvas = tkinter.Canvas(formulario_frame2, background="#2E3BAC")
        scrollbar = tkinter.Scrollbar(formulario_frame2, orient='vertical', command=canvas.yview)

        canvas.config(yscrollcommand=scrollbar.set, width= 750, height=450, scrollregion=canvas.bbox("all"))
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        subformulario_frame2 = tkinter.Frame(canvas, background="#2E3BAC")
        subformulario_frame2.config(width= 750, height=450)
        canvas.create_window((0,0), window=subformulario_frame2, anchor='nw')
        subformulario_frame2.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        label_1 = tkinter.Label(canvas, text='¿Has tenido alguna lesión cutánea en el pasado que haya sido removida \nquirúrgicamente?', background="#2E3BAC", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 30), window=label_1, anchor='w')

        #Radiobuttons
        options_1 = ["Si", "No"]
        select_option_1 = tkinter.StringVar(value=options_1[0])
        style.configure('TRadiobutton', background="#2E3BAC", foreground="black")

        for i, option in enumerate(options_1):
            radio_1 = tkinter.Radiobutton(canvas, text=option, variable=select_option_1, value=option, background="#2E3BAC", font= ("Helvetica", 13))
            canvas.create_window((240+(i*130), 80+i), window=radio_1, anchor='w')

        label_2 = tkinter.Label(canvas, text='Si es así, ¿cuál fue el motivo de la remoción o el tratamiento?', background="#2E3BAC", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 120), window=label_2, anchor='w')

        scroll_area_1 = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 190), window=scroll_area_1, anchor='w', width=620, height=60)

        label_3 = tkinter.Label(canvas, text='¿Cuál es tu historial de exposición solar significativa, como trabajar al aire \nlibre o participar en actividades recreativas bajo el sol?', background="#2E3BAC", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 270), window=label_3, anchor='w')

        scroll_area_2 = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 350), window=scroll_area_2, anchor='w', width=620, height=60)

        label_4 = tkinter.Label(canvas, text='¿Has notado cambios en el tamaño, forma, color o textura de las lesiones \ncutáneas existentes?', background="#2E3BAC", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 420), window=label_4, anchor='w')

        #Radiobuttons
        options_2 = ["Si", "No"]
        select_option_2 = tkinter.StringVar(value=options_2[0])
        style.configure('TRadiobutton', background="#2E3BAC", foreground="black")

        for i, option in enumerate(options_2):
            radio_2 = tkinter.Radiobutton(canvas, text=option, variable=select_option_2, value=option, background="#2E3BAC", font= ("Helvetica", 13))
            canvas.create_window((240+(i*130), 470+i), window=radio_2, anchor='w')
        
        label_5 = tkinter.Label(canvas, text='Si la respuesta es sí, describa cuáles han sido los cambios', background="#2E3BAC", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 520), window=label_5, anchor='w')

        scroll_area_3 = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 590), window=scroll_area_3, anchor='w', width=620, height=60)

        label_6 = tkinter.Label(canvas, text='¿Has tenido algún episodio previo de quemadura solar grave en la \ninfancia o en la adultez?', background="#2E3BAC", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 660), window=label_6, anchor='w')

        #Radiobuttons
        options_3 = ["Si", "No"]
        select_option_3 = tkinter.StringVar(value=options_3[0])
        style.configure('TRadiobutton', background="#2E3BAC", foreground="black")

        for i, option in enumerate(options_3):
            radio_3 = tkinter.Radiobutton(canvas, text=option, variable=select_option_3, value=option, background="#2E3BAC", font= ("Helvetica", 13))
            canvas.create_window((240+(i*130), 720+i), window=radio_3, anchor='w')
        
        label_7 = tkinter.Label(canvas, text='¿Has sido diagnosticado con otros problemas de piel, como queratosis actínicas \no cáncer de piel no melanoma?', background="#2E3BAC", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 770), window=label_7, anchor='w')

        #Radiobuttons
        options_4 = ["Si", "No"]
        select_option_4 = tkinter.StringVar(value=options_4[0])
        style.configure('TRadiobutton', background="#2E3BAC", foreground="black")

        for i, option in enumerate(options_4):
            radio_4 = tkinter.Radiobutton(canvas, text=option, variable=select_option_4, value=option, background="#2E3BAC", font= ("Helvetica", 13))
            canvas.create_window((240+(i*130), 830+i), window=radio_4, anchor='w')

        label_8 = tkinter.Label(canvas, text='¿Has tenido alguna biopsia de lesiones cutáneas sospechosas de \nmelanoma en el pasado?', background="#2E3BAC", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 890), window=label_8, anchor='w')

        #Radiobuttons
        options_5 = ["Si", "No"]
        select_option_5 = tkinter.StringVar(value=options_5[0])
        style.configure('TRadiobutton', background="#2E3BAC", foreground="black")

        for i, option in enumerate(options_5):
            radio_5 = tkinter.Radiobutton(canvas, text=option, variable=select_option_5, value=option, background="#2E3BAC", font= ("Helvetica", 13))
            canvas.create_window((240+(i*130), 950+i), window=radio_5, anchor='w')

        label_9 = tkinter.Label(canvas, text='Si se ha realizado una biopsia, ¿cuál fue el resultado? (Por ejemplo, benigno, \nmelanoma in situ, melanoma invasivo) y ¿en qué fecha se realizó?', background="#2E3BAC", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 1010), window=label_9, anchor='w')

        scroll_area_4 = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 1070), window=scroll_area_4, anchor='w', width=620, height=60)
        #############################################################################################################################

        # Formulario 3
        formulario_frame3 = tkinter.Frame(tab3, background="#73B62D")
        formulario_frame3.pack(fill='both', expand=True)
        formulario_frame3.place(relx=0, rely=0)

        canvas = tkinter.Canvas(formulario_frame3, background="#73B62D")
        scrollbar = tkinter.Scrollbar(formulario_frame3, orient='vertical', command=canvas.yview)

        canvas.config(yscrollcommand=scrollbar.set, width= 750, height=450, scrollregion=canvas.bbox("all"))
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        subformulario_frame3 = tkinter.Frame(canvas, background="#73B62D")
        subformulario_frame3.config(width= 750, height=450)
        canvas.create_window((0,0), window=subformulario_frame3, anchor='nw')
        subformulario_frame3.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        lbl_1 = tkinter.Label(canvas, text='¿Has utilizado camas de bronceado con regularidad en el pasado?', background="#73B62D", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 30), window=lbl_1, anchor='w')

        #Radiobuttons
        opt_1 = ["Si", "No"]
        selectoption_1 = tkinter.StringVar(value=opt_1[0])
        style.configure('TRadiobutton', background="#73B62D", foreground="black")

        for i, option in enumerate(opt_1):
            rad_1 = tkinter.Radiobutton(canvas, text=option, variable=selectoption_1, value=option, background="#73B62D", font= ("Helvetica", 13))
            canvas.create_window((240+(i*130), 80+i), window=rad_1, anchor='w')

        lbl_2 = tkinter.Label(canvas, text='¿Con qué frecuencia realizas autoexámenes de la piel para buscar cambios o \nlesiones inusuales?', background="#73B62D", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 130), window=lbl_2, anchor='w')

        etr1 = tkinter.Entry(canvas, width=60)
        canvas.create_window((170, 190), window=etr1, anchor='w')

        lbl_3 = tkinter.Label(canvas, text='¿Utilizas protector solar regularmente cuando te expones al sol?', background="#73B62D", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 250), window=lbl_3, anchor='w')
        
        #Radiobuttons
        opt_2 = ["Si", "No"]
        selectoption_1 = tkinter.StringVar(value=opt_1[0])
        style.configure('TRadiobutton', background="#73B62D", foreground="black")

        for i, option in enumerate(opt_2):
            rad_1 = tkinter.Radiobutton(canvas, text=option, variable=selectoption_1, value=option, background="#73B62D", font= ("Helvetica", 13))
            canvas.create_window((240+(i*130), 300+i), window=rad_1, anchor='w')

        lbl_4 = tkinter.Label(canvas, text='¿Tienes una rutina regular de protección solar, como usar ropa protectora y sombreros?', background="#73B62D", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 350), window=lbl_4, anchor='w')

        etr2 = tkinter.Entry(canvas, width=60)
        canvas.create_window((170, 400), window=etr2, anchor='w')

        lbl_5 = tkinter.Label(canvas, text='¿Has recibido educación sobre la detección temprana de melanoma y cómo hacer autoexámenes de la piel?', background="#73B62D", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 350), window=lbl_5, anchor='w')

        #Radiobuttons
        opt_3 = ["Si", "No"]
        selectoption_3 = tkinter.StringVar(value=opt_3[0])
        style.configure('TRadiobutton', background="#73B62D", foreground="black")

        for i, option in enumerate(opt_3):
            rad_3 = tkinter.Radiobutton(canvas, text=option, variable=selectoption_3, value=option, background="#73B62D", font= ("Helvetica", 13))
            canvas.create_window((240+(i*130), 300+i), window=rad_3, anchor='w')
        

       
        

    def menu():
        f1 = Frame(app2, width=150, height=900, bg=color)
        f1.place(x=0, y=0)
        def Botones(x,y,text,bcolor,fcolor, funcion):
            def on_enter(e):
                mybutton1['background'] = bcolor
                mybutton1['foreground'] = fcolor
            def on_leave(e):
                mybutton1['background'] = fcolor
                mybutton1['foreground'] = bcolor
            mybutton1 = Button(f1, width=22, height=2, text=text, fg=bcolor, border=2, bg=fcolor, activebackground=bcolor, activeforeground=fcolor, command=funcion)
            mybutton1.bind("<Enter>", on_enter)
            mybutton1.bind("<Leave>", on_leave)
            mybutton1.place(x=x, y=y)
        def nuevo_analisis(screen):
            screen.destroy()
            pantallanueva2 = CapturarImagen.PantallaImagen()
        def salir():
            messagebox.showinfo("Salir", "Vuelva pronto")
            sys.exit(0)
        
        Botones(0, 50, 'Acerca de', color4,color2, None)
        Botones(0, 90, 'Cáncer de piel', color4,color2, None)
        Botones(0, 130, 'Redes neuronales', color4,color2, None)
        Botones(0, 170, 'Nuevo análisis', color4,color2, nuevo_analisis(app2))
        Botones(0, 210, 'Salir', color4,color2, salir)

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