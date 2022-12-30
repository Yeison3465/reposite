"""if(PIN in code):
            userAd = (input("Ingrese la usuario: "))
            passW = (input("Ingrese la contraseña: "))
            if(ad.verify(userAd, passW)):
                very=(input("Ingrese el codido para ver el menu: "))
                if(very in code1):
                    print("")
                    print("====== BIENVENIDO AL MENU DE ADMINS ======")
                else:
                    print("NO TIENE ACCESO AL MENU")
            else:
                print("ERROR")
                time.sleep(1)
                system("cls")
                break
        else:
            print("ACCESO DENEGADO")
            print("VUELVA ABRIR EL PROGRAMA")
            time.sleep(5)
            system("cls")
            break"""



"""print("ingrese el PIN de para iniciar sesion")
            try:
                PIN = (int(input("Ingrese: ")))
            except Exception:
                print("Hubo un error")
                time.sleep(0.5)
                i = i + 1
                if(i == 4):
                    print("HUBO MUCHOS INTENTOS")
                    break
                system("cls")"""
import base
import sqlite3 as sl
import admin as a
def access():
    conn=sl.connect("PINGUINO.db")
    cursor = conn.cursor()
    instrucion2 =("SELECT * FROM Estudiante ORDER BY Nombre ASC")
    cursor.execute(instrucion2)
    datos = cursor.fetchall()
    print("se añadio un  dato")
    conn.commit()
    print((datos))
    conn.close()

access()
a.eliminar("asdads",401)

