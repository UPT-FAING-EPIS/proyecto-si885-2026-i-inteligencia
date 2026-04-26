<center>

![Logo UPT](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingenieria de Sistemas**

**Proyecto EPIS Analytics**

Curso: *Inteligencia de negocios*

Docente: *Mag. Patrick Cuadros Quiroga*

Integrantes:

***Enzo Leonel Laqui Luyo (2022073907)***

***Steven Christopher Yizuka Baldeón (2002023628)***

**Tacna - Peru**

***2026***

</center>

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Sistema EPIS Analytics

## Documento de Vision

Version *1.0*

| CONTROL DE VERSIONES ||||||
| :-: | :- | :- | :- | :- | :- |
| Version | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | Equipo del proyecto | Equipo del proyecto | Docente del curso | 25/04/2026 | Version inicial del informe de vision |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Indice General

1. [Introduccion](#1-introduccion)
2. [Posicionamiento](#2-posicionamiento)
3. [Descripcion de los interesados y usuarios](#3-descripcion-de-los-interesados-y-usuarios)
4. [Vista General del Producto](#4-vista-general-del-producto)
5. [Contenido para GitHub Wiki](#5-contenido-para-github-wiki)
6. [RoadMap del Proyecto](#6-roadmap-del-proyecto)
7. [Caracteristicas del Producto](#7-caracteristicas-del-producto)
8. [Restricciones](#8-restricciones)
9. [Rangos de Calidad](#9-rangos-de-calidad)
10. [Precedencia y Prioridad](#10-precedencia-y-prioridad)
11. [Otros Requerimientos del Producto](#11-otros-requerimientos-del-producto)
12. [Conclusiones](#12-conclusiones)
13. [Recomendaciones](#13-recomendaciones)
14. [Bibliografia](#14-bibliografia)
15. [Webgrafia](#15-webgrafia)

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Informe de Vision

## 1. Introduccion

### 1.1. Proposito

El presente documento tiene como proposito definir la vision general del sistema **EPIS Analytics**, describiendo su alcance, usuarios, necesidades, capacidades, restricciones, prioridades y evolucion esperada. El informe tambien consolida el contenido preparado para la documentacion tipo **GitHub Wiki**, incluyendo un RoadMap del proyecto.

El documento busca servir como guia para el equipo de desarrollo, docentes, revisores y futuros responsables de mantenimiento del sistema.

### 1.2. Alcance

EPIS Analytics es un sistema web de analisis de contenido social orientado a estudiantes de la Escuela Profesional de Ingenieria de Sistemas. El sistema permite consultar metricas personales y globales relacionadas con publicaciones simuladas en redes sociales como LinkedIn, Instagram y YouTube.

El alcance actual incluye:

| Elemento | Incluido |
| :- | :-: |
| Generacion de datos simulados | Si |
| Modelo de publicaciones por estudiante, ciclo y red social | Si |
| Dashboard personal | Si |
| Dashboard global | Si |
| Filtros por red social | Si |
| Login con usuario, contrasena y token | Si |
| API REST con FastAPI | Si |
| Frontend web con Angular | Si |
| Graficos con ECharts | Si |
| Infraestructura Terraform para analisis de costos | Si |
| Integracion real con APIs de redes sociales | No, queda para una fase futura |
| Despliegue real en AWS | No, queda preparado pero no aplicado |

### 1.3. Definiciones, siglas y abreviaturas

| Termino | Definicion |
| :- | :- |
| EPIS | Escuela Profesional de Ingenieria de Sistemas |
| API | Interfaz de programacion de aplicaciones |
| REST | Estilo de arquitectura para servicios web |
| Frontend | Aplicacion cliente visible para el usuario |
| Backend | Aplicacion servidor que procesa datos y reglas de negocio |
| Dashboard | Panel visual de indicadores |
| Token | Credencial digital usada para autenticar solicitudes |
| IaC | Infrastructure as Code, infraestructura como codigo |
| Terraform | Herramienta para declarar y gestionar infraestructura |
| Infracost | Herramienta para estimar costos cloud desde Terraform |
| RoadMap | Plan de evolucion del producto |

### 1.4. Referencias

| Referencia | Descripcion |
| :- | :- |
| `FD01-Informe-Factibilidad.md` | Informe de factibilidad del proyecto |
| `arquitectura_epis.puml` | Diagrama conceptual de arquitectura |
| `infra/terraform` | Modulo Terraform para infraestructura propuesta |
| Repositorio GitHub del curso | Plantillas FD01 y FD02 |
| Documentacion oficial de Angular | Desarrollo frontend |
| Documentacion oficial de FastAPI | Desarrollo backend |
| Documentacion oficial de Terraform | Infraestructura como codigo |

### 1.5. Vision general

El sistema EPIS Analytics busca convertirse en una herramienta academica para interpretar la presencia digital estudiantil mediante visualizaciones claras, filtros simples y una arquitectura extensible. La vision del producto es permitir que estudiantes, docentes y coordinacion academica consulten informacion de actividad social en un entorno centralizado, seguro y preparado para evolucionar hacia datos reales en el futuro.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 2. Posicionamiento

### 2.1. Oportunidad de negocio

Aunque el proyecto se desarrolla en un contexto academico, representa una oportunidad para demostrar como una escuela profesional puede transformar datos dispersos de actividad digital en informacion util para seguimiento, visibilidad institucional y toma de decisiones.

La oportunidad se centra en:

| Oportunidad | Valor |
| :- | :- |
| Analitica academica | Permite observar actividad por estudiante, ciclo y red social |
| Visibilidad institucional | Ayuda a comprender que redes tienen mayor alcance |
| Seguimiento estudiantil | Facilita una vista individual de indicadores |
| Modernizacion tecnologica | Usa Angular, FastAPI, pruebas, token e infraestructura como codigo |
| Reutilizacion futura | La arquitectura puede ampliarse a datos reales o nuevos modulos |

### 2.2. Definicion del problema

Actualmente, la informacion de publicaciones e interacciones digitales suele estar distribuida en diferentes redes sociales. Esto dificulta analizar el impacto de la actividad social de estudiantes, comparar redes, identificar tendencias por ciclo y observar indicadores agregados.

| Aspecto | Situacion actual | Impacto |
| :- | :- | :- |
| Informacion dispersa | Cada red social maneja datos por separado | Dificulta la consulta consolidada |
| Falta de indicadores | No hay metricas centralizadas | Reduce la capacidad de analisis |
| Consulta manual | Requiere revisar perfiles o publicaciones una por una | Consume tiempo |
| Baja trazabilidad | No existe un repositorio unico de datos | Complica comparaciones por ciclo o estudiante |
| Seguridad | Sin login no hay control de acceso | Riesgo para vistas personales |

### 2.3. Sentencia de posicionamiento

Para estudiantes, docentes y responsables academicos de EPIS que necesitan consultar indicadores de presencia digital, EPIS Analytics es un sistema web de analitica social que permite visualizar metricas personales y globales por red social, ciclo y estudiante. A diferencia de revisiones manuales o reportes aislados, el sistema centraliza datos, muestra graficos interactivos y protege las vistas mediante autenticacion.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 3. Descripcion de los interesados y usuarios

### 3.1. Resumen de los interesados

| Interesado | Responsabilidad | Interes principal |
| :- | :- | :- |
| Estudiantes EPIS | Usuarios de perfil personal | Consultar sus metricas y compararlas por red social |
| Docentes | Revisores academicos | Ver indicadores globales y tendencias |
| Coordinacion academica | Toma de decisiones | Analizar participacion por ciclo y red |
| Equipo de desarrollo | Construccion y mantenimiento | Implementar, probar y documentar el sistema |
| Administrador tecnico | Configuracion y despliegue | Mantener ambiente, datos y seguridad |

### 3.2. Resumen de los usuarios

| Usuario | Descripcion | Acceso |
| :- | :- | :- |
| Estudiante | Consulta su perfil y metricas personales | Login con usuario y contrasena |
| Docente | Revisa dashboard global y tendencias | Acceso autenticado |
| Administrador | Gestiona configuracion tecnica y datos | Acceso tecnico al backend y repositorio |

### 3.3. Entorno de usuario

El usuario accede desde un navegador web. La aplicacion frontend Angular consume la API FastAPI mediante HTTP/REST. El sistema usa datos simulados persistidos en SQLite para el prototipo.

| Elemento | Descripcion |
| :- | :- |
| Navegador | Chrome, Edge, Firefox u otro navegador moderno |
| Dispositivo | PC, laptop o tablet |
| Autenticacion | Usuario, contrasena y token firmado |
| Interaccion principal | Seleccion de filtros y visualizacion de graficos |
| Datos | Simulados para LinkedIn, Instagram y YouTube |

### 3.4. Perfiles de los interesados

#### Estudiante EPIS

Necesita una vista simple que le permita identificar su actividad, interacciones, publicaciones y red con mejor desempeno.

#### Docente

Necesita observar tendencias generales de estudiantes y ciclos, sin revisar manualmente cada registro.

#### Coordinacion academica

Necesita informacion agregada para interpretar patrones de presencia digital y planificar acciones de comunicacion.

#### Equipo tecnico

Necesita una arquitectura mantenible, testeable y documentada para continuar el desarrollo del sistema.

### 3.5. Necesidades de interesados y usuarios

| Necesidad | Prioridad | Solucion propuesta |
| :- | :-: | :- |
| Consultar metricas personales | Alta | Dashboard personal por estudiante |
| Consultar informacion global | Alta | Dashboard global |
| Filtrar por red social | Alta | Selector de red con vista general y especifica |
| Controlar acceso | Alta | Login con token |
| Interpretar datos visualmente | Alta | Graficos con ECharts |
| Preparar despliegue cloud | Media | Terraform e Infracost |
| Integrar datos reales | Media | RoadMap de evolucion futura |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 4. Vista General del Producto

### 4.1. Perspectiva del producto

EPIS Analytics es un sistema cliente-servidor compuesto por:

| Componente | Tecnologia | Responsabilidad |
| :- | :- | :- |
| Frontend | Angular | Login, vistas, filtros y graficos |
| Backend | FastAPI | API REST, CORS, autenticacion y respuestas JSON |
| Servicios | Python | Analitica, autenticacion y generacion de datos |
| Repositorios | Python + SQLite | Acceso a publicaciones y usuarios |
| Modelos | Python dataclasses | Entidades de dominio |
| Infraestructura | Terraform | Definicion de recursos cloud |

### 4.2. Resumen de capacidades

| Capacidad | Descripcion | Estado |
| :- | :- | :-: |
| Login | Acceso por usuario y contrasena | Implementado |
| Token | Proteccion de endpoints privados | Implementado |
| Dashboard personal | Metricas por estudiante | Implementado |
| Dashboard global | Indicadores agregados | Implementado |
| Filtro por red social | Todas, LinkedIn, Instagram, YouTube | Implementado |
| Graficos | Series, barras, tortas y rankings | Implementado |
| Pruebas | Backend y frontend | Implementado |
| Terraform | Infraestructura AWS propuesta | Validado |
| Infracost | Estimacion de costos base | Validado |
| Datos reales | Integracion con APIs externas | Pendiente |

### 4.3. Suposiciones y dependencias

| Suposicion o dependencia | Descripcion |
| :- | :- |
| Datos simulados | El prototipo no consume APIs reales de redes sociales |
| Estudiantes EPIS | Se consideran estudiantes distribuidos del ciclo I al X |
| Redes iniciales | LinkedIn, Instagram y YouTube |
| Backend local | FastAPI se ejecuta en desarrollo en `127.0.0.1:8000` |
| Frontend local | Angular se ejecuta en desarrollo en `127.0.0.1:4200` |
| SQLite | Base suficiente para prototipo |
| AWS | Proveedor propuesto para analisis de infraestructura |

### 4.4. Costos y precios

El costo de desarrollo se detalla en el FD01. Para la infraestructura cloud, el modulo Terraform fue validado con Infracost y estima un costo base de **USD 9.19 mensuales**, compuesto principalmente por una instancia EC2 t3.micro y almacenamiento EBS gp3.

| Recurso | Costo mensual estimado |
| :- | -: |
| EC2 t3.micro Linux | USD 7.59 |
| EBS gp3 20 GB | USD 1.60 |
| S3 y CloudFront | Variable segun uso |
| **Total base** | **USD 9.19** |

### 4.5. Licenciamiento e instalacion

El sistema utiliza tecnologias libres o de uso gratuito para desarrollo academico:

| Tecnologia | Licenciamiento / uso |
| :- | :- |
| Python | Open source |
| FastAPI | Open source |
| Angular | Open source |
| SQLite | Dominio publico |
| ECharts | Open source |
| Terraform | Herramienta de IaC bajo licencia de HashiCorp |
| Infracost | Herramienta de estimacion de costos con CLI disponible |

Instalacion local resumida:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
python -m uvicorn api.main:app --reload
cd epis-web
npm install
npm start
```

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 5. Contenido para GitHub Wiki

El repositorio remoto consultado no tiene una GitHub Wiki publicada al momento de la revision: la ruta `/wiki` redirige al repositorio principal y el repositorio `.wiki.git` no esta disponible. Por ello, esta seccion consolida el contenido que debe publicarse en la GitHub Wiki del proyecto.

### 5.1. Home

**EPIS Analytics** es un sistema web de analisis de contenido social para estudiantes de EPIS. Permite visualizar indicadores personales y globales de publicaciones simuladas en LinkedIn, Instagram y YouTube, considerando estudiantes de los ciclos I al X.

Contenido sugerido para la portada:

| Tema | Descripcion |
| :- | :- |
| Objetivo | Analizar metricas de actividad social de estudiantes EPIS |
| Tecnologias | Angular, FastAPI, SQLite, ECharts, Terraform |
| Arquitectura | Cliente-servidor con backend por capas |
| Estado | Prototipo funcional |
| Acceso local | Angular en `4200`, FastAPI en `8000` |

### 5.2. Arquitectura

La arquitectura se divide en frontend Angular y backend FastAPI. El frontend consume endpoints REST y el backend organiza la logica por capas:

```text
Angular Frontend
  Componentes
  Servicios HTTP
  Guard e interceptor de autenticacion

FastAPI Backend
  Rutas / controladores
  Servicios de negocio
  Repositorios
  Modelos
  Base SQLite
```

El diagrama principal se mantiene en `arquitectura_epis.puml`.

### 5.3. Instalacion local

Backend:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
python -m pytest -q
python -m uvicorn api.main:app --host 127.0.0.1 --port 8000 --reload
```

Frontend:

```bash
cd epis-web
npm install
npm test -- --watch=false
npm run build
npm start
```

### 5.4. Uso del sistema

1. Abrir `http://127.0.0.1:4200/login`.
2. Seleccionar un estudiante.
3. Ingresar la contrasena demo `epis123`.
4. Entrar al dashboard personal.
5. Cambiar entre vista personal y global.
6. Filtrar por todas las redes o por LinkedIn, Instagram y YouTube.

### 5.5. API

| Endpoint | Metodo | Descripcion | Seguridad |
| :- | :-: | :- | :- |
| `/api/health` | GET | Verifica estado de API | Publico |
| `/api/estudiantes` | GET | Lista estudiantes disponibles | Publico |
| `/api/auth/login` | POST | Inicia sesion | Publico |
| `/api/auth/me` | GET | Retorna sesion autenticada | Bearer token |
| `/api/dashboard/perfil` | GET | Dashboard personal | Bearer token |
| `/api/dashboard/global` | GET | Dashboard global | Bearer token |

### 5.6. Pruebas

Comandos principales:

```bash
python -m pytest -q
cd epis-web
npm test -- --watch=false
npm run build
```

Resultado validado:

| Componente | Resultado |
| :- | :- |
| Backend | 50 pruebas pasadas |
| Frontend | 2 pruebas pasadas |
| Angular build | Correcto |
| Terraform validate | Correcto |
| Infracost breakdown | USD 9.19/mes |

### 5.7. Terraform y costos

La infraestructura propuesta esta en `infra/terraform`.

Comandos:

```bash
terraform init
terraform fmt -recursive
terraform validate
infracost breakdown --path . --terraform-var frontend_bucket_name=epis-analytics-dev-frontend-demo
```

Resultado base:

```text
OVERALL TOTAL $9.19
```

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 6. RoadMap del Proyecto

El RoadMap define la evolucion del sistema desde el prototipo actual hasta una version mas completa, segura y preparada para datos reales.

### 6.1. RoadMap general

| Fase | Periodo estimado | Objetivo | Estado |
| :- | :-: | :- | :-: |
| Fase 1 | Semana 1 | Analisis inicial y estructura base del proyecto | Completado |
| Fase 2 | Semana 2 | Modelos, repositorios y servicios base | Completado |
| Fase 3 | Semana 3 | Controladores/API y pruebas backend | Completado |
| Fase 4 | Semana 4 | Frontend Angular y dashboards | Completado |
| Fase 5 | Semana 5 | Login con token y rutas protegidas | Completado |
| Fase 6 | Semana 6 | Graficos, filtros por red social y responsividad | Completado |
| Fase 7 | Semana 7 | Documentacion FD01, FD02 y README | En progreso |
| Fase 8 | Semana 8 | Terraform, costos e infraestructura validada | En progreso |
| Fase 9 | Futuro | Integracion con datos reales o APIs externas | Pendiente |
| Fase 10 | Futuro | Despliegue cloud controlado | Pendiente |

### 6.2. RoadMap funcional

| Funcionalidad | Prioridad | Estado | Observacion |
| :- | :-: | :-: | :- |
| Login real | Alta | Completado | Usuario, contrasena, token |
| Dashboard personal | Alta | Completado | Metricas por estudiante |
| Dashboard global | Alta | Completado | Agregados por ciclo y red |
| Filtro por red social | Alta | Completado | Todas, LinkedIn, Instagram, YouTube |
| Busqueda de estudiante | Media | Pendiente | Buscar y abrir perfil desde listado |
| Power BI simulado o embebido | Media | Pendiente | Evaluar alternativa visual |
| Administracion de usuarios | Media | Pendiente | Cambio de contrasena y roles |
| Exportacion de reportes | Baja | Pendiente | PDF/CSV |

### 6.3. RoadMap tecnico

| Mejora tecnica | Prioridad | Estado | Beneficio |
| :- | :-: | :-: | :- |
| Pruebas unitarias backend | Alta | Completado | Reduce regresiones |
| Pruebas frontend | Media | Completado | Valida render inicial |
| Terraform | Alta | Completado | Infraestructura reproducible |
| Infracost | Alta | Completado | Costos antes de desplegar |
| CI/CD GitHub Actions | Media | Pendiente | Automatiza pruebas y build |
| PostgreSQL | Media | Pendiente | Mejor persistencia para produccion |
| HTTPS y dominio | Media | Pendiente | Acceso seguro en despliegue |
| Observabilidad | Baja | Pendiente | Logs y metricas de operacion |

### 6.4. Hitos de entrega

| Hito | Criterio de aceptacion |
| :- | :- |
| Prototipo local funcional | Login, dashboard personal y global operan desde navegador |
| API validada | Pruebas backend pasan correctamente |
| Frontend validado | Build Angular y pruebas pasan correctamente |
| Documentacion base | FD01, FD02 y README completos |
| Infraestructura validada | `terraform validate` correcto e Infracost con costo estimado |
| Presentacion final | Demostracion del flujo completo y explicacion de arquitectura |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 7. Caracteristicas del Producto

| Caracteristica | Descripcion | Prioridad |
| :- | :- | :-: |
| Autenticacion | Login con usuario, contrasena y token | Alta |
| Perfil personal | Consulta de metricas por estudiante | Alta |
| Vista global | Consulta de indicadores agregados | Alta |
| Filtros | Seleccion por red social | Alta |
| Graficos | Visualizacion con ECharts | Alta |
| Datos simulados | Base controlada para pruebas | Alta |
| Arquitectura por capas | Separacion modelo, repositorio, servicio y controlador | Alta |
| Terraform | Infraestructura declarada como codigo | Media |
| Estimacion de costos | Analisis con Infracost | Media |
| Wiki | Documentacion navegable del proyecto | Media |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 8. Restricciones

| Restriccion | Descripcion |
| :- | :- |
| Datos simulados | El sistema no consume aun datos reales de redes sociales |
| APIs externas | LinkedIn, Instagram y YouTube requieren permisos y cumplimiento de terminos |
| SQLite | Adecuado para prototipo, limitado para produccion multiusuario |
| Despliegue | Terraform esta validado, pero no aplicado en AWS |
| Seguridad | El login actual es valido para prototipo, pero produccion requeriria gestion robusta de secretos |
| Presupuesto | La infraestructura debe mantenerse de bajo costo |
| Tiempo academico | El alcance se limita al periodo del curso |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 9. Rangos de Calidad

| Atributo | Criterio | Meta |
| :- | :- | :- |
| Usabilidad | Flujo claro de login y dashboard | Usuario puede consultar metricas sin instrucciones extensas |
| Rendimiento | Respuesta rapida para dataset simulado | Consultas menores a 2 segundos en local |
| Seguridad | Proteccion de dashboards | Endpoints privados requieren token |
| Mantenibilidad | Codigo organizado por capas | Cambios localizados por modulo |
| Portabilidad | Ejecucion local y posible despliegue cloud | Backend y frontend separables |
| Testeabilidad | Pruebas automatizadas | Backend y frontend con pruebas ejecutables |
| Costo | Infraestructura controlada | Costo base estimado menor a USD 10/mes |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 10. Precedencia y Prioridad

| Requerimiento | Prioridad | Justificacion |
| :- | :-: | :- |
| Login | Alta | Controla acceso a vistas privadas |
| Dashboard personal | Alta | Funcionalidad principal para estudiante |
| Dashboard global | Alta | Funcionalidad principal para analisis general |
| Filtros por red | Alta | Permite comparar LinkedIn, Instagram y YouTube |
| Pruebas | Alta | Sustenta calidad del prototipo |
| Documentacion | Alta | Requerida para evaluacion academica |
| Terraform/Infracost | Media | Sustenta factibilidad y costos |
| Integracion real con redes | Media | Aporta valor futuro, pero requiere permisos |
| Power BI | Baja | Puede mejorar impacto visual, pero no es critico |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 11. Otros Requerimientos del Producto

### 11.1. Estandares legales

El prototipo usa datos simulados. Si se incorporan datos reales, se debera cumplir normativa de proteccion de datos personales, terminos de uso de redes sociales y consentimiento de los participantes.

### 11.2. Estandares de comunicacion

La comunicacion entre frontend y backend se realiza mediante HTTP/REST con JSON. Para produccion se recomienda HTTPS.

### 11.3. Estandares de cumplimiento de plataforma

El sistema debe ejecutarse en navegadores modernos y mantener compatibilidad con ambientes Windows, Linux o servicios cloud.

### 11.4. Estandares de calidad y seguridad

| Estandar | Aplicacion en el proyecto |
| :- | :- |
| Separacion por capas | Models, repositories, services, routes y Angular components |
| Pruebas automatizadas | Pytest y pruebas Angular |
| Control de acceso | Bearer token |
| Infraestructura reproducible | Terraform |
| Costos controlados | Infracost |
| Documentacion | README, FD01, FD02 y Wiki propuesta |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 12. Conclusiones

1. EPIS Analytics cuenta con una vision clara como sistema web de analitica social academica para estudiantes EPIS.

2. El producto se encuentra orientado a resolver la dispersion de informacion social mediante dashboards personales y globales.

3. La arquitectura cliente-servidor con Angular y FastAPI permite mantener separadas la interfaz, la API y la logica de negocio.

4. La inclusion de login con token mejora el nivel de seguridad respecto a un login simulado.

5. El contenido preparado para GitHub Wiki permite documentar instalacion, arquitectura, API, pruebas, Terraform y RoadMap.

6. El RoadMap permite proyectar mejoras futuras como busqueda de estudiantes, administracion de usuarios, CI/CD, PostgreSQL e integracion con datos reales.

## 13. Recomendaciones

1. Publicar la GitHub Wiki del repositorio con las secciones propuestas en este documento.

2. Mantener actualizado el RoadMap conforme se completen nuevas funcionalidades.

3. Agregar GitHub Actions para validar pruebas backend, frontend y Terraform en cada cambio.

4. Evaluar PostgreSQL para una futura version productiva.

5. No ejecutar `terraform apply` sin presupuesto, credenciales revisadas y reglas de seguridad adecuadas.

## 14. Bibliografia

- Sommerville, I. *Software Engineering*. Pearson.
- Pressman, R. *Software Engineering: A Practitioner's Approach*. McGraw-Hill.
- Fowler, M. *Patterns of Enterprise Application Architecture*. Addison-Wesley.

## 15. Webgrafia

- Repositorio del proyecto: https://github.com/UPT-FAING-EPIS/proyecto-si885-2026-i-inteligencia
- Plantilla FD02: https://github.com/UPT-FAING-EPIS/proyecto-si885-2026-i-inteligencia/blob/main/FD02-Informe-Vision.md
- Angular Documentation: https://angular.dev/
- FastAPI Documentation: https://fastapi.tiangolo.com/
- Terraform Documentation: https://developer.hashicorp.com/terraform/docs
- Infracost Documentation: https://www.infracost.io/docs/
