import os
import pandas as pd
import matplotlib.pyplot as plt


RUTA_GRAFICOS = os.path.join(os.path.dirname(__file__), "..", "assets", "graficos")


def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)


def preparar_datos_productos(data_frame):
    df = data_frame.copy()
    df["precio"] = pd.to_numeric(df["precio"], errors="coerce")
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce")
    df = df.dropna(subset=["id", "nombre", "categoria", "precio", "stock"])
    return df


def graficar_stock_por_producto(datos_agrupados,
                                 columna_nombre="nombre",
                                 columna_stock="stock",
                                 titulo="Stock por producto",
                                 color_barras="#4CAF50",
                                 nombre_archivo="stock_por_producto.png",
                                 ruta_destino=RUTA_GRAFICOS):
    crear_ruta_si_no_existe(ruta_destino)
    resumen = datos_agrupados.groupby(columna_nombre)[columna_stock].sum().reset_index()

    figura, area_dibujo = plt.subplots(figsize=(12, 6))
    area_dibujo.bar(
        resumen[columna_nombre],
        resumen[columna_stock],
        color=color_barras,
        edgecolor="black"
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_nombre.capitalize(), fontsize=12)
    area_dibujo.set_ylabel("Stock", fontsize=12)
    plt.xticks(rotation=45)

    for index, fila in resumen.iterrows():
        area_dibujo.text(index,
                         fila[columna_stock] + max(resumen[columna_stock]) * 0.01,
                         int(fila[columna_stock]),
                         ha="center",
                         va="bottom",
                         fontsize=10)

    plt.tight_layout()
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de stock por producto guardado en: {ruta_completa}")


def graficar_cantidad_productos_por_categoria(datos,
                                               columna_categoria="categoria",
                                               titulo="Cantidad de productos por categoría",
                                               color_barras="#2196F3",
                                               nombre_archivo="cantidad_productos_por_categoria.png",
                                               ruta_destino=RUTA_GRAFICOS):
    crear_ruta_si_no_existe(ruta_destino)
    resumen = datos.groupby(columna_categoria)["id"].nunique().reset_index(name="cantidad")

    figura, area_dibujo = plt.subplots(figsize=(10, 5))
    area_dibujo.bar(
        resumen[columna_categoria],
        resumen["cantidad"],
        color=color_barras,
        edgecolor="black"
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_categoria.capitalize(), fontsize=12)
    area_dibujo.set_ylabel("Cantidad de productos", fontsize=12)
    plt.xticks(rotation=45)

    for index, fila in resumen.iterrows():
        area_dibujo.text(index,
                         fila["cantidad"] + max(resumen["cantidad"]) * 0.01,
                         int(fila["cantidad"]),
                         ha="center",
                         va="bottom",
                         fontsize=10)

    plt.tight_layout()
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de cantidad de productos por categoría guardado en: {ruta_completa}")


if __name__ == "__main__":
    datos_de_ejemplo = [
        {"id": 1, "nombre": "Desayuno sorpresa premium", "precio": 150000, "categoria": "Desayunos sorpresa", "descripcion": "Delicioso desayuno saludable", "stock": 30},
        {"id": 2, "nombre": "Caja de dulces", "precio": 32000, "categoria": "Otros Detalles", "descripcion": "Cajita de dulces con variedad", "stock": 52},
        {"id": 3, "nombre": "Recordatorio Lupe Baby", "precio": 85000, "categoria": "Velas artesanales", "descripcion": "Recordatorio virgen guadalupe en caja", "stock": 33},
        {"id": 4, "nombre": "Retablo Personalizado", "precio": 35000, "categoria": "Retablos personalizados", "descripcion": "Retablos con imagen personalizada", "stock": 63},
        {"id": 5, "nombre": "Ancheta feliz dia", "precio": 85000, "categoria": "Anchetas", "descripcion": "Ancheta de dulces y mekato", "stock": 15}
    ]

    df_productos = pd.DataFrame(datos_de_ejemplo)
    df_productos = preparar_datos_productos(df_productos)

    graficar_stock_por_producto(df_productos)
    graficar_cantidad_productos_por_categoria(df_productos)
