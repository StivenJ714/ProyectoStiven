from pelicula import Pelicula
from catalogo_peliculas import CatalogoPeliculas as catalogo_peliculas

print ("*** App Catalogo de Peliculas ***\n")
opcion = None
while opcion != 4:
    try:
        print ('''*** Opciones ***\n
        1. Agregar pelicula
        2. Listar Peliculas
        3. Eliminar catalogo peliculas
        4. Salir\n''')
        
        opcion = int(input("Selecciona una Opción (1-4): "))

        if opcion == 1:
            nombre_pelicula = input("Escribe el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo_peliculas.agregar_peliculas(pelicula)
        
        elif opcion == 2:
            catalogo_peliculas.listar_pelicuas()

        elif opcion == 3:
            catalogo_peliculas.eliminar_peliculas()

    except Exception as e:
        print (f"\nOcurrio un error: {e}\n")

else:
    print ("Saliendo del programa")

