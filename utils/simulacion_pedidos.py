import random
def simular_pedido(numeroSimulaciones):
    #semillas por cada atributo de mi tabla 
    #fecha de creacion, fecha de entrega, tipo de detalle, estado, valor total


    
    fechas_creaciones=["2026-04-01-","2026-12-23","2026-06-22","2026-12-23","2026-12-23"]
    id_pedidos=[1,2,3,4,5]
    id_clientes=[1,2,3,4,5]
    id_empleados=[1,2,3,4,5]
    fechas_entregas=["2026-04-02-","2026-12-24","2026-06-23","2026-12-24","2026-12-24"]
    tipos_detalles=["desayuno","caja regalo","combo 1","velitas","caja_cumpleaños"]
    estados=["pendiente","en proceso","entregado","cancelado","en espera"]
    valores=[150000,50000,100000,15000,80000]
    
    pedidos=[]

    for _ in range (numeroSimulaciones):
        pedido={
            "id_pedido":random.choice(id_pedidos),
            "id_cliente":random.choice(id_clientes),
            "id_empleado":random.choice(id_empleados),
            "fecha_creacion":random.choice(fechas_creaciones),
            "fecha_entrega":random.choice(fechas_entregas),
            "tipo_detalle":random.choice(tipos_detalles),
            "estado":random.choice(estados),
            "valor":random.choice(valores),       
                      
        }
        pedidos.append(pedido)
    return pedidos