import pandas as pd

df = pd.read_csv('Ejercicios con Pandas/archivos/ventas.csv')

# Agrupando por Tiendas y obteniendo las ventas totales de las mismas. Asignamos un alias a la columna resultante del total de ventas.
ventas_totales = df.groupby('Tienda').sum()['Ventas'].rename('Total de Ventas')

print(ventas_totales)