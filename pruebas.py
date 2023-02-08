import sqlite3
from config import *
import requests
from flask import request
from registro_ig.models import *

cantidades_criptos=[]
lista_criptos=criptos_compradas()
for item in range(len(lista_criptos)):
    cantidades=valor_actual_cripto(lista_criptos[item])
    cantidades_criptos.append(cantidades)
    item +=1

#cripto = valor_actual_cripto('BTC')
print(cantidades_criptos)

'''
errores=[]
if request.form['from_q'] > valor_actual_cripto(request.form['value_q']): 
    errores.append("Moneda insuficiente. Debes comprar menos cantidad")



con = sqlite3.connect(INVERSION_DATA)
cur = con.cursor()

res = cur.execute(f"SELECT SUM(Quantity_to) FROM inversiones WHERE Moneda_to = 'EUR' " )

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
    #resultado2 = resultado[0]['SUM(Quantity_to)']
    #resultado2 = float(resultado2)

    
con.close()
monedas = []
moneda = 0
for moneda in range(len(resultado)): 
    if resultado[moneda]['SUM(Quantity_to)']== None:
        print('No hay monedas de este tipo')
        
    else:
        print(resultado)
        
        #cripto = resultado[moneda]
        #monedas.append(cripto)
        #moneda+=1

#return resultado2





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
print(monedas)
return monedas



con = sqlite3.connect(INVERSION_DATA)
cur = con.cursor()

res = cur.execute("SELECT SUM (Quantity_from) FROM inversiones where Moneda_from = 'EUR' " )
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
print(resultado1)
    #return resultado1


con = sqlite3.connect(INVERSION_DATA)
cur = con.cursor()

res=cur.execute(f"SELECT DISTINCT Moneda_to FROM inversiones WHERE quantity_to != 0 AND Moneda_to != 'EUR' " ) 

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
    #resultado1 = resultado[0]['SUM (Quantity_from)']
    #resultado1 = float(resultado1)

for coins in resultado:
    cantidad_cripto=resultado

con.close()
print(resultado)
     


def sales():
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    res = cur.execute("SELECT SUM(Quantity_to) FROM inversiones WHERE Moneda_to = 'EUR' " )

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
    return resultado

'''