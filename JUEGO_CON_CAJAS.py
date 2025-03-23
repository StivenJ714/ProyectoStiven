import random
import tkinter as tk
from tkinter import simpledialog, messagebox

VIDA_PC = 90
VIDA_USUA = 100

Sables_pc = 3
Sables_usua = 3

#Mejora de Proyecto2
juego_activo = True

while VIDA_PC > 0 and VIDA_USUA > 0 and juego_activo == True:
    GO1 = messagebox.showinfo("¿Continuar?", "DALE ACEPTAR PARA VER QUIEN ATACA: ")
    Empezar = random.randint(1,2)
    if Empezar == 1:
        messagebox.showwarning("infomación", "ATACA PC.")
        ataca_pc = random.randint(1,2)
        if ataca_pc == 1:
            VIDA_USUA -= 10
        elif ataca_pc == 2 and Sables_pc > 0:
            VIDA_USUA -= 15
            Sables_pc -= 1
        else:
            messagebox.showinfo("Sin Sables", "PC NO TIENE SABLES DISPONIBLES, ATACA POR DEFECTO CON LANZA")
            VIDA_USUA -= 10
    
    else:
        messagebox.showwarning("infomación", "ATACA USUARIO")
        ataque_usua = simpledialog.askstring("¿Que ataque usaras?", "SELECCIONE ATAQUE: [A]LANZA, [B]SABLE: ")
        if ataque_usua is None:
            messagebox.showinfo ("Cerrando Juego", "ÉL JUGADOR CANCELO EL JUEGO, CERRANDO JUEGO....")
            break
        else:
            ataque_usua = ataque_usua.upper()

        while ataque_usua not in ["A","B"]:
            messagebox.showwarning("Error", f"OPCIÓN NO VALIDA, SELECCIONASTE: {ataque_usua}")
            ataque_usua = simpledialog.askstring("¿Que ataque usaras?", "SELECCIONE ATAQUE: [A]LANZA, [B]SABLE: ")
            if ataque_usua is None:
                messagebox.showinfo ("Cerrando Juego", "ÉL JUGADOR CANCELO EL JUEGO, CERRANDO JUEGO....")
                #Mejora
                juego_activo = False
                break
            else:
                ataque_usua = ataque_usua.upper()
        
        if ataque_usua == "A":
            VIDA_PC -= 10
        elif ataque_usua == "B":
            if Sables_usua > 0:
                VIDA_PC -= 15
                Sables_usua -= 1
                messagebox.showwarning ("Sables Disponibles", f"TE QUEDAN {Sables_usua} SABLES")
            else: #Mejora para en el caso de que no tenga sables y no pierda el turno.
                messagebox.showinfo("Sin Sables", "USUARIO NO TIENE SABLES DISPONIBLES, ATACA POR DEFECTO CON LANZA")
                VIDA_PC -= 10

    messagebox.showinfo ("Vida", f"VIDA PC {VIDA_PC} - VIDA USUARIO {VIDA_USUA}")

if VIDA_PC > VIDA_USUA:
    messagebox.showinfo ("Ganador", "TE GANO LA PC")
elif VIDA_PC == 90 and  VIDA_USUA == 100:
    messagebox.showinfo ("Finalizando", "EL JUEGO TERMINO.")
else:
    messagebox.showinfo ("Ganador", "EL GANADOR ES EL USUARIO")