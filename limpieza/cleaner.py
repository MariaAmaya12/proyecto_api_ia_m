from __future__ import annotations

from typing import Any, Mapping, Optional

import pandas as pd

from .pipeline import (
    convertir_a_numerico_seguro,
    convertir_vacios_a_nan,
    eliminar_duplicados,
    estandarizar_nombres_columnas,
    imputar_nulos,
    limpiar_columnas_monetarias,
)
from .schemas import LimpiezaConfigSchema, LimpiezaReporteSchema


class DataCleaner:
    """
    Encapsula el pipeline de limpieza en una clase con configuración validada por Pydantic.
    """

    def __init__(self, config: Optional[LimpiezaConfigSchema | Mapping[str, Any]] = None) -> None:
        if config is None:
            self.config = LimpiezaConfigSchema()
        elif isinstance(config, LimpiezaConfigSchema):
            self.config = config
        else:
            self.config = LimpiezaConfigSchema.model_validate(config)

    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        df_work = df.copy()

        estandarizar_nombres_columnas(df_work)
        convertir_vacios_a_nan(df_work)
        eliminar_duplicados(df_work)

        if self.config.columnas_monetarias:
            limpiar_columnas_monetarias(df_work, self.config.columnas_monetarias)

        convertir_a_numerico_seguro(
            df_work,
            columnas_objetivo=self.config.columnas_numericas_objetivo,
            umbral_conversion=self.config.umbral_conversion,
        )

        imputar_nulos(
            df_work,
            estrategia_num=self.config.estrategia_num,
            estrategia_cat=self.config.estrategia_cat,
        )

        return df_work

    def run_with_report(
        self, df: pd.DataFrame, preview_rows: int = 5
    ) -> tuple[pd.DataFrame, LimpiezaReporteSchema]:
        n_in = len(df)
        df_out = self.run(df)
        n_out = len(df_out)

        preview = df_out.head(preview_rows).to_dict(orient="records") if preview_rows > 0 else []

        reporte = LimpiezaReporteSchema(
            n_filas_entrada=n_in,
            n_filas_salida=n_out,
            columnas=list(df_out.columns),
            preview=preview,
        )
        return df_out, reporte