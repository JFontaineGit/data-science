import pandas as pd
import numpy as np

#Creando a CSV
#dicc = {"Name": ["Alexis","Joaquin","Maria","Patrick","Yohan"],
#        "LastName": ["Zambrano","Torrejon","Chavesta","Jane","Rodr"],
#        "Age": [np.random.randint(15,30) for x in range(5)]}
#df = pd.DataFrame(dicc)
#df.to_csv("datos.csv",index=False)

#Abriendo CSV
df = pd.read_csv("datos.csv")

#Mostrando filas y columnas que tiene nuestro DataFrame
#fil_col = df.shape
#print(f"El DataFrame tiene {fil_col[0]} filas y {fil_col[1]} columnas")

#Mostrando nombres de columnas de nuestro DataFrame
col = df.columns
