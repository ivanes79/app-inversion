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

    cur.execute("insert into inversiones(date,time,Moneda_from,Quantity_from,Moneda_to,Quantity_to) values(?,?,?,?,?,?)",compra)

    con.commit()
    con.close()


def invertido():
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    inversion = cur.execute("SELECT SUM (Quantity_from) FROM inversiones where Moneda_from = 'EUR' " )
    
    con.close()

    return inversion

def sales():
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    vendido_EUR = cur.execute("SELECT SUM(Quantity_from) FROM inversiones WHERE Moneda_to = 'EUR' " )
    
    con.close()

    return vendido_EUR



def criptos_compradas():
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    criptos_compradas=cur.execute(f"SELECT DISTINCT Moneda_to FROM inversiones WHERE quantity_to != 0 AND Moneda_to != 'EUR' " ) 

    lista_criptos = []
    posicion=0
    for cripto in criptos_compradas:

        lista_criptos.append(criptos_compradas[posicion])
        posicion +1

    return lista_criptos

    #vendido = cur.execute(f"SELECT SUM(Quantity_to) FROM inversiones WHERE Moneda_to = {cripto} " )

     


def Q_criptos(cripto):

    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()
    compra_cripto = cur.execute(f"SELECT SUM(quantity_to) FROM inversiones WHERE Moneda_to = {cripto} " )
    venta_cripto = cur.execute(f"SELECT SUM(quantity_from) FROM inversiones WHERE Moneda_from = {cripto} " )
    cantidad_cripto = compra_cripto - venta_cripto
    con.close()

    
    

    return cantidad_cripto
