import random

from datetime import datetime,timedelta

def generar_simulacion(numeroSimulaciones):

    fechas_creaciones=["2026-04-01-","2026-12-23","2026-06-22","2026-12-23","2026-12-23"]
    id_pedidos=[1,2,3,4,5]
    id_clientes=[1,2,3,4,5]
    id_empleados=[1,2,3,4,5]
    fechas_entregas=["2026-04-02-","2026-12-24","2026-06-23","2026-12-24","2026-12-24"]
    tipos_detalles=["desayuno","caja regalo","combo 1","velitas","caja_cumpleaños"]
    estados=["pendiente","en proceso","entregado","cancelado","en espera"]
    valores=[150000,50000,100000,15000,80000]

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        simulacion={
            "id_pedido":random.choice(id_pedidos),
            "id_cliente":random.choice(id_clientes),
            "id_empleado":random.choice(id_empleados),
            "fecha_creacion":random.choice(fechas_creaciones),
            "fecha_entrega":random.choice(fechas_entregas),
            "tipo_detalle":random.choice(tipos_detalles),
            "estado":random.choice(estados),
            "valor":random.choice(valores),
        }
        #inyectando errores controlados
        probabilidadError=random.random()

        if(probabilidadError<0.2):
            simulacion["id_pedido"]=None
        elif(probabilidadError<0.4):
            simulacion["id_cliente"]=random.choice(["clased de python","clase de ingles"])
        elif(probabilidadError<0.5):
            simulacion["id_empleado"]=random.choice([0,-10000,None])
        elif(probabilidadError<0.8):
            simulacion["fecha_creacion"]=" "+simulacion["fecha_creacion"].upper()
        elif(probabilidadError<0.9):
            simulacion["fecha_entrega"]=None
        elif(probabilidadError<0.95):
            simulacion["tipo_detalle"]=random.choice([" ","desayuno",None]) 
        elif(probabilidadError<0.98):
            simulacion["estado"]=random.choice([" ","pendiente",None])  
        elif(probabilidadError<0.99):
            simulacion["valor"]=random.choice([-1000,0,None])

        simulaciones.append(simulacion)
    return simulaciones