<center>

![Logo UPT](FD06-EPIS-PropuestaProyecto-media/media/image1.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingenieria de Sistemas**

**Propuesta del Proyecto *EPIS Analytics***

Curso: *Inteligencia de negocios*

Docente: *Mag. Patrick Cuadros Quiroga*

Integrantes:

***Enzo Leonel Laqui Luyo (2022073907)***

***Steven Christopher YIZUKA BALDEÓN (2002023628)***

**Tacna - Peru**

***2026***

</center>

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<center>

# Proyecto

***EPIS Analytics: Sistema web de analitica social para estudiantes de la Escuela Profesional de Ingenieria de Sistemas, Tacna, 2026***

**Presentado por:**

***Enzo Leonel Laqui Luyo***

***Steven Christopher YIZUKA BALDEÓN***

***Estudiantes desarrolladores del curso Inteligencia de negocios***

***25/04/2026***

</center>

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

| CONTROL DE VERSIONES ||||||
| :-: | :- | :- | :- | :- | :- |
| Version | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | Equipo del proyecto | Equipo del proyecto | Docente del curso | 25/04/2026 | Version inicial de la propuesta del proyecto |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Tabla de contenido

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [I. Propuesta narrativa](#i-propuesta-narrativa)
3. [1. Planteamiento del Problema](#1-planteamiento-del-problema)
4. [2. Justificacion del proyecto](#2-justificacion-del-proyecto)
5. [3. Objetivo general](#3-objetivo-general)
6. [4. Beneficios](#4-beneficios)
7. [5. Alcance](#5-alcance)
8. [6. Requerimientos del sistema](#6-requerimientos-del-sistema)
9. [7. Restricciones](#7-restricciones)
10. [8. Supuestos](#8-supuestos)
11. [9. Resultados esperados](#9-resultados-esperados)
12. [10. Metodologia de implementacion](#10-metodologia-de-implementacion)
13. [11. Actores claves](#11-actores-claves)
14. [12. Papel y responsabilidades del personal](#12-papel-y-responsabilidades-del-personal)
15. [13. Plan de monitoreo y evaluacion](#13-plan-de-monitoreo-y-evaluacion)
16. [14. Cronograma del proyecto](#14-cronograma-del-proyecto)
17. [15. Hitos de entregables](#15-hitos-de-entregables)
18. [II. Presupuesto](#ii-presupuesto)
19. [1. Planteamiento de aplicacion del presupuesto](#1-planteamiento-de-aplicacion-del-presupuesto)
20. [2. Presupuesto](#2-presupuesto)
21. [3. Analisis de Factibilidad](#3-analisis-de-factibilidad)
22. [4. Evaluacion Financiera](#4-evaluacion-financiera)
23. [Anexo 01 - Requerimientos del Sistema EPIS Analytics](#anexo-01---requerimientos-del-sistema-epis-analytics)

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Resumen Ejecutivo

| Campo | Descripcion |
| :- | :- |
| **Nombre del Proyecto propuesto** | **EPIS Analytics: Sistema web de analitica social para estudiantes de la Escuela Profesional de Ingenieria de Sistemas, Tacna, 2026** |
| **Proposito del Proyecto y Resultados esperados** | Desarrollar una plataforma web de inteligencia de negocios que centralice y visualice indicadores simulados de publicaciones, alcance e interacciones de estudiantes EPIS en LinkedIn, Instagram y YouTube. Se espera obtener login funcional, dashboard personal, dashboard global, filtros por red social, graficos, API REST, base de datos local, documentacion tecnica y propuesta de infraestructura cloud con analisis de costos. |
| **Poblacion Objetivo** | Estudiantes de la Escuela Profesional de Ingenieria de Sistemas de la Universidad Privada de Tacna, docentes y responsables academicos vinculados al seguimiento de indicadores digitales academicos. |
| **Monto de Inversion estimado** | **S/ 4,280.00** para desarrollo academico del prototipo. Infraestructura cloud base estimada: **USD 9.192 mensuales**. |
| **Duracion del Proyecto** | **2 meses**, equivalentes a 8 semanas academicas de analisis, diseno, desarrollo, pruebas y documentacion. |

EPIS Analytics propone resolver la falta de una vista consolidada de indicadores digitales estudiantiles mediante un sistema web separado en frontend Angular y backend FastAPI. La propuesta utiliza datos simulados para proteger el alcance academico del proyecto, pero deja preparada una arquitectura que puede evolucionar hacia datos reales, base de datos productiva y despliegue cloud.

El proyecto se sustenta en los informes FD01 a FD05, donde se documentaron factibilidad, vision, requerimientos, arquitectura e informe final. Esta propuesta consolida el planteamiento formal del proyecto, sus beneficios, alcance, recursos, cronograma, presupuesto y criterios de evaluacion.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# I. Propuesta narrativa

## 1. Planteamiento del Problema

La Escuela Profesional de Ingenieria de Sistemas no cuenta con una herramienta centralizada que permita visualizar indicadores de actividad digital estudiantil en redes sociales relevantes. Actualmente, la informacion que podria mostrar participacion academica, profesional o comunicacional se encuentra dispersa en plataformas como LinkedIn, Instagram y YouTube.

Esta situacion genera los siguientes problemas:

| Problema identificado | Consecuencia |
| :- | :- |
| Informacion distribuida entre varias redes sociales | Dificulta comparar indicadores y obtener una vista global |
| Ausencia de dashboard personal | El estudiante no cuenta con una vista clara de sus indicadores simulados |
| Ausencia de dashboard global | El docente o responsable academico no puede observar tendencias agregadas |
| Falta de filtros por red social | No se puede analizar comportamiento por LinkedIn, Instagram o YouTube |
| Datos no segmentados por ciclo academico | Se pierde la lectura academica de estudiantes de ciclos I al X |
| Acceso sin mecanismo de autenticacion | No se controla la consulta de vistas privadas |

Por ello, se propone el desarrollo de un sistema web de analitica social que permita centralizar indicadores, proteger el acceso y presentar resultados mediante graficos utiles para la toma de decisiones academicas.

## 2. Justificacion del proyecto

La propuesta se justifica porque combina el enfoque de inteligencia de negocios con una necesidad academica concreta: analizar informacion de manera clara, visual y segmentada. Aunque el prototipo trabaja con datos simulados, permite validar el flujo completo de una solucion real: autenticacion, consulta de datos, filtros, visualizacion y evaluacion de infraestructura.

El proyecto aporta al curso de Inteligencia de negocios porque permite aplicar:

| Aspecto | Aplicacion en EPIS Analytics |
| :- | :- |
| Analisis de datos | Indicadores de publicaciones, alcance e interacciones |
| Visualizacion | Dashboards y graficos con ECharts |
| Arquitectura de software | Separacion Angular + FastAPI + servicios + repositorios |
| Gestion de requerimientos | Historias de usuario en GitHub Issues |
| Infraestructura como codigo | Modulo Terraform para propuesta cloud |
| Control de costos | Estimacion con Infracost |
| Pruebas | Pytest, pruebas Angular y validacion Terraform |

Asimismo, EPIS Analytics se alinea con una cultura institucional de mejora continua y uso de informacion para apoyar la gestion academica.

## 3. Objetivo general

Desarrollar un sistema web de inteligencia de negocios para analizar indicadores simulados de actividad social de estudiantes EPIS, permitiendo consultar metricas personales y globales por red social, con autenticacion basica, graficos, documentacion tecnica y propuesta de infraestructura cloud de bajo costo.

### Objetivos especificos

| ID | Objetivo especifico |
| :-: | :- |
| OE-01 | Definir la factibilidad tecnica, economica, operativa, social, legal y ambiental del proyecto |
| OE-02 | Construir una API REST con FastAPI para autenticacion, estudiantes y dashboards |
| OE-03 | Implementar una interfaz Angular con login, dashboard personal y dashboard global |
| OE-04 | Generar datos simulados para estudiantes EPIS de ciclos I al X |
| OE-05 | Incorporar filtros por red social para LinkedIn, Instagram, YouTube y vista general |
| OE-06 | Visualizar indicadores mediante graficos dinamicos |
| OE-07 | Proteger rutas privadas mediante token |
| OE-08 | Validar funcionalidad con pruebas automatizadas |
| OE-09 | Declarar infraestructura propuesta con Terraform y estimar costos con Infracost |
| OE-10 | Documentar vision, requerimientos, arquitectura, informe final y propuesta del proyecto |

## 4. Beneficios

### Beneficios academicos

| Beneficio | Descripcion |
| :- | :- |
| Mejora de seguimiento | Permite observar indicadores personales y globales de estudiantes |
| Apoyo a decisiones | Presenta informacion organizada para docentes o responsables academicos |
| Comparacion por redes | Facilita analizar diferencias entre LinkedIn, Instagram y YouTube |
| Segmentacion por ciclos | Considera estudiantes desde ciclo I hasta ciclo X |

### Beneficios tecnicos

| Beneficio | Descripcion |
| :- | :- |
| Arquitectura separada | Angular y FastAPI pueden evolucionar de manera independiente |
| Mantenibilidad | Capas de modelos, repositorios, servicios, API y vistas |
| Testeabilidad | Pruebas backend, frontend y validacion Terraform |
| Escalabilidad futura | Posible migracion de SQLite a PostgreSQL y datos reales |
| Control de costos | Infraestructura propuesta evaluada antes de desplegar |

### Beneficios para estudiantes

| Beneficio | Descripcion |
| :- | :- |
| Vista personal | Cada estudiante puede observar sus indicadores simulados |
| Interpretacion visual | Los graficos reducen complejidad de lectura |
| Reflexion profesional | Las metricas pueden orientar mejoras en presencia digital academica |

## 5. Alcance

El alcance de la propuesta comprende:

- Desarrollo de backend FastAPI.
- Desarrollo de frontend Angular.
- Login basico con usuario, contrasena y token.
- Dashboard personal para un estudiante autenticado.
- Dashboard global con indicadores agregados.
- Filtros por red social en vista personal y global.
- Datos simulados de LinkedIn, Instagram y YouTube.
- Consideracion de ciclos academicos I al X.
- Persistencia local en SQLite.
- Graficos con ECharts.
- Pruebas unitarias y de rutas API.
- Build y pruebas frontend.
- Modulo Terraform para infraestructura AWS propuesta.
- Analisis de costos con Infracost.
- Documentacion en Markdown, PDF, GitHub Wiki e informes FD01-FD06.

Fuera del alcance actual:

- Consumo real de APIs de redes sociales.
- Despliegue real en AWS mediante `terraform apply`.
- Integracion real con Power BI.
- Gestion avanzada de usuarios, roles y permisos.
- Almacenamiento de datos personales reales sin consentimiento formal.

## 6. Requerimientos del sistema

### Requerimientos funcionales

| ID | Requerimiento | Prioridad |
| :-: | :- | :-: |
| RF-01 | Iniciar sesion con usuario, contrasena y token | Alta |
| RF-02 | Consultar dashboard personal del estudiante autenticado | Alta |
| RF-03 | Filtrar dashboard personal por red social | Alta |
| RF-04 | Consultar dashboard global con indicadores agregados | Alta |
| RF-05 | Filtrar dashboard global por LinkedIn, Instagram o YouTube | Alta |
| RF-06 | Consultar lista de estudiantes disponibles | Media |
| RF-07 | Proteger rutas privadas mediante token valido | Alta |
| RF-08 | Visualizar metricas mediante graficos | Alta |
| RF-09 | Validar infraestructura y costos con Terraform e Infracost | Media |

### Requerimientos no funcionales

| ID | Requerimiento | Prioridad |
| :-: | :- | :-: |
| RNF-01 | Seguridad: rutas privadas protegidas por token | Alta |
| RNF-02 | Usabilidad: interfaz clara para login y dashboards | Alta |
| RNF-03 | Rendimiento: consultas aceptables para prototipo academico | Media |
| RNF-04 | Mantenibilidad: organizacion por capas y componentes | Alta |
| RNF-05 | Portabilidad: ejecucion local y proyeccion cloud | Media |
| RNF-06 | Testeabilidad: pruebas backend, frontend y Terraform | Alta |
| RNF-07 | Escalabilidad funcional: preparada para nuevas redes o datos reales | Media |
| RNF-08 | Control de costos: estimacion previa al despliegue | Media |

## 7. Restricciones

| Restriccion | Descripcion |
| :- | :- |
| Datos simulados | El prototipo no consume datos reales de redes sociales |
| Redes iniciales | Solo considera LinkedIn, Instagram y YouTube |
| Persistencia local | SQLite es suficiente para prototipo, no para uso productivo masivo |
| Seguridad academica | El token implementado es adecuado para prototipo, no reemplaza una estrategia productiva completa |
| Despliegue cloud | Terraform se valida, pero no se ejecuta `terraform apply` en esta etapa |
| Presupuesto | Se prioriza infraestructura de bajo costo |
| Tiempo | El desarrollo se ajusta a un periodo academico de aproximadamente 8 semanas |

## 8. Supuestos

| Supuesto | Impacto |
| :- | :- |
| Los datos simulados representan de manera suficiente el flujo analitico | Permite validar la solucion sin depender de APIs externas |
| Los usuarios principales son estudiantes y responsables academicos EPIS | Orienta el diseno de vistas y filtros |
| El entorno local cuenta con Python, Node.js y dependencias necesarias | Permite ejecutar backend, frontend y pruebas |
| La infraestructura cloud sera evaluada antes de desplegarse | Reduce riesgo de costos inesperados |
| El sistema puede evolucionar por fases | Permite dejar fuera datos reales y Power BI para una etapa posterior |

## 9. Resultados esperados

Al finalizar el proyecto se espera contar con:

| Resultado | Evidencia esperada |
| :- | :- |
| API REST funcional | Endpoints `/api/health`, `/api/estudiantes`, `/api/auth/login`, `/api/dashboard/perfil`, `/api/dashboard/global` |
| Frontend Angular funcional | Login, vista personal y vista global |
| Datos simulados cargados | SQLite con publicaciones y usuarios demostrativos |
| Filtros por red social | Opcion Todas, LinkedIn, Instagram y YouTube |
| Graficos analiticos | Visualizaciones ECharts |
| Seguridad basica | Token, guard e interceptor |
| Pruebas automatizadas | Pytest y pruebas Angular |
| Infraestructura declarada | Archivos Terraform en `infra/terraform` |
| Analisis de costos | Infracost con costo base mensual estimado |
| Documentacion completa | FD01, FD02, FD03, FD04, FD05, FD06, README y Wiki |

## 10. Metodologia de implementacion

Se propone una metodologia incremental, organizada por fases cortas:

| Fase | Actividad principal | Producto |
| :-: | :- | :- |
| 1 | Analisis del problema y factibilidad | FD01 |
| 2 | Vision del producto y RoadMap | FD02 y Wiki |
| 3 | Especificacion de requerimientos | FD03 e Issues GitHub |
| 4 | Implementacion base por capas | Modelos, repositorios, servicios y pruebas |
| 5 | Desarrollo API REST | FastAPI y endpoints |
| 6 | Desarrollo frontend | Angular, login y dashboards |
| 7 | Arquitectura e infraestructura | FD04, diagramas y Terraform |
| 8 | Validacion y cierre documental | FD05 y FD06 |

El enfoque incremental permite validar cada bloque antes de avanzar, reduciendo riesgos tecnicos y facilitando la trazabilidad entre requerimientos, codigo, pruebas y documentos.

## 11. Actores claves

| Actor | Rol dentro del proyecto |
| :- | :- |
| Estudiante EPIS | Usuario que consulta sus indicadores personales |
| Docente EPIS | Usuario que analiza indicadores globales |
| Responsable academico | Interesado en seguimiento agregado y toma de decisiones |
| Equipo del proyecto | Responsable de analisis, desarrollo, pruebas y documentacion |
| Docente del curso | Revisor academico de entregables |
| Equipo tecnico futuro | Encargado de mantenimiento y posible despliegue |

## 12. Papel y responsabilidades del personal

| Responsable | Papel | Responsabilidades |
| :- | :- | :- |
| Enzo Leonel Laqui Luyo | Integrante del equipo | Analisis, documentacion, soporte de implementacion y validacion |
| Steven Christopher YIZUKA BALDEÓN | Integrante del equipo | Analisis, documentacion, soporte de implementacion y validacion |
| Mag. Patrick Cuadros Quiroga | Docente tutor | Revision academica, orientacion metodologica y evaluacion |
| Equipo del proyecto | Desarrollo integral | Backend, frontend, pruebas, infraestructura y documentos |
| Usuarios EPIS | Validacion funcional | Revisar si las vistas y filtros responden al caso academico |

## 13. Plan de monitoreo y evaluacion

El monitoreo se realizara a partir de indicadores tecnicos, funcionales y documentales:

| Indicador | Metodo de verificacion | Meta |
| :- | :- | :-: |
| Requerimientos implementados | Comparacion RF-01 a RF-09 | 100% del alcance base |
| Pruebas backend | `python -m pytest -q` | Pruebas exitosas |
| Build frontend | `npm run build` | Compilacion correcta |
| Pruebas frontend | `npm test -- --watch=false` | Pruebas exitosas |
| Validacion Terraform | `terraform validate` | Configuracion valida |
| Estimacion de costos | `infracost breakdown` | Costo base identificado |
| Documentacion | Revision FD01-FD06 | Informes completos |
| Trazabilidad | Relacion entre Issues, SRS y pruebas | Historias HU-01 a HU-09 documentadas |

### Criterios de evaluacion

| Criterio | Condicion de aceptacion |
| :- | :- |
| Funcionalidad | Login, dashboards y filtros operan correctamente |
| Usabilidad | Las vistas permiten lectura clara de indicadores |
| Seguridad | Las rutas privadas requieren token |
| Mantenibilidad | El codigo conserva separacion por capas |
| Factibilidad | El costo estimado y la infraestructura son sustentables |
| Documentacion | Los documentos entregables mantienen coherencia entre si |

## 14. Cronograma del proyecto

| Semana | Actividad | Entregable |
| :-: | :- | :- |
| 1 | Identificacion del problema, alcance y factibilidad | FD01 |
| 2 | Vision del producto, usuarios y RoadMap | FD02 y Wiki |
| 3 | Historias de usuario, criterios y escenarios | FD03 |
| 4 | Modelos, repositorios, servicios y pruebas | Codigo backend base |
| 5 | API FastAPI, endpoints y autenticacion | Backend web |
| 6 | Frontend Angular, login y dashboards | Aplicacion web |
| 7 | Diagramas, arquitectura e infraestructura | FD04 y Terraform |
| 8 | Informe final, propuesta y validaciones | FD05 y FD06 |

## 15. Hitos de entregables

| Hito | Entregable | Criterio de cierre |
| :-: | :- | :- |
| H1 | Informe de factibilidad | Viabilidad y costos documentados |
| H2 | Documento de vision | Usuarios, caracteristicas, Wiki y RoadMap definidos |
| H3 | Documento SRS | Historias, criterios y escenarios documentados |
| H4 | Prototipo funcional | Backend y frontend ejecutables |
| H5 | Arquitectura de software | Diagramas de codigo, base de datos e infraestructura generados |
| H6 | Validacion tecnica | Pruebas y build ejecutados correctamente |
| H7 | Informe final | Consolidacion de resultados y anexos |
| H8 | Propuesta del proyecto | Planteamiento formal de ejecucion y presupuesto |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# II. Presupuesto

## 1. Planteamiento de aplicacion del presupuesto

El presupuesto se plantea para un prototipo academico. La mayor parte del costo corresponde al esfuerzo del equipo de desarrollo y documentacion. Las herramientas utilizadas no generan costos de licencia directa, ya que Angular, FastAPI, SQLite, Terraform, Infracost CLI, Pytest y ECharts cuentan con alternativas de uso sin pago inicial para el alcance del curso.

La infraestructura cloud se presenta como propuesta estimada, no como gasto ejecutado. El objetivo es demostrar que el proyecto puede proyectarse a un despliegue basico en AWS manteniendo costos controlados.

## 2. Presupuesto

### 2.1. Costos de desarrollo

| Concepto | Costo estimado |
| :- | :-: |
| Recursos generales del proyecto | S/ 180.00 |
| Costos operativos directos | S/ 0.00 |
| Ambiente base local | S/ 0.00 |
| Personal del equipo del proyecto | S/ 4,100.00 |
| **Total estimado de desarrollo** | **S/ 4,280.00** |

### 2.2. Costos cloud estimados

| Recurso | Descripcion | Costo mensual estimado |
| :- | :- | :-: |
| EC2 t3.micro | Backend FastAPI | USD 7.592 |
| EBS gp3 20 GB | Disco de instancia | USD 1.600 |
| S3 | Frontend Angular estatico | Variable por uso |
| CloudFront | Distribucion del frontend | Variable por uso |
| Security Group | Control de acceso | USD 0.00 |
| **Total base mensual** | Infraestructura minima | **USD 9.192** |

Con tipo de cambio referencial de S/ 3.75:

| Periodo | Costo USD | Costo aproximado en soles |
| :-: | :-: | :-: |
| 1 mes | USD 9.192 | S/ 34.47 |
| 6 meses | USD 55.15 | S/ 206.81 |
| 12 meses | USD 110.30 | S/ 413.63 |

## 3. Analisis de Factibilidad

| Dimension | Evaluacion | Resultado |
| :- | :- | :-: |
| Tecnica | Tecnologias disponibles, conocidas y compatibles con el alcance | Factible |
| Economica | Costo de desarrollo moderado e infraestructura base baja | Factible |
| Operativa | Flujo simple para login, vista personal, vista global y filtros | Factible |
| Social | Apoya analisis academico y cultura de datos | Factible |
| Legal | Se usan datos simulados; datos reales requieren revision posterior | Factible para prototipo |
| Ambiental | Infraestructura minima y controlada por Terraform | Factible |

## 4. Evaluacion Financiera

La evaluacion financiera considera que el proyecto es academico y no genera ingresos directos en esta etapa. Su valor se mide por beneficios formativos, mejora de trazabilidad documental, validacion de arquitectura moderna y posibilidad de evolucionar hacia un sistema real.

| Elemento | Evaluacion |
| :- | :- |
| Inversion estimada de desarrollo | S/ 4,280.00 |
| Costo cloud base mensual | USD 9.192 |
| Costo cloud anual referencial | S/ 413.63 |
| Retorno esperado | Valor academico, tecnico y documental |
| Riesgo financiero | Bajo, si no se ejecuta infraestructura sin validacion previa |
| Control financiero | Terraform e Infracost permiten estimar antes de desplegar |

La propuesta es financieramente viable para el entorno academico porque utiliza herramientas de bajo costo, infraestructura minima y datos simulados. Para una version productiva, la evaluacion deberia ampliarse con usuarios reales, volumen de datos, seguridad, soporte, monitoreo y costos de mantenimiento.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Anexo 01 - Requerimientos del Sistema EPIS Analytics

## Historias de usuario asociadas

| ID | Historia | Referencia |
| :-: | :- | :- |
| HU-01 | Autenticacion de estudiante | GitHub Issue #1 |
| HU-02 | Consulta de dashboard personal | GitHub Issue #2 |
| HU-03 | Filtro por red social en dashboard personal | GitHub Issue #3 |
| HU-04 | Consulta de dashboard global | GitHub Issue #4 |
| HU-05 | Filtro por red social en dashboard global | GitHub Issue #5 |
| HU-06 | Consulta de lista de estudiantes | GitHub Issue #6 |
| HU-07 | Proteccion de rutas privadas con token | GitHub Issue #7 |
| HU-08 | Visualizacion de metricas con graficos | GitHub Issue #8 |
| HU-09 | Validacion de infraestructura y costos | GitHub Issue #9 |

## Requerimientos funcionales resumidos

| ID | Requerimiento | Estado esperado |
| :-: | :- | :-: |
| RF-01 | Login con usuario, contrasena y token | Implementado |
| RF-02 | Dashboard personal | Implementado |
| RF-03 | Filtro por red social en dashboard personal | Implementado |
| RF-04 | Dashboard global | Implementado |
| RF-05 | Filtro por red social en dashboard global | Implementado |
| RF-06 | Lista de estudiantes | Implementado |
| RF-07 | Proteccion de rutas privadas | Implementado |
| RF-08 | Graficos de metricas | Implementado |
| RF-09 | Terraform e Infracost | Implementado |

## Evidencias tecnicas relacionadas

| Evidencia | Archivo o comando |
| :- | :- |
| Backend API | `api/main.py`, `api/routes/auth_routes.py`, `api/routes/dashboard_routes.py` |
| Frontend Angular | `epis-web/src/app` |
| Servicios de negocio | `services/auth_service.py`, `services/analytics_service.py` |
| Repositorios | `repositories/sqlite_publicacion_repository.py`, `repositories/sqlite_usuario_repository.py` |
| Base de datos | `epis_data.db` |
| Infraestructura | `infra/terraform/main.tf` |
| Pruebas backend | `python -m pytest -q` |
| Build frontend | `npm run build` |
| Pruebas frontend | `npm test -- --watch=false` |
| Validacion Terraform | `terraform validate` |
| Costos | `infracost breakdown` |

## Documentos vinculados

| Documento | Archivo |
| :- | :- |
| Informe de Factibilidad | `FD01-Informe-Factibilidad.md` |
| Documento de Vision | `FD02-Informe-Vision.md` |
| Especificacion de Requerimientos | `FD03-EPIS-Informe-Especificacion-Requerimientos.md` |
| Arquitectura de Software | `FD04-EPIS-Informe-Arquitectura-de-Software.md` |
| Informe Final | `FD05-EPIS-Informe-ProyectoFinal.md` |
| Propuesta del Proyecto | `FD06-EPIS-PropuestaProyecto.md` |
