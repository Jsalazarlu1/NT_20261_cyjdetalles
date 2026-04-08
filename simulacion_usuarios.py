import random
def simular_servicio(numeroSimulaciones):
    #Semillas por cada atributo de mi tabla

    #id nombres contraseña rol idempleado

    nombres=["ana perez","pedro pascal","marta puntico"]

    ids=[1,2,3,4,5]

   ''' mascotas=["Zuker","Faustino","Primorosa","Dana","Lorenzo"]

    dueños=["Carlos Tevez","Cachaza Hernandez","Totono Grisales","Jhon Doe","Amparo Grisales"]

    fechas=["2026-04-02","2025-12-24","2026-06-23","2024-12-24","2023-12-24"]

    codigos=["AM1","AM2","AM45","AM50","AM500"]'''

    servicios=[]

    for _ in range (numeroSimulaciones):
        servicio={
            "id": random.choice(codigos),
            "fecha": random.choice(fechas),
            "mascota":random.choice(mascotas),
            "dueño": random.choice(dueños),
            "valor": random.choice(valores),
            "nombra": random.choice(nombres)
        }
        servicio.append(servicio)
    return servicios    