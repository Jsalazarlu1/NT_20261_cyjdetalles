import panda as pd
def transformar_datos_usuarios(data_frame_limpio):
    print("***** FILTROS APLICADOS *****")

    #1. FILTRO PARA AGRUPAR ROL CLIENTE Y ID (ÚTIL PARA GRÁFICO DE LÍNEAS)
    filtro1=data_frame_limpio.query("rol == 'cliente' ")
    agrupacion1=filtro1.groupby("rol")["id"].count().reset_index(name="cantidad")
    print(agrupacion1)

    #2. FILTRO PARA AGRUPAR ROL VENDEDOR Y ID 
    filtro2=data_frame_limpio.query("rol == 'vendedor' ")
    agrupacion2=filtro2.groupby("rol")["id"].count().reset_index(name="cantidad")
    print(agrupacion2)