import pandas as pd

df = pd.read_csv("Ejercicios con Pandas/archivos/estudiantes.csv")

# Filtros
c1 = df['Edad'] > 18
c2 = df['Matematicas'] > 70
# Creamos una copia del DataFrame original filtrando por Edad mayor a 18 y calificación en Matematicas mayor a 70
df_copia = df.where(c1 & c2)
# Limpiamos los valores que no cumplan con las condiciones (NaN)
df_final = df_copia.dropna()


print(df_final)