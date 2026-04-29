# Infraestructura Terraform - EPIS Analytics

Este directorio contiene una propuesta de infraestructura como codigo para desplegar el prototipo EPIS Analytics en AWS.

La configuracion esta pensada para sustentar el analisis de factibilidad y costos del informe FD01. No debe ejecutarse `terraform apply` sin revisar credenciales, region, AMI, llave SSH, dominio, presupuesto y politicas de seguridad.

## Arquitectura propuesta

- Amazon EC2 `t3.micro` para ejecutar el backend FastAPI.
- Volumen raiz EBS `gp3` de 20 GB.
- Security Group para HTTP, API y SSH restringible.
- Bucket S3 privado para publicar el build estatico de Angular.
- CloudFront como CDN para exponer el frontend.

## Comandos de validacion

```bash
terraform init
terraform fmt -recursive
terraform validate
terraform plan -out=tfplan
```

## Analisis de costos

Con Infracost instalado y autenticado:

```bash
infracost breakdown --path . --terraform-var frontend_bucket_name=epis-analytics-dev-frontend-demo
```

El costo esperado para el escenario academico de bajo consumo es aproximadamente:

| Recurso | Costo mensual estimado |
| :- | -: |
| EC2 t3.micro Linux | USD 7.59 |
| EBS gp3 20 GB | USD 1.60 |
| S3 Standard | Variable segun almacenamiento y solicitudes |
| CloudFront bajo consumo | Variable segun transferencia y solicitudes |
| **Total base estimado por Infracost** | **USD 9.19** |

Validacion local realizada:

```text
Terraform v1.14.9
Infracost v0.10.44
terraform init: correcto
terraform validate: correcto
infracost breakdown --path . --terraform-var frontend_bucket_name=epis-analytics-dev-frontend-demo: USD 9.19/mes de costo base
```

## Advertencia

Esta configuracion es una base academica. Para produccion se recomienda:

- Usar HTTPS real con ACM y dominio propio.
- Restringir SSH a una IP especifica.
- Usar base de datos administrada o persistencia separada.
- Configurar monitoreo, backups y rotacion de secretos.
- Revisar costos con `infracost breakdown` antes de aplicar cambios.
