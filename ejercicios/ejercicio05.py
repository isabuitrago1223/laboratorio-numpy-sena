# Importar la biblioteca NumPy
import numpy as np


# Función que analiza la producción
def analizar_produccion():

    # Generar una matriz de 30 días y 3 líneas de producción
    produccion = np.random.randint(50, 201, (30, 3))

    # Mostrar la matriz
    print("\n========== PRODUCCIÓN ==========")
    print(produccion)

    # Producción diaria
    produccion_diaria = np.sum(produccion, axis=1)

    # Producción semanal
    produccion_semanal = []

    for i in range(0, 30, 7):
        semana = np.sum(produccion[i:i + 7])
        produccion_semanal.append(semana)

    # Producción mensual
    produccion_mensual = np.sum(produccion)

    # Producción por línea
    produccion_lineas = np.sum(produccion, axis=0)

    # Línea más productiva
    linea_mayor = np.argmax(produccion_lineas) + 1

    # Mostrar resultados
    print("\n========== REPORTE ==========")

    print("\nProducción diaria:")
    for i, total in enumerate(produccion_diaria, start=1):
        print(f"Día {i}: {total}")

    print("\nProducción semanal:")
    for i, total in enumerate(produccion_semanal, start=1):
        print(f"Semana {i}: {total}")

    print(f"\nProducción mensual: {produccion_mensual}")

    print("\nProducción por línea:")
    for i, total in enumerate(produccion_lineas, start=1):
        print(f"Línea {i}: {total}")

    print(f"\nLínea más productiva: Línea {linea_mayor}")


# Función principal
def main():

    # Ejecutar el análisis de producción
    analizar_produccion()


# Verificar que el archivo se ejecute directamente
if __name__ == "__main__":
    main()