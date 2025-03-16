import tkinter as tkr
from tkinter import simpledialog

# Crear la ventana principal
base = tkr.Tk()
# PARA PONER TITULO A LA VENTANA PRINCIPAL
base.title("djfngdher")

# Mostrar el input box
ingreso_dato = simpledialog.askinteger("ttttXX", "ppppYYY")

# Muestra el resultado en un Label
usar_label = tkr.Label(base, text=ingreso_dato,font=("Arial",20))
usar_label.pack(pady=30)

# Cerrar la ventana
#base.destroy()

#bucle eterno hasta que el usuario cierre la ventana
base.mainloop()