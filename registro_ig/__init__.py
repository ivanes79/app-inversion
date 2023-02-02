from flask import Flask #importar flask

app = Flask(__name__,instance_relative_config=True)   # definir la app que en init definimos en main y para que funcione la clave secreta
app.config.from_object("config")    #para que reconozca la clave secreta desde config.py

from registro_ig.routes import *