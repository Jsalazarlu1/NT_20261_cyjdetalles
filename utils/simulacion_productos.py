import random

def producto (numeroproductos):
    

    nombres=["Desayuno sorpresa premium", "Caja de dulces", "Recordatorio Lupe Baby", "Retablo Personalizado", "Ancheta feliz dia"]
    precios=[150000, 32000,85000,35000,85000]
    categorias=["Desayunos sorpresa","Otros Detalles","Velas artesanales","Retablos personalizados","Anchetas"]
    descripciones=["Delicioso desayuno saludable", "Cajita de dulces con variedad de gomitas y chocolates", "Recordatorios virgen guadalupe en caja", "Retablos con imagen personalizada","Ancheta de dulces y mekato"]
    stocks=["30", "52", "33","63","15"]
    ids=["1", "2", "3", "4", "5"]

    productos=[]
    for _ in range (numeroproductos):
        servicio={
            "id": random.choice(ids),
            "stock": random.choice(stocks), #Debe ser con el mismo nombre definidos en java
            "categoria": random.choice(categorias),
            "descripcion": random.choice(descripciones),
            "precio": random.choice(precios),
            "nombre": random.choice(nombres)
        }
        productos.append(producto) 
    return productos