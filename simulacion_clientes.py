import random
import pandas as pd

def simular_clientes(cantidad):
    nombres = ["Ana Perez", "Juan Camilo", "Marta Restrepo", "Carlos Cano", "Luisa Gil"]
    tipos = ["CC", "CE", "NIT"]
    ciudades = ["Medellin", "Itagui", "Envigado", "Bello", "Sabaneta"]
    calles = ["Calle 10", "Carrera 43", "Avenida 80", "Circular 1"] # Para la dirección

    clientes = []
    for i in range(1, cantidad + 1):
        cliente = {
            "id": i,
            "tipo_doc": random.choice(tipos),
            "documento": random.randint(1000000, 9999999),
            "nombre": random.choice(nombres),
            "telefono": random.randint(3000000000, 3509999999), # Teléfono celular
            "direccion": f"{random.choice(calles)} # {random.randint(1, 99)}-{random.randint(1, 99)}",
            "ciudad": random.choice(ciudades),
            "email": f"usuario{i}@gmail.com",
            "fecha_registro": f"2024-05-{random.randint(1, 28):02d}" # Formato YYYY-MM-DD

            #la f se usa para reconocer la variable dentro de la cadena, y el :02d se usa para formatear el número con dos dígitos, agregando un cero a la izquierda si es necesario.
        }
        clientes.append(cliente)
    return clientes

# --- EJECUCIÓN ---
datos = simular_clientes(10)
df = pd.DataFrame(datos)
print(df)