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
import Bordes2

def crear_pdf(file_path, nfile, lista, lista2, lista3, lista4):
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
    elementos.append(Paragraph("INFORME DE RESULTADOS OBTENIDOS MEDIANTE LA TOMA DE UNA  IMAGEN DIGÍTAL", estilo_titulo))
    elementos.append(Spacer(1, espacio))

    # Breve explicación
    histo = "Historial clínico:"
    elementos.append(Paragraph(histo, style=ParagraphStyle(name='Normal', fontSize=12)))
    elementos.append(Spacer(1, espacio))
    explicacion = f"""Nombre del paciente:{lista[0]} <br /><br /> Edad: {lista[1]} <br /><br /> Sexo: {lista[2]} <br /><br /> Médico que atendió: {lista[3]}  <br /><br /> Fecha: {lista[4]}  <br /><br />
    ¿El paciente mencionó si algún miembro de su familia ha sido diagnósticado previamente con melanoma? {lista[5]} <br /><br />
    Si la respuesta fue "Sí", ¿cuál es la relación familiar y cuándo fue el diagnóstico? {lista[6]} <br /><br /> 
    ¿El paciente refiere si existen antecendentes familiares o directo del paciente si lo a llevado a cambios en el comportamiento? {lista[7]} <br /><br />
    ¿Existen antecedentes familiares de cáncer que podrían estar relacionados con un mayor riesgo de melanoma?{lista[8]} ¿Cuál? {lista[9]} <br /><br />
    ¿El paciente se han realizado pruebas genéticas dentro de su familia para detectar mutaciones relacionadas con el melanoma u otros cánceres? {lista[10]} <br /><br />
    Si es así, ¿cuáles fueron los resultados? {lista[11]} <br /><br /> 
    ¿Existen otros factores hereditarios que puedan aumentar el riesgo de melanona? {lista[12]} <br /><br />
    El paciente refiere que {lista2[0]} ha tenido alguna lesión cutánea que se haya removido. En el caso de que la respuesta haya sido si, el motivo de la remoción fue {lista2[1]} <br /><br />
    Refiere que su historial sobre la exposición solar es {lista2[2]}. El paciente menciona que {lista2[3]} ha notado cambios los cuales son: {lista2[4]}. Se menciona que {lista2[5]} ha tenido algún episodio previo de quemadura solar grave. <br /><br />
    {lista2[6]} se han presentado otros problemas de la piel. De igual forma se menciona que {lista2[7]} se ha tenido alguna biopsia de lesión cutánea que ha sido sospechosa de melanoma. <br /><br />
    En caso de haberse realizado la biopsia los resultados que se obtuvieron fueron: {lista2[8]} . <br /><br />
    Por otro lado, el paciente refiere que {lista3[0]} ha usado camas de bronceado de manera regular. Se menciona que la frecuencia con la que se realiza autoexámenes de la piel es de {lista3[1]}. <br /><br />
    Se hace mención que {lista3[2]} utiliza protección solar de manera regular. Su rutina de protección solar es {lista3[3]}. También se hace mención que {lista3[4]} ha recibido educación sobre detección de melanoma o cómo se realiza un autoexámen de la piel.
"""
    elementos.append(Paragraph(explicacion, style=ParagraphStyle(name='Normal', fontSize=12)))
    elementos.append(Spacer(1, espacio))

    texto1 = "De acuerdo con el método ABCD se encontraron los siguientes parámetros:"
    elementos.append(Paragraph(texto1, style=ParagraphStyle(name='Normal', fontSize=12)))
    espacio2 = 0.2 * inch
    elementos.append(Spacer(1, espacio2))
    texto2 = f"Diametro de la lesión: {lista4[0]}"
    elementos.append(Paragraph(texto2, style=ParagraphStyle(name='Normal', fontSize=12)))

    puntuacion_texto = "Puntuación:"
    factor_texto = "Factor de corrección:"
    
    # Agrega espacio antes de la tabla
    
    elementos.append(Spacer(1, espacio2))
    asimetri = 1
    facto_asimetria = asimetri * 1.3
    bordes = Bordes2.bordes(nfile)
    facto_bordes = int(bordes) * 0.1
    colores = 4
    facto_colores = colores * 0.5
    estructuras = int(lista4[1])+int(lista4[2])+int(lista4[3])+int(lista4[4])+int(lista4[5])
    estructuras2 = float(estructuras)
    factorestruc = estructuras2 * 0.5
    # Crea una tabla para organizar los fragmentos de texto
    datos = [["ASIMETRÍA"],
        [puntuacion_texto + "0 a 2", f"____{asimetri}_____", factor_texto + "1,3", f"{facto_asimetria}"],
        ["BORDES"],
        [puntuacion_texto + "0 a 8", f"____{bordes}_____", factor_texto + "0,1", f"{facto_bordes}"],
        ["COLORES"],
        [puntuacion_texto + "1 a 6", f"____{colores}_____", factor_texto + "0,5", f"{facto_colores}"],
        ["DIF. ESTRUCTURAS"],
        [puntuacion_texto + "1 a 5", f"____{estructuras}_____", factor_texto + "0,5", f"{factorestruc}"]
    ]

    tabla = Table(datos, colWidths=[2*inch, 1.5*inch, 2*inch, 1.5*inch], hAlign='LEFT')
    
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
    dermaTotal = facto_asimetria + facto_bordes + facto_colores + factorestruc
    indice = f"Índice dermatoscópico total: {dermaTotal}"
    elementos.append(Paragraph(indice, style=ParagraphStyle(name='Normal', fontSize=12)))
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
    if dermaTotal < 4.75 :
        res = f"Resultados según el ABCD: {dermaTotal} Benigna "
    elif dermaTotal >4.8 and dermaTotal <5.45 :
        res = f"Resultados según el ABCD: {dermaTotal} Sospechosa "
    elif dermaTotal >5.45:
        res = f"Resultados según el ABCD: {dermaTotal} Maligna "
    elementos.append(Paragraph(res, style=ParagraphStyle(name='Normal', fontSize=10)))
    elementos.append(Spacer(1, espacio))
    # Pie de página con advertencia
    advertencia = "El contenido de este documento no suple el diagnóstico de un médico"
    elementos.append(Paragraph(advertencia, style=ParagraphStyle(name='Normal', fontSize=10)))

    # Construir el PDF
    pdf.build(elementos)
    
    pantallanueva = Resultados.Res(nfile, file_path,lista[0])


