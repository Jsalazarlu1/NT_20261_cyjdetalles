import pandas as pd

# 📌 1. Cargar dataset
df = pd.read_csv("clientes.csv")

print("✅ Dataset cargado")
print(df.head())


# 📌 2. Transformaciones necesarias
df["fecha_registro"] = pd.to_datetime(df["fecha_registro"])
df["anio_registro"] = df["fecha_registro"].dt.year
df["mes_registro"] = df["fecha_registro"].dt.month


# ======================================================
# 📊 AGRUPACIÓN 1: Clientes por nombre
# (¿Qué nombres son más frecuentes?)
# ======================================================

agrupacion1 = df.groupby("nombre").agg({
    "id_cliente": "count"
}).rename(columns={"id_cliente": "cantidad_clientes"})

print("\n--- Agrupación 1: Clientes por nombre ---")
print(agrupacion1.sort_values(by="cantidad_clientes", ascending=False))


# ======================================================
# 📊 AGRUPACIÓN 2: Clientes por mes de registro
# (Comportamiento temporal)
# ======================================================

agrupacion2 = df.groupby("mes_registro").agg({
    "id_cliente": "count"
}).rename(columns={"id_cliente": "cantidad_clientes"})

print("\n--- Agrupación 2: Clientes por mes ---")
print(agrupacion2.sort_index())


# ======================================================
# 📊 AGRUPACIÓN 3 (PRO 🔥): Nombre + Mes
# (Segmentación cruzada)
# ======================================================

agrupacion3 = df.groupby(["nombre", "mes_registro"]).agg({
    "id_cliente": "count"
}).rename(columns={"id_cliente": "cantidad_clientes"})

print("\n--- Agrupación 3: Nombre y mes ---")
print(agrupacion3.head(10))


# ======================================================
# 📊 MÉTRICAS ADICIONALES (más nivel)
# ======================================================

resumen = df.groupby("nombre").agg({
    "id_cliente": ["count"],
    "mes_registro": ["min", "max"]
})

print("\n--- Resumen adicional por nombre ---")
print(resumen)