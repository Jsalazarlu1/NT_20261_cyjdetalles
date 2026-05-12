import pandas as pd

def limpiar_datos_clientes(df_sucio):
    # Creamos una copia para no modificar el original
    df = df_sucio.copy()

    # 1. Rutina de textos: Quitar espacios extra y pasar a minúsculas
    # Aplicamos a nombre, ciudad, email y dirección
    columnas_texto = ["nombre", "rol", "contrasena"]
    for col in columnas_texto:
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip().str.lower()

    # 2. Rutina de números: Asegurar que sean valores numéricos
    df["id"] = pd.to_numeric(df["id"], errors="coerce")

    # 3. Campos obligatorios: Si no hay id o nombre, borramos la fila
    df = df.dropna(subset=["id", "nombre", "contrasena"])

    # 4. Duplicados: Borrar registros idénticos
    df = df.drop_duplicates()

    return df