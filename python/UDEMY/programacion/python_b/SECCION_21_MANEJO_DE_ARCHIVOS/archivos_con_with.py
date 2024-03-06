from ManejoArchivos import ManejoArchivos
# Forma simplificada del try except o un administrador de recursos
with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())

# Utiliza dos metodos
# __enter__ para abrir el archivo
# __exit__ para cerrar el archivo