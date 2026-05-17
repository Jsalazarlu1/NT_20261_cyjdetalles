import pandas as pd

def transformar_datos(data_frame_limpio):

    print("***** FILTROS APLICADOS *****")

    # ==================================================
    # FILTRO 1:
    # Pedidos entregados agrupados por fecha_creacion
    # (ideal para gráfico de líneas)

    filtro1 = data_frame_limpio.query("estado == 'entregado'")
    agrupacion1 = filtro1.groupby("fecha_creacion")["id_pedido"].count().reset_index(name="cantidad")
    print(agrupacion1)

    # ==================================================
    # FILTRO 2:
    # Pedidos con valor mayor o igual a 100000
    # agrupados por tipo_detalle
    # (ideal gráfico de barras)
    # ==================================================
    filtro2 = data_frame_limpio.query("valor >= 100000")
    agrupacion2 =filtro2.groupby("tipo_detalle")["id_pedido"].count().reset_index(name="cantidad")
    print(agrupacion2)


    # ==================================================
    # FILTRO 3:
    # Pedidos creados en abril de 2026
    # ==================================================
    filtro3 = data_frame_limpio.query(
        "fecha_creacion >= '2026-04-01' and fecha_creacion <= '2026-04-30'"
    )

    agrupacion3 = (
        filtro3.groupby("estado")["id_pedido"]
        .count()
        .reset_index(name="cantidad")
    )

    print("\n3. PEDIDOS DE ABRIL 2026")
    print(agrupacion3)


    # ==================================================
    # FILTRO 4:
    # Promedio del valor por estado
    # ==================================================
    agrupacion4 = (
        data_frame_limpio.groupby("estado")["valor"]
        .mean()
        .reset_index(name="promedio_valor")
    )

    print("\n4. PROMEDIO DE VALOR POR ESTADO")
    print(agrupacion4)


    # ==================================================
    # FILTRO 5:
    # Total de ventas por mes
    # (ideal gráfico mensual)
    # ==================================================
    data_frame_limpio["mes"] = data_frame_limpio["fecha_creacion"].dt.month

    agrupacion5 = (
        data_frame_limpio.groupby("mes")["valor"]
        .sum()
        .reset_index(name="ventas_totales")
    )

    print("\n5. VENTAS TOTALES POR MES")
    print(agrupacion5)


    # retornar resultados por si los necesitas luego
    return {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }