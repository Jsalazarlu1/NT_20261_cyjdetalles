import random
from datetime import datetime

def crear_clientes(numero_clientes):

    nombres = ["Juan Perez", "Maria Lopez", None, "  carlos ruiz ", "ANA TORRES"]
    telefonos = ["3001234567", None, "ABC123", "3017654321", " 3024567890 "]
    direcciones = ["Calle 10", "Carrera 20", None, "  Av 30 ", "calle 50"]
    emails = ["juan@mail.com", "maria@mail.com", None, "carlosmail.com", " ANA@MAIL.COM "]

    clientes = []

    # 🔹 Generación inicial (con posibles errores)
    for i in range(numero_clientes):
        cliente = {
            "id_cliente": i + 1,
            "nombre": random.choice(nombres),
            "telefono": random.choice(telefonos),
            "direccion": random.choice(direcciones),
            "email": random.choice(emails),
            "fecha_registro": "2026-04-18" if i % 2 == 0 else "18-04-2026"  # formatos distintos
        }
        clientes.append(cliente)

    print("\n📌 DATASET ORIGINAL:")
    print(clientes)

    # =====================================================
    # 🧹 LIMPIEZA DE DATOS
    # =====================================================

    transformaciones = {
        "nulos": 0,
        "duplicados": 0,
        "tipos_corregidos": 0,
        "textos_normalizados": 0
    }

    clientes_limpios = []
    ids_vistos = set()

    for cliente in clientes:

        # 🔸 1. Validar nulos
        if None in cliente.values():
            transformaciones["nulos"] += 1
            continue  # eliminar registro

        # 🔸 2. Eliminar duplicados (por id)
        if cliente["id_cliente"] in ids_vistos:
            transformaciones["duplicados"] += 1
            continue
        ids_vistos.add(cliente["id_cliente"])

        # 🔸 3. Normalizar textos
        cliente["nombre"] = cliente["nombre"].strip().title()
        cliente["direccion"] = cliente["direccion"].strip().title()
        cliente["email"] = cliente["email"].strip().lower()
        cliente["telefono"] = cliente["telefono"].strip()

        transformaciones["textos_normalizados"] += 1

        # 🔸 4. Corregir tipos de datos

        # teléfono → solo números
        if not cliente["telefono"].isdigit():
            transformaciones["tipos_corregidos"] += 1
            continue  # eliminar si no es válido

        # email básico válido
        if "@" not in cliente["email"]:
            transformaciones["tipos_corregidos"] += 1
            continue

        # fecha → formato YYYY-MM-DD
        try:
            if "-" in cliente["fecha_registro"]:
                fecha = datetime.strptime(cliente["fecha_registro"], "%Y-%m-%d")
            else:
                fecha = datetime.strptime(cliente["fecha_registro"], "%d-%m-%Y")

            cliente["fecha_registro"] = fecha.strftime("%Y-%m-%d")
            transformaciones["tipos_corregidos"] += 1

        except:
            continue

        clientes_limpios.append(cliente)

    # =====================================================
    # 📊 RESULTADOS
    # =====================================================

    print("\n✅ DATASET LIMPIO:")
    print(clientes_limpios)

    print("\n📊 REPORTE DE TRANSFORMACIONES:")
    print(f"Registros con nulos eliminados: {transformaciones['nulos']}")
    print(f"Duplicados eliminados: {transformaciones['duplicados']}")
    print(f"Correcciones de tipo: {transformaciones['tipos_corregidos']}")
    print(f"Textos normalizados: {transformaciones['textos_normalizados']}")

    return clientes_limpios


# prueba
if __name__ == "__main__":
    crear_clientes(10)