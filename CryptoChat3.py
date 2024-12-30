'''***************************************************************************************
                Detalles preliminares 
    El programa CryptoChat3 es un programa de red social anonimo que permite a un 
usuario entre entrar a su perfil, crear uno o salir. El usuario puede introducir su nombre, 
su alias, y varios datos importantes para que otros usuarios lo identifiquen con el. 

CryptoChad3.py es una version optmizada y utilizando el paradigma funcional para agilizar
el programa y reducir la cantidad de errores presedentes en el software. El programa cuenta 
con funciones de logus(), menuIntro(), capturaDatos(), inicioSesion(), mensajeMuro() y actividad()
******************************************************************************************'''
### Bibliotecas necesarias para que el software funcione, so para borrado del terminal, 
### msvcrt para el manejo de los asteriscos en el codigo, y data time para entablar fecha y 
### hora en que se publican las cosas en el muro
import os
import msvcrt
from datetime import datetime

### Funcion de impresion de la introduccion 
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

### Funcion de impresion del menu
def menuIntro():
    os.system("cls")
    print("Bienvenido a ... ")
    logus()
    print("             |1.- Iniciar Sesion  |   ")
    print("             |2.- Crear una cuenta|   ")
    print("             |3.-    Salir       |    ")

### Funcion del asterisko para las claves. 
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



### Funcion de captura de datos 
def capturarDatos():
    logus()
    ##Primera pregunta, pedi nombre y nombre de usuario 
    print("Empezaremos iniciando tu perfil, pero para ello, necesitamos algunos datos") 
    name = str(input("Cual es tu nombre?:   "))
    userName = str(input("Como te gusta que te llamen?:   ")) 
    ctrl = True
    while ctrl:
        op = str(input("Como te gustaria iniciar sesion con su numbre de pila Y - Nombre, N = Apodo?:   "))
        if op ==  "Y" or op == "y":
            nameCheck = True
            ctrl = False
        else: 
            nameCheck = False
            ctrl = False
        ## Segunda pregunta, pedir anio de nacimiento 
        logus()
        print("Ahora continuaremos con tu edad, en que anio naciste?:    ")
        edad = int(input()) 
        edad = 2024 - edad 

        ## Tercera pregunta, pedor altura
        logus()
        altura = float(input("Muy bien, ahora requerimos tu altura, expresalo en metros:  "))
        alturaM = int(altura)
        alturaCM = int((altura - alturaM)*100)

        ## Cuara pregunta, pedir ciudad
        logus() 
        print("Gracias, ya vamos a la mitad del proceso. ")
        ciudad = str(input("Cual es la ciudad en donde habitas?:   "))
        ##  Decision para mostrar u ocultar ciudad 
        print("Aqui en CryptoChat nos importa tu privacidad. Entonces esta informacion es decision tuya si prefieres que aparezca en tu perfil. ")
        print("Existe mucha gente mala que podria usar tu informacion para extorcionarte o incluso secuestrate. ")
        print("Entonces deseas que tu ciudad aparezca en tu ciudad: S/N")
        showCiudad = str(input())
        if showCiudad ==  "Y" or showCiudad ==  "y": 
            showCiudad =  True
        elif showCiudad ==  "N" or showCiudad ==  "n": 
            showCiudad = False
        else: 
            showCiudad = True 

        ##  Pedir cantidad de amigos que tiene el usuario
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

    return name, userName, nameCheck, edad, alturaM, alturaCM, ciudad, showCiudad, amigosNum, psw

### Funcion para escribir en el muro.. 
def muroWrite(userName): 
    muroWriteOn = True
    while muroWriteOn:
        os.system("cls")
        logus()
        print("Que actividad desea hacer?")
        print("1. Escribir tu muro")
        print("2. Configuraciones")
        print("3. Cerrar sesion")
        op = int(input())
        if op == 1: 
            print("")
            while True: 
                logus()
                signOffquestion = str(input("Deseas escribir algo en tu muro?   S/N"))
                if signOffquestion == 's' or signOffquestion == 'S':
                    now = datetime.now()
                    mensaje =  input()
                    logus()
                    print("---------------------------------------------------")
                    print(now, " ", userName, " dice:  ", mensaje)
                    os.system("pause")
                elif signOffquestion == 'N' or signOffquestion == 'n':
                    break 
            logus()
            print("Gracias por utilizar CryptoChat. ")
            print("Te esperamos pronto!!! ") 
        elif op == 2:
            print("Proximamente!!!")
            os.system("pause")
        elif op == 3: 
            muroWriteOn = False
        else:
            print("Esa opcion no existe!!!")  

    return 

## Funcion para iniciar sesion
def iniciaSesion(name, userName, nameCheck, edad, alturaM, alturaCM, ciudad, showCiudad,amugosNum, psd): 
    ##  Mostrar el logo de la aplicacion 
    logus()
    inicioOn = True 
    while inicioOn:
        nameCuenta = str(input("Cuenta:   "))
        psw = str(inputAsterisk("Contrasena:  "))
        if nameCheck == True : 
            if nameCuenta == name and psw == psd: 
                os.system("cls")
                logus()
                print("     Bienvenido a CryptoChat!!! ")
                os.system("pause")
                inicioOn = muroWrite(userName)
            elif nameCuenta == " " and psw == " ":
                inicioOn = False
 
            else: 
                os.system("cls")
                logus()
                print("La cuenta o contrasena son incorrectos!!")
                os.system("pause")
        else: 
            if nameCuenta == userName and psw == psd: 
                os.system("cls")
                print("     Bienvenido a CryptoChat!!! ")
                os.system("pause")
                inicioOn = muroWrite(userName)
            elif nameCuenta == " " and psw == " ":
                break 
            else: 
                os.system("cls")
                logus()
                print("La cuenta o contrasena son incorrectos!!")
                os.system("pause")


### Programa main 
# Imprimir logo y menu
progOn = True
###Variables necesarias para operar el programa de red social 

while progOn:
    logus()
    menuIntro()

    opcion = int(input())
    ### Seleccionador de las opciones 
    if opcion == 1: 
        iniciaSesion(name, userName, nameCheck, edad, alturaM, alturaCM, ciudad, showCiudad,amigosNum, psd)
    elif opcion == 2: 
        name, userName, nameCheck, edad, alturaM, alturaCM, ciudad, showCiudad,amigosNum, psd = capturarDatos() 
        os.system("cls")
        print(showCiudad)
        if showCiudad == True: 
            print("               Felicidades, tu cuenta ha sido creada!!!      ")
            print("|============================================================")
            print("| Nombre: ", name, "                                         ")
            print("| UserName: ", userName, "                                   ")
            print("| Edad: ", edad, "anios                                      ")
            print("| Estatura: ", alturaM, " metros y ", alturaCM, " centimetros")
            print("| Ciudad: ", ciudad, "                                       ")
            print("| Amigos: ", amigosNum,"                                     ")
            print("|============================================================")
            os.system("pause")
        else: 
            print("               Felicidades, tu cuenta ha sido creada!!!      ")            
            print("|============================================================")
            print("| Nombre: ", name, "                                         ")
            print("| UserName: ", userName, "                                   ")
            print("| Edad: ", edad, "anios                                      ")
            print("| Estatura: ", alturaM, " metros y ", alturaCM, " centimetros")
            print("| Amigos: ", amigosNum,"                                    ")
            print("|============================================================")
            os.system("pause")                

    elif opcion == 3:
        os.system("cls")
        print("Gracias por utilizar CryptoChat!!!")
        print("         Vuelva pronto!!!")
        os.system("pause")
        os.system("cls")
        break 
    else: 
        print("Esa opcion no se encuentra disponible!!")
        os.system("pause")