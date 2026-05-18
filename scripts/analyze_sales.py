from pathlib import Path
import csv
from collections import defaultdict


def load_sales_data(csv_path):
    sales = []
    with csv_path.open(newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                date = row['sales_date']
                amount = float(row['sales_amount'])
                sales.append((date, amount))
            except (KeyError, ValueError):
                continue
    return sales


def summarize_sales(sales):
    total = sum(amount for _, amount in sales)
    count = len(sales)
    average = total / count if count else 0.0

    best_day = max(sales, key=lambda item: item[1]) if sales else (None, 0)
    worst_day = min(sales, key=lambda item: item[1]) if sales else (None, 0)

    sales_by_month = defaultdict(float)
    for date, amount in sales:
        month = date[:7]
        sales_by_month[month] += amount

    return {
        'total': total,
        'count': count,
        'average': average,
        'best_day': best_day,
        'worst_day': worst_day,
        'sales_by_month': dict(sorted(sales_by_month.items())),
    }


def write_summary(summary, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as f:
        f.write('Resumen de ventas del local\n')
        f.write('==========================\n')
        f.write(f'Total de ventas: ${summary["total"]:,.2f}\n')
        f.write(f'Cantidad de días: {summary["count"]}\n')
        f.write(f'Venta promedio diaria: ${summary["average"]:,.2f}\n')
        f.write(f'Día con mayor venta: {summary["best_day"][0]} (${summary["best_day"][1]:,.2f})\n')
        f.write(f'Día con menor venta: {summary["worst_day"][0]} (${summary["worst_day"][1]:,.2f})\n')
        f.write('\nVentas por mes:\n')
        for month, value in summary['sales_by_month'].items():
            f.write(f'  {month}: ${value:,.2f}\n')


if __name__ == '__main__':
    repo_root = Path(__file__).resolve().parent.parent
    input_path = repo_root / 'datos' / 'ventas_sample.csv'
    output_path = repo_root / 'resultados' / 'ventas_resumen.txt'

    if not input_path.exists():
        raise FileNotFoundError(
            f'No se encontró el archivo de datos: {input_path}\n'
            'Asegúrate de copiar ventas_sample.csv a la carpeta datos/.'
        )

    sales = load_sales_data(input_path)
    summary = summarize_sales(sales)
    write_summary(summary, output_path)
    print(f'Resumen generado en: {output_path}')
