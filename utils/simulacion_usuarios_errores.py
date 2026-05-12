import random

from datetime import datetime,timedelta

def generar_simulacion(numeroSimulaciones):

    nombres=["ana perez","pedro pascal","marta puntico"]
    ids=[1,2,3,4,5]
    contrasenas=["12345","1234","123456"]
    roles=["Administrador","Vendedor"]
   

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        simulacion={
            "id":random.choice(ids),
            "nombre":random.choice(nombres),
            "contrasena":random.choice(contrasenas),
            "rol":random.choice(roles)            
        }
        #inyectando errores controlados
        probabilidadError=random.random()

        if(probabilidadError<0.2):
            simulacion["id"]=None
        elif(probabilidadError<0.4):
            simulacion["nombre"]=random.choice(["Agua","Montaña"])
        elif(probabilidadError<0.5):
            simulacion["contrasena"]=random.choice([" ","Comida","Bebida",None])
        elif(probabilidadError<0.8):
            simulacion["rol"]=random.choice([" ","Cerrajero","Conductor",None])        

        simulaciones.append(simulacion)
    return simulaciones