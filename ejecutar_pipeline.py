import pandas as pd
from limpieza import limpiar_dataframe

# Leer datos crudos
df = pd.read_csv("inmuebles_bogota.csv", encoding="utf-8")

# Aplicar limpieza
df_limpio = limpiar_dataframe(
    df,
    columnas_monetarias=["valor"]
)

# Guardar directamente en la carpeta principal del proyecto
df_limpio.to_csv("data_limpia.csv", index=False)

print("Base limpia guardada correctamente.")
