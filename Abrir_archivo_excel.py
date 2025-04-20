import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def abrir_archivo ():
    Tk().withdraw()
    archivo_excel = askopenfilename(
        title="Abrir Documento Excel",
        filetypes=[("Archivos Excel", "*.xlsx *.xls"), 
                ("Todos los archivos", "*.*")])

    if archivo_excel:
        df = pd.read_excel(archivo_excel)
        print("Archivo cargado correctamente:\n")

        texto = df.head(6).to_string()
    
        file_name = "5_filas.txt"

        with open (file_name, "w", encoding="utf-8") as archivo:
            print(f"Agregando las 6 primeras filas del excel en {file_name}\n")
            archivo.write(f"Se agregaron las 6 primeras filas del Excel {archivo_excel}.\n\n")
            archivo.write(texto)

        with open (file_name, "r", encoding="utf-8") as leer:
            print (f"Leyendo Archivo: {file_name}\n")
            print (leer.read())
        
    else:
        print("No se seleccionó ningún archivo")


if __name__ == "__main__":
    abrir_archivo()

