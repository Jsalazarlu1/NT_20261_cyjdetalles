import requests

def consumir_pedidos():
    url="http://localhost:8081/api/pedidos"
    respuesta=requests.get(url)
    respuesta.raise_for_status()
    datos=respuesta.json()
    return datos