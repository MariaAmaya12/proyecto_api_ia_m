# limpieza.py

import pandas as pd
import numpy as np
import unicodedata


def estandarizar_nombres_columnas(df: pd.DataFrame) -> pd.DataFrame:
    columnas = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    columnas = [
        unicodedata.normalize('NFKD', col)
        .encode('ascii', errors='ignore')
        .decode('utf-8')
        for col in columnas
    ]

    return df.set_axis(columnas, axis=1)


def eliminar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def convertir_vacios_a_nan(df: pd.DataFrame) -> pd.DataFrame:
    return df.replace(r'^\s*$', np.nan, regex=True)


def convertir_a_numerico(df: pd.DataFrame) -> pd.DataFrame:
    """
    Intenta convertir automáticamente todas las columnas
    a numéricas cuando sea posible.
    """
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass
    return df


def limpiar_columnas_monetarias(df: pd.DataFrame, columnas: list) -> pd.DataFrame:
    """
    Limpia columnas que contienen símbolos monetarios
    o caracteres no numéricos.
    """
    for col in columnas:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(r"[^\d]", "", regex=True)
            )
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def tratar_nulos(
    df: pd.DataFrame,
    estrategia_num: str = "median",
    valor_cat: str = "desconocido"
) -> pd.DataFrame:
    """
    Manejo básico de valores nulos.
    - Numéricos: mediana o media
    - Categóricos: valor fijo
    """

    for col in df.select_dtypes(include=np.number):
        if estrategia_num == "median":
            df[col] = df[col].fillna(df[col].median())
        elif estrategia_num == "mean":
            df[col] = df[col].fillna(df[col].mean())

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].fillna(valor_cat)

    return df


def limpiar_dataframe(
    df: pd.DataFrame,
    columnas_monetarias: list = None
) -> pd.DataFrame:
    """
    Pipeline general de limpieza.
    """

    df = estandarizar_nombres_columnas(df)
    df = convertir_vacios_a_nan(df)
    df = eliminar_duplicados(df)

    if columnas_monetarias:
        df = limpiar_columnas_monetarias(df, columnas_monetarias)

    df = convertir_a_numerico(df)
    df = tratar_nulos(df)

    return df
