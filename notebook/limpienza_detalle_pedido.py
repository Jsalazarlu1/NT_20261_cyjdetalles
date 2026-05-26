import pandas as pd

def limpiar_detalle_pedido(data_frame_sucio):
    
    data_frame_limpio = data_frame_sucio.copy()
    
    # 1. Limpiar espacios en blanco en columnas de texto
    for col in data_frame_limpio.select_dtypes(include='object').columns:
        data_frame_limpio[col] = data_frame_limpio[col].str.strip()
    
    # 2. id_detalle se mantiene como texto (código alfanumérico)
    # Reemplazar vacíos con NaN para que dropna los elimine
    data_frame_limpio["id_detalle"] = data_frame_limpio["id_detalle"].replace("", pd.NA)
    
    # 3. Convertir IDs numéricos (id_pedido, id_producto)
    data_frame_limpio["id_pedido"] = pd.to_numeric(data_frame_limpio["id_pedido"], errors='coerce')
    data_frame_limpio["id_producto"] = pd.to_numeric(data_frame_limpio["id_producto"], errors='coerce')

    # 4. Columnas numéricas (cantidad, precios)
    columnas_numericas = ["cantidad", "precio_unitario", "subtotal", "total"]
    for col in columnas_numericas:
        data_frame_limpio[col] = pd.to_numeric(data_frame_limpio[col], errors='coerce')

    # 5. Filtros de validación lógica
    data_frame_limpio = data_frame_limpio[data_frame_limpio["cantidad"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["total"] > 0]

    # 6. Manejo de campos obligatorios y duplicados
    campos_obligatorios = ["id_detalle", "id_pedido", "id_producto"]
    data_frame_limpio = data_frame_limpio.dropna(subset=campos_obligatorios)
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio