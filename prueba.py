import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import PhotoImage

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

color = '#1B4CA4'  # Azul medio
color2 = '#122E60'  # Azul muy oscuro
color3 = '#48F0FA'  # Azul muy claro
color4 = '#E8FBFC'  # Letras en los botones

app = CTk()
app.geometry('1200x700+250+110')
app.minsize(1100, 700)
app.config(bg=color2)
app.title('LaB-DETECTION')

def button_function():
    print("button pressed")

button = CTkButton(master=app, text="Iniciar", border_width=1, border_color=color3, command=button_function)
button.place(relx=0.5, rely=0.5, anchor='center')

# Define una función para ajustar el tamaño del frame cuando la ventana se redimensiona
def resize(event):
    frame.grid(row=0, column=0, sticky='nsew', padx=640, pady=3)

app.bind('<Configure>', resize)

# Calcular el ancho en píxeles correspondiente a 3 cm
cm_to_pixels = 0.393701  # Relación de centímetros a píxeles (dpi estándar)
width_in_cm = 3  # Ancho en centímetros
width_in_pixels = int(width_in_cm * cm_to_pixels)

frame = CTkFrame(master=app, fg_color=color4, width=width_in_pixels)
frame.grid(column=0, row=0, sticky='ns')

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

app.mainloop()
