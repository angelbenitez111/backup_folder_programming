archivo = open("prueba.txt", "r", encoding="utf8")

# print(archivo.read())

# Leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# Leer linear completas
# print(archivo.readline())

# iterar el archivo

# iterar el archivo:
# for linea in archivo:
#    print(linea)

# Leer todas las lineas con un solo metodo (regresa una lista)
# print(archivo.readlines()[2])

# Copiar un archivo a uno nuevo
archivo2 = open("copia.txt", "a", encoding="utf8")
# Leemos todo el contenido del archivo original y lo escribimos en la copia.
archivo2.write(archivo.read())

archivo2.close()
archivo.close()
print("Proceso concluido")
