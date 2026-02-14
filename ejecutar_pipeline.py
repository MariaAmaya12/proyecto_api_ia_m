# main.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from limpieza import pipeline_limpieza


# ==========================
# 1. Cargar y limpiar datos
# ==========================

ruta = "inmuebles_bogota.csv"
df = pipeline_limpieza(ruta)

print("Dimensiones del dataset limpio:")
print(df.shape)

print("\nPrimeras filas:")
print(df.head())


# ==========================
# 2. Información general
# ==========================

print("\nInformación general:")
df.info()

print("\nResumen estadístico:")
print(df.describe())


# ==========================
# 3. Análisis Exploratorio
# ==========================

# Precio promedio
print("\nPrecio promedio:")
print(df["valor"].mean())


# Precio promedio por barrio
if "barrio" in df.columns:
    print("\nPrecio promedio por barrio:")
    print(df.groupby("barrio")["valor"].mean().sort_values(ascending=False))


# ==========================
# 4. Visualizaciones
# ==========================

sns.set(style="whitegrid")

# Histograma del precio
plt.figure(figsize=(8,5))
sns.histplot(df["valor"], bins=30, kde=True)
plt.title("Distribución del Precio")
plt.show()


# Boxplot del precio
plt.figure(figsize=(8,5))
sns.boxplot(x=df["valor"])
plt.title("Boxplot del Precio")
plt.show()


# Relación precio vs área
if "area" in df.columns:
    plt.figure(figsize=(8,5))
    sns.scatterplot(x="area", y="valor", data=df)
    plt.title("Precio vs Área")
    plt.show()


# Matriz de correlación
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()
