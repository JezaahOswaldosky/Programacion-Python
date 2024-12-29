############################################################
# Bienvenida
import os 

print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

## Solicitar del nombre 
nombre = input("Oara empezar, dime como te llamadas: ")
print() 
print("Hola ", nombre, ", bienvenido a MiRed")
print()

###Calculo de edad
anio =  int(input("Para preparar tu perfil, dime que anio naciste:  "))
edad = 2024 - anio 
print() 

###Calculo de estatura 
estatura = float(input("Cuentame mas de to, para agregarlo a tu perfil, cuanto mide??, dimelo en metros: "))
estatura_m = int(estatura)
estatura_cm = int((estatura - estatura_m)*100)

### CAntidad de amigops 
num_amigos = int(input("Muy bien, Finalmente, cuentame cuantos amigos tienes:  "))

##Borrar pantalla de la termina 
os.system("cls")

###  Con los datos recolectados, expresamos en la pantalla la informacion... 
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("------------------------------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "anios")
print("Estatura:", estatura_m,"metros y ", estatura_cm, "centimetros")
print("Amigos:  ", num_amigos)
print("------------------------------------------------------------------------")
print("Gracias por la informacion. Esperamos que disfrutes de mi MiRed")
print()

##Usaremos una variable bool para indicar si el usuario desea continuar utilizando 
## el programa o no 
continuar = True 

##Este ciclo mantiene en ejecucion hasta que el usuario desee salir 

while continuar:
    #Solitar opcion al usuario 
    escribirMensaje = str(input("Desea escribir un mensaje? (S/N)"))

    ## Vamos a aceptar que el usuario ingrese un mensaje cuando escriban S
    if escribirMensaje == "S": 
        mensaje = input("Vamos a publicar un mensaje. Que piesas hoy??  ")
        print()
        print("---------------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("---------------------------------------------------------")
        ##3 En caso que sea otra respuesta, vamos a decidir salir. 
    else: 
        continuar = False 

##Mensaje de salida, una vez que el ciclo ha terminado 
print("Gracias por usar MiRed. Hasta pronto!!")

##Ahora puedes escribir mensajes todas las veces que quieras
##Observa que hemos utilizado un ciclo while que permite repetir la accion de preguntar por un mensaje
# hasta que el usuario escribe algo destino de S 


''' 
Te proponemos los siguientes desafios: 
1. Este programa termina cada vez que el valor de escribir_mensaje es distintoa a 
S o a s. 
Modifique el mensaje para que el programa termine UNICAMENTE cuando se ingresa N o  n 
En caso de que se ingrese algo distinto, debe volver a solicitar una opcion al usuario 

2. Modifica este menu para que le permita al usuario realizar mas de una accion. 
Por ejemplo, puedes agregar una accion que permita al usuario modificar su nombre. 
'''


