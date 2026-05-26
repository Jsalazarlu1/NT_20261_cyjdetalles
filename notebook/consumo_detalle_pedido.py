import requests


def cargar_datos():
    url = "http://localhost:8081/api/detallepedidos"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos
