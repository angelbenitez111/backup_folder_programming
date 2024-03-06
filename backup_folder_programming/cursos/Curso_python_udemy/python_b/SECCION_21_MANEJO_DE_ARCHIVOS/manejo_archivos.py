# w = write

try:
    # Definimos la codificacion de archivo en este caso utf8 para los acentos
    archivo = open("prueba.txt", "w", encoding="utf8")
    # agregamos informacion
    archivo.write("Agregamos informacion al archivo\n")
    archivo.write("Adios")

# SI OCURRE UN ERRROR SE EJECUTA
except Exception as e:
    print(e)

# SIEMPRE SE EJECUTA
finally:
    archivo.close()
    # Una vez ya cerrado ya no se puede agregar más informacion.
    # archivo.write("nuevo texto")
