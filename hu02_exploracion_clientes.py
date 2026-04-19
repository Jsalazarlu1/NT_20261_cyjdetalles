import pandas as pd

def explorar_clientes(clientes):

    # =====================================================
    # ✔ 1. Cargar dataset en DataFrame
    # =====================================================
    df = pd.DataFrame(clientes)

    print("\n📌 DATAFRAME CARGADO CORRECTAMENTE\n")

    # =====================================================
    # ✔ 2. Visualizar muestras
    # =====================================================
    print("🔹 HEAD (primeros registros):")
    print(df.head())

    print("\n🔹 TAIL (últimos registros):")
    print(df.tail())

    # =====================================================
    # ✔ 3. Inspección de estructura
    # =====================================================
    print("\n🔹 INFO DEL DATAFRAME:")
    print(df.info())

    # =====================================================
    # ✔ 4. Estadísticas descriptivas
    # =====================================================
    print("\n🔹 DESCRIBE (estadísticas):")
    print(df.describe(include='all'))

    # =====================================================
    # ✔ 5. Filas, columnas y nombres
    # =====================================================
    print("\n🔹 DIMENSIONES DEL DATASET:")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")

    print("\n🔹 NOMBRES DE COLUMNAS:")
    print(df.columns.tolist())

    # =====================================================
    # ✔ 6. Identificar tipos de columnas
    # =====================================================
    columnas_numericas = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()

    print("\n🔹 COLUMNAS NUMÉRICAS:")
    print(columnas_numericas)

    print("\n🔹 COLUMNAS CATEGÓRICAS:")
    print(columnas_categoricas)

    return df


# =====================================================
# 🔹 PRUEBA
# =====================================================
if __name__ == "__main__":

    from hu01_crear_cliente import crear_clientes

    clientes = crear_clientes(10)

    explorar_clientes(clientes)