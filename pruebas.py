import sqlite3
from config import *
import requests
from flask import request
from registro_ig.models import *



datos = select_all()
print(datos)




