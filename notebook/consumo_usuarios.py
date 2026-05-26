import requests

def consumir_usuarios():
    url="http://localhost:8081/api/usuarios"
    respuesta=requests.get(url)
    respuesta.raise_for_status()
    datos=respuesta.json()
    return datos