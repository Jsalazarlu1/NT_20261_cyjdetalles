import pandas as pd
def transformar_datos(data_frame_limpio):
    print ("** FILTROS APLICADOS **")

    #1. Filtro para obtener los productos con precio mayor o igual a 100000

    filtro1= data_frame_limpio.query("precio >= 100000")
    agrupacion1= filtro1.groupby("producto")["id"].count().reset_index(name="cantidad")
    print (agrupacion1)

    #2 Filtro para obtener los productos con stock menor o igual a 5 unidades

    filtro2= data_frame_limpio.query("stock <= 5")
    agrupacion2= filtro2.groupby("producto")["id"].count().reset_index(name="cantidad")
    print (agrupacion2)

    