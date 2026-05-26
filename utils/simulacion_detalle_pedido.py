import random

def generar_simulacion_detalle_pedido(numerSimulaciones):
    id_detalle_pedidos = ["AM1", "AM2", "AM3", "AM4", "AM5"]
    id_pedidos = [1, 2, 3, 4, 5]
    id_productos = [150000, 5000000, 1000000, 500000, 80000]
    cantidades = [1, 2, 3, 4, 5]
    precios_unitarios = [150000, 50000, 100000, 15000, 80000]

    simulaciones = []
    for _ in range(numerSimulaciones):
        cantidad = random.choice(cantidades)
        precio = random.choice(precios_unitarios)
        subtotal = cantidad * precio
        total = subtotal + int(subtotal * 0.19)

        detalle = {
            "id_detalle": random.choice(id_detalle_pedidos),
            "id_pedido": random.choice(id_pedidos),
            "id_producto": random.choice(id_productos),
            "cantidad": cantidad,
            "precio_unitario": precio,
            "subtotal": subtotal,
            "total": total,
        }

        probabilidadError = random.random()
        if probabilidadError < 0.15:
            detalle["id_detalle"] = ""
        elif probabilidadError < 0.25:
            detalle["id_pedido"] = random.choice(["", "cuatro", None])
        elif probabilidadError < 0.35:
            detalle["cantidad"] = random.choice([0, -1, "cinco", None])
        elif probabilidadError < 0.45:
            detalle["precio_unitario"] = random.choice([-5000, "cien mil", None])
        elif probabilidadError < 0.55:
            detalle["id_detalle"] = f"  {detalle['id_detalle']}  "

        simulaciones.append(detalle)

    return simulaciones
