import random

def simular_detallepedido(numeroSimulaciones): # Simula el detalle del pedido, generando datos aleatorios para cada atributo de la tabla DetallePedido
    # Semillas por cada atributo de mi tabla

    id_detalle = ["AM1", "AM2", "AM45", "AM50", "AM25"]
    id_pedido = [1, 2, 3, 4, 5]
    id_producto = [150000, 5000000, 1000000, 500000, 80000]
    cantidades = [10, 20, 30, 40, 50]
    precios = [150000, 5000000, 1000000, 500000, 80000]

    detalles_pedido = []  #Lista para almacenar los detalles del pedido generados
    for _ in range(numeroSimulaciones):
        cantidad = random.choice(cantidades)
        precio = random.choice(precios)
        subtotal = cantidad * precio
        total = subtotal + int(subtotal * 0.19)

#Creo un diccionario para cada detalle del pedido con los atributos correspondientes y lo agrego a la lista detalles_pedido
        detalle_pedido = {
            "id_detalle": random.choice(id_detalle),
            "id_pedido": random.choice(id_pedido),
            "id_producto": random.choice(id_producto),
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal,
            "total": total,
        }
        detalles_pedido.append(detalle_pedido)

    return detalles_pedido