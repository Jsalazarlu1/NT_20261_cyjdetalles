import pandas as pd
import random
from datetime import datetime, timedelta

# 📌 1. Configuración
n = 1000

nombres = ["Ana", "Luis", "Carlos", "Marta", "Sofia", "Pedro"]
calles = ["Calle 10", "Carrera 50", "Av Siempre Viva", "Calle 80"]
dominios = ["gmail.com", "hotmail.com", "yahoo.com"]

data = []

# 📌 2. Generar datos sintéticos
for i in range(n):
    nombre = random.choice(nombres)
    
    registro = {
        "id_cliente": i + 1,
        "nombre": nombre,
        "telefono": "3" + str(random.randint(100000000, 999999999)),
        "direccion": random.choice(calles) + " #" + str(random.randint(1, 200)),
        "email": nombre.lower() + str(i) + "@" + random.choice(dominios),
        "fecha_registro": datetime.now() - timedelta(days=random.randint(0, 365))
    }
    
    data.append(registro)

df = pd.DataFrame(data)

print("✅ Dataset creado")
print(df.head())


# 📌 3. Exportar a CSV
df.to_csv("clientes.csv", index=False)
print("✅ CSV generado")


# 📌 4. Exportar a JSON
df.to_json("clientes.json", orient="records", date_format="iso")
print("✅ JSON generado")


# 📌 5. Volver a cargar
df_csv = pd.read_csv("clientes.csv")
df_json = pd.read_json("clientes.json")

print("✅ Archivos cargados nuevamente")


# 📌 6. Validación
print("\n--- VALIDACIÓN ---")
print("Filas CSV:", len(df_csv))
print("Filas JSON:", len(df_json))

print("\nColumnas CSV:", df_csv.columns.tolist())
print("Columnas JSON:", df_json.columns.tolist())

print("\n¿Estructura igual CSV?", df_csv.shape == df.shape)
print("¿Estructura igual JSON?", df_json.shape == df.shape)