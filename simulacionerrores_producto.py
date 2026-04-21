import random

def generar_simulacion(numeroSimulaciones):

    nombres=["Desayuno Premium","Ancheta Saludale","Vela intencionada"]
    codigos=["D8","A5","V5"]
    costos=[150000,100000,25000]
    

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        simulacion={
            "id":random.randint(0,200),
            "servicio":random.choice(nombres),
            "costo":random.choice(costos),
            "codigo":random.choice(codigos),
         
        }

        #Inyectando errores controlados
        probablilidadError=random.random()
        if(probablilidadError<0.2):
            simulacion["id"]=None #Eliminar el id para generar error
        elif(probablilidadError<0.4):
            simulacion["nombres"]=random.choice(["cinta", "lentes"]) #Insertar datos que no correspondan al servicio para generar error
        elif(probablilidadError<0.5):
            simulacion["costo"]=random.choice([0, -10000, None]) #Insertar costos no válidos para generar error
        elif(probablilidadError<0.8):
            simulacion["codigo"]=simulacion["codigo"]= " " + simulacion["codigo"].upper() #Agregar espacios al código para generar error y ponerlas en mayucula con upper
        
        simulaciones.append(simulacion)
    return simulaciones

