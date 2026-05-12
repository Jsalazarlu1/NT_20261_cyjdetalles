import pandas as pd
from utils.simulacionerrores_clientes import simular_clientes

def limpiar_clientes(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # Rutina textos
    columnas_texto = ["tipo_doc", "nombre", "ciudad", "email", "direccion"]
    for columna in columnas_texto:
        if columna in data_frame_limpio.columns:
            data_frame_limpio[columna] = (
                data_frame_limpio[columna]
                .astype("string")
                .str.strip()
                .str.lower()
            )
    tipos_esperados = ["cc", "ce", "nit"]
    data_frame_limpio["tipo_doc"] = data_frame_limpio["tipo_doc"].where(
        data_frame_limpio["tipo_doc"].isin(tipos_esperados),
        pd.NA
    )

    # Rutina números
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio["documento"] = pd.to_numeric(data_frame_limpio["documento"], errors="coerce")
    data_frame_limpio["telefono"] = pd.to_numeric(data_frame_limpio["telefono"], errors="coerce")
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]

    # Rutina fechas
    data_frame_limpio["fecha_registro"] = pd.to_datetime(
        data_frame_limpio["fecha_registro"], errors="coerce"
    )
    fecha_default = pd.to_datetime("2024-01-01")
    data_frame_limpio["fecha_registro"] = data_frame_limpio["fecha_registro"].fillna(fecha_default)

    # Campos obligatorios
    columnas_obligatorias = ["id", "tipo_doc", "documento", "nombre"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # Duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio


# --- EJECUCIÓN ---
if __name__ == "__main__":
    datos = simular_clientes(10)
    df_sucio = pd.DataFrame(datos)

    print("=== DATOS SUCIOS ===")
    print(df_sucio.to_string())
    print(f"\nTotal filas sucias: {len(df_sucio)}")
    print(f"Nulos por columna:\n{df_sucio.isnull().sum()}")

    df_limpio = limpiar_clientes(df_sucio)

    print("\n=== DATOS LIMPIOS ===")
    print(df_limpio.to_string())
    print(f"\nTotal filas limpias: {len(df_limpio)}")