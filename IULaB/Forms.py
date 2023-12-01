#FORMULARIO
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, ttk, scrolledtext, messagebox
from tkcalendar import Calendar
from datetime import datetime
import sys
import os
import CapturarImagen 
import Acercade
from claseCentrar import centerScreen
import CapturarImagen
def NewPantalla():
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green

    color = '#003F79' # color menú lateral
    color2 = '#122E60' #Azul muy oscuro
    color3 = '#48F0FA' #Azul muy claro
    color4 = '#E8FBFC' #Letras en los botones
    color5 = '#0D2764'
    color6 = '#2E6FAC'
    centro = centerScreen()
    app2 = customtkinter.CTk()
    app2.geometry(centro.situarLaB(1200,700)) #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
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

    global img
    img = Image.open('Images\Cambiar_1.png')
    img_tam2 = (45, 45)
    img_nueva2 = img.resize(img_tam2)
    n_img = ImageTk.PhotoImage(img_nueva2)
    
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
        notebook.add(tab2, text='       PATOLÓGICO       ')
        notebook.add(tab3, text='       NO PATOLÓGICO       ')

        # Formulario 1
        formulario_frame = tkinter.Frame(tab1, background="#4d7091")
        formulario_frame.pack(fill='both', expand=True)
        formulario_frame.place(relx=0, rely=0)

        canvas = tkinter.Canvas(formulario_frame, background="#4d7091")
        scrollbar = tkinter.Scrollbar(formulario_frame, orient='vertical', command=canvas.yview, activebackground=color6, troughcolor="#D222D8", background=color6)
        
        canvas.config(yscrollcommand=scrollbar.set, width= 750, height=450, scrollregion=canvas.bbox("all"))
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        subformulario_frame = tkinter.Frame(canvas, background="#4d7091")
        subformulario_frame.config(width= 750, height=450)
        canvas.create_window((0,0), window=subformulario_frame, anchor='nw')
        subformulario_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        label1 = tkinter.Label(canvas, text='Nombre completo:', background="#4d7091", fg="white", font= ("Helvetica", 13), width=15) 
        entry1 = tkinter.Entry(canvas, width=60)
        
        canvas.create_window((10, 30), window=label1, anchor='w')
        canvas.create_window((170, 30), window=entry1, anchor='w')
       
        label2 = tkinter.Label(canvas, text='Edad:', background="#4d7091", fg="white", font= ("Helvetica", 13), width=15) 
        entry2 = tkinter.Entry(canvas, width=10)
        canvas.create_window((5, 80), window=label2, anchor='w')
        canvas.create_window((170, 80), window=entry2, anchor='w')
    

        label3 = tkinter.Label(canvas, text='Sexo:', background="#4d7091", fg="white", font= ("Helvetica", 13), width=15) 
        canvas.create_window((5, 130), window=label3, anchor='w')
        #Radiobuttons
        options = ["Femenino", "Masculino", "Otro"]
        select_option = tkinter.StringVar(value=options[0])

        # Crear estilo para los Radiobuttons sin resaltado en estado 'hover'
        style.configure('TRadiobutton', background="#4d7091", foreground="black")

        for i, option in enumerate(options):
            radio = tkinter.Radiobutton(canvas, text=option, variable=select_option, value=option, background="#4d7091", fg="black", activebackground="black", font= ("Helvetica", 13), width=7)
            #radio.grid(row=2+i, column=1, padx=3, pady=5, sticky='w')
            canvas.create_window((170+(i*130), 130+i), window=radio, anchor='w')
        entry3 = tkinter.Entry(canvas)
        canvas.create_window((550, 130), window=entry3, anchor='w')

        label0_1 = tkinter.Label(canvas, text='Médico que atiende:', background="#4d7091", fg="white", font= ("Helvetica", 13), width=20) 
        entry0_1 = tkinter.Entry(canvas, width=60)
        canvas.create_window((5, 180), window=label0_1, anchor='w')
        canvas.create_window((200, 180), window=entry0_1, anchor='w')

        label_fecha = tkinter.Label(canvas, text='Fecha:', background="#4d7091", fg="white", font= ("Helvetica", 13), width=15)
        canvas.create_window((5, 280), window=label_fecha, anchor='w')

        entry_fecha = tkinter.Entry(canvas)
        canvas.create_window((170, 280), window=entry_fecha, anchor='w')

        fecha_actual = datetime.now().date()
        cal = Calendar(canvas, selectmode="day", date_pattern="yyyy-mm-dd", date_var=tkinter.StringVar(value=fecha_actual))
        global lista
        lista = []
        def actualizar_fecha():
            fecha_seleccionada_str = cal.get_date()
            fecha_seleccionada = datetime.strptime(fecha_seleccionada_str, "%Y-%m-%d")
            fecha_formateada = "{:02d}/{:02d}/{}".format(fecha_seleccionada.month, fecha_seleccionada.day, fecha_seleccionada.year)
            entry_fecha.delete(0, "end")  # Limpiar el contenido actual
            entry_fecha.insert(0, fecha_formateada)  # Insertar la nueva fecha formateada
        
        canvas.create_window((350, 300), window=cal, anchor='w')
        #Para no revolverte, guarda lo que está en el entry_fecha, así no importa si cambia, tu solo recupera la fecha que esté ahí 
        cal.bind("<<CalendarSelected>>", lambda event: actualizar_fecha())

        label4 = tkinter.Label(canvas, text='¿Algún miembro de la familia ha sido diagnósticado previamente con melanoma?', background="#4d7091", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((35, 430), window=label4, anchor='w')
        
        #Radiobuttons
        options2 = ["Si", "No"]
        select_option2 = tkinter.StringVar(value=options2[0])
        style.configure('TRadiobutton', background="#4d7091", foreground="black")

        for i, option in enumerate(options2):
            radio2 = tkinter.Radiobutton(canvas, text=option, variable=select_option2, value=option, background="#4d7091", font= ("Helvetica", 13))
            canvas.create_window((170+(i*130), 480+i), window=radio2, anchor='w')

        label5 = tkinter.Label(canvas, text='Si la respuesta es "Sí" en la pregunta anterior, ¿cuál es la relación familiar \ny cuándo fue el diagnóstico?', background="#4d7091", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 530), window=label5, anchor='w')
        scroll_area = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 580), window=scroll_area, anchor='w', width=620, height=100)

        label6 = tkinter.Label(canvas, text='¿Hay antecendentes en usted o en su familia que haya llevado a cambios en el \ncomportamiento, como una mayor conciencia de protección solar?', background="#4d7091", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 630), window=label6, anchor='w')

        #Radiobuttons
        options3 = ["Si", "No"]
        select_option3 = tkinter.StringVar(value=options3[0])
        style.configure('TRadiobutton', background="#4d7091", foreground="black")

        for i, option in enumerate(options3):
            radio3 = tkinter.Radiobutton(canvas, text=option, variable=select_option3, value=option, background="#4d7091", font= ("Helvetica", 13))
            canvas.create_window((170+(i*130), 680+i), window=radio3, anchor='w')
        
        label7 = tkinter.Label(canvas, text='¿Existen otros tipos de cáncer en la familia que podrían estar relacionados con un \nmayor riesgo de melanoma? (Por ejemplo, cáncer de piel no melanoma,\n cáncer de mama, cáncer de páncreas, etc.)', background="#4d7091", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 730), window=label7, anchor='w')
        #Radiobuttons
        options4 = ["Si", "No"]
        select_option4 = tkinter.StringVar(value=options4[0])
        style.configure('TRadiobutton', background="#4d7091", foreground="black")

        for i, option in enumerate(options4):
            radio4 = tkinter.Radiobutton(canvas, text=option, variable=select_option4, value=option, background="#4d7091", font= ("Helvetica", 13))
            canvas.create_window((170+(i*130), 780+i), window=radio4, anchor='w')
        
        label8 = tkinter.Label(canvas, text='¿Cuál?', background="#4d7091", fg="white", font= ("Helvetica", 13), width=20) 
        canvas.create_window((0, 830), window=label8, anchor='w')
        entry8 = tkinter.Entry(canvas, width=30)
        canvas.create_window((145, 830), window=entry8, anchor='w')

        label9 = tkinter.Label(canvas, text='¿Se han realizado pruebas genéticas dentro de su familia para detectar mutaciones \nrelacionadas con el melanoma u otros cánceres?', background="#4d7091", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((55, 880), window=label9, anchor='w')
        #Radiobuttons
        options5 = ["Si", "No"]
        select_option5 = tkinter.StringVar(value=options5[0])
        style.configure('TRadiobutton', background="#4d7091", foreground="black")

        for i, option in enumerate(options5):
            radio4 = tkinter.Radiobutton(canvas, text=option, variable=select_option5, value=option, background="#4d7091", font= ("Helvetica", 13))
            canvas.create_window((170+(i*130), 940+i), window=radio4, anchor='w')
        
        label10 = tkinter.Label(canvas, text='Si es así, ¿cuáles fueron los resultados?', background="#4d7091", fg="white", font= ("Helvetica", 13), width=40) 
        canvas.create_window((40, 990), window=label10, anchor='w')
        scroll_area2 = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 1050), window=scroll_area2, anchor='w', width=620, height=60)

        label10 = tkinter.Label(canvas, text='¿Se conocen otros factores hereditarios que puedan aumentar el riesgo de melanona, \ncomo una predisposición genética a la sensibilidad solar o a la pigmentación de la piel?', background="#4d7091", fg="white", font= ("Helvetica", 13), width=70) 
        canvas.create_window((40, 1110), window=label10, anchor='w')
        scroll_area3 = scrolledtext.ScrolledText(canvas, wrap=tkinter.WORD)
        canvas.create_window((60, 1160), window=scroll_area3, anchor='w', width=620, height=60)

        def Datos_recabados_1():
            
            nombre = entry1.get()
            lista.append(nombre)
            edad = entry2.get()
            lista.append(edad)
            sexo = select_option.get()
            if sexo == "Otro":
                sexo2 = sexo
                lista.append(sexo2)
                otro = entry3.get()
                lista.append(otro)
            else :
                lista.append(sexo)
            medico = entry0_1.get()
            lista.append(medico)
            fecha = entry_fecha.get()
            lista.append(fecha)
            pregunta_familia = select_option2.get()
            lista.append(pregunta_familia)
            relacion_familiar = entry3.get()
            lista.append(relacion_familiar)
            diagnostico_familiar = scroll_area.get("1.0", "end-1c")
            lista.append(diagnostico_familiar)
            cambios_comportamiento = select_option3.get()
            lista.append(cambios_comportamiento)
            tipos_cancer = entry8.get()
            lista.append(tipos_cancer)
            pruebas_geneticas = select_option5.get()
            lista.append(pruebas_geneticas)
            resultados_pruebas = scroll_area2.get("1.0", "end-1c")
            lista.append(resultados_pruebas)
            factores_hereditarios = scroll_area3.get("1.0", "end-1c")
            lista.append(factores_hereditarios)

            if not all([nombre, edad, sexo, pregunta_familia, relacion_familiar, diagnostico_familiar, cambios_comportamiento, tipos_cancer, pruebas_geneticas, resultados_pruebas, factores_hereditarios  ]):
                messagebox.showerror("Error", "Para poder continuar, debe llenar todos los campos.")
                return

            # Cambiar a la siguiente pestaña
            notebook.select(1)  # Cambiar el índice según sea necesario
        # Asegúrate de asociar esta función al botón correspondiente
        

        boton_formulario_1 = Button(canvas, image=n_img, border=0, command=lambda: Datos_recabados_1(), cursor="hand2", activebackground="#4d7091", bg="#4d7091")
        canvas.create_window((700, 1220), window=boton_formulario_1)
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


        global lista2
        lista2 = []

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

        def Datos_recabados_2():
            
            respuesta_1 = select_option_1.get()
            lista2.append(respuesta_1)

            respuesta_2 = scroll_area_1.get("1.0", "end-1c")
            lista2.append(respuesta_2)

            respuesta_3 = scroll_area_2.get("1.0", "end-1c")
            lista2.append(respuesta_3)

            respuesta_4 = select_option_2.get()
            lista2.append(respuesta_4)

            respuesta_5 = scroll_area_3.get("1.0", "end-1c")
            lista2.append(respuesta_5)

            respuesta_6 = select_option_3.get()
            lista2.append(respuesta_6)

            respuesta_7 = select_option_4.get()
            lista2.append(respuesta_7)

            respuesta_8 = select_option_5.get()
            lista2.append(respuesta_8)

            respuesta_9 = scroll_area_4.get("1.0", "end-1c")
            lista2.append(respuesta_9)

            # Cambiar a la siguiente pestaña
            notebook.select(2)  # Cambiar el índice según sea necesario
            if not all([respuesta_1, respuesta_2, respuesta_3, respuesta_4, respuesta_5, respuesta_6, respuesta_7, respuesta_8, respuesta_9  ]):
                messagebox.showerror("Error", "Para poder continuar, debe llenar todos los campos.")
                return
        # Asegúrate de asociar esta función al botón correspondiente
        

        boton_formulario_2 = Button(canvas, image=n_img, border=0, command=lambda: Datos_recabados_2(), cursor="hand2", activebackground="#4d7091", bg="#4d7091")
        canvas.create_window((700, 1140), window=boton_formulario_2)
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

        global lista3
        lista3 = []

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
        selectoption_02 = tkinter.StringVar(value=opt_1[0])
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

        def Datos_recabados_3(screen):
            
            respuesta1 = selectoption_1.get()
            lista3.append(respuesta1)
            
            respuesta2 = etr1.get()
            lista3.append(respuesta2)

            respuesta3 = selectoption_02.get()
            lista3.append(respuesta3)

            respuesta4 = etr2.get()
            lista3.append(respuesta4)

            respuesta5 = selectoption_3.get()
            lista3.append(respuesta5)

            # Cambiar a la siguiente pestaña
            if not all([respuesta1, respuesta2, respuesta3, respuesta4, respuesta5  ]):
                messagebox.showerror("Error", "Para poder continuar, debe llenar todos los campos.")
                return
            else :
                screen.destroy()
                datos = CapturarImagen.capturar(lista, lista2, lista3)
        # Asegúrate de asociar esta función al botón correspondiente
        
        button_siguiente = CTkButton(master=app2, text="Siguiente", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=lambda: Datos_recabados_3(app2))
        button_siguiente.place(relx=0.78, rely=0.936, anchor= tkinter.CENTER)
        

    def menu():
        f1 = Frame(app2, width=150, height=900, bg=color)
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

        Botones(0, 50, 'Acerca de', color4,color2, 1, None)
        Botones(0, 90, 'Cáncer de piel', color4,color2, 1, None)
        Botones(0, 130, 'Redes neuronales', color4,color2, 1, None)
        Botones(0, 170, 'Nuevo análisis', color4,color2, 0, None)
        Botones(0, 210, 'Salir', color4,color2, 1, lambda: salir())

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