import pandas as pd

df = pd.read_csv("Ejercicios con Pandas/archivos/inventario.csv")

# Reemplazamos las categorias "Electrónica" y "Moda" por "Tech" y "Fashion"
df["Categoría"] = df["Categoría"].replace({'Electrónica':'Tech', 'Moda':'Fashion'})

print(df)
