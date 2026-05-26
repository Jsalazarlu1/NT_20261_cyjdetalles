import pandas as pd

def transformar_detalle_pedido(date_frame_limpio):
    # transformacion 1 (cuantos detalles por cada pedido)
    filtro1 = date_frame_limpio.groupby("id_pedido").size().reset_index(name="cantidad_detalles")
    agrupacion1 = filtro1.groupby("cantidad_detalles").size().reset_index(name="cantidad_pedidos")
    print("Cantidad de detalles por pedido:", agrupacion1)

    # transformacion 2 (productos que se vendieron mayor de 100000)
    filtro2 = date_frame_limpio.query("precio_unitario > 100000")
    agrupacion2 = filtro2.groupby("id_producto").size().reset_index(name="cantidad_veces_vendido")
    print("Productos vendidos con precio mayor a 100000:", agrupacion2)

    # transformacion 3 (total recaudado por cada producto)
    agrupacion3 = date_frame_limpio.groupby("id_producto")["total"].sum().reset_index(name="total_recaudado")
    print("Total recaudado por producto:", agrupacion3)

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3
    }

    return agrupacion_resumen
