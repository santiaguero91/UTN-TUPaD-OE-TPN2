

# Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial (Git, GitHub y Jira)

## Datos institucionales

| | |
|---|---|
| **Institución** | Universidad Tecnológica Nacional — Tecnicatura Universitaria en Programación (TUP) — Modalidad a Distancia |
| **Cátedra** | Organización Empresarial |
| **Cuerpo Docente** | Prof. Gabriela Martínez (Titular), Prof. Mario Raúl López, Prof. Andrea Ramos, Prof. Carolina Bruno (Adjuntos) |
| **Año Lectivo** | 2026 |

## Alumno

Santiago Nicolás Aguero Urquiza

---


# Proyecto de Ventas en Local

Este proyecto es un ejemplo de análisis de ventas diarias en un local comercial, armado según el trabajo práctico de Gestión Colaborativa, Control de Versiones y Organización Empresarial.

## Objetivo
- Usar los datos de `datos/ventas_sample.csv`
- Implementar un script reproducible para analizar las ventas
- Generar resultados en `resultados/ventas_resumen.txt`
- Mantener una estructura clara de carpetas para Git y para un flujo de trabajo en equipo

## Estructura del proyecto
- `datos/ventas_sample.csv` — fuente de datos de ventas
- `scripts/analyze_sales.py` — script de análisis de ventas
- `resultados/` — salida generada con el resumen de ventas
- `Jira-issues.md` — ejemplo de tareas/Issues para Jira
- `.gitignore` — exclusiones recomendadas para el repositorio

## Descripción del dataset utilizado

- Archivo: `datos/ventas_sample.csv`
- Formato: CSV (valores separados por comas)
- Columnas:
  | Columna / Tipo / Descripción 
  | `id`: int / id del registro 
  | `sales_date`: Date (YYYY-MM-DD) / Fecha correspondiente a la venta 
  | `sales_amount`: int / Monto total de ventas del día


  ## Instrucciones para ejecutar el script 
1. Clonar o descargar el repositorio.
2. Copiar `ventas_sample.csv` a la carpeta `datos/` si no está allí.
3. Ejecutar desde la raíz del proyecto:
   ```bash
   python scripts/analyze_sales.py
   ```
4. Revisar el archivo `resultados/ventas_resumen.txt` para ver el resumen generado.

## Resultados esperados
- Total de ventas
- Promedio diario de ventas
- Día con mayor y menor venta
- Totales por mes

