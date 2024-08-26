import pandas as pd
import numpy as np

data = {
    'Producot': ["Laptop","Smartphone","Ropa","Zapatos"],
    'Categoria': ["Electronica","Electronica","Moda","Moda"],
    'Ventas': [1200,800,300,150],
} 

df = pd.DataFrame(data)

# Ordenando ventas de menor a mayor.
#df_ord_desc = df.sort_values(by='Ventas', ascending=False)

# Calculando el promedio de las ventas.
ingresos = df['Ventas'].sum()
ventas_totales = df['Ventas'].count()
promedio_de_ventas = ingresos / ventas_totales
print(promedio_de_ventas)