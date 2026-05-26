import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

def graficar_detalle_pedido(df):
    # --- GRÁFICO 1: TORTA ---
    total_producto = df.groupby("id_producto")["total"].sum().reset_index(name="total_recaudado")
    graficar_torta(
        datos_agrupados=total_producto,
        columna_etiquetas="id_producto",
        columna_valores="total_recaudado",
        titulo="Distribución del total recaudado por producto",
        ruta_destino="graficos/detalle_pedido"
    )
    # --- GRÁFICO 2: BARRAS ---
    ventas_producto = df.groupby("id_producto")["cantidad"].sum().reset_index(name="cantidad_vendida")
    graficar_barras(
        datos_agrupados=ventas_producto,
        columna_categorias="id_producto",
        columna_valores="cantidad_vendida",
        titulo="Cantidad de productos vendidos por producto",
        ruta_destino="graficos/detalle_pedido"
    )

def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)

def graficar_barras(datos_agrupados, columna_categorias, columna_valores,
                    titulo="Gráfico de barras", color_barras="#4CAF50",
                    nombre_archivo="barras.png", ruta_destino="graficos"):
    crear_ruta_si_no_existe(ruta_destino)
    figura, area_dibujo = plt.subplots(figsize=(10, 5))
    area_dibujo.bar(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)
    area_dibujo.set_ylabel(columna_valores, fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de barras guardado en: {ruta_completa}")

def graficar_torta(datos_agrupados, columna_etiquetas, columna_valores,
                   titulo="Gráfico de torta", lista_colores=None,
                   nombre_archivo="torta.png", ruta_destino="graficos"):
    crear_ruta_si_no_existe(ruta_destino)
    if lista_colores is None:
        lista_colores = ["#FF9800", "#2196F3", "#4CAF50", "#E91E63", "#9C27B0"]
    figura, area_dibujo = plt.subplots(figsize=(8, 8))
    cantidad_categorias = len(datos_agrupados)
    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas],
        autopct="%1.1f%%",
        colors=lista_colores[:cantidad_categorias],
        startangle=90,
        wedgeprops={"edgecolor": "black", "linewidth": 0.5}
    )
    area_dibujo.set_title(titulo, fontsize=14)
    plt.tight_layout()
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de torta guardado en: {ruta_completa}")

if __name__ == "__main__":
    from consumo_detalle_pedido import cargar_datos
    from limpienza_detalle_pedido import limpiar_detalle_pedido

    datos = cargar_datos()
    df = limpiar_detalle_pedido(pd.DataFrame(datos))
    graficar_detalle_pedido(df)