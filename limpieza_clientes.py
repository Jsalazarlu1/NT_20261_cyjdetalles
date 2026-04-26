import pandas as pd

def limpiar_datos_clientes(df_sucio):
    # Creamos una copia para no modificar el original
    df = df_sucio.copy()

    # 1. Rutina de textos: Quitar espacios extra y pasar a minúsculas
    # Aplicamos a nombre, ciudad, email y dirección
    columnas_texto = ["nombre", "ciudad", "email", "direccion", "tipo_doc"]
    for col in columnas_texto:
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip().str.lower()

    # 2. Rutina de números: Asegurar que sean valores numéricos
    df["documento"] = pd.to_numeric(df["documento"], errors="coerce")
    df["telefono"] = pd.to_numeric(df["telefono"], errors="coerce")
    df["id"] = pd.to_numeric(df["id"], errors="coerce")

    # 3. Rutina de fechas: Convertir a formato fecha real
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], errors="coerce")

    # 4. Manejo de vacíos: Si la fecha falló, ponemos una por defecto
    fecha_default = pd.to_datetime("2026-01-01")
    df["fecha_registro"] = df["fecha_registro"].fillna(fecha_default)

    # 5. Campos obligatorios: Si no hay id o nombre, borramos la fila
    df = df.dropna(subset=["id", "nombre", "documento"])

    # 6. Duplicados: Borrar registros idénticos
    df = df.drop_duplicates()

    return df