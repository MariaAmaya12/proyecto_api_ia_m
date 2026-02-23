# Proyecto API IA – Fase 1  
## Limpieza y Exposición de Datos Inmobiliarios (Bogotá)

Este proyecto implementa una API REST para la limpieza estructurada de datos inmobiliarios utilizando:

- **Pandas** (procesamiento y transformación de datos)
- **Programación Orientada a Objetos (POO)** – clase `DataCleaner`
- **Pydantic** (validación de esquemas de entrada y salida)
- **FastAPI** (exposición de servicio REST)
- **Uvicorn** (servidor ASGI)

---

# 1. Objetivo del Proyecto

Desarrollar un módulo reutilizable de limpieza de datos y exponerlo como una API validada y documentada automáticamente.

El proyecto corresponde a la **Fase 1 (Semanas 1–4)** del curso, donde se integran:

- Limpieza básica en Pandas  
- Modularización en funciones  
- Encapsulación mediante clases  
- Validación estructurada con Pydantic  
- Implementación de una API con FastAPI  

---

# 2. Dataset Utilizado

## Inmuebles Bogotá

El conjunto de datos contiene información sobre inmuebles en Bogotá, Colombia.

### Variables incluidas:

- **Tipo**: tipo de propiedad (apartamento, casa, oficina, local, lote, bodega, etc.)
- **Descripción**: descripción textual del inmueble
- **Habitaciones**: número de habitaciones
- **Baños**: número de baños
- **Área**: área en metros cuadrados
- **Barrio**: barrio donde se ubica el inmueble
- **UPZ**: Unidad de Planeamiento Zonal
- **Valor**: precio en pesos colombianos




Archivo principal utilizado:

```
inmuebles_bogota.csv
```

---

# 3. Estructura del Proyecto

```
proyecto_api_ia/
│
├── api/
│   └── main.py
│
├── limpieza/
│   ├── __init__.py
│   ├── pipeline.py
│   ├── cleaner.py
│   └── schemas.py
│
├── eda/
│   ├── analisis.ipynb
│   └── eda.py
│
├── scripts/
│   ├── ejecutar_pipeline.py
│   ├── ejecutar_pipeline_semana1.py
│   └── limpieza_semana1.py
│
├── inmuebles_bogota.csv
├── data_limpia.csv
├── requirements.txt
└── README.md
```

---

# 4. Descripción de Carpetas

## 📁 api/
Contiene la aplicación FastAPI.

- Define los endpoints:
  - `POST /limpiar`
  - `GET /health`
- Integra los esquemas Pydantic.
- Expone documentación automática en `/docs`.

---

## 📁 limpieza/
Módulo reutilizable de limpieza de datos.

### pipeline.py
Funciones puras de transformación:
- Estandarización de nombres de columnas
- Conversión de vacíos a NaN
- Eliminación de duplicados
- Limpieza de columnas monetarias
- Conversión numérica segura
- Imputación de valores faltantes

### cleaner.py
Clase `DataCleaner`:
- Encapsula el pipeline de limpieza
- Recibe configuración validada
- Genera reporte estructurado

### schemas.py
Modelos Pydantic:
- `LimpiezaConfigSchema`
- `LimpiezaReporteSchema`

---

## 📁 eda/
Exploración inicial del dataset:
- Análisis descriptivo
- Validación preliminar
- Exploración de variables

---

## 📁 scripts/
Archivos auxiliares utilizados durante el desarrollo inicial del proyecto.

---

# 5. Flujo del Pipeline de Limpieza

1. Copia segura del DataFrame
2. Normalización de nombres de columnas
3. Conversión de valores vacíos a NaN
4. Eliminación de registros duplicados
5. Limpieza de columnas monetarias
6. Conversión numérica controlada
7. Imputación de valores faltantes
8. Generación de reporte estructurado

---

# 6. Instalación

Clonar el repositorio:

```bash
git clone <URL_DEL_REPO>
cd proyecto_api_ia
```

Crear entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# 7. Ejecución de la API

```bash
python -m uvicorn api.main:app --reload
```

Documentación interactiva disponible en:

```
http://127.0.0.1:8000/docs
```

---

# 8. Endpoints Disponibles

## GET /health
Verifica que la API esté activa.

Respuesta:

```json
{"status": "ok"}
```

---

## POST /limpiar

Recibe:

- `config`: parámetros de limpieza
- `data`: lista de registros JSON

Valida automáticamente con Pydantic.

Devuelve:

- Número de filas de entrada
- Número de filas de salida
- Columnas finales
- Vista previa del dataset limpio

Si la configuración es inválida (por ejemplo, `umbral_conversion > 1`), devuelve:

```
HTTP 422 – Unprocessable Entity
```

---

# 9. Estado del Proyecto

✔ Fase 1 completada  
✔ Modularización implementada  
✔ Encapsulación con POO  
✔ Validación estructurada con Pydantic  
✔ API REST funcional  
✔ Documentación automática con Swagger  

---

# 10. Autor

Proyecto académico – Curso Python para APIs e IA  
Universidad – 2026