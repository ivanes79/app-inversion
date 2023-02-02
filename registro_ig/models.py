import sqlite3
from config import *
import requests


def select_all():
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    res = cur.execute("select date,time,moneda_from,quantity_from,moneda_to,quantity_to from inversiones;")

    filas = res.fetchall()    #capturo las filas de datos
    columnas= res.description   #capturo los nombres de columnas

       #objetivo crear una lista de diccionario con filas y columnas

    
    resultado =[]   #lista para guadar diccionario
   
    for fila in filas:
        dato={}   #diccionario para cada registro
        posicion=0   #posicion de columna

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)


    con.close()
    return resultado

def change_coins(moneda1,moneda2):
    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda1}/{moneda2}?apikey={APIKEY}")
    cambio = r.json()
    
    return cambio["rate"]

def insert(compra):
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    cur.execute("insert into inversiones(date,time,moneda_from,quantity_from,moneda_to,quantity_to)values(?,?,?,?,?,?)",compra)
    con.close()
