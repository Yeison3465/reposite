import sqlite3 as sl

def CrearBAse():
    conn=sl.connect("PINGUINO.db")
    conn.commit()
    conn.close()