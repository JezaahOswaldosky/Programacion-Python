'''***************************************************************************************
                Detalles preliminares 
    El programa CriptoChat2 cuenta con unuevas funcionalidades como el escribir mensajes 
en el muro las veces que desee el usuario, asi como las funcionalidades anteriores como 
la creacion del perfil. 

Programador: Jezaah Oswaldosky
Fecha: 12-25-2024

CryptoChat2.py es un programa extension de CryptoChat.py con la funcionalidad de escribir
en el muro la cantidad de veces que se desee. 
El usuario proporcionara informacion de su perfil. Posteriormente se le preguntara al 
cliente si desea subir algo en su muro o cerrar la sesion en un menu descrptivo. 
******************************************************************************************'''
### Importamos la biblioteca para instrucciones en la consola, Nota: Esto nos permitira borrar la consoal 
import os
import msvcrt
from datetime import datetime

def logus():
    os.system("cls")
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

def inputAsterisk(prompt=""):
    print(prompt, end="", flush=True)
    password = "" 
    while True: 
        char = msvcrt.getch()   ###Captura la tecla 
        if char == b'\r':   # Reconocer la tecla Enter
            print()         # Nueva linea 
            break 
        elif char == b'\0x':    #   Retroceso
            if len(password) > 0:
                password = password[:1]
                print("\b \b", end="", flush=True)
        else:
            password += char.decode("utf-8")
            print("*", end="", flush=True)
    
    return password 

while True: 
    ##Introduccion de la plataforma. Con selector para para iniciar sesion o crear una cuenta  
    os.system("cls")
    print("Bienvenido a ... ")
    logus()
    print("             |1.- Iniciar Sesion  |   ")
    print("             |2.- Crear una cuenta|   ")
    print("             |3.-    Salir       |    ")
    ## Capturar opcion 
    print() 
    op1 =  int(input())

    ### Entramos al menu de opciones para trabajar 
    if op1 == 1: 
        logus() 
        if showName == True: 
            cuenta = str(input("Cuenta: "))
            pswInicio = inputAsterisk("Contrasena: ")
            if ((cuenta == nombre) and (pswInicio ==  psw)):
                logus()
                print("Bienvenido a CryptoChat ", nombre)
                os.system("pause")
                ### Seguir a 
                muroOn = True
                while muroOn:
                    logus()
                    signOffquestion = str(input("Deseas escribir algo en tu muro?   S/N"))
                    if signOffquestion == 's' or signOffquestion == 'S':
                        now = datetime.now()
                        mensaje =  input()
                        logus()
                        print("----------------------------------------------------")
                        print(now, " ", nombre, " dice:  ", mensaje)
                        os.system("pause")
                    elif signOffquestion == 'N' or signOffquestion == 'n':
                        muroOn = False
                logus()
                print("Gracias por utilizar CryptoChat. ")
                print("Te esperamos pronto!!! ")
            else: 
                logus()
                print("Nombre de usuario o contrasena incorrecta!!!")
                os.system("pause")
        else: 
            cuenta = str(input("Cuenta: "))
            pswInicio = inputAsterisk("Contrasena: ")
            if ((cuenta == nickName) and (pswInicio ==  psw)):
                logus()
                print("Bienvenido a CryptoChat ", nickName)
                os.system("pause")
                ####    Continua codigo para escribir en el muro.. 
                muroOn = True
                while muroOn:
                    logus()
                    signOffquestion = str(input("Deseas escribir algo en tu muro?   S/N"))
                    if signOffquestion == 's' or signOffquestion == 'S':
                        now = datetime.now()
                        mensaje =  input()
                        logus()
                        print("----------------------------------------------------")
                        print(now, " ", nombre, " dice:  ", mensaje)
                        os.system("pause")
                    elif signOffquestion == 'N' or signOffquestion == 'n':
                        muroOn = False
                logus()
                print("Gracias por utilizar CryptoChat. ")
                print("Te esperamos pronto!!! ") 
            else: 
                logus()
                print("Nombre de usuario o contrasena incorrecta!!!")
                os.system("pause")
    elif op1 == 2: 
        logus()
        ### Pedir nombre del usuario
        print("Bueno, vamos a empezar...")
        nombre = str(input("Cual es tu nombre? "))
        logus()
        ## Pedir apodo o nombre de usuario 
        nickName = str(input("Todos tenemos un nombre alias. Como te gusta que te llame??  "))
        logus()
            ##Consultar si desea iniciar sesion con nombre o nickname 
        showName = int(input("Como quieres iniciar sesion? 1.-Con tu nombres 2.- Con tu apodo"))
        if showName ==  1:      ##  Iniciar sesion con el nombre 
            showName = True
        else: 
            showName = False    ##  Iniciar sesion con el apodo 
        logus()
        ### Pedir el anio de nacimiento del usuario 
        print("Muchas gracias. Ahora continuaremos con el anio que naciste.")
        anio = int(input("En que anio naciste?? "))
        anio = 2024 - anio 
        ### Pedir la estatura del usuario 
        logus()
        print("Proseguimos con tu registro. Ya casi acabamos.")
        estatura = float(input("Cuanto mides? Expresalo en metros.   "))
        estaturaM= int(estatura)
        estaturaCm= int((estatura - estaturaM)*100)
        ### Ciudad 
        logus()
        print("Ahora determinaremos tu ciudad. Es muy importante que las personas te conozcan y sepan donde vives o que lugares visitas.")
        ciudad = str(input("En que ciudad vives: "))
        ## Decision de privacidad del usuario
        logus()
        print() 
        print("Aqui en CryptoChat nos importa tu privacidad. Entonces esta informacion es decision tuya si prefieres que aparezca en tu perfil. ")
        print("Existe mucha gente mala que podria usar tu informacion para extorcionarte o incluso secuestrate. ")
        print("Entonces deseas que tu ciudad aparezca en tu ciudad: S/N")
        showCiudad = str(input())
        if showCiudad == "S" or showCiudad == "s": 
            showCiudad =  True
        elif showCiudad ==  "N" or showCiudad ==  "n": 
            showCiudad = False
        else: 
            showCiudad = True 
        
        ### Pedir la cantidad de amigos que tiene el usuario 
        logus()
        print("Ahora terminamos con esta ultima informacion")
        amigosNum = int(input("De cuantos amigos dispones?  "))
        logus()
        print("Muchas gracias!!!")
        print("Ahora tu perfil ya esta hecho.")

        ### Pedir una contrasena para salvaguardar el programa 
        logus()
        pswEq = True
        while pswEq:     
            print("Para nosotros la seguridad es muy importante. Entonces requerimos una ultima informacion.")
            print("Requerimos una contrasena para autenticar tu inicio de sesion ")
            psw = inputAsterisk("Contrasena:  ")
            print("Confirmar contrasena")
            psw1 = inputAsterisk("Nuevamente la contrasena:   ")
            if psw ==  psw1: 
                logus()
                print("Felicitaciones, ya tienes tu cuenta de CryptoChad!!!")
                pswEq = False
            else: 
                logus()
                print("Las contrasenas no coinciden. Intentelo de nuevo. ")
                pswEq = True
        logus()
        if showCiudad == True: 
            print("Felicidaciones, ya cuentas con tu perfil de CryptoChat.")
            print("---------------------------------------------------------------------")
            print("Nombre:      ", nombre)
            print("Apodo:       ", nickName)
            print("Edad:        ", anio)
            print("Estatura:    ", estaturaM, " metros y ", estaturaCm, "centimetros")
            print("CiudadL:     ", ciudad)
            print("Amigos:      ", amigosNum)
            print("---------------------------------------------------------------------")
        else: 
            print("Felicidaciones, ya cuentas con tu perfil de CryptoChat.")
            print("---------------------------------------------------------------------")
            print("Nombre:      ", nombre)
            print("Apodo:       ", nickName)
            print("Edad:        ", anio, " anios")
            print("Estatura:    ", estaturaM, " metros y ", estaturaCm, "centimetros")
            print("Ciudad:      No Disponible")
            print("Amigos:      ", amigosNum)
            print("---------------------------------------------------------------------")
        ##  Pausamos para apreciar la informacion... 
        os.system("pause")


    elif op1 == 3: 
        os.system("cls")
        break 
    else: 
        print("Esa opcion no existe. Favor de escoger otra opcion!!!")
    