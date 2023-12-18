#Modulo de cifrado de archivo pdf
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from cryptography.fernet import Fernet
from PyPDF2 import PdfReader, PdfWriter

# Contenido para el PDF
contenido = "Hola, ¿Cómo te encuentras?. Este es un PDF cifrado que nos sirve de prueba para ver cómo se pide una contraseña en un pdf."

# Crear el PDF
pdf_file = "documento.pdf"

doc = SimpleDocTemplate(pdf_file, pagesize=letter)
elements = []

# Agregar contenido al PDF
paragraph = Paragraph(contenido)
elements.append(paragraph)

doc.build(elements)

# Cifrar el PDF
def cifrar_pdf(pdf_file_path, password):
    try:
        # Abrir el PDF original
        pdf = PdfReader(open(pdf_file_path, "rb"))

        # Crear un PDF cifrado
        pdf_cifrado = PdfWriter()

        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            pdf_cifrado.add_page(page)

        # Crear una clave Fernet
        clave = Fernet.generate_key()
        fernet = Fernet(clave)

        # Convertir la contraseña a cadena (string)
        password_str = password.decode('utf-8')
        print(password_str)
        # Cifrar la contraseña
        #password_cifrado = fernet.encrypt(password_str.encode('utf-8'))
        #print(password_cifrado) <-- en caso de que se quiera cifrar la contraseña también

        # Establecer la contraseña del PDF en formato de cadena
        pdf_cifrado.encrypt(password_str, use_128bit=True) # aquí se le agrega password_cifrado.decode('utf-8')

        # Guardar el PDF cifrado
        with open("documento_cifrado.pdf", "wb") as pdf_cifrado_file:
            pdf_cifrado.write(pdf_cifrado_file)

        print("PDF cifrado exitosamente.")
    except Exception as e:
        print("Error al cifrar el PDF:", str(e))

# Cifrar el PDF utilizando la contraseña "Melanoma" en formato de bytes
cifrar_pdf(pdf_file, b'Melanoma')