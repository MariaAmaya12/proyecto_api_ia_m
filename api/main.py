from __future__ import annotations

from typing import Any

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

from limpieza import DataCleaner, LimpiezaConfigSchema, LimpiezaReporteSchema

app = FastAPI(title="API Limpieza - Proyecto")


class LimpiezaRequest(BaseModel):
    """
    Request para la API:
    - config: validado con tu LimpiezaConfigSchema
    - data: lista de registros (cada registro es un dict)
    """
    config: LimpiezaConfigSchema = Field(default_factory=LimpiezaConfigSchema)
    data: list[dict[str, Any]] = Field(..., min_length=1)


@app.post("/limpiar", response_model=LimpiezaReporteSchema)
def limpiar(request: LimpiezaRequest) -> LimpiezaReporteSchema:
    df = pd.DataFrame(request.data)

    cleaner = DataCleaner(config=request.config)
    _, reporte = cleaner.run_with_report(df, preview_rows=5)

    return reporte


@app.get("/")
def root():
    return {"message": "API de limpieza activa. Ve a /docs"}