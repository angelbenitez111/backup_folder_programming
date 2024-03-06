from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None
while opcion != 4:

    try:
        opcion = int(input("1. Agregar película.\n2. Listar peliculas.\n3. Eliminar catalogo de películas\n4. Salir "
                       "\nEscribe tu opción (1-4): "))

        if opcion == 1:
            nombre_pelicula = input("Proporciona el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_peliculas(pelicula)

        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()

        elif opcion == 3:
            CatalogoPeliculas.eliminar()

    except Exception as e:
        print(f"Ocurrio un error {e}")
        opcion = None


else:
    print("Salimos del programa...")
