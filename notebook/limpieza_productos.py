import pandas as pd

def limpiar_simulacion(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #Rutina para evaluar textos
 
    #Seleccionar todas las columnas tipo texto y eliminar los espacios y convertir a minusculas
    columnas_texto=["nombre","categoria","descripcion"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()

    #limpiar los textos solo con valores esperados
    productos_esperados=["Desayuno sorpresa premium", "Caja de dulces", "Recordatorio Lupe Baby", "Retablo Personalizado", "Ancheta feliz dia"]
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].where(
        data_frame_limpio["nombre"].isin(productos_esperados),
        pd.NA
    )


    #Rutina para evaluar numeros
    #Evaluar que las rutinas numericas si son números
    columnas_numericas=["id","precio","stock"]
    for columna in columnas_numericas:
        data_frame_limpio[columna]=pd.to_numeric(data_frame_limpio[columna])
    
    #Evaluar solo valores numericos permitidos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["precio"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["stock"]>=0]

    #Rutina para evaluar novedades
    #Rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["id","nombre","precio","stock", "categoria"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio


