import base
import sqlite3 as sl
import time
from os import system
system("cls")


def AddNotes(note1,note2,note3,name): # ingresar notas 
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        while(True):
            if(note1 < 0 or note1 > 5):
                print("error al ingresar nota")
                break
            elif(note2 < 0 or note2 > 5):
                print("error al ingresar nota")
                break
            elif(note3 < 0 or note3 > 5):
                print("error al ingresar nota")
                break
            else:
                cursor.execute(f"UPDATE Estudiante  SET PrimerCorte = {note1} , SegundoCorte = {note2} , tercerCorte = {note3} where Nombre = '{name}'")
                print("nota ingresada CON EXITO :)")
                break
        conn.commit()
    except sl.OperationalError:
            print("ERROR")
    conn.close()

def AverageOfAll(): # promedio de los estudiantes
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"SELECT * FROM Estudiante")
        cursor.execute(introducion)
        conn.commit()
        data = cursor.fetchall()
        i = 0
        for x,y,z,x1,y1,z1 in data: 
            z = (z * 30)/100
            x1 = (x1 * 30)/100
            y1 = (y1 * 40)/100
            z1 = z + x1 + y1
            introducion2 =(f"UPDATE Estudiante SET Definitiva = {z1} WHERE Nombre like '{y}'")
            cursor.execute(introducion2)
            conn.commit()
            i = i + 1
            print(f"{i} || Codigo : {x} || Nombre : {y} || Primer Corte : {z} || Segundo Corte : {x1} || Tercer Corte : {y1} || Definitiva : {z1} ||")
            print("nota registrada") 
        print("======================================================================================================================================")
        print("")
        print("NOTAS SIN EL PORCENTAJE ")
        for x,y,z,x1,y1,z1 in data:
            print(f"Codigo : {x} || Nombre : {y} || Primer Corte : {z} || Segundo Corte : {x1} || Tercer Corte : {y1} || Definitiva : {z1} ")
    except sl.OperationalError:
        print("ERROR")
    conn.close()
    

def updateNotes(name): # actulizar nota de estudiante
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"SELECT * FROM Estudiante WHERE Nombre = '{name}'")
        cursor.execute(introducion)
        conn.commit()
        data = cursor.fetchall()
        i = 1
        for x,y,z,x1,y1,z1 in data:
            print(f"{i} || Codigo : {x} || Nombre : {y} || Primer Corte : {z} || Segundo Corte : {x1} || Tercer Corte : {y1} || Definitiva : {z1} ||") 

        # mini menu 
        while(True):
            print("actualizar \n 1.Primer Corte \n 2.Segundo Corte \n 3.Tercer Corte \n ")
            query = (input("ingrese: "))
            if(query == "1"):
                try:
                    query2 =(float(input("ingrese la nota: ")))
                    if(query2 < 0 or query2 > 5  ):
                        print("error al ingresar nota")
                        break
                    else:
                        cursor.execute(f"UPDATE Estudiante  SET PrimerCorte = {query2} WHERE Nombre = '{name}'")
                        conn.commit()
                        print("nota ingresada CON EXITO :)")
                        break
                except Exception:
                    print("algo salio mal")
            elif(query == "2"):
                try:
                    query2 =(float(input("ingrese la nota: ")))
                    if(query2 < 0 or query2 > 5  ):
                        print("error al ingresar nota")
                        break
                    else:
                        cursor.execute(f"UPDATE Estudiante  SET SegundoCorte = {query2} WHERE Nombre = '{name}'")
                        break
                except Exception:
                    print("algo salio mal")
            elif(query == "3"):
                try:
                    query2 =(float(input("ingrese la nota: ")))
                    if(query2 < 0 or query2 > 5  ):
                        print("error al ingresar nota")
                        break
                    else:
                        cursor.execute(f"UPDATE Estudiante  SET tercerCorte = {query2} WHERE Nombre = '{name}'")
                        break
                except Exception:
                    print("algo salio mal")
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def peticionprofe(code, name,asign,peti): # peticiones profesores
    try:
        conn = sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion =(f"INSERT INTO PeticionesProfes VALUES ({code},'{name}','{asign}','{peti}','Espere su respuesta')")
        cursor.execute(introducion)
        conn.commit()
        print("peticion añadida")
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def SeePetiAnswers(name): # respuesta de las peticiones profesores
    try:
        conn = sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion = (f"SELECT * FROM  PeticionesProfes WHERE Nombre = '{name}'")
        cursor.execute(introducion)
        conn.commit()
        data = cursor.fetchall()
        for x,y,z,x1,y1 in data:
            print(f"Codigo : {x} || Nombre : {y}  || Asignatura : {z} ||Peticion : {x1} || respuesta : {y1}")
    except sl.OperationalError:
        print("ERROR")
    conn.close()
        
        
