from registro_ig import app
from flask import render_template,request
from config import *
from registro_ig.models import select_all,change_coins



@app.route("/")
def index():

    datos = select_all()
    
    return render_template("index.html",pageTitle="Listas",data=datos)


@app.route("/purchase", methods=["GET","POST"])
def operate():
    if request.method == "GET":
        return render_template("purchase.html",form="")

    else:
        
    
        if 'calcular' in request.form:

            moneda1=request.form['value_from']
            moneda2=request.form['value_to']

            cambio = change_coins(moneda1,moneda2)
            

            value_from_q=float(request.form['from_q'])

            valor_pu=value_from_q/cambio

            list_request={
                "value_from":request.form['value_from'],
                "from_q":request.form['from_q'],
                "value_to":request.form['value_to'],
                "to_q":str(cambio),
                "P_U":str(valor_pu)
            }
                
            return render_template("purchase.html", form=list_request)

        if 'comprar'in request.form:
            pass






@app.route("/status")
def status():
    return render_template("status.html")