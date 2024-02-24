# filtro.py

import sys

# Lista de precios de productos (ejemplo)
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar_productos(precios, umbral, operacion='mayor'):
    try:
        umbral = int(umbral)
    except ValueError:
        print("El umbral debe ser un número entero válido")
        return {}

    productos_filtrados = {p: v for p, v in precios.items() if (v > umbral) if operacion == 'mayor' else (v < umbral)}
    return productos_filtrados

if len(sys.argv) == 2:
    umbral = sys.argv[1]
    productos = filtrar_productos(precios, umbral)
    if productos:
        print(f"Los productos mayores al umbral son: {', '.join(productos.keys())}")
elif len(sys.argv) == 3:
    umbral, operacion = sys.argv[1], sys.argv[2]
    productos = filtrar_productos(precios, umbral, operacion)
    if productos:
        print(f"Los productos {operacion} al umbral son: {', '.join(productos.keys())}")
