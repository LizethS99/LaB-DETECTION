from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, Spacer
from reportlab.lib.units import inch

from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
from tkinter import  messagebox
import Resultados

def crear_pdf(file_path, nfile):
    texto = "Espere un momento, los resultados se están obteniendo."    
    messagebox.showinfo("Cargando...", texto)

    # Crear un documento PDF
    pdf = SimpleDocTemplate(file_path, pagesize=letter)

    # Lista para contener los elementos del PDF
    elementos = []

    # Encabezado con una imagen
    imagen_encabezado = ".\Images\LogoDocumento.png"  
    imagen = Image(imagen_encabezado, width=2*inch, height=1*inch, hAlign='LEFT')
    elementos.append(imagen)

    espacio = 0.5 * inch

    # Título en el cuerpo
    estilo_titulo = getSampleStyleSheet()["Title"]
    elementos.append(Paragraph("DATOS OBTENIDOS MEDIANTE LA TOMA DE UNA  IMAGEN DIGÍTAL", estilo_titulo))
    elementos.append(Spacer(1, espacio))

    # Breve explicación
    histo = "Historial clínico:"
    elementos.append(Paragraph(histo, style=ParagraphStyle(name='Normal', fontSize=12)))
    elementos.append(Spacer(1, espacio))
    explicacion = """Dentro de este espacio voy a poner todos los datos que se ingresaron desde el foormulario, la verdad es que todavía no sé cómo voy a lograr eso pero pues vemos. \nTambién quiero ver hasta dónde se escribe el texto y para completar ahí va una canción de
    la Taylor, amonos Draw the cat eye, sharp enough to kill a man
You did some bad things, but I'm the worst of them
Sometimes I wonder which one will be your last lie
They say looks can kill and I might try
I don't dress for women
I don't dress for men
Lately I've been dressing for revenge
I don't start it but I can tell you how it ends
Don't get sad, get even
So on the weekends
I don't dress for friends
Lately I've been dressing for revenge
She needed cold hard proof so I gave her some
She had the envelope, where you think she got it from?
Now she gets the house, gets the kids, gets the pride
Picture me thick as thieves with your ex-wife
And she looks so pretty
Driving in your Benz
Lately she's been dressing for revenge
She don't start it, but she can tell you how it ends
Don't get sad, get even
So on the weekends
She don't dress for friends
Lately she's been dressing for revenge
Ladies always rise above
Ladies know what people want
Someone sweet and kind and fun
The lady simply had enough
While he was doing lines
And crossing all of mine
Someone told his white collar crimes to the FBI
And I don't dress for villains
Or for innocents
I'm on my vigilante shh again
I don't start it, but I can tell you how it ends
Don't get sad, get even
So on the weekends
I don't dress for friends
Lately I've been dressing for revenge"""
    elementos.append(Paragraph(explicacion, style=ParagraphStyle(name='Normal', fontSize=12)))
    elementos.append(Spacer(1, espacio))

    texto1 = "De acuerdo con el método ABCD se encontraron los siguientes parámetros:"
    elementos.append(Paragraph(texto1, style=ParagraphStyle(name='Normal', fontSize=12)))
    espacio2 = 0.2 * inch
    elementos.append(Spacer(1, espacio2))
    texto2 = "Asimetría:"
    elementos.append(Paragraph(texto2, style=ParagraphStyle(name='Normal', fontSize=12)))

    puntuacion_texto = "Puntuación:"
    factor_texto = "Factor de corrección:"
    
    # Agrega espacio antes de la tabla
    
    elementos.append(Spacer(1, espacio2))

    # Crea una tabla para organizar los fragmentos de texto
    datos = [["ASIMETRÍA"],
        [puntuacion_texto, "__________", factor_texto, "________ 1,3"],
        ["BORDES"],
        [puntuacion_texto, "__________", factor_texto, "________ 0,1"],
        ["COLORES"],
        [puntuacion_texto, "__________", factor_texto, "________ 0,5"],
        ["DIÁMETRO"],
        [puntuacion_texto, "__________", factor_texto, "________ 0,5"]
    ]

    tabla = Table(datos, colWidths=[1.5*inch, 1*inch, 2*inch, 1.5*inch], hAlign='LEFT')
    
    # Aplica estilos a la tabla
    estilo_tabla = TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    tabla.setStyle(estilo_tabla)

    # Agrega la tabla a la lista de elementos
    elementos.append(tabla)
    elementos.append(Spacer(1, espacio))
    texto2 = "Índice dermatoscópico total:"
    elementos.append(Paragraph(texto2, style=ParagraphStyle(name='Normal', fontSize=12)))
    elementos.append(Spacer(1, espacio))

    # Crea una tabla2 para organizar los fragmentos de texto
    datos2 = [
        [" <4,75 ", " 4,8 - 5,45 ", " >5,45 "],
        [" Benigna ", " Sospechosa", " Maligna "]
    ]

    tabla2 = Table(datos2, colWidths=[1.5*inch, 1.5*inch, 1.5*inch], hAlign='LEFT')
    
    # Aplica estilos a la tabla
    estilo_tabla = TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    tabla2.setStyle(estilo_tabla)

    # Agrega la tabla a la lista de elementos
    elementos.append(tabla2)
    elementos.append(Spacer(1, espacio))

    # Datos de la tabla (se pueden modificar)
    """datos_tabla = [
        ["A", "B", "C", "D", "E"],
        ["1", "2", "3", "4", "5"],
        ["6", "7", "8", "9", "10"],
        ["11", "12", "13", "14", "15"]
    ]

    # Configurar estilos para la tabla
    estilo_tabla = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Crear la tabla
    tabla = Table(datos_tabla)
    tabla.setStyle(estilo_tabla)
    elementos.append(tabla)"""
    elementos.append(Spacer(1, espacio))
    # Pie de página con advertencia
    advertencia = "El contenido de este documento no suple el diagnóstico de un médico"
    elementos.append(Paragraph(advertencia, style=ParagraphStyle(name='Normal', fontSize=10)))

    # Construir el PDF
    pdf.build(elementos)
    pantallanueva = Resultados.Res(nfile, file_path)


