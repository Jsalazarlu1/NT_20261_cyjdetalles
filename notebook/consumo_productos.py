import requests

def consumir_productos():
    url = "http://localhost:8081/api/productos"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos