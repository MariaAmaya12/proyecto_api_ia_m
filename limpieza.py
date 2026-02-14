# limpieza.py

import pandas as pd
import numpy as np
import unicodedata


def cargar_datos(ruta):
    """
    Carga el dataset desde una ruta específica.
    """
    return pd.read_csv(ruta, encoding="latin-1")


def estandarizar_nombres_columnas(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # eliminar tildes
    df.columns = [
        unicodedata.normalize('NFKD', col)
        .encode('ascii', errors='ignore')
        .decode('utf-8')
        for col in df.columns
    ]

    return df


def eliminar_duplicados(df):
    """
    Elimina registros duplicados.
    """
    return df.drop_duplicates().copy()


def eliminar_columnas_irrelevantes(df, columnas):
    """
    Elimina columnas que no aportan al análisis.
    """
    df = df.copy()
    return df.drop(columns=columnas, errors="ignore")


def convertir_precio_a_numerico(df, columna_precio):
    """
    Limpia y convierte la columna precio a tipo numérico.
    """
    df = df.copy()
    df[columna_precio] = (
        df[columna_precio]
        .astype(str)
        .str.replace(r"[^\d]", "", regex=True)
    )
    df[columna_precio] = pd.to_numeric(df[columna_precio], errors="coerce")
    return df


def convertir_columnas_numericas(df, columnas):
    """
    Convierte columnas específicas a numéricas.
    """
    df = df.copy()
    for col in columnas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def tratar_nulos(df):
    """
    Manejo básico de valores nulos.
    - Numéricos: imputación con mediana
    - Categóricos: imputación con 'desconocido'
    """
    df = df.copy()

    for col in df.select_dtypes(include=np.number):
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].fillna("desconocido")

    return df


def pipeline_limpieza(ruta):
    """
    Pipeline completo de limpieza.
    """
    df = cargar_datos(ruta)
    df = estandarizar_nombres_columnas(df)
    print("Columnas después de estandarizar:")
    print(df.columns)

    df = eliminar_duplicados(df)

    # Ajusta según tu dataset
    df = convertir_precio_a_numerico(df, "valor")


    columnas_numericas = ["area", "habitaciones", "banos"]
    df = convertir_columnas_numericas(df, columnas_numericas)

    df = tratar_nulos(df)

    return df
