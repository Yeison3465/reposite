import base
import sqlite3 as sl

# aqui va lo que de los estudiantes 

def SeeNotes(name): # ver las notas de un estudiante expecifico
    try:
        conn = sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion = (f"SELECT * FROM  Estudiante WHERE Nombre = '{name}'")
        cursor.execute(introducion)
        conn.commit()
        data = cursor.fetchall()
        for x,y,z,x1,y1,z1 in data:
            print(f"Codigo : {x} || Nombre : {y} || Primer Corte : {z} || Segundo Corte : {x1} || Tercer Corte : {y1} || Definitiva : {z1} ")
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def peti(code, name,peti): # envia runa peticion
    try:
        conn = sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion =(f"INSERT INTO Peticiones VALUES ({code},'{name}','{peti}','espere su respuesta')")
        cursor.execute(introducion)
        conn.commit()
        print("peticion añadida")

    except sl.OperationalError:
        print("ERROR")
    conn.close()

def SeePetiAnswersEstu(name): # ver respuesta de la peticion
    try:
        conn = sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion = (f"SELECT * FROM  Peticiones WHERE Nombre = '{name}'")
        cursor.execute(introducion)
        conn.commit()
        data = cursor.fetchall()
        for x,y,x1,y1 in data:
            print(f"Codigo : {x} || Nombre : {y} || Peticion : {x1} || respuesta : {y1}")
    except sl.OperationalError:
        print("ERROR")
    conn.close()

