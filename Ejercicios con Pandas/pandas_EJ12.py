import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Ejercicios con Pandas/archivos/ventas_mensuales.csv")

def crear_grafico(titulo,xtexto,ytexto,rotacion):
    plt.title(titulo)
    plt.xlabel(xtexto)
    plt.ylabel(ytexto)
    plt.xticks(rotation=rotacion)
    plt.show()

# Filtrando por las ventas en el mes de Enero
condicion = df["Mes"] == "Enero"
ventas_enero = df[condicion]
# Creando un gráfico de barras
ventas_enero.plot(x="Producto",y="Ventas",kind="bar",figsize=(10,5),legend=True)
crear_grafico("Ventas mensuales", "Producto", "Ventas", 0)
print(df[condicion])
