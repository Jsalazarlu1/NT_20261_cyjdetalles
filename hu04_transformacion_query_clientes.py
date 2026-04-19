import pandas as pd

# 📌 1. Cargar dataset (generado en HU3)
df = pd.read_csv("clientes.csv")

print("✅ Dataset cargado")
print(df.head())


# 📌 2. Transformaciones necesarias
df["fecha_registro"] = pd.to_datetime(df["fecha_registro"])

# Nuevas columnas para análisis
df["anio_registro"] = df["fecha_registro"].dt.year
df["mes_registro"] = df["fecha_registro"].dt.month


# ======================================================
# 🔍 CONSULTA 1: Clientes registrados recientemente
# ======================================================
consulta1 = df.query("anio_registro >= 2025")

print("\n--- Consulta 1: Clientes recientes ---")
print(consulta1.head())
print("Cantidad:", len(consulta1))


# ======================================================
# 🔍 CONSULTA 2: Clientes con celular (empiezan en 3)
# ======================================================
consulta2 = df.query("telefono.str.startswith('3')", engine="python")

print("\n--- Consulta 2: Clientes con celular ---")
print(consulta2.head())
print("Cantidad:", len(consulta2))


# ======================================================
# 🔍 CONSULTA 3: Clientes específicos (Ana y Carlos)
# ======================================================
consulta3 = df.query("nombre in ['Ana', 'Carlos']")

print("\n--- Consulta 3: Clientes Ana y Carlos ---")
print(consulta3.head())
print("Cantidad:", len(consulta3))


# ======================================================
# 🔍 CONSULTA 4 (PRO 🔥): Clientes registrados en un mes específico
# (Ejemplo: marzo = mes 3)
# ======================================================
consulta4 = df.query("mes_registro == 3")

print("\n--- Consulta 4: Clientes registrados en marzo ---")
print(consulta4.head())
print("Cantidad:", len(consulta4))


# ======================================================
# ✅ VALIDACIONES (muy importante para la HU)
# ======================================================
print("\n--- VALIDACIONES ---")

print("Consulta 1 válida:",
      (consulta1["anio_registro"] >= 2025).all())

print("Consulta 2 válida:",
      consulta2["telefono"].str.startswith("3").all())

print("Consulta 3 válida:",
      consulta3["nombre"].isin(["Ana", "Carlos"]).all())

print("Consulta 4 válida:",
      (consulta4["mes_registro"] == 3).all())