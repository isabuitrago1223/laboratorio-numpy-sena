# Importar la biblioteca NumPy
import numpy as np


# Función que genera y analiza las ventas
def analizar_ventas():

    # Generar una matriz de 5 productos y 4 semanas
    # con valores aleatorios entre 100 y 1000
    ventas = np.random.randint(100, 1001, (5, 4))

    # Mostrar la matriz de ventas
    print("\n------MATRIZ DE VENTAS ------")
    print(ventas)

    # Calcular el total vendido por cada producto
    total_productos = np.sum(ventas, axis=1)

    # Calcular el total vendido por cada semana
    total_semanas = np.sum(ventas, axis=0)

    # Encontrar el producto con mayores ventas
    mejor_producto = np.argmax(total_productos) + 1

    # Mostrar resultados
    print("\n------REPORTE ------")

    print("\nTotal de ventas por producto:")
    for i, total in enumerate(total_productos, start=1):
        print(f"Producto {i}: ${total}")

    print("\nTotal de ventas por semana:")
    for i, total in enumerate(total_semanas, start=1):
        print(f"Semana {i}: ${total}")

    print(f"\nProducto con mayores ventas: Producto {mejor_producto}")


# Función principal
def main():

    # Ejecutar el análisis de ventas
    analizar_ventas()


# Verificar que el archivo se ejecute directamente
if __name__ == "__main__":
    main()