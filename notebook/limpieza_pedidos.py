import pandas as pd

def limpiar_pedidos(data_frame_sucio):

    data_frame_limpio = data_frame_sucio.copy()

    # limpieza de columnas de texto
    columnas_texto = ["tipo_detalle", "estado", "fecha_creacion"]

    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    # valores válidos
    detalles_validos = ["desayuno","caja regalo","combo 1","velitas","caja_cumpleaños"]
    estados_validos = ["pendiente","en proceso","entregado","cancelado","en espera"]

    data_frame_limpio["tipo_detalle"] = data_frame_limpio["tipo_detalle"].where(
        data_frame_limpio["tipo_detalle"].isin(detalles_validos),
        pd.NA
    )

    data_frame_limpio["estado"] = data_frame_limpio["estado"].where(
        data_frame_limpio["estado"].isin(estados_validos),
        pd.NA
    )

    # limpieza de columnas numéricas
    columnas_numericas = ["id_pedido", "id_cliente", "id_empleado", "valor"]

    for col in columnas_numericas:
        data_frame_limpio[col] = pd.to_numeric(data_frame_limpio[col], errors="coerce")

    # reglas de negocio
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_pedido"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_cliente"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_empleado"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["valor"] > 10000]

    # limpieza de fechas
    data_frame_limpio["fecha_creacion"] = pd.to_datetime(
        data_frame_limpio["fecha_creacion"], errors="coerce"
    )

    data_frame_limpio["fecha_entrega"] = pd.to_datetime(
        data_frame_limpio["fecha_entrega"], errors="coerce"
    )

    fecha_defecto = pd.to_datetime("2026-01-01")

    data_frame_limpio["fecha_creacion"] = data_frame_limpio["fecha_creacion"].fillna(fecha_defecto)
    data_frame_limpio["fecha_entrega"] = data_frame_limpio["fecha_entrega"].fillna(fecha_defecto)

    # eliminar filas con valores nulos en columnas obligatorias
    columnas_obligatorias = [
        "id_pedido","id_cliente","id_empleado",
        "tipo_detalle","estado","valor"
    ]

    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio

