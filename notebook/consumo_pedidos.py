import requests

def consumir_pedidos():
    url="http://localhost:8080"
    respuesta=requests.get(url)
    respuesta.raise_for_status()
    datos=respuesta.json()
    return datos