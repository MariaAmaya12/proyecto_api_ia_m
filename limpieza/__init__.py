### Se define la API publica del paquete.

from .pipeline import limpiar_dataframe ## pipeline funcional 
from .cleaner import DataCleaner        ## Clases 
from .schemas import LimpiezaConfigSchema, LimpiezaReporteSchema  ## contratos Pydantic


## Con __all__ se define, mediante una lista,
# qué nombres públicos del módulo se importan con from ... import *.
__all__ = [
    "limpiar_dataframe",
    "DataCleaner",
    "LimpiezaConfigSchema",
    "LimpiezaReporteSchema",
]