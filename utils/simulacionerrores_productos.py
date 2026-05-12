import random

from datetime import datetime,timedelta

def generar_simulacion(numeroSimulaciones):

    
    id_productos=[1,2,3,4,5]
    nombres=["Desayuno sorpresa premium", "Caja de dulces", "Recordatorio Lupe Baby", "Retablo Personalizado", "Ancheta feliz dia"]
    precios=[150000, 32000,85000,35000,85000]
    categorias=["Desayunos sorpresa","Otros Detalles","Velas artesanales","Retablos personalizados","Anchetas"]
    stocks=["30", "52", "33","63","15"]
    

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        simulacion={
            "id_producto":random.choice(id_productos),
            "nombre":random.choice(nombres),
            "precio":random.choice(precios),
            "categoria":random.choice(categorias),            
            "stock":random.choice(stocks),
            
        }
        #inyectando errores controlados
        probabilidadError=random.random()

        if(probabilidadError<0.2):
            simulacion["id_productos"]=None
        elif(probabilidadError<0.4):
            simulacion["nombre"]=random.choice(["Libro","Gelatina"])
        elif(probabilidadError<0.5):
            simulacion["precio"]=random.choice([0,-10000,None])
        elif(probabilidadError<0.8):
            simulacion["categoria"]=random.choice([" ","Comida","Bebida",None])        
        elif(probabilidadError<0.95):
            simulacion["stock"]=random.choice([-100,None])

        simulaciones.append(simulacion)
    return simulaciones