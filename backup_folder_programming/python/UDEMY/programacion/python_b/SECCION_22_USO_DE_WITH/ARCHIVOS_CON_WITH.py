# alternativa a try finally, pesta estructura abre y cierra el archivo de manera automatica
from ManejoArchivos import ManejoArchivos

# with open("prueba.txt", "r", encoding="utf8") as archivo:
with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())


#Utiliza los metodos __enter__ y __exit__ para abrir y cerrar el archivo