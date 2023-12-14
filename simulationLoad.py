from procesoLoad import PantallaCarga
from ultralytics import YOLO
import threading
def modelLoading():
    global model
    model = YOLO('./runs/runs/classify/train9/weights/last.pt')

def funcion1(text):
    PantallaCarga(text,1)

def funcion3(text):
    PantallaCarga(text,1)

hilo1 = threading.Thread(target=modelLoading)
hilo2 = threading.Thread(target=lambda:funcion1("Cargando Modelo..."))

hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()



clases = ["Atipica", "Común", "Melanoma"]
#PRUEBAS con imagenes
def extractClass(verbose):
    result = ""
    finalClass = ""
    for i in verbose:
        if i == ",":
            break
        result+=i
    for i in result:
        if i ==" ":
            break
        finalClass+=i
    if finalClass=="Common":
        return clases[1]
    elif finalClass=="Atypical":
        return clases[0]
    else:
        return clases[2]

def funcion2():
    resultado = model.predict("./IMD004.bmp")
    print("La imagen fue clasificada como: "+extractClass(resultado[0].verbose()))



# Crear dos hilos
hilo2 = threading.Thread(target=lambda:funcion1("Analizando imagen..."))
hilo3 = threading.Thread(target=funcion2)

# Iniciar ambos hilos al mismo tiempo
hilo2.start()
hilo3.start()

# Esperar a que ambos hilos terminen
hilo2.join()
hilo3.join()

print("Ambos hilos han terminado")