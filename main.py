import os
import sys
import pandas as pd

# Añadimos AMBAS carpetas al path
BASE_DIR = os.path.dirname(__file__)
NOTEBOOK_DIR = os.path.join(BASE_DIR, "notebook")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)        # raíz → simulacionerrores_clientes.py

if NOTEBOOK_DIR not in sys.path:
    sys.path.insert(0, NOTEBOOK_DIR)    # notebook → limpieza_clientes.py, limpieza_pedidos.py

from utils.simulacionerrores_clientes import simular_clientes
from limpieza_clientes import limpiar_clientes
from simulacion_pedidos_limpieza import generar_simulacion
from limpieza_pedidos import limpiar_pedidos
from limpienza_detalle_pedido import limpiar_detalle_pedido
from notebook.consumo_detalle_pedido import cargar_datos


if __name__ == "__main__":
    # Clientes con errores y limpieza
    datos_clientes = simular_clientes(10)
    df_clientes_sucio = pd.DataFrame(datos_clientes)

    print("=== CLIENTES: DATOS SUCIOS ===")
    print(df_clientes_sucio.to_string())
    print(f"\nTotal filas sucias: {len(df_clientes_sucio)}")
    print(f"Nulos por columna:\n{df_clientes_sucio.isnull().sum()}")

    df_clientes_limpio = limpiar_clientes(df_clientes_sucio)

    print("\n=== CLIENTES: DATOS LIMPIOS ===")
    print(df_clientes_limpio.to_string())
    print(f"\nTotal filas limpias: {len(df_clientes_limpio)}")

    # Pedidos con errores y limpieza
    pedidos = generar_simulacion(10)
    df_pedidos_sucio = pd.DataFrame(pedidos)

    print("\n=== PEDIDOS: DATOS SUCIOS ===")
    print(df_pedidos_sucio.to_string())
    print(f"\nTotal pedidos sucios: {len(df_pedidos_sucio)}")
    print(f"Nulos por columna:\n{df_pedidos_sucio.isnull().sum()}")

    pedidos_limpios = limpiar_pedidos(df_pedidos_sucio)

    print("\n=== PEDIDOS: DATOS LIMPIOS ===")
    print(pedidos_limpios.to_string())
    print(f"\nTotal pedidos limpios: {len(pedidos_limpios)}")

    # Detalle Pedidos con errores y limpieza
    print("=== DETALLE_PEDIDO: DATOS SUCIOS ===")
    df_detallepedido_sucio = pd.DataFrame(cargar_datos())
    print(df_detallepedido_sucio.to_string())
    print(f"\nTotal registros sucios: {len(df_detallepedido_sucio)}")
    print(f"Nulos por columna:\n{df_detallepedido_sucio.isnull().sum()}")

    df_detallepedido_limpio = limpiar_detalle_pedido(df_detallepedido_sucio)

    print("=== DETALLE_PEDIDO: DATOS LIMPIOS ===")
    print(df_detallepedido_limpio.to_string())
    print(f"\nTotal registros limpios: {len(df_detallepedido_limpio)}")