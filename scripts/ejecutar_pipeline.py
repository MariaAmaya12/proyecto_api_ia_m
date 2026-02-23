import pandas as pd
from limpieza import DataCleaner

df = pd.read_csv("inmuebles_bogota.csv", encoding="utf-8")

cleaner = DataCleaner(
    config={
        "columnas_monetarias": ["valor"],
        "estrategia_num": "median",
        "estrategia_cat": "moda",
        "umbral_conversion": 0.85,
    }
)

df_limpio, reporte = cleaner.run_with_report(df, preview_rows=3)

df_limpio.to_csv("data_limpia.csv", index=False)
print("Base limpia guardada correctamente.")
print("Reporte (dict):", reporte.model_dump())