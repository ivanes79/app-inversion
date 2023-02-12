from registro_ig import app
from flask import render_template,request,url_for,redirect
from config import *
from registro_ig.models import select_all,change_coins,insert,invertido,recuperado,criptos_compradas,change_coins_to_EUR
from datetime import datetime



@app.route("/")
def index():

    datos = select_all()
    return render_template("index.html",pageTitle="Listas",data=datos)
    


@app.route("/purchase", methods=["GET","POST"])
def operate():
    if request.method == "GET":
        return render_template("purchase.html",form="",msgError='error')

    else:
        
    
        if 'calcular' in request.form:

            
            moneda1=request.form['value_from']
            moneda2=request.form['value_to']

            cambio = change_coins(moneda1,moneda2)
            

            value_from_q=float(request.form['from_q'])

            valor_pu=value_from_q * cambio

            list_request={
                "value_from":request.form['value_from'],
                "from_q":request.form['from_q'],
                "value_to":request.form['value_to'],
                "to_q":str(valor_pu),
                "P_U":str(cambio)
            }
                
            return render_template("purchase.html", form=list_request,msgError='error' )

        if 'comprar'in request.form:


            moneda1=request.form['value_from']
            moneda2=request.form['value_to']

            cambio = change_coins(moneda1,moneda2)
            

            value_from_q=float(request.form['from_q'])

            valor_pu=value_from_q * cambio

            list_request={
                "value_from":request.form['value_from'],
                "from_q":request.form['from_q'],
                "value_to":request.form['value_to'],
                "to_q":str(valor_pu),
                "P_U":str(cambio)
            }
 
            now = datetime.now()

            
            if request.form['value_from'] == "EUR":
                insert([now.strftime("%Y-%m-%d"),
                        now.strftime("%H:%M:%S"),
                        request.form["value_from"],
                        request.form["from_q"],
                        request.form["value_to"],
                        request.form["to_q"] ])
                
                return redirect(url_for("index"))
           
            else :
                
                errores=[]
                if float(request.form['from_q']) > recuperado(request.form['value_from']):
                    errores.append("Moneda insuficiente. Debes comprar menos cantidad")
                    return render_template("purchase.html", msgError=errores, form=list_request)
                
                else:
                    insert([now.strftime("%Y-%m-%d"),
                            now.strftime("%H:%M:%S"),
                            request.form["value_from"],
                            request.form["from_q"],
                            request.form["value_to"],
                            request.form["to_q"] ])

                    return redirect(url_for("index"))
            
@app.route("/status")
def status():

    ventas=recuperado('EUR')
    compras=invertido('EUR')
    valor_de_compra=compras-ventas
    
    lista_criptos=criptos_compradas()
    valor_actual=0
    for cripto in lista_criptos:
        cantidad = recuperado(cripto)
        valor_actual += cantidad  * change_coins_to_EUR(cripto)



    color= ""    
    if valor_actual > valor_de_compra:
        color = "verde"
        
    else:
        color = "rojo"

    



    return render_template("status.html",compras=compras,ventas=ventas,valor_de_compra=valor_de_compra,valor_actual=valor_actual,color=color)
       
               