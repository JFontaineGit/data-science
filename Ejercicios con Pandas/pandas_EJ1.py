import pandas as pd
import numpy as np

# Convirtiendo una lista en un Pandas Series
list = [2,4,6,8]
serie = pd.Series(list)

# Convirtiendo un Pandas Series en una lista
serie_to_list = serie.tolist()

# Creando un DataFrame con un diccionario
dicc = {"Name": ["Alexis","Joaquin","Maria","Patrick","Yohan"],
        "LastName": ["Zambrano","Torrejon","Chavesta","Jane","Rodr"],
        "Age": [np.random.randint(15,30) for x in range(5)]}
df = pd.DataFrame(dicc)
