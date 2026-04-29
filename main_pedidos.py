import pandas as pd

from simulacion_pedidos_limpieza import generar_simulacion
from limpieza_pedidos import limpiar_pedidos

pedidos = generar_simulacion(10)

pedidos_df = pd.DataFrame(pedidos)

pedidos_limpios = limpiar_pedidos(pedidos_df)

print(pedidos_limpios)