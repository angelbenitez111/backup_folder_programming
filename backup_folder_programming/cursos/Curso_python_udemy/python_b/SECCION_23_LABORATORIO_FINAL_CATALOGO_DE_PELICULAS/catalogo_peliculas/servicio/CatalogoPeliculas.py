from os import remove

# La idea es que este objeto nos permita interacturactuar con el archivo.txt
# realizar las operaciones sobre el archivo de peliculas.txt

class CatalogoPeliculas:
    # Archivo en donde vamos a guardar los nombres de los archivos - variable de clase
    ruta_archivo = "C:\\Users\\abenitez\\Desktop\\programacion\\python_b\\SECCION_23_LABORATORIO_FINAL_CATALOGO_DE_PELICULAS\\catalogo_peliculas\\catalogo_peliculas.txt"

    #agregar una nueva pelicula al archivo static (archivo en modo append
    # staticmethod no tiene acceso a los metodos de clase, y classmehtod puede acceder directamente al metodo de clase
    @classmethod
    def agregar_peliculas(cls, Pelicula): #<Static>
        with open(cls.ruta_archivo, "a", encoding="utf8") as archivo:
            archivo.write(f"- {Pelicula.nombre}\n")

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, "r", encoding="utf8") as archivo:
            print("Catalodo de Peliculas".center(50,"-"))
            print(archivo.read())

    # import os | os.remove(path)
    @classmethod
    def eliminar(cls):
        remove(cls.ruta_archivo)
        print(f"Archivo eliminado: {cls.ruta_archivo}")
