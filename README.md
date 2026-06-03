

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

Este proyecto es un ejemplo de análisis de ventas de un local comercial, armado según el trabajo práctico de Gestión Colaborativa, Control de Versiones y Organización Empresarial.

## Escenario elegido

Escenario B — Análisis de Ventas de una Pequeña Empresa.

## Objetivo
- Usar los datos de `datos/ventas_sample.csv`
- Implementar un script reproducible para analizar las ventas por producto y por mes
- Generar un resumen en texto y un gráfico de barras en `resultados/`
- Mantener una estructura clara de carpetas para Git y para un flujo de trabajo en equipo

## Estructura del proyecto
- `datos/ventas_sample.csv` — fuente de datos de ventas
- `scripts/analyze_sales.py` — script de análisis de ventas
- `resultados/ventas_resumen.txt` — resumen generado al ejecutar el script
- `resultados/ventas_grafico.png` — gráfico de barras generado al ejecutar el script
- `.gitignore` — exclusiones del repositorio

## Descripción del dataset utilizado

- Archivo: `datos/ventas_sample.csv`
- Formato: CSV (valores separados por comas)
- Registros: 115
- Período: enero–abril 2024

| Columna | Tipo | Descripción |
|---|---|---|
| `id` | int | Identificador del registro |
| `fecha_venta` | date (YYYY-MM-DD) | Fecha de la transacción |
| `producto` | string | Nombre del producto vendido |
| `cantidad` | int | Unidades vendidas |
| `precio` | float | Precio unitario |

## Instrucciones para ejecutar el script

1. Clonar el repositorio en Google Colab:
   ```
   !git clone https://github.com/santiaguero91/UTN-TUPaD-OE-TPN2.git
   %cd UTN-TUPaD-OE-TPN2
   ```
2. Ejecutar el script desde la raíz del proyecto:
   ```
   !python scripts/analyze_sales.py
   ```
3. Revisar los resultados generados en la carpeta `resultados/`.

## Resultados esperados
- Total de ventas del período
- Promedio de venta por transacción
- Producto más vendido por unidades
- Totales de ventas agrupados por mes
- Gráfico de barras con la evolución mensual de ventas (`resultados/ventas_grafico.png`)
