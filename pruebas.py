import sqlite3
from config import *

def criptos_compradas():
    con = sqlite3.connect(INVERSION_DATA)
    cur = con.cursor()

    criptos_compradas=cur.execute(f"SELECT DISTINCT Moneda_to FROM inversiones WHERE quantity_to != 0 AND Moneda_to != 'EUR' " ) 
    

    return criptos_compradas
    