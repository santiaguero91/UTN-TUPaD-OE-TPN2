# matplotlib.use('Agg') debe llamarse antes de importar pyplot porque Google Colab
# no tiene backend de pantalla interactivo; Agg guarda el grafico directo a archivo
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from pathlib import Path
import csv
from collections import defaultdict


# Carga y valida los registros de ventas desde el archivo CSV.
# Se usa try/except por fila para que datos malformados no abortan el analisis completo.
def load_sales_data(csv_path):
    sales = []
    with csv_path.open(newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                fecha = row['fecha_venta']
                producto = row['producto']
                cantidad = int(row['cantidad'])
                precio = float(row['precio'])
                # El importe se calcula aqui para no repetir la multiplicacion en cada analisis
                importe = cantidad * precio
                sales.append((fecha, producto, cantidad, precio, importe))
            except (KeyError, ValueError):
                continue
    return sales


# Calcula totales, promedios, producto mas vendido y ventas por mes.
# El "mas vendido" se determina por unidades, no por importe, para no favorecer
# productos de precio alto con pocas ventas.
def summarize_sales(sales):
    total = sum(s[4] for s in sales)
    count = len(sales)
    average = total / count if count else 0.0

    # defaultdict evita verificar si la clave existe antes de acumular cada valor
    ventas_por_producto = defaultdict(float)
    cantidad_por_producto = defaultdict(int)
    for _, producto, cantidad, _, importe in sales:
        ventas_por_producto[producto] += importe
        cantidad_por_producto[producto] += cantidad

    producto_mas_vendido = max(cantidad_por_producto, key=lambda p: cantidad_por_producto[p])

    ventas_por_mes = defaultdict(float)
    for fecha, _, _, _, importe in sales:
        mes = fecha[:7]
        ventas_por_mes[mes] += importe

    return {
        'total': total,
        'count': count,
        'average': average,
        'producto_mas_vendido': producto_mas_vendido,
        'cantidad_producto_mas_vendido': cantidad_por_producto[producto_mas_vendido],
        # Se ordena descendente para mostrar primero los productos mas rentables
        'ventas_por_producto': dict(sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True)),
        'ventas_por_mes': dict(sorted(ventas_por_mes.items())),
    }


# Escribe el resumen generado en un archivo de texto dentro de /resultados.
# mkdir con parents=True crea la carpeta si no existe en el entorno de ejecucion (ej. Colab tras clonar).
def write_summary(summary, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as f:
        f.write('Resumen de ventas del local\n')
        f.write('==========================\n')
        f.write(f'Total de ventas: ${summary["total"]:,.2f}\n')
        f.write(f'Cantidad de registros: {summary["count"]}\n')
        f.write(f'Venta promedio por registro: ${summary["average"]:,.2f}\n')
        f.write(f'Producto más vendido: {summary["producto_mas_vendido"]} '
                f'({summary["cantidad_producto_mas_vendido"]} unidades)\n')
        f.write('\nVentas por mes:\n')
        for mes, valor in summary['ventas_por_mes'].items():
            f.write(f'  {mes}: ${valor:,.2f}\n')
        f.write('\nVentas por producto (de mayor a menor ingreso):\n')
        for prod, valor in summary['ventas_por_producto'].items():
            f.write(f'  {prod}: ${valor:,.2f}\n')


# Genera un grafico de barras con la evolucion mensual de ventas y lo guarda en /resultados.
# Se usa barras en lugar de linea porque los meses son categorias discretas, no un eje continuo.
def generate_chart(summary, output_path):
    meses = list(summary['ventas_por_mes'].keys())
    # Se convierte a miles para que el eje Y sea legible sin notacion cientifica
    valores = [v / 1000 for v in summary['ventas_por_mes'].values()]

    _, ax = plt.subplots(figsize=(10, 5))
    ax.bar(meses, valores, color='steelblue')
    ax.set_title('Evolución de ventas mensuales', fontsize=14)
    ax.set_xlabel('Mes')
    ax.set_ylabel('Ventas (miles de $)')
    ax.set_ylim(0, max(valores) * 1.2)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


# Bloque principal de ejecucion: carga, procesa y exporta los datos de ventas.
# Path(__file__) resuelve rutas desde la ubicacion del script para que funcione
# desde cualquier directorio (ej: !python scripts/analyze_sales.py desde la raiz del repo en Colab).
if __name__ == '__main__':
    repo_root = Path(__file__).resolve().parent.parent
    input_path = repo_root / 'datos' / 'ventas_sample.csv'
    output_txt = repo_root / 'resultados' / 'ventas_resumen.txt'
    output_chart = repo_root / 'resultados' / 'ventas_grafico.png'

    if not input_path.exists():
        raise FileNotFoundError(
            f'No se encontró el archivo de datos: {input_path}\n'
            'Asegurate de que ventas_sample.csv esté en la carpeta datos/.'
        )

    sales = load_sales_data(input_path)
    summary = summarize_sales(sales)
    write_summary(summary, output_txt)
    generate_chart(summary, output_chart)
    print(f'Resumen generado en: {output_txt}')
    print(f'Gráfico generado en: {output_chart}')
