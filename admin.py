import base
import sqlite3 as sl
from os import system
system("cls")
import time
def createtable():
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Profesores(
            Codigo integer,
            Nombre text,
            Asignatura text 
        )"""
    )
    conn.commit()
    conn.close()

def CreateTableResquestsTeacher(): # tabla de los profesores
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE PeticionesProfes(
            Codigo integer,
            Nombre text,
            Asignatura text,
            peticion text,
            respuesta text 
        )"""
    )
    conn.commit()
    conn.close()

def CreateTableRequests():
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Peticiones(
            Codigo integer,
            Nombre text,
            Peticion text, 
            Respuesta text
        )"""
    )
    conn.commit()
    conn.close()

def CreatetableStudent(nameTable):
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""CREATE TABLE {nameTable}(
            Codigo integer,
            Nombre text,
            PrimerCorte real,
            SegundoCorte real,
            tercerCorte real,
            Definitiva real
        )"""
    )
    conn.commit()
    conn.close()
def Createtableadmin():
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE ADMINS(
            Usuario text,
            Contraseña text
        )"""
    )
    conn.commit()
    print("tabla creada")
    conn.close()

def InsertAdmin(user,contraseña): # Añadir admin
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO ADMINS VALUES ('{user}','{contraseña}')")
    conn.commit()
    print("BIENVENIDO ADMIN")
    conn.close()

def InsertEstudens(code,name): # insertar estudiante
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    instrucion=(f"INSERT INTO Estudiante VALUES ({code},'{name}',0,0,0,0)")
    cursor.execute(instrucion)
    instrucion2 =("SELECT * FROM Estudiante ORDER BY Nombre ASC")
    cursor.execute(instrucion2)
    print("se añadio un  dato")
    conn.commit()
    conn.close()

def Insert(code,name,asign): # insertar profes 
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    instrucion=(f"INSERT INTO profesores VALUES ({code},'{name}','{asign}')")
    cursor.execute(instrucion)
    conn.commit()
    conn.close()
def verify(user,password): # verific ADMINS
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    introducion=(f"SELECT * FROM ADMINS WHERE Usuario='{user}' AND Contraseña='{password}'")
    cursor.execute(introducion)
    conn.commit()
    tmp = cursor.fetchall()
    if(tmp):
        return True
    else:
        return False
    conn.close()

def verifyTeacher(user,code): # verificTeacher
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"SELECT * FROM Profesores WHERE Nombre ='{user}' AND Codigo='{code}'")
        cursor.execute(introducion)
        conn.commit()
        tmp = cursor.fetchall()
        if(tmp):
            return True
        else:
            return False
        
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def verifyStudent(user,code): # verificStudent
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"SELECT * FROM Estudiante WHERE Nombre ='{user}' AND Codigo= {code}")
        cursor.execute(introducion)
        conn.commit()
        tmp = cursor.fetchall()
        if(tmp):
            return True
        else:
            return False
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def verTablaAdmin(): # ver tabla de admin
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"SELECT * FROM ADMINS")
        cursor.execute(introducion)
        conn.commit()
        instrucion2 =("SELECT * FROM ADMINS ORDER BY Usuario ASC")
        cursor.execute(instrucion2)
        data = cursor.fetchall()
        i = 1
        for x, y in data:
            print(f"{i} Usuario {x} || password {y}")
            i = i + 1

    except sl.OperationalError:
        print("ERROR")
    conn.close()

def seeTableTeacher(): # ver tabla de profesores
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"SELECT * FROM Profesores")
        cursor.execute(introducion)
        conn.commit()
        instrucion2 =("SELECT * FROM Profesores ORDER BY Nombre ASC")
        cursor.execute(instrucion2)
        data = cursor.fetchall()
        i = 1
        for x,y,z in data:
            print(f"{i} || Codigo : {x} || Nombre : {y} || Asignatura : {z}") 
            i = i + 1
    except sl.OperationalError:
        print("ERROR")

def seeTableTeacherPeti(): # leer peticiones de profesores
    try:
        conn = sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"SELECT * FROM PeticionesProfes")
        cursor.execute(introducion)
        conn.commit()
        data = cursor.fetchall()
        i = 1 
        for x,y,z,x1,y1 in data:
            print(f"{i} || Codigo : {x} || Nombre : {y} || Asignatura : {z} || Peticion : {x1} || Respuesta : {y1}")
            i = i + 1
    except sl.OperationalError:
        print("ERROR")

def seeTableStudent(): # ver tabla de estudiante
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"SELECT * FROM Estudiante")
        cursor.execute(introducion)
        conn.commit()
        instrucion2 =("SELECT * FROM Estudiante ORDER BY Nombre ASC")
        cursor.execute(instrucion2)
        data = cursor.fetchall()
        i = 1
        for x,y,z,x1,y1,z1 in data:
            print(f"{i} || Codigo : {x} || Nombre : {y} || Primer Corte : {z} || Segundo Corte : {x1} || Tercer Corte : {y1} || Definitiva : {z1} ||") 
            i = i + 1
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def seeTableResponse(): # ver tabla de peteciones
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"SELECT * FROM Peticiones")
        cursor.execute(introducion)
        conn.commit()
        data = cursor.fetchall()
        i = 1
        for x,y,z,x1 in data:
            print(f"{i} || Codigo : {x} || Nombre : {y} || peticion : {z} || respuesta : {x1}") 
            i = i + 1
    except sl.OperationalError:
        print("ERROR")
    conn.close()



def UpdateTableStudens(code,name,note1,note2,note3,Rname): # actualizacion de la tabla de estudiante
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"UPDATE Estudiante  SET Codigo = {code},Nombre = '{name}',PrimerCorte = {note1},SegundoCorte = {note2},TercerCorte = {note3} where Nombre = '{Rname}'")
        cursor.execute(introducion)
        conn.commit()
        print("actualizacion de datos completa")
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def UpdateTableTeacher(code,user,Ruser): # actualizacion de la tabla de profesores
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"UPDATE Profesores  SET Codigo = {code} , Nombre = '{user}' where Nombre = '{Ruser}'")
        cursor.execute(introducion)
        print("actualizacion de datos completa")
        conn.commit()
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def response(response,name): # repuesta de peticion 
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion2 = (f"UPDATE Peticiones SET respuesta = '{response}' WHERE Nombre = '{name}'")
        cursor.execute(introducion2) 
        
        conn.commit()
        print("peticion de datos completa")
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def answer(name,response): # respuesta de profesores
    try:
        conn= sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion2 = (f"UPDATE PeticionesProfes SET Respuesta = '{response}' WHERE Nombre = '{name}'")
        cursor.execute(introducion2)
        conn.commit()
        print("respuesta añadida")
    except sl.OperationalError:
        print("ERROR")
    conn.close()

def DelateDataTable(table): # eliminar todos los datos
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        introducion=(f"TRUNCATE TABLE '{table}'")
        cursor.execute(introducion)
        conn.commit()
        print("datos eliminados")
    except sl.OperationalError:
        print("ERROR")
    conn.close()
    


def eliminar(tabla,code): # eliminar user o lo que este en untabla
    try:
        conn=sl.connect("PINGUINO.db")
        cursor = conn.cursor()
        instrucion= (f"DELETE from '{tabla}' where Codigo = {code}")
        cursor.execute(instrucion)
        conn.commit()
        print("Dato borrado")
    except Exception:
        print("ERROR")
    conn.close()

def borrartabla(table): # borra tabla
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    instrucion=(f"DROP TABLE '{table}' ")
    cursor.execute(instrucion)
    conn.commit()
    tmp = cursor.fetchall()
    print("tabla borrada")
    conn.close()


