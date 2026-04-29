import pandas as pd

def limpiar_detalle_pedido(data_frame_sucio):
    # Crear una copia para evitar modificar el original
    data_frame_limpio = data_frame_sucio.copy()

    # 1. Rutina para evaluar los textos y estandarizar
    # Convertimos a string, quitamos espacios y pasamos a MAYÚSCULAS 
    # (Usamos upper porque tus "datos_esperados" están en mayúsculas)
    columna_texto = ["id_detalle", "id_pedido", "id_producto"]
    for columna in columna_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.upper()

    # 2. Definir los datos esperados según tu simulación
    datos_esperados = {
        "id_detalle": ["AM1", "AM2", "AM45", "AM50", "AM25"],
        "id_pedido": ["1", "2", "3", "4", "5"],
        "id_producto": ["150000", "5000000", "1000000", "500000", "80000"],
    }

    # 3. Limpiar con los datos esperados
    # Si un valor no está en la lista, se marca como pd.NA (nulo)
    for columna, valores in datos_esperados.items():
        data_frame_limpio[columna] = data_frame_limpio[columna].where(
            data_frame_limpio[columna].isin(valores), pd.NA)

    # 4. Rutina para evaluar números (cantidades y precios)
    columnas_numericas = ["cantidad", "precio", "subtotal", "total"]
    for col in columnas_numericas:
        data_frame_limpio[col] = pd.to_numeric(data_frame_limpio[col], errors='coerce')

    # 5. Filtros de validación lógica
    # Solo aceptamos registros con cantidades y totales positivos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["cantidad"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["total"] > 0]

    # 6. Manejo de campos obligatorios y duplicados
    campos_obligatorios = ["id_detalle", "id_pedido", "id_producto"]
    data_frame_limpio = data_frame_limpio.dropna(subset=campos_obligatorios)
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio