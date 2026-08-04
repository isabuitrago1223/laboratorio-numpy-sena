# Importar la biblioteca NumPy
import numpy as np


# Función que analiza el inventario
def analizar_inventario():

    # Generar una matriz de 15 productos y 8 sucursales
    inventario = np.random.randint(0, 101, (15, 8))

    # Mostrar la matriz de inventario
    print("\n========== INVENTARIO ==========")
    print(inventario)

    # Calcular el total por producto
    total_productos = np.sum(inventario, axis=1)

    # Calcular el total por sucursal
    total_sucursales = np.sum(inventario, axis=0)

    # Producto con mayor existencia
    producto_mayor = np.argmax(total_productos) + 1

    # Sucursal con menor inventario
    sucursal_menor = np.argmin(total_sucursales) + 1

    # Inventario total
    inventario_total = np.sum(inventario)

    # Inventario promedio
    inventario_promedio = np.mean(inventario)

    # Buscar productos agotados
    agotados = np.where(inventario == 0)

    # Mostrar resultados
    print("\n========== REPORTE ==========")
    print(f"Producto con mayor existencia: Producto {producto_mayor}")
    print(f"Sucursal con menor inventario: Sucursal {sucursal_menor}")
    print(f"Inventario total: {inventario_total}")
    print(f"Inventario promedio: {inventario_promedio:.2f}")

    print("\nProductos agotados:")

    if len(agotados[0]) == 0:
        print("No hay productos agotados.")
    else:
        for producto, sucursal in zip(agotados[0], agotados[1]):
            print(f"Producto {producto + 1} - Sucursal {sucursal + 1}")


# Función principal
def main():

    # Ejecutar el análisis del inventario
    analizar_inventario()


# Verificar que el archivo se ejecute directamente
if __name__ == "__main__":
    main()