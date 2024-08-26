import pandas as pd

df = pd.read_csv('Ejercicios con Pandas/archivos/temperaturas.csv')

print(df)

# Calculando MEDIA, MEDIANA Y DESVIACIÓN ESTANDAR de la temperatura para cada ciudad.
df["Media"] = df.groupby("Ciudad")["Temperatura"].transform('mean')
df["Mediana"] = df.groupby("Ciudad")["Temperatura"].transform('median')
df["Desviacion Estandar"] = df.groupby("Ciudad")["Temperatura"].transform('std')
# Mostramos solo las columnas necesarias y limpiamos valores duplicados.
print(df[["Ciudad","Media","Mediana","Desviacion Estandar"]].drop_duplicates('Ciudad'))