import os

class CatalogoPeliculas:
    nombre_archivo = "peliculas.txt"

    @classmethod
    def agregar_peliculas(cls, pelicula):
        with open (cls.nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{pelicula}\n")

    @classmethod
    def listar_pelicuas(cls):
        with open (cls.nombre_archivo, "r", encoding="utf-8") as archivo:
            print ("*** Listado de Peliculas ***\n")
            print (archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.nombre_archivo)
        print (f"Archivo eliminado: {cls.nombre_archivo}")
        
