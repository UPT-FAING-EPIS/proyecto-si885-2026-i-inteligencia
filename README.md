# EPIS Analytics

Aplicación web analítica en Streamlit para evaluar la producción de contenido en redes sociales de estudiantes de Ingeniería de Sistemas.

## Objetivo

El proyecto genera datos simulados en SQLite y muestra dos dashboards:

- **Dashboard Operacional (Mi Perfil):** métricas e interacciones de un estudiante seleccionado, con filtro por red social.
- **Dashboard Táctico (Impacto Global EPIS):** alcance por ciclo, interacciones por red social y Top 10 de estudiantes por engagement.

## Arquitectura

El proyecto está organizado por capas:

- `models/`: entidades y filtros del dominio.
- `repositories/`: acceso a datos con patrón Repository y SQLite.
- `services/`: casos de uso y lógica de negocio.
- `controllers/`: coordinación entre servicios y vistas.
- `views/`: interfaz Streamlit.
- `tests/`: pruebas unitarias.
- `app.py`: punto de entrada de la aplicación.

También incluye el diagrama conceptual en `arquitectura_epis.puml`.

## Instalación

```bash
python -m pip install -r requirements.txt
```

Para ejecutar pruebas:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Ejecución

Para levantar el dashboard Streamlit:

```bash
python -m streamlit run app.py
```

La primera ejecución crea automáticamente la base de datos local `epis_data.db` si no existe.

Para levantar el backend FastAPI de la versión web separada:

```bash
python -m uvicorn api.main:app --reload
```

Endpoints principales:

- `GET /api/health`
- `GET /api/estudiantes`
- `POST /api/auth/login`
- `GET /api/dashboard/perfil?estudiante=...&red_social=...`
- `GET /api/dashboard/global?red_social=...`

Para levantar el frontend Angular:

```bash
cd epis-web
npm.cmd start
```

La app Angular consume la API en `http://127.0.0.1:8000/api`.

## Reglas de negocio cubiertas

- Generación automática de 1500 registros simulados.
- Datos de los últimos 12 meses.
- Ciclos académicos desde `I` hasta `X`.
- Redes sociales consideradas: `LinkedIn`, `Instagram` y `YouTube`.
- Filtro general por red social con opción `Todas`.
- Picos de publicaciones en julio y diciembre.
- Las interacciones nunca superan el alcance.
- Las publicaciones de tipo `Video` tienen mayor promedio de interacciones que `Texto`.
