import sqlite3
from config import *
import requests
from flask import request


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


def change_coins_to_EUR(moneda1):

    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda1}/EUR?apikey={APIKEY}")
    cambio = r.json()
    
    return cambio["rate"]





def insert(compra):
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    cur.execute("insert into inversiones(date,time,Moneda_from,Quantity_from,Moneda_to,Quantity_to) values(?,?,?,?,?,?)",compra)

    con.commit()
    con.close()


def invertido(moneda):
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    res = cur.execute(f"SELECT SUM (Quantity_from) FROM inversiones where Moneda_from = ?",[moneda] )
    filas = res.fetchall()
    columnas= res.description

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
    
    con.close()
   
    return resultado1


def recuperado(moneda):
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    res = cur.execute(f"SELECT SUM(Quantity_to) FROM inversiones WHERE Moneda_to == ?",[moneda] )

    filas = res.fetchall()#capturo las filas de datos
    columnas= res.description#capturo los nombres de columnas

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

    con.close()
    return resultado2


def criptos_compradas():
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    res=cur.execute(f"SELECT DISTINCT Moneda_to FROM inversiones WHERE quantity_to != 0 AND Moneda_to != 'EUR' " ) 

    filas=res.fetchall()
    columnas= res.description
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

    con.close()
    
    return monedas

def valor_actual_cripto(moneda):

    
    ventas = recuperado(moneda)
    

   
    return ventas

def validar_compra():
    
    errores=[]
    if request.form['from_q'] > valor_actual_cripto(request.form['value_q']): 
        errores.append("Moneda insuficiente. Debes comprar menos cantidad")
    '''
    if requestForm['concept'] == "":
        errores.append("concepto vacio: Introduce un concepto para el registro")
    if requestForm['quantity'] == "" or float(requestForm['quantity']) == 0.0:
        errores.append("cantidad vacio o cero: Introduce una cantidad positiva o negativa")  
    '''
    return errores
    

def q_monedas(moneda1):

    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    res = cur.execute(f"SELECT SUM(quantity_to) FROM inversiones WHERE Moneda_to = {moneda1} " )

    compra_cripto = res.fetchall()
   
    
    

  

    con.close()

    
    

    return cantidad_cripto
