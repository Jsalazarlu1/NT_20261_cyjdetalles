import random
def simular_usuario(numeroSimulaciones):
    #Semillas por cada atributo de mi tabla

    #id nombres contraseña rol idempleado

    nombres=["ana perez","pedro pascal","marta puntico"]

    ids=[1,2,3,4,5]

    contrasenas=["12345","1234","123456"]

    roles=["Administrador","Vendedor"]

    usuarios=[]

    for _ in range (numeroSimulaciones):
        usuario={
            "id": random.choice(ids),
            "nombre": random.choice(nombres),
            "contrasena":random.choice(contrasenas),
            "rol": random.choice(roles)
        }
        usuario.append(usuario)
    return usuarios    