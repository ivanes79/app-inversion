import sqlite3
from config import *
import requests
from flask import request
from registro_ig.conexion import Conexion



def select_all():
    connect = Conexion("select date,time,moneda_from,quantity_from,moneda_to,quantity_to from inversiones;")

    filas = connect.res.fetchall()    
    columnas= connect.res.description  

       

    
    resultado =[]   #lista para guadar diccionario
   
    for fila in filas:
        dato={}   #diccionario para cada registro
        posicion=0   #posicion de columna

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)

    

    connect.con.close()
    return resultado

def change_coins(moneda1,moneda2):
    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda1}/{moneda2}?apikey={APIKEY}")
    cambio = r.json()
    
    return cambio["rate"]


def change_coins_to_EUR(moneda1):

    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda1}/EUR?apikey={APIKEY}")
    cambio = r.json()
    
    return cambio["rate"]





def insert(compra):
    connect = Conexion("insert into inversiones(date,time,Moneda_from,Quantity_from,Moneda_to,Quantity_to) values(?,?,?,?,?,?)",compra)

    connect.con.commit()
    connect.con.close()


def invertido(moneda):
    connect = Conexion(f"SELECT SUM (Quantity_from) FROM inversiones where Moneda_from = ?",[moneda] )
    filas = connect.res.fetchall()
    columnas= connect.res.description

    resultado =[]

    for fila in filas:
        dato={}
        posicion=0

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)
        resultado1 = resultado[0]['SUM (Quantity_from)']
        resultado1 = float(resultado1)
    
    connect.con.close()
   
    return resultado1


def recuperado(moneda):
    connect = Conexion(f"SELECT SUM(Quantity_to) FROM inversiones WHERE Moneda_to == ?",[moneda] )

    filas = connect.res.fetchall()#capturo las filas de datos
    columnas= connect.res.description#capturo los nombres de columnas

    #objetivo crear una lista de diccionario con filas y columnas


    resultado =[]#lista para guadar diccionario

    for fila in filas:
        dato={}#diccionario para cada registro
        posicion=0#posicion de columna

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)
        resultado2 = resultado[0]['SUM(Quantity_to)']
        resultado2 = float(resultado2)

    connect.con.close()
    return resultado2


def criptos_compradas():
    connect = Conexion(f"SELECT DISTINCT Moneda_to FROM inversiones WHERE quantity_to != 0 AND Moneda_to != 'EUR' " ) 

    filas=connect.res.fetchall()
    columnas= connect.res.description
    resultado =[]

    for fila in filas:
        dato={}
        posicion=0

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)
        

        
    monedas = []
    moneda = 0
        
    for moneda in range(len(resultado)):
        
        cripto = resultado[moneda]
        monedas.append(cripto['Moneda_to'])
        moneda+=1

    connect.con.close()
    
    return monedas



    


   
    
    

  

   

    
    

   
