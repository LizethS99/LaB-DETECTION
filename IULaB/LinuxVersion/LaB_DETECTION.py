#Home
import tkinter
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, messagebox, scrolledtext
import os
import sys
import Forms 
import Acercade
from win32api import GetSystemMetrics
from claseCentrar import centerScreen

def funcion_principal():
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green


    color = '#003F79' # color menú lateral
    color2 = '#001E6F' #Azul muy oscuro
    color3 = '#48F0FA' #Azul muy claro
    color4 = '#E8FBFC' #Letras en los botones
    color5 = '#0D2764'

    app = customtkinter.CTk()
    centro = centerScreen()
    app.geometry(centro.situarLaB(1200,700)) #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
    app.minsize(1100,700)
    app.maxsize(1400, 700)
    app.config(bg=color5)
    app.title('LaB-DETECTION')
    ruta = 'Images\Segundologo.png'
    ruta2 = 'Images\\fondo.png'
    imagen_logo = PhotoImage(file=ruta)
    #app.iconbitmap("Images\logo.ico")
    fondo = PhotoImage(file=ruta2)
    lbl_fondo = Label(image=fondo).place(x=0, y=0)

    def menu():
        f1 = Frame(app, width=150, height=900, bg=color)
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

        def Aboutus(screen, imagen1, imagen2):
            for widget in screen.winfo_children():
                widget.destroy()

            pantallanueva3 = Acercade.Acerca_de(app, imagen1, imagen2)

        Botones(0, 50, 'Acerca de', color4,color2, 1, lambda: Aboutus(app, ruta, ruta2))
        Botones(0, 90, 'Cáncer de piel', color4,color2, 1, None)
        Botones(0, 130, 'Redes neuronales', color4,color2, 1, None)
        Botones(0, 170, 'Nuevo análisis', color4,color2, 0, None)
        Botones(0, 210, 'Salir', color4,color2, 1, salir)

        def dele():
            f1.destroy()
        global img2
        imagen = Image.open('Images\close.png')
        nuevo_tam = (30, 30)
        imagen_nueva = imagen.resize(nuevo_tam)
        img2 = ImageTk.PhotoImage(imagen_nueva)
        Button(f1, image=img2, command=dele, border=0, activebackground=color, bg=color, cursor="hand2").place(x=5, y=10)

    frame = Frame(app, width=80, height=900, bg=color)
    frame.place(x=0, y=0)
    imagen2 = Image.open('Images\open4.png')
    nuevo_tam2 = (35, 35)
    imagen_nueva2 = imagen2.resize(nuevo_tam2)
    img1 = ImageTk.PhotoImage(imagen_nueva2)
    Button(app, image=img1, border=0, activebackground=color, bg=color, command=menu, cursor="hand2").place(x=15, y=15)

    def default_home():
        label = CTkLabel(app, image=imagen_logo, fg_color="#00042A", text='')
        label.pack()
        label.place(relx=0.2, rely=0.2)

    default_home()

    def button_function():
        print("button pressed")
        # Función para mostrar la ventana de Términos y Condiciones
        def mostrar_ventana_terminos():
            if not os.path.exists("aceptado.txt"):
                ventana_terminos = CTk()
                ventana_terminos.geometry('600x450+530+310')
                ventana_terminos.title('Términos y Condiciones')

                # Crear un Frame dentro de la ventana con área de desplazamiento
                frame_terminos = CTkFrame(ventana_terminos)
                frame_terminos.pack(fill='both', expand=True)
                #frame_terminos.configure(height=80, width=70)

                # Crear un área de desplazamiento (scroll) y un widget de texto
                scroll_area = scrolledtext.ScrolledText(frame_terminos, wrap=tkinter.WORD)
                scroll_area.pack(fill='both', expand=True)
                #scroll_area.configure(height=450, width=250)

                # Agregar los términos y condiciones al área de desplazamiento
                terminos_texto = """\tLaB-DETECTION Términos y Condiciones de Uso\n \tFecha de entreada en vigor: 27-noviembre-2023\n 1. ACEPTACIÓN DE LOS TÉRMINOS Y CONDICIONES. \nAl acceder y utilizar LaB-DETECTION aceptas y te comprometes a cumplir con estos Términos y Condiciones. Si no estás de acuerdo con alguno de los términos aquí establecidos, te rogamos que no utilices la herramienta.\n
                2. USO DEL SERVICIO\n 2.1.Al hacer uso de la aplicación se compromete a no almacenar las imágenes capturadas mediante la aplicación. De no ser así los desarrolladores no se harán responsable spor el uso que se le de a dichas imágenes. Se hace responsable de todas las actividades que ocurran bajo el periodo en el que se haga uso del software.\n 2.2.Conducta del usuario. Se compromete a utilizar el servicioo de manera ética y cumplir con todas las leyes y regulaciones aplicables.\n
                3. CONTENIDO\n 3.1.Derechos de propiedad. El contenido disponible a través del servicio puede estar protegido por derechos de propiedad intelectual. No puede copiar, modificar, distribuir, vender o alquilar ningun contenido del servicio sin el permiso explicíto de los desarrolladores de LaB-DETECTION.\n
                4. PRIVACIDAD\n 4.1.Recopilación de datos. El servicio puede recopilar información personal de acuerdo a nuestra Política de Privacidad.\n
                5. LIMITACIÓN DE RESPONSABILIDAD. \n 5.1.Uso bajo su propio riesgo. LaB-DETECTION es una herramienta sin garantía de ningún tipo, el Instituto Politécnico Nacional y LaB-DETECTION no se hace responsable de daños directos, indirectos, incidentales, especiales o consecuentes del uso de la herramienta.\n
                6. MODIFICACIONES DE LOS TÉRMINOS Y CONDICIONES\n 6.1.Actualizaciones. LaB-DETECTION se reserva el derecho a modificar estos términos y condiciones en cualquier momento. Los cambios entrarán en vigor una vez publicada la herramienta. El uso de la herramienta después de dichos cambios constituirá la aceptación de los nuevos términos.\n
                7. LEY APLICABLE\n 7.1.Jurisdicción. Estos términos y condiciones se rigen por y se interpretan de acuerdo con las leyes de Los Estados Unidos Mexicanos. Cualquier disputa derivada de estos Términos y condiciones estará sujeta a la jurisdicción exclusiva de los tribunales de Los Estados Unidos Mexicanos.\n
                8. AVISO LEGAL.\n 8.1.Propósito educativo. Este proyecto es puramente educativo e informativo y no pretende reemplazar el diagnóstico médico ni el asesoramiento de profesionales de la salud. Los usuarios deben comprender que el proyecto es una herramienta para la detección y concientización sobre el cáncer de piel del tipo melanoma, pero no debe utilizarse com un sustituto de la atención médica profesional.\n
                9. RESPONSABILIDAD DEL USUARIO\n 9.1.Interpretación de los resultados. El usuario es el único responsable de la interpretación y aplicación de los resultados proporcionados por LaB-DETECTION y los algoritmos desarrollados para esta implementación.\n 9.2.Asesoramiento para médico no especialista. Se recomienda encarecidamente a los usuarios y médicos no especializados consultar a un profesional en el área dermatologica antes de tomar cualquier decisión o tratamiento basado en los resultados de software.\n
                10. PROPÓSITO DEL SERVICIO.\n 10.1.Para médicos. LaB-DETECTION se ofrece como una herramienta de apoyo para profesionales de la salud y no debe reemplazar el diagnóstico médico ni el asesoramiento de profesionales de la salud.\n
                """
                scroll_area.insert('1.0', terminos_texto)

                def aceptar_terminos():
                    with open("aceptado.txt", "w") as archivo:
                        archivo.write("Aceptado")
                    ventana_terminos.destroy()
                boton_aceptar = CTkButton(frame_terminos, text="Aceptar", command=aceptar_terminos, height=30, width=20)
                boton_aceptar.pack()
                ventana_terminos.mainloop()
            else:
                # Los términos y condiciones ya se han aceptado
                print("Los términos y condiciones ya se han aceptado.")
                def Pantalla(screen):
                    screen.destroy()
                    pantallanueva = Forms.NewPantalla()
            Pantalla(app)
        mostrar_ventana_terminos()

    button = customtkinter.CTkButton(master=app, text="Iniciar", border_width=1.5 ,border_color=color3, font=('Arial', 20), height=50, command=button_function)
    button.place(relx=0.5, rely=0.7, anchor= tkinter.CENTER)

    app.mainloop()

if __name__ == "__main__":
    # Llama a la función principal si se ejecuta este script directamente
    funcion_principal()