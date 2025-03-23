import random
import tkinter as tkr
from tkinter import simpledialog, messagebox, Toplevel

VIDA_PC = 90
VIDA_USUA = 100

sables_pc = 3
sables_usua = 3

juego_activo = True

historial_ataques = []

def historial ():
    global historial_ven

    historial_ven = Toplevel(base)
    historial_ven.title("Historial de ataques")
    historial_ven.geometry("430x800")

    for accion in historial_ataques:
        etiqueta_histo = tkr.Label(historial_ven, text=accion, font=("Arial", 12, "bold"), fg="black")
        etiqueta_histo.pack(pady=5)
       

def iniciar_juego ():
    global ventana_hija, Boton_iniciar
    Boton_entrar.config(state=tkr.DISABLED)

    ventana_hija = Toplevel(base)
    ventana_hija.title("Empezando el Juego")
    ventana_hija.geometry("420x160")

    etiqueta1 = tkr.Label(ventana_hija, text="⚔ Juego de Azar, Buena suerte! ⚔", font=("Arial",15,"bold"), fg="#02c826")#VERDE
    etiqueta1.pack(pady=20)

    Boton_iniciar = tkr.Button(ventana_hija, text="Iniciar", font=("Arial",11,"bold"), activebackground="lightblue", fg="Green", command=Iniciar)
    Boton_iniciar.pack(pady=10)

def Iniciar ():
    global etiqueta_g, Boton_conti, etiqueta_ataque, Boton_historial, opcion_select, frame_radios, etiqueta_vida
    Boton_iniciar.config(state=tkr.DISABLED)

    ventana_hija.geometry("420x600")
    
    etiqueta_g = tkr.Label(ventana_hija, text="🛡 Empieza el Juego 🛡\nDale Continuar para ver quien Ataca", font=("Arial",15,"bold"), fg="Purple" )
    etiqueta_g.pack(pady=10)

    frame_botones = tkr.Frame(ventana_hija)
    frame_botones.pack(pady=10)

    Boton_conti = tkr.Button(frame_botones, text="Continuar", font=("Arial",11,"bold"), fg="Green", activebackground="lightblue", command=continuar)
    Boton_conti.pack(side = "left", padx=10, pady=10)

    Boton_historial = tkr.Button(frame_botones, text="Historial", font=("Arial",11,"bold"), fg="Purple", activebackground="lightblue", command=historial)
    Boton_historial.pack(side = "left", padx=10, pady=10)

    etiqueta_ataque = tkr.Label(ventana_hija, text="", font=("Arial",15,"bold"), fg="#5697b0")
    etiqueta_ataque.pack(pady=10)

    etiqueta_vida = tkr.Label(ventana_hija, text="", font=("Arial",15,"bold"), fg="#d614c1")
    etiqueta_vida.pack(pady=10)

    frame_radios = tkr.Frame(ventana_hija)
    frame_radios.pack()


def seleccion_a_b ():

    global opcion_select, radio_a, radio_b, boton_confirmar

    opcion_select = tkr.StringVar()
    opcion_select.set("A")

    radio_a = tkr.Radiobutton(frame_radios, text="Lanza (A)", variable=opcion_select, value="A",font=("Arial",10,"bold"))
    radio_a.pack(side="left", padx=10, pady=10)
    radio_b = tkr.Radiobutton(frame_radios, text="Sable (B)", variable=opcion_select, value="B", font=("Arial",10,"bold"))
    radio_b.pack(side="left", padx=10, pady=10)

    boton_confirmar = tkr.Button (ventana_hija, text="Confirmar", font=("Arial", 11, "bold"), fg="Green", command=confirmar_seleccion)
    boton_confirmar.pack(pady=10)

def ocultar (): #Propiedad para ocultar Widgets
    radio_a.pack_forget()
    radio_b.pack_forget()
    boton_confirmar.pack_forget()

def bloqueo_seleccion ():
    radio_a.config(state="disabled")
    radio_b.config(state="disabled")
    boton_confirmar.config(state=tkr.DISABLED)
    
def desbloque_seleccion ():#ESTA FUNCION SOBRA, NO HACE FALTA, PERO LA DEJO POR SI ACASO C:
    radio_a.config(state="normal")
    radio_b.config(state="normal")
    boton_confirmar.config(state=tkr.ACTIVE)


def continuar ():
    ventana_hija.geometry("420x600")
    global VIDA_PC, VIDA_USUA, juego_activo, sables_pc, sables_usua

    go = random.randint(1,2)

    if go == 1:

        etiqueta_g.config(text="⚔ Ataca PC ⚔", font=("Arial",15,"bold"), fg="#cfa93c")
        ataquepc= random.randint(1,2) #(1)Lanza , (2)Sable

        if VIDA_PC <= 0 and VIDA_USUA > 0:
            etiqueta_g.config(text="⚔ GANO USUARIO ⚔\n😀", font=("Arial",15,"bold"), fg="#00cd03")
            Boton_conti.config(state=tkr.DISABLED)
            accion = "⚔ GANO USUARIO ⚔\n😀"
        elif VIDA_USUA <= 0 and VIDA_PC > 0:
            etiqueta_g.config(text="⚔ GANO PC ⚔\n😞", font=("Arial",15,"bold"), fg="#ff0000")
            Boton_conti.config(state=tkr.DISABLED)
            accion = "⚔ GANO PC ⚔\n😞"

        elif ataquepc == 1:
            VIDA_USUA -= 10
            accion = "⚔ PC ⚔ \nAtaque con Lanza | Usuario: 🛡 -10 de vida"
            #etiqueta_ataque.config(text="Ataque con Lanza ➹\nUsuario: 🛡 -10 de vida")
        elif ataquepc == 2 and sables_pc > 0:
            VIDA_USUA -= 15
            sables_pc -=1
            accion = "⚔ PC ⚔ \nAtaque con Sable | Usuario: 🛡 -15 de vida"
            #etiqueta_ataque.config(text="Ataque con Sable 🗡\nUsuario: 🛡 -15 de vida")
        elif sables_pc <= 0:
            VIDA_USUA -= 10
            ventana_hija.geometry("510x680")
            accion = "⚠ PC no tiene Sables ⚠\nAtaca con Lanza➹ | Usuario: 🛡 -10 de vida"
            #etiqueta_ataque.config(text="PC no tiene Sables🗡\nAtaca por defecto con Lanza➹\nUsuario: 🛡 -10 de vida")
        historial_ataques.append(accion)
        etiqueta_ataque.config(text=accion)
        etiqueta_vida.config(text=f"Vida PC: 🛡{VIDA_PC} | Vida Usuario 🛡{VIDA_USUA}")
        
    else:
        etiqueta_ataque.config(text="")
        etiqueta_g.config(text="⚔ Ataca Usuario ⚔\nSeleccione Ataque [A]Lanza o [B]Sable", font=("Arial",15,"bold"), fg="#c2c640")
        seleccion_a_b()
        desbloque_seleccion() #ESTA FUNCION SOBRA, NO HACE FALTA, PERO LA DEJO POR SI ACASO C:
        Boton_conti.config(state=tkr.DISABLED)

    
def confirmar_seleccion ():
    ventana_hija.geometry("420x600")
    global VIDA_PC, VIDA_USUA, juego_activo, sables_pc, sables_usua
    seleccion = opcion_select.get()
    bloqueo_seleccion()

    ataqueusu = seleccion
    
    if VIDA_PC <= 0 and VIDA_USUA > 0:
        etiqueta_g.config(text="⚔ GANO USUARIO ⚔\n😀", font=("Arial",15,"bold"), fg="#00cd03")
        Boton_conti.config(state=tkr.DISABLED)
        accion = "⚔ GANO USUARIO ⚔\n😀"
    elif VIDA_USUA <= 0 and VIDA_PC > 0:
        etiqueta_g.config(text="⚔ GANO PC ⚔\n😞", font=("Arial",15,"bold"), fg="#ff0000")
        Boton_conti.config(state=tkr.DISABLED)
        accion = "⚔ GANO PC ⚔\n😞"

    elif ataqueusu == "A":
        VIDA_PC -= 10
        accion = "⚔ Usuario ⚔ \nAtacas con Lanza | PC: 🛡 -10 de vida"
        #etiqueta_ataque.config(text="Ataque con Lanza➹\nPC: 🛡 -10 de vida")
    elif ataqueusu == "B" and sables_usua > 0:
        VIDA_PC -= 15
        sables_usua -= 1
        accion = f"⚔ Usuario ⚔ \nAtacas con Sable | PC: 🛡 -15 de vida\nTe quedan {sables_usua} Sables"
        #etiqueta_ataque.config(text=f"Ataque con Sable 🗡\nPC: 🛡 -15 de vida\nTe quedan {sables_usua} Sables")
    elif sables_usua <= 0:
        VIDA_PC -=10
        ventana_hija.geometry("510x680")
        accion = "⚠ Usuario sin Sables ⚠\nAtacas por defecto con Lanza➹ | PC: 🛡 -10 de vida"
        #etiqueta_ataque.config(text="No tienes Sables🗡\nAtacas por defecto con Lanza➹\nPC: 🛡 -10 de vida")
    ocultar()
    Boton_conti.config(state=tkr.ACTIVE)
    historial_ataques.append(accion)
    etiqueta_ataque.config(text=accion)
    etiqueta_vida.config(text=f"Vida PC: 🛡{VIDA_PC} | Vida Usuario 🛡{VIDA_USUA}")

    #Historial actualizable, con la ventana abierta.
    #etiqueta_histo = tkr.Label(historial_ven, text=accion, font=("Arial", 12, "bold"), fg="black")
    #etiqueta_histo.pack(pady=10)


base = tkr.Tk()
base.title ("Ventana Principal")
base.geometry ("380x120")

etiqueta = tkr.Label(base, text="¿Quieres Ingresar al Juego?", font=("Arial", 15, "bold"), fg="Blue")
etiqueta.pack(pady=20)

frame_botones = tkr.Frame(base)
frame_botones.pack()

Boton_entrar = tkr.Button(frame_botones, text="Entrar", font=("Arial", 11, "bold"), fg="Green", activebackground="lightblue", command=iniciar_juego)
Boton_entrar.pack(side="left", padx=20)

Boton_cerrar = tkr.Button(frame_botones, text="Cerrar", font=("Arial", 11, "bold"), fg="Red", activebackground="lightblue", command=base.destroy)
Boton_cerrar.pack(side="left", padx=20)

base.mainloop()