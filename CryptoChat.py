"""
**************************************************************
                    Detalles preliminares

El programada bienvenida al usuario a la plataforma CryptoChat 
para formular su perfil. El programa captura la informacion del 
usuario como nombre de usuario, anio de nacimiento, estatura, 
genero y ciudad donde vive. 

Programador: Jezaah Oswaldosky 
Fecha: 12/23/2024

CyrptoChat.py es un programa base de una plataforma de red 
social que da la bienvenida a un usuario para introducir los 
datos de registro, como nombre de usuario, edad, estatura, genero, 
donde vive y la cantida dde amigos que tiene. El programa se 
ejecuta de la siguiente manera: 
Mensaje de Bienvenida, Preguntar por nombre, anio de nacimiento, 
estatura, genero, ciudad y cantidad de amigos. 
finalmente limpiar la pantalla, para desplegar la informacion 
al usuario. 
**************************************************************
"""
import os


##Introduccion de la plataforma. 
print("Bienvenido a ... ")
print("""
  _____                  _         _____ _           _   
 / ____|                | |       / ____| |         | |  
| |     _ __ _   _ _ __ | |_ ___ | |    | |__   __ _| |_ 
| |    | '__| | | | '_ \| __/ _ \| |    | '_ \ / _` | __|
| |____| |  | |_| | |_) | || (_) | |____| | | | (_| | |_ 
 \_____|_|   \__, | .__/ \__\___/ \_____|_| |_|\__,_|\__|
              __/ | |                                    
             |___/|_|                                    
""")

### Pedir informacion al usuario para crear el perfil 
nombre = input("Cual es tu nombre? ")
print()
print("Hola, " + nombre + ", bienvenido a CryptoChat ")
print()

### Pedir anio de nacimiento 
anio = int(input("Cuantos anios tienes?? "))
edad = 2024-anio-1
print() 

### Solicitar estatura al usuario 
estatura = float(input("Cuanto mides? "))
estaturaMetros = int(estatura)
estaturaCentimetros = int((estatura - estaturaMetros)*100)

### Cuantos amigos tiene 
print()
numAmigos = int(input("Ya casi terminamos, ahora, cuantos amigos tienes? "))

###Limpiamos pantalla
os.system("cls")

### Imprimir los datos recolectados
print("Muy bien, ", nombre, ". Entonces podemos crear tu perfil con los datos proporcionados")
print("-------------------------------------------------------------------------------------")
print("Nombre:   ", nombre)
print("Edad:     ",edad, anio)
print("Estatura: ", estaturaMetros, "metros y ", estaturaCentimetros, "centimetros")
print("Amigos:   ", numAmigos)
print("--------------------------------------------------------------------------------------")
print()
print("Gracias por la informacion. Esperamos que disfrutes de CryptoChat")
print()

### Solicitar un mensaje de prueba que se muestre en tu perfil 
print("Ahora vamos a publicar el primer mensaje en tu muro")
mensaje = input()
print()
print("--------------------------------------------------------------------------------------")
print(nombre, "dice ", mensaje)
print("--------------------------------------------------------------------------------------")


