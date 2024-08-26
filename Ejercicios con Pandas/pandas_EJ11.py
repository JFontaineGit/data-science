import pandas as pd

df1 = pd.read_csv("Ejercicios con Pandas/archivos/estudiantes1.csv")
df2 = pd.read_csv("Ejercicios con Pandas/archivos/profesores.csv")

# Concatenando DataFrames con estudiantes, cursos y profesores correspondientes.
df_nuevo = pd.merge(df1,df2,on="Curso",how="inner")
print(df_nuevo)