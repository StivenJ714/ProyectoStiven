#Reglas generales de las funciones:
#1- no se ejecuta la funcion a menos que la llames
#2- la puedo llamar la cantidad de veces que quiera
#3- primero hay que definir la funcion, y despues llamarla
#4- primero van los parametros requeridos, y al final los opcionales
#5- para cambiar el scope de una variable, utilizar return

#FUNCIONES SIN PARAMETROS

#def miFuncion():
    #conjunto de instrucciones


def derechos_humanos():
    #print ("Derecho a la vida")
    #print("Derecho a la igualdad ante la ley")
    #print("Derecho a la libertad")
    return "\nDerecho a la vida\nDerecho a la igualdad ante la ley\nDerecho a la libertad"

def derechos_mayorDeEdad():
    #print("Derecho a votar")
    #print("Derecho al trabajo")
    return "Drecho a votar\nDerecho al trabajo" 

def mayoria_de_edad(nombre,edad):
    mensaje = f'Según la edad de {nombre}, sus derechos son:\n'
    if edad >= 18:
        mensaje += derechos_humanos() + "\n" + derechos_mayorDeEdad ()
        return mensaje
    else:
        mensaje += derechos_humanos()
        return mensaje

def mayoria_de_edad2(edad,nombre='DESCONOCIDO'):
    mensaje = f'Según la edad de {nombre}, sus derechos son:\n'
    if edad >= 18:
        mensaje += derechos_humanos() + "\n" + derechos_mayorDeEdad ()
        #derechos_humanos()
        #derechos_mayorDeEdad()
    else:
        mensaje += derechos_humanos()
    return mensaje

#MM = int(input("digite su edad"))
#SS = input("ESCRIBA SU NFFFFOMBRE")
#mayoria_de_edad2(MM)

if __name__ == "__main__":
    mayoria_de_edad()
    mayoria_de_edad2()
    

