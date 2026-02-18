import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# -------------------------------------------------
# 1. Información general
# -------------------------------------------------
def info_general(df: pd.DataFrame) -> None:
    print("\n=== INFORMACIÓN GENERAL ===")
    print("Dimensiones:", df.shape)
    print("\nTipos de datos:")
    print(df.dtypes)


# -------------------------------------------------
# 2. Valores nulos
# -------------------------------------------------
def analizar_nulos(df: pd.DataFrame) -> None:
    print("\n=== VALORES NULOS ===")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0])


# -------------------------------------------------
# 3. Variables numéricas
# -------------------------------------------------
def analizar_numericas(df: pd.DataFrame) -> None:
    print("\n=== VARIABLES NUMÉRICAS ===")
    
    numericas = df.select_dtypes(include=np.number).columns
    
    for col in numericas:
        print(f"\n--- {col} ---")
        print(df[col].describe())
        
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribución de {col}")
        plt.show()


# -------------------------------------------------
# 4. Variables categóricas
# -------------------------------------------------
def analizar_categoricas(df: pd.DataFrame) -> None:
    print("\n=== VARIABLES CATEGÓRICAS ===")
    
    categoricas = df.select_dtypes(include="object").columns
    
    for col in categoricas:
        print(f"\n--- {col} ---")
        print(df[col].value_counts().head())


# -------------------------------------------------
# 5. Correlación
# -------------------------------------------------
def matriz_correlacion(df: pd.DataFrame) -> None:
    print("\n=== MATRIZ DE CORRELACIÓN ===")
    
    numericas = df.select_dtypes(include=np.number)
    
    if numericas.shape[1] > 1:
        corr = numericas.corr()
        print(corr)
        
        plt.figure()
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Matriz de correlación")
        plt.show()
    else:
        print("No hay suficientes variables numéricas para correlación.")


# -------------------------------------------------
# Función principal para ejecutar todo el EDA
# -------------------------------------------------
def ejecutar_eda(df: pd.DataFrame) -> None:
    info_general(df)
    analizar_nulos(df)
    analizar_numericas(df)
    analizar_categoricas(df)
    matriz_correlacion(df)
