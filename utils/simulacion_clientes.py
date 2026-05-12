import random
import pandas as pd
import requests

API_URL = "http://localhost:8080/api/clientes"

def simular_clientes(cantidad):

    nombres = [
        "Ana Perez",
        "Juan Camilo",
        "Marta Restrepo",
        "Carlos Cano",
        "Luisa Gil"
    ]

    tipos = ["CC", "CE", "NIT"]

    ciudades = [
        "Medellin",
        "Itagui",
        "Envigado",
        "Bello",
        "Sabaneta"
    ]

    calles = [
        "Calle 10",
        "Carrera 43",
        "Avenida 80",
        "Circular 1"
    ]

    clientes = []

    for i in range(1, cantidad + 1):

        cliente = {

            # NO enviamos ID
            # porque MySQL lo genera automático

            "ti_documento": random.choice(tipos),

            "n_documento": random.randint(
                1000000,
                9999999
            ),

            "nombre": random.choice(nombres),

            "telefono": str(
                random.randint(
                    3000000000,
                    3509999999
                )
            ),

            "direccion":
                f"{random.choice(calles)} # "
                f"{random.randint(1,99)}-"
                f"{random.randint(1,99)}",

            # ciudad NO existe en tu tabla
            # así que la agregamos a dirección

            "email": f"usuario{i}@gmail.com",

            "fecha_registro":
                f"2026-05-{random.randint(1,28):02d}"
        }

        clientes.append(cliente)

        # ENVIAR A SPRING
        respuesta = requests.post(
            API_URL,
            json=cliente
        )

        print(
            f"Cliente enviado → "
            f"{respuesta.status_code}"
        )

    return clientes


# --- EJECUCIÓN ---

datos = simular_clientes(10)

df = pd.DataFrame(datos)

print(df)