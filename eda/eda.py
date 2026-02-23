import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# 1. Información general
# -------------------------------------------------
def info_general(df: pd.DataFrame) -> None:
    """Imprime dimensiones y tipos de datos."""
    print("\n=== INFORMACIÓN GENERAL ===")
    print("Dimensiones (filas, columnas):", df.shape)
    print("\nTipos de datos:")
    print(df.dtypes)


# -------------------------------------------------
# 2. Valores nulos
# -------------------------------------------------
def analizar_nulos(df: pd.DataFrame) -> None:
    """Muestra conteo de valores nulos (solo columnas con nulos)."""
    print("\n=== VALORES NULOS ===")
    nulos = df.isna().sum()
    nulos = nulos[nulos > 0].sort_values(ascending=False)

    if len(nulos) == 0:
        print("No hay valores nulos.")
    else:
        print(nulos)


# -------------------------------------------------
# 3. Histograma robusto (p1–p99)
# -------------------------------------------------
def histograma_robusto(
    serie: pd.Series,
    nombre: str,
    bins: int = 30,
    p_low: float = 0.01,
    p_high: float = 0.99
) -> None:
    """
    Grafica un histograma recortando extremos SOLO para visualización.
    No modifica los datos originales.
    """

    s = serie.dropna()

    if len(s) < 2:
        print(f"{nombre}: no hay suficientes datos para graficar.")
        return

    # Percentiles para recorte visual
    low = s.quantile(p_low)
    high = s.quantile(p_high)

    s_plot = s[(s >= low) & (s <= high)]

    plt.figure()
    plt.hist(s_plot, bins=bins)
    plt.title(f"Distribución de {nombre} (p{int(p_low*100)}–p{int(p_high*100)})")
    plt.xlabel(nombre)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()


# -------------------------------------------------
# 4. Variables numéricas
# -------------------------------------------------
def analizar_numericas(df: pd.DataFrame, graficar: bool = True) -> None:
    """
    Analiza variables numéricas:
    - Estadísticas descriptivas
    - Histograma robusto (opcional)
    """

    print("\n=== VARIABLES NUMÉRICAS ===")
    numericas = df.select_dtypes(include=[np.number]).columns

    if len(numericas) == 0:
        print("No hay variables numéricas.")
        return

    for col in numericas:
        print(f"\n--- {col} ---")
        print(df[col].describe())

        if graficar:
            histograma_robusto(df[col], col)


# -------------------------------------------------
# 5. Variables categóricas
# -------------------------------------------------
def analizar_categoricas(df: pd.DataFrame, top: int = 10) -> None:
    """
    Muestra las categorías más frecuentes.
    Detecta object, string y category.
    """

    print("\n=== VARIABLES CATEGÓRICAS ===")
    categoricas = df.select_dtypes(include=["object", "string", "category"]).columns

    if len(categoricas) == 0:
        print("No hay variables categóricas.")
        return

    for col in categoricas:
        print(f"\n--- {col} ---")
        print(df[col].value_counts(dropna=False).head(top))


# -------------------------------------------------
# 6. Matriz de correlación
# -------------------------------------------------
def matriz_correlacion(df: pd.DataFrame, max_cols: int = 12) -> None:
    """
    Calcula correlación de Pearson entre variables numéricas.
    No grafica si hay demasiadas columnas (para evitar ilegibilidad).
    """

    print("\n=== MATRIZ DE CORRELACIÓN ===")
    numericas = df.select_dtypes(include=[np.number])

    if numericas.shape[1] < 2:
        print("No hay suficientes variables numéricas para correlación.")
        return

    corr = numericas.corr()
    print(corr)

    if corr.shape[0] <= max_cols:
        plt.figure()
        plt.imshow(corr, aspect="auto")
        plt.colorbar()
        plt.xticks(range(corr.shape[1]), corr.columns, rotation=45, ha="right")
        plt.yticks(range(corr.shape[0]), corr.index)
        plt.title("Matriz de correlación (Pearson)")
        plt.tight_layout()
        plt.show()
    else:
        print("Demasiadas variables para graficar matriz de correlación.")


# -------------------------------------------------
# 7. Ejecutar EDA completo
# -------------------------------------------------
def ejecutar_eda(df: pd.DataFrame, graficar: bool = True) -> None:
    """Ejecuta análisis exploratorio completo."""
    info_general(df)
    analizar_nulos(df)
    analizar_numericas(df, graficar=graficar)
    analizar_categoricas(df)
    matriz_correlacion(df)