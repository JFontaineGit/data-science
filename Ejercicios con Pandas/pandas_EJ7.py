import pandas as pd

df = pd.read_csv('Ejercicios con Pandas/archivos/empleados.csv')

# Añadiendo una columa con el total del salario + la bonificacion. Ordenamos de mayor a menor.
df['Total Pago'] = df['Salario'] + df['Bonificacion']
print(df.sort_values(by="Total Pago", ascending=False))