import base as b
import admin as ad
import teacher as t
import studens as s
from os import system
import sys
system("cls")
import time
code =[8813] 
code1 = ["2"]
#code1 =["312\89ñl@"]
# este es el main de donde se ejecuta el codigo
i = 1
i2 = 1
i4 = 1
i5 = 1
i6 = 6
i7 = 1
i8 = 1
while(True):
    print("======= BIENVENIDO AL MENU =======")
    print("")
    print("Quien es \n 1. Estudiante \n 2. Profesor \n 3. ADMIN \n 4. salir")# menu principal y opciones
    opcion = (input("Ingrese: "))
    if(opcion == "1"): # estudiante
        system("cls")
        while(True): # inicio de sesion
            while(True): 
                try:
                    nameestu = (input("Ingrese el nombre: "))
                    codeEstu = (int(input("Ingrese el codigo: ")))
                    if(codeEstu <0):
                        print("HUBO UN ERROR")
                        time.sleep(0.7)
                        system("cls")
                    else:
                        break
                except Exception:
                    print("Error")
                    time.sleep(1)
                    system("cls")
                    i = i + 1
                    if(i == 4):
                        print("MUCHOS INTENTOS")
                        break
            if(i == 4):
                time.sleep(2)
                system("cls")
                break
            elif(ad.verifyStudent(nameestu,codeEstu)):
                system("cls")
                while(True):
                    print(f"BIENVENIDO {nameestu}")
                    print("")
                    opcion18 =(input("======== MENU DEL ESTUDIANTE ======== \n 1. Ver notas \n 2. Enviar peticion \n 3. Respuesta de peticion \n 4. Salir \n Ingrese: "))
                    if(opcion18 == "1"):
                        system("cls")
                        while(True):
                            s.SeeNotes(nameestu)
                            print("================================================================")
                            salir = (input("precione 'enter' para salir \n Ingrese: "))
                            if(salir == ""):
                                system("cls")
                                break
                    elif(opcion18 == "2"):
                        system("cls")
                        while(True):
                            peti = (input("Ingrese la peticion: "))
                            s.peti(codeEstu,nameestu,peti)
                            time.sleep(1)
                            system("cls")
                            break
                    elif(opcion18 == "3"):
                        system("cls")
                        while(True):
                            s.SeePetiAnswersEstu(nameestu)
                            enter =(input("Ingrese 'enter' para salir: "))
                            if(enter == ""):
                                system("cls")
                                break
                    elif(opcion18 == "4"):
                        system("cls")
                        break
                    else:
                        print("ERROR")
                if(opcion18 == "4"):
                    system("cls")
                    break
            else:
                system("cls")
                break
    elif(opcion == "2"): # aqui va los profesores
        system("cls")
        while(True):
            while(True):
                try:
                    nombreTE= (input("Ingrese el nombre: "))
                    codeTE =(int(input("Ingrese el codigo: ")))
                    if(codeTE < 0):
                        print("ERROR")
                    else:
                        break
                except Exception:
                    print("ERROR")
                    time.sleep(1)
                    system("cls")
                    i8 = i8 + 1
                    if(i8 == 4):
                        print("MUCHOS INTENTOS")
                        break   
            if(i8 == 4):
                time.sleep(1)
                system("cls")
                break
            elif(ad.verifyTeacher(nombreTE, codeTE)):
                system("cls")
                while(True):
                    print(f"BIENVENIDO DOCENTE {nombreTE}")
                    print("")
                    opcion20 = (input(" ======== MENU DE PROFESORES ========= \n 1. Ingresar notas  \n 2. Actualizar notas de estudiante \n 3. Enviar y ver peticion \n 4. Salir \n Ingrese aqui:"))
                    if(opcion20 == "1"):
                        system("cls")
                        time.sleep(0.5)
                        ad.seeTableStudent()
                        print("================================================================")
                        print("")
                        opcion23 = (input("Ingrese el nombre del estudiante: "))
                        if(opcion23.isalpha()):
                            i13 = 1
                            while(True):
                                try:
                                    note1a = (float(input("Ingrese la primera nota: ")))
                                    note2a = (float(input("Ingrese la segunda nota: ")))
                                    note3a = (float(input("Ingrese la tercera nota: ")))
                                    if((note1a <0 or note1a >5) or (note2a <0 or note2a >5) or (note3a <0 or note3a >5)):
                                        print("error")
                                        print("")
                                    else:
                                        time.sleep(1)
                                        t.AddNotes(note1a, note2a, note3a,opcion23)
                                        time.sleep(1)
                                        system("cls")
                                        break
                                except Exception:
                                    print("Error")
                                    i13 = i13 + 1
                                    if(i13  == 4):
                                        print("Muchos intentos")
                                        time.sleep(2)
                                        system("cls")
                                        break
                        else:
                            print("Error")
                            time.sleep(1)
                            break
                    elif(opcion20 == "2"):
                        system("cls")
                        ad.seeTableStudent()
                        print("================================================================================================================================")
                        print("")
                        while(True):
                            i10 = 1
                            opcion22 = (input("Ingrese el estudiante que para modificar \n Ingrese: "))
                            if(opcion22.isalpha()):
                                while(True):
                                    try:
                                        codeStu= (int(input("codigo: ")))
                                        if(codeStu <0):
                                            print("error")
                                        else:
                                            break
                                    except Exception:
                                        print("error")
                                        i10 = i10 + 1
                                        if(i10 == 4):
                                            break
                                nameStu =(input("Nombre: "))
                                if(nameStu.isalpha() and i10 < 4):
                                    while(True):
                                        try:
                                            note1 =(float(input("note1: ")))
                                            if(note1 < 0 or note1 >5):
                                                print("error")
                                            else:
                                                break
                                        except Exception:
                                            print("error")
                                    while(True):
                                        try:
                                            note2 =(float(input("note2: ")))
                                            if(note2 < 0 or note2 > 5):
                                                print("error")
                                            else:
                                                break
                                        except Exception:
                                            print("error")
                                    while(True):
                                        try:
                                            note3 =(float(input("note3: ")))
                                            if(note3 < 0 or note3 > 5):
                                                    print("error")
                                            else:
                                                break
                                        except Exception:
                                            print("error")
                                    ad.UpdateTableStudens(codeStu,nameStu,note1,note2,note3,opcion22)
                                    t.AverageOfAll()
                                    time.sleep(5)
                                    exit2 =(input("preciona 'ENTER' para seguir actulizando  o '2' para salir salir "))
                                    if(exit2 == "2"):
                                        system("cls")
                                        break
                                else:
                                    print("Error al ingresar los datos")
                                    time.sleep(1)
                                    system("cls")
                                    break 
                    elif(opcion20 == "3"):
                        system("cls")
                        while(True):
                            opcion21 = (input("\n Escoje una opcion \n 1. Enviar una peticion \n 2. Ver peticion \n 3.Salir \n Ingrese aqui:"))
                            if(opcion21 == "1"):
                                while(True):
                                    system("cls")
                                    peti2 =(input("Ingrese la peticion: "))
                                    asign = (input("Ingrese la asignatura: "))
                                    t.peticionprofe(codeTE,nombreTE,asign,peti2)
                                    break
                            elif(opcion21 == "2"):
                                system("cls")
                                while(True):
                                    t.SeePetiAnswers(nombreTE)
                                    salir = (input("Precione enter para salir: "))
                                    if(salir == ""):
                                        system("cls")
                                        break
                            elif(opcion21 == "3"):
                                system("cls")
                                break
                            else:
                                print("No se encontro opcion")
                    elif(opcion20 == "4"):
                        print("Saliendo..")
                        time.sleep(1)
                        print("Saliendo...")
                        time.sleep(2)
                        system("cls")
                        break
                    else:
                        print("No se encontro opcion")
                if(opcion20 == "4"):
                    break
            else:
                print("ERROR")
                system("cls")
                break
    elif(opcion == "3"): # aqui va los admin
        system("cls")
        print("Al parece hay un admin")
        while(True):
            while(True):
                print("ingrese el PIN de para iniciar sesion")
                try:
                    PIN = (int(input("Ingrese: ")))
                    break
                except Exception:
                    print("Hubo un error")
                    time.sleep(0.5)
                    i = i + 1
                    if(i == 4):
                        print("HUBO MUCHOS INTENTOS")
                        time.sleep(2.5)
                        break
                    system("cls")
            if(i == 4): # intentos de ingresar 
                system("cls")
                break
            else:
                if(PIN in code): # verificacion del PIN
                    userAd = (input("Ingrese la usuario: "))
                    passW = (input("Ingrese la contraseña: "))
                    if(ad.verify(userAd,passW)):# Verficacion del inicio de sesion
                        very=(input("Ingrese el codigo para ver el menu: "))
                        if(very in code1):# verificacion del MENU
                            system("cls") # esto esta las lista de la linea 9
                            print("")
                            while(True):
                                print("====== BIENVENIDO AL MENU DE ADMINS ======") # menu de los admins
                                print("")
                                print(" \n 1. Añadir \n 2. Ver tablas \n 3. Peticiones \n 4. Actulizar datos \n 5. Eliminar datos \n 6. Salir")
                                opcion2=(input("Ingrese: "))# opciones 
                                if(opcion2 == "1"):# Añadir
                                    system("cls")
                                    while(True):
                                        opcion3=(input("\n 1. Añadir Estudiante \n 2. Añadir Profesor \n 3.Salir \n Ingrese la opcion: "))
                                        if(opcion3 == "1"):
                                            system("cls")
                                            while(True):
                                                while(True):
                                                    try:
                                                        codeStu =(int(input("Ingrese el codigo: ")))
                                                        if(codeStu < 0):
                                                            print("parece que hay un error")
                                                            time.sleep(0.6)
                                                            system("cls")
                                                        elif(codeStu == "" or codeStu == " "):
                                                            print("error")
                                                        else:
                                                            break
                                                    except Exception:
                                                        print("Hubo un error")
                                                        time.sleep(0.5)
                                                        i2 = i2 + 1
                                                        if(i2 == 7):
                                                            print(f"Que pasa {userAd} estas como NERVIOSO")
                                                            break
                                                    system("cls")
                                                if(i2 == 7):
                                                    i2=0
                                                    system("cls")
                                                    break
                                                else:
                                                    nameStu =(input("Ingrese el nombre del estudiante: "))
                                                    if nameStu.isalpha():
                                                        print("listo")
                                                        ad.InsertEstudens(codeStu,nameStu)
                                                        time.sleep(2.3)
                                                        system("cls")
                                                        break
                                                    else:
                                                        print("esto tiene numero")
                                                        time.sleep(2)
                                                        system("cls")
                                        elif(opcion3 == "2"):
                                            system("cls")
                                            while(True):
                                                i3 = 1
                                                while(True):
                                                    try:
                                                        codePro =(int(input("Ingrese el codigo: ")))
                                                        if(codePro < 0):
                                                            print("parece que hay un error")
                                                            time.sleep(0.6)
                                                            system("cls")
                                                            break
                                                        elif(codePro == "" or codePro == " "):
                                                            break
                                                        else:
                                                            break
                                                    except Exception:
                                                        print("Hubo un error")
                                                        time.sleep(0.5)
                                                        i3 = i3 + 1
                                                        if(i3 == 7):
                                                            print(f"Que pasa {userAd} estas como NERVIOSO")
                                                            break
                                                    system("cls")
                                                if(i3 == 7):
                                                    i3 = 0
                                                    system("cls")
                                                    break
                                                else:
                                                    namePro =(input("Ingrese el nombre del profesor: "))
                                                    nameAsgn =(input("Ingrese la asignatura: "))
                                                    if namePro.isalpha and nameAsgn.isalpha():
                                                        print("listo")
                                                        ad.Insert(codePro, namePro , nameAsgn)
                                                        time.sleep(2.3)
                                                        system("cls")
                                                        break
                                                    else:
                                                        print("esto tiene numero")
                                                        time.sleep(2)
                                                        system("cls")
                                        elif(opcion3 == "3"):
                                            print("SALIENDO.")
                                            time.sleep(0.2)
                                            print("SALIENDO..")
                                            print("SALIENDO...")
                                            time.sleep(0.7)
                                            system("cls")
                                            break 
                                elif(opcion2 == "2"): # aqui va Ver las tablas
                                    system("cls")
                                    while(True):
                                        opcion4 = (input("\n 1. Ver tabla de Profesores \n 2. Ver tabla de estudiante \n 3. Ver tabla de ADMINS \n 4. Salir \n ingrese aqui: "))
                                        if(opcion4 == "1"): # tabla de profesores
                                            system("cls")
                                            while(True):
                                                ad.seeTableTeacher()
                                                print("")
                                                print("================================================")
                                                subopcion4 = (input("Si quiere salir precione enter: "))
                                                system("cls")
                                                break
                                        elif(opcion4 == "2"): # tabla de estudiante
                                            system("cls")
                                            while(True):
                                                ad.seeTableStudent()
                                                print("")
                                                print("================================================")
                                                subopcion4 = (input("Si quiere salir precione enter: "))
                                                system("cls")
                                                break
                                        elif(opcion4 == "3"): # tabla de ADMINS
                                            system("cls")
                                            while(True):
                                                ad.verTablaAdmin()
                                                print("")
                                                print("================================================")
                                                subopcion4 = (input("Si quiere salir precione enter: "))
                                                system("cls")
                                                break
                                        elif(opcion4 == "4"): # Salir
                                            print("SALIENDO.")
                                            time.sleep(0.7)
                                            print("SALIENDO..")
                                            time.sleep(0.7)
                                            print("SALIENDO...")
                                            time.sleep(0.7)
                                            system("cls")
                                            break
                                        else:
                                            print("no se encontro opcion")
                                elif(opcion2 == "3"): # ver peticiones y responder peticiones
                                    system("cls")
                                    while(True):
                                        print("====== Opciones de menu ====== \n 1. Ver peticiones y responder peticiones de profesores \n 2. Ver peticiones y responder peticiones de estudiantes \n 3. Salir")
                                        opcion24 = (input("Ingrese: "))
                                        if(opcion24 == "1"):
                                            system("cls")
                                            while(True):
                                                ad.seeTableTeacherPeti()
                                                print("================================================")
                                                print("")
                                                opcion25 = (input("Ingrese el nombre el usuario que va a responder : "))
                                                if(opcion25.isalpha()):
                                                    Rta = (input("Ingrese una respueta: "))
                                                    ad.answer(opcion25, Rta)
                                                    exit3 = (input("presiones 2 para salir o 'ENTER' para seguir \n Ingrese: "))
                                                    if(exit3 == 2):
                                                        system("cls")
                                                        time.sleep(1)
                                                        break
                                                else:
                                                    print("hay numeros")
                                                    time.sleep(1)
                                                    system("cls")
                                        elif(opcion24 == "2"):
                                            system("cls")
                                            while(True):
                                                ad.seeTableResponse()
                                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                                print("")
                                                opcion26 = (input("Ingrese el nombre el usuario que va a responder : "))
                                                if(opcion26.isalpha()):
                                                    Rtat = (input("Ingrese una respueta: "))
                                                    ad.response(Rtat,opcion26)
                                                    exit4 = (input("presiones 2 para salir o 'ENTER' para seguir \n Ingrese: "))
                                                    if(exit4 == "2"):
                                                        system("cls")
                                                        time.sleep(1)
                                                        break
                                                else:
                                                    print("hay numeros")
                                                    time.sleep(1)
                                                    system("cls")
                                        elif(opcion24 == "3"):
                                            system("cls")
                                            break
                                        else:
                                            system("cls")
                                            break
                                elif(opcion2 == "4"): # actualizacion de datos
                                    system("cls")
                                    while(True):
                                        print("actualizar  datos de: \n 1. Profesores \n 2. Estudiante \n 3. salir")
                                        opcion12 = (input("Ingrese: "))
                                        if(opcion12 == "1"): # profesores
                                            system("cls")
                                            ad.seeTableTeacher() # tabla de profesores
                                            print("")
                                            print("================================================================================================================================")
                                            print("")
                                            while(True):
                                                opcion14 = (input("Ingrese el nombre del profesor que va modificar \n : "))
                                                if(opcion14.isalpha()):
                                                    while(True):
                                                        try:
                                                            codePro=(int(input("codigo: ")))
                                                            if(codePro <0):
                                                                print("error")
                                                            else:
                                                                break
                                                        except Exception:
                                                            print("Hubo un error")
                                                    nameprO=(input("Nombre: "))
                                                    if(nameprO.isalpha()):
                                                        ad.UpdateTableTeacher(codePro, nameprO,opcion12)
                                                        print("precione 'enter' si quiere seguir o 2 si quiere salir")
                                                        opcion15 =(input("Ingrese: "))
                                                        if(opcion15 == "2"):
                                                            system("cls")
                                                            break
                                                        ad.seeTableTeacher()
                                                    else:
                                                        print("aqui hay numeros")
                                                else:
                                                    print("Error")
                                        elif(opcion12 == "2"): # estudiante
                                            system("cls")
                                            ad.seeTableStudent()
                                            print("================================================================================================================")
                                            print("")
                                            while(True):
                                                i9 = 1
                                                opcion13 = (input("Ingrese el estudiante para modificar \n ingrese: "))
                                                if(opcion13.isalpha()):
                                                    while(True):
                                                        try:
                                                            codeSt= (int(input("codigo: ")))
                                                            if(codeSt <0):
                                                                print("error")
                                                            else:
                                                                break
                                                        except Exception:
                                                            print("error")
                                                            i9 = i9 + 1
                                                            if(i9 == 4):
                                                                break
                                                    NameSt =(input("Nombre: "))
                                                    if(NameSt.isalpha() and i9 < 4):
                                                        while(True):
                                                            try:
                                                                note1 =(float(input("note1: ")))
                                                                if(note1 < 0 or note1 >5):
                                                                    print("error")
                                                                else:
                                                                    break
                                                            except Exception:
                                                                print("error")
                                                        while(True):
                                                            try:
                                                                note2 =(float(input("note2: ")))
                                                                if(note2 < 0 or note2 > 5):
                                                                    print("error")
                                                                else:
                                                                    break
                                                            except Exception:
                                                                print("error")
                                                        while(True):
                                                            try:
                                                                note3 =(float(input("note3: ")))
                                                                if(note3 < 0 or note3 > 5):
                                                                    print("error")
                                                                else:
                                                                    """ad.UpdateTableStudens(codeSt,nameStu,note1,note2,note3,opcion13)
                                                                    t.AverageOfAll()
                                                                    time.sleep(10)"""
                                                                    break
                                                            except Exception:
                                                                print("error")
                                                        ad.UpdateTableStudens(codeSt,NameSt,note1,note2,note3,opcion13)
                                                        t.AverageOfAll()
                                                        time.sleep(5)
                                                        exit2 =(input("preciona 'ENTER' para seguir actilizando  o '2' para salir salir "))
                                                        if(exit2 == "2"):
                                                            system("cls")
                                                            break
                                                    else:
                                                        system("cls")
                                                        break
                                        elif(opcion12 == "3"): # salir
                                            system("cls") 
                                            break
                                        else:
                                            print("no se encontro opcion")
                                elif(opcion2 == "5"):# eliminar datos
                                    system("cls")
                                    while(True):
                                        opcion16 =(input("en que tabla va a borra \n 1.Profesores \n 2. Estudiante \n 3. Salir \n ingrese: "))
                                        if(opcion16 == "1"): # profesores
                                            system("cls")
                                            ad.seeTableTeacher()
                                            tableProNAme =("Profesores")
                                            while(True):
                                                try:
                                                    code2 =(int(input("codigo: ")))
                                                    if(code2 <0):
                                                        print("ERROR")
                                                    else:
                                                        break
                                                except Exception:
                                                    print("ERROR")
                                            ad.eliminar(tableProNAme,code2)
                                            time.sleep(3)
                                            system("cls")
                                        elif(opcion16 == "2"): # estudiante
                                            system("cls")
                                            ad.seeTableStudent()
                                            while(True):
                                                try:
                                                    opcion17 =(int(input("codigo:")))
                                                    if(opcion17 < 0):
                                                        print("ERROR")
                                                    else:
                                                        break
                                                except Exception:
                                                    print("ERROR")
                                            ad.eliminar("Estudiante",opcion17)
                                            time.sleep(3)
                                            system("cls")
                                        elif(opcion16 == "3"): # salir
                                            print("SALIENDO.")
                                            time.sleep(0.7)
                                            print("SALIENDO..")
                                            time.sleep(0.7)
                                            print("SALIENDO...")
                                            time.sleep(0.7)
                                            system("cls")
                                            break 
                                        else: 
                                            print("no se encontro opcion")
                                elif(opcion2 == "6"): # salir del menu de admins
                                    print("SALIENDO.")
                                    time.sleep(0.7)
                                    print("SALIENDO..")
                                    time.sleep(0.7)
                                    print("SALIENDO...")
                                    time.sleep(0.7)
                                    system("cls")
                                    break 
                                else:
                                    print("no se encontro opcion")
                                    system("cls")
                            if(opcion2 == "6"):
                                break
                        else:
                            print("NO TIENE ACCESO AL MENU")
                            time.sleep(3)
                            system("cls")
                            break
                    else:
                        print("ERROR")
                        time.sleep(1)
                        system("cls")
                        break
                else:
                    print("ACCESO DENEGADO")
                    time.sleep(5)
                    system("cls")
                    break

        
    elif(opcion == "4"): # salir del programa
        print("SALIENDO.")
        time.sleep(0.7)
        print("SALIENDO..")
        time.sleep(0.7)
        print("SALIENDO...")
        time.sleep(0.7)
        system("cls")
        break 
    else:
        print("no se encontro opcion")
        time.sleep(0.6)
        system("cls")














