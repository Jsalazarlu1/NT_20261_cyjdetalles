### esto debe ir el en main.py, pero se deja aquí para que el código quede completo

# from simulacion_pedidos_limpieza import generar_simulacion
# from limpieza import limpiar_datos
# from transformacion import transformar_datos
# from graficacion_pedidos import graficar_resultados
# from utils.simulacionerrores_productos import generar_simulacion


# datos = generar_simulacion(100)

# df_limpio = limpiar_datos(datos)

# resultado = transformar_datos(df_limpio)

# graficar_resultados(resultado)###
#########################################################################################




# se importa matplotlib
import matplotlib.pyplot as plt

# se importa os
import os


# ruta para guardar imágenes
RUTA_ASSETS = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "mi-app-react",
    "src",
    "assets",
    "graficos"
)


def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_resultados(resultado_transformacion):
    """
    recibe el diccionario retornado desde transformar_datos()
    """

    print("***** GENERANDO GRAFICOS *****")

    crear_ruta_si_no_existe(RUTA_ASSETS)

    # ===================================================
    # GRAFICO 1
    # usa agrupacion1:
    # pedidos entregados por fecha
    # ===================================================
    datos1 = resultado_transformacion["agrupacion1"]

    figura1, area1 = plt.subplots(figsize=(10, 5))

    area1.plot(
        datos1["fecha_creacion"],
        datos1["cantidad"],
        marker="o",
        color="blue",
        linewidth=2
    )

    area1.set_title("Pedidos entregados por fecha")
    area1.set_xlabel("fecha_creacion")
    area1.set_ylabel("cantidad")
    area1.grid(True)

    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta1 = os.path.join(RUTA_ASSETS, "pedidos_entregados_lineas.png")
    figura1.savefig(ruta1)
    plt.close(figura1)

    print(f"grafico 1 guardado en: {ruta1}")


    # ===================================================
    # GRAFICO 2
    # usa agrupacion2:
    # pedidos mayores a 100000
    # ===================================================
    datos2 = resultado_transformacion["agrupacion2"]

    figura2, area2 = plt.subplots(figsize=(10, 5))

    area2.bar(
        datos2["tipo_detalle"],
        datos2["cantidad"],
        color="green",
        edgecolor="black"
    )

    area2.set_title("Pedidos mayores a 100000")
    area2.set_xlabel("tipo_detalle")
    area2.set_ylabel("cantidad")

    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta2 = os.path.join(RUTA_ASSETS, "pedidos_barras.png")
    figura2.savefig(ruta2)
    plt.close(figura2)

    print(f"grafico 2 guardado en: {ruta2}")

    print("***** GRAFICOS TERMINADOS *****")