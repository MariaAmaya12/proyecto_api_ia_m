from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field, ConfigDict


class LimpiezaConfigSchema(BaseModel):
    """
    Contrato de entrada (Input) para configurar la limpieza.

    Valida y documenta:
    - tipos
    - restricciones básicas con Field
    """

    model_config = ConfigDict(extra="forbid")  # no permite parámetros desconocidos

    columnas_monetarias: Optional[list[str]] = Field(
        default=None,
        description="Lista de columnas con formato monetario (ej: ['valor']).",
        examples=[["valor"]],
    )

    columnas_numericas_objetivo: Optional[list[str]] = Field(
        default=None,
        description="Columnas que se deben convertir a numérico sí o sí.",
        examples=[["area", "habitaciones"]],
    )

    estrategia_num: str = Field(
        default="median",
        description="Estrategia de imputación numérica.",
        pattern="^(median|mean)$",
        examples=["median"],
    )

    estrategia_cat: str = Field(
        default="moda",
        description="Estrategia de imputación categórica: 'moda' o un valor constante.",
        examples=["moda", "desconocido"],
    )

    umbral_conversion: float = Field(
        default=0.85,
        description="Proporción mínima para convertir una columna texto a numérica.",
        ge=0.0,
        le=1.0,
        examples=[0.85],
    )


class LimpiezaReporteSchema(BaseModel):
    """
    Contrato de salida (Output) para reportar el resultado de la limpieza.
    Serializable a JSON con model_dump().
    """

    n_filas_entrada: int = Field(..., ge=0, description="Número de filas antes de limpiar.")
    n_filas_salida: int = Field(..., ge=0, description="Número de filas después de limpiar.")
    columnas: list[str] = Field(..., description="Lista final de columnas en el DataFrame limpio.")

    # Preview opcional (sirve para APIs; evita retornar todo el DF)
    preview: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Muestra de filas limpias en formato JSON (records).",
    )