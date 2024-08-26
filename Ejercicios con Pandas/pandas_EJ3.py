import pandas as pd

# Creando un data frame en base a un diccionario

dic = {
    "nombre": ["Juan","Ana","Luis","Marta"],
    "edad": [25,30,22,29],
    "ciudad": ["Madrid","Barcelona","Valencia","Sevilla"]
}

df = pd.DataFrame(dic)

# Mostrando filas donde la edad sea mayor a 25 años.

#condicion = df['edad'] > 25
#print(df[condicion])


# Añadiendo más datos al dataframe. Haremos uso de reset_index para evitar indices repetidos y "drop=True" para evitar que el antiguo indice se guarde y conserve solo el nuevo.
#new = pd.DataFrame([{'nombre': 'Axis', 'edad': 19, 'ciudad': 'Guadalajara'}])
#df = pd.concat([df,new])
#df.reset_index(drop=True)
#print(df)

# Cambiando el nombre de la columna "Ciudad" a "Ubicación".

#df.rename(columns={'ciudad':'ubicación'},inplace=True)
#print(df)

# Añadiendo un año más de longevidad a las personas.

df['edad'] = df['edad'] + 1
print (df)