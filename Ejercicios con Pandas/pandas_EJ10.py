import pandas as pd

df = pd.read_csv("Ejercicios con Pandas/archivos/proyectos_investigacion.csv")

# Rellenar datos faltantes en Presupuesto con la mediana 
median_pre = df["Presupuesto"].median()
df["Presupuesto"] = df["Presupuesto"].fillna(median_pre)
# Eliminando filas donde "Fecha de Inicio sea NaN (Nulo)"
df = df.drop(df[df["Fecha de Inicio"].isna()].index) # Forma 1
#df = df.dropna(subset=["Fecha de Inicio"]) # Forma 2

print(df)