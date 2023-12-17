import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage, Frame, Label, Button, ttk, scrolledtext, filedialog, messagebox
import os
import numpy as np
import cv2
import crearpdf
import re
from claseCentrar import centerScreen
import getpass
import smtplib
from email.message import EmailMessage
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


letras =["A","B","C","D","E","F","G"]
letras2 =["h","i","j","k","l","m","n","ñ"]
numeros = [1,2,3,4,5,6,7,8,9,0]
simbolos =["#",".","$","&","%"]

def enviarCorreo(destinatario, name):
    correo = "labdetection@gmail.com"
    email = MIMEMultipart()
    email["From"]=correo
    email["To"] = destinatario
    email["Subject"]="Resultados del ánalisis de "+name
    generarContraPDF =random.choice(letras)+str(random.choice(numeros))+str(random.choice(numeros))+random.choice(letras2)+random.choice(letras2)+random.choice(simbolos)+str(random.choice(numeros))+random.choice(letras)+random.choice(letras2)+str(random.choice(numeros))+random.choice(letras2)
    mensaje = "Su contraseña del PDF es: "+generarContraPDF
    email.attach(MIMEText(mensaje,"plain"))
    """with open("./Resultados_LaB_DETECTION.pdf","rb") as archivos:
        parte = MIMEBase("application","octet-stream")
        parte.set_payload(archivos.read())
    encoders.encode_base64(parte)
    parte.add_header("Content-Disposition",f"attachment; filename=Resultados_LaB-Detection.pdf")
    email.attach(parte)"""
    try:
        smtp = smtplib.SMTP("smtp.gmail.com")
        smtp.starttls()
        print(correo)
        smtp.login(correo,"LaBDetection@17.")
        smtp.send_message(email)
        smtp.quit()
        return 1
    except smtplib.SMTPException as e:
        print(f"Error {e}")
        return 0

def validarCorreo(correo):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(email_regex,correo):
        return True
    else:
        return False

def confirmar_imagen(nfile, lista, lista2, lista3):
    global fondo
    color3 = '#48F0FA'
    color5 = '#002266'
    ventana_confirmar = CTk()
    centro = centerScreen()
    fondo = Image.open("./Images/fondoLabel.png")
    fondo = ImageTk.PhotoImage(fondo)
    fondo2 = Image.open("./Images/fondoLabel1.png")
    fondo2 = ImageTk.PhotoImage(fondo2)
    fondo3 = Image.open("./Images/fondoLabel2.png")
    fondo3 = ImageTk.PhotoImage(fondo3)
    ventana_confirmar.geometry(centro.situarLaB(500,300)) #Colocamos el tamaño de la ventana y en qué posición deseamos que aparezca (derecha+abajo)
    ventana_confirmar.config(bg=color5)
    ventana_confirmar.title('Confirmar')
    ventana_confirmar.iconbitmap("Images\logo.ico")
    labelfondo = Label(ventana_confirmar, image=fondo2)
    labelfondo.place(x=-1,y=-1)
    lbl_text= Label(ventana_confirmar, text= "Ingrese el correo del paciente", background=color5, fg='white', font= ("Helvetica", 20))
    lbl_text.place(x=70, y=30)
    entry_correoDoc = customtkinter.CTkEntry(ventana_confirmar, placeholder_text="ejemplo_doctor@outlook.com", width=250, height=40, border_width=2, corner_radius=10, fg_color="#FFFFFF",text_color="#000000",border_color=color3)
    entry_passDoc = customtkinter.CTkEntry(ventana_confirmar, placeholder_text="●●●●●●●●●", width=250, height=40, border_width=2, corner_radius=10, fg_color="#FFFFFF",text_color="#000000",border_color=color3,show="●")
    lbl_advice = Label(ventana_confirmar, text="*Por su seguridad siempre se pedirá su contraseña", bg=color5,fg="white")
    entry_correo = customtkinter.CTkEntry(ventana_confirmar, placeholder_text="ejemplo_correo@outlook.com", width=250, height=40, border_width=2, corner_radius=10, fg_color="#FFFFFF",text_color="#000000",border_color=color3)
    entry_correo.place(relx=0.30,rely=0.45)
    alertLabel = Label(ventana_confirmar, text="*Formato de correo incorrecto", fg="#ff004e",bg=color5)
    
    """def validacion():
        nombre="Juan Pérez"
        correo=entry_correoDoc.get()
        
        if validarCorreo(correo) and correo!="" and entry_passDoc.get()!="":
            if enviarCorreo(correo, entry_passDoc.get(),correoSend, nombre) == 1:
                labelfondo.configure(image=fondo3)
                entry_correoDoc.place_forget()
                entry_passDoc.place_forget()
                lbl_advice.place_forget()
                lbl_text.configure(text="¡Correo enviado exitosamente!")
                ventana_confirmar.after(2000,ventana_confirmar.destroy)

        elif correo=="" or entry_passDoc.get()=="":
            alertLabel.configure(text="*Llene correctamente los campos")
            alertLabel.place(relx=0.3,rely=0.75)
            
        else:
            alertLabel.place(relx=0.3,rely=0.75)
        ventana_confirmar.after(2000,ocultarEtiqueta)"""
    #button_continuar2 = CTkButton(master=ventana_confirmar, text="Continuar", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=validacion)
    
    def ocultarEtiqueta():
        alertLabel.place_forget()
        
    

    def buttonPress(button):
        global correoSend
        correoSend = entry_correo.get()

        if validarCorreo(correoSend):
            if enviarCorreo(correoSend,"Juan Perez") == 1:
                entry_correo.place_forget()
                labelfondo.configure(image=fondo3)
                button.place_forget()
                lbl_text.configure(text="¡Correo enviado exitosamente!")
                ventana_confirmar.after(2000,exit)

        else:
            
            alertLabel.place(relx=0.20,rely=0.6)
            
            print("Formato de correo incorrecto")
        ventana_confirmar.after(2000,ocultarEtiqueta)

    button_continuar = CTkButton(master=ventana_confirmar, text="Continuar", border_width=1.5 ,border_color=color3, font=('Arial', 16), height=50, command=lambda:buttonPress(button_continuar))
    button_continuar.place(relx=0.50, rely=0.88, anchor= tkinter.CENTER) 
    
    ventana_confirmar.mainloop()


    

    #return ventana_confirmar

nfile = 'IMD004.bmp'
confirmar_imagen(nfile,[],[],[])