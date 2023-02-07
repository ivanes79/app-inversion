from registro_ig import app
from flask import render_template,request,url_for,redirect
from config import *
from registro_ig.models import select_all,change_coins,insert,invertido,sales,Q_criptos
import datetime



@app.route("/")
def index():

    datos = select_all()
    if datos == "":
        print("NO HAY MOVIMIENTOS")

    else:
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
            '''
            insert(["25-12-2022",
                    "10:00:00",
                    request.form["value_from"],
                    request.form["from_q"],
                    request.form["value_from"],
                    request.form["to_q"] ])
                    
            return redirect(url_for("index"))

            date = datetime.date.today()
            
            time = datetime.date.today()


            '''

            if request.form['value_from'] == "EUR":
                insert(["01-01-2023",
                    "10:00:00",
                    request.form["value_from"],
                    request.form["from_q"],
                    request.form["value_from"],
                    request.form["to_q"] ])

                return redirect(url_for("index"))
           
            else :
                
                if request.form['from_q'] > Q_criptos(request.form['value_from']):
                    print("Esta compra no se puede realizar")

                else:
                    insert(["01-01-2023",
                    "10:00:00",
                    request.form["value_from"],
                    request.form["from_q"],
                    request.form["value_from"],
                    request.form["to_q"] ])

                    return redirect(url_for("index"))
            
            
               
            






@app.route("/status")
def status():

    cripto = Q_criptos()


    return render_template("status.html",data=cripto)
    '''
    Esta pantalla mostrará tres valores relativos al valor en euros de nuestra cartera de criptomonedas, a saber:
    Invertido: Es el total de euros con el que se han comprado criptos. Se calcula como 
    la suma de la columna Cantidad_from de todos los movimientos cuya Moneda_from es EUROS.

    Recuperado: Es el total de euros obtenidos con la venta de cualquier cripto (registrada en nuestro sistema). Se calcula como 
    la suma de la columna Cantidad_to de todos los movimientos cuya Moneda_to es EUROS.

    Valor de compra: Es el resultado de la operación Invertido - Recuperado

    Valor actual en euros de nuestras criptos: Al existir varias posibles criptos debemos
    Para cada cripto obtener su total como: La suma de Cantidad_to de todos los movimientos cuya Moneda_to
     es la cripto en cuestión menos la suma de Cantidad_from de todos los movimientos 
    '''
    '''
            elif request.form['value_to'] == "EUR":
                insert(["01-01-2023",
                    "10:00:00",
                    request.form["value_from"],
                    request.form["from_q"],
                    request.form["value_from"],
                    request.form["to_q"] ])

                return redirect(url_for("index"))
    '''