import FUNCIONESS as fun
from FUNCIONESS import mayoria_de_edad, mayoria_de_edad2
import tkinter as tkr
from tkinter import simpledialog

base = tkr.Tk()
base.title ("")

nombre = simpledialog.askstring ("Nombre", "Ingrese su nombre: ")
edad = simpledialog.askinteger ("Edad", "Ingrese su edad: ")

msg = mayoria_de_edad(nombre, edad)

usar_label = tkr.Label(base, text=msg, font=("Arial",20))
usar_label.pack(pady=30)


base.mainloop()