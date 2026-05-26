import random
import pandas as pd

def simular_clientes(cantidad):
    nombres = ["Ana Perez", "Juan Camilo", "Marta Restrepo", "Carlos Cano", "Luisa Gil"]
    tipos = ["CC", "CE", "NIT"]
    ciudades = ["Medellin", "Itagui", "Envigado", "Bello", "Sabaneta"]
    calles = ["Calle 10", "Carrera 43", "Avenida 80", "Circular 1"]

    clientes = []
    for i in range(1, cantidad + 1):
        cliente = {
            "id": i,
            "tipo_doc": random.choice(tipos),
            "documento": random.randint(1000000, 9999999),
            "nombre": random.choice(nombres),
            "telefono": random.randint(3000000000, 3509999999),
            "direccion": f"{random.choice(calles)} #{random.randint(1, 99)}-{random.randint(1, 99)}",
            "ciudad": random.choice(ciudades),
            "email": f"usuario{i}@gmail.com",
            "fecha_registro": f"2024-05-{random.randint(1, 28):02d}"
        }
        clientes.append(cliente)

    # --- ERRORES FORZADOS ---

    # Nulos en campos obligatorios
    clientes[0]["nombre"] = None
    clientes[1]["tipo_doc"] = None
    clientes[2]["documento"] = None

    # Valores inválidos en tipo_doc
    clientes[3]["tipo_doc"] = "XX"
    clientes[4]["tipo_doc"] = "cc"

    # Errores en números
    clientes[5]["id"] = "abc"
    clientes[6]["documento"] = "error"
    clientes[7]["telefono"] = "N/A"

    # Fechas inválidas
    clientes[8]["fecha_registro"] = "fecha_mala"
    clientes[9]["fecha_registro"] = None

    # Campos vacíos
    clientes[0]["ciudad"] = "   "
    clientes[1]["email"] = ""

    # Duplicados garantizados
    clientes.append(clientes[4].copy())
    clientes.append(clientes[4].copy())

    return clientes


# --- EJECUCIÓN ---
if __name__ == "__main__":
    datos = simular_clientes(10)
    df = pd.DataFrame(datos)
    print("=== DATOS CON ERRORES ===")
    print(df.to_string())