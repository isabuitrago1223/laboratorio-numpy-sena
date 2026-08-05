# Importar la biblioteca NumPy
import numpy as np


# Función que genera el reporte estadístico
def dashboard_estadistico():

    # Crear una matriz de ejemplo de 5 filas y 5 columnas
    matriz = np.random.randint(1, 101, (5, 5))

    # Mostrar la matriz
    print("\n========== MATRIZ ==========")
    print(matriz)

    # Obtener la dimensión de la matriz
    dimension = matriz.ndim

    # Obtener el número de filas y columnas
    filas = matriz.shape[0]
    columnas = matriz.shape[1]

    # Obtener el total de datos
    total_datos = matriz.size

    # Obtener el valor máximo
    maximo = np.max(matriz)

    # Obtener el valor mínimo
    minimo = np.min(matriz)

    # Calcular el promedio
    promedio = np.mean(matriz)

    # Calcular la mediana
    mediana = np.median(matriz)

    # Calcular la varianza
    varianza = np.var(matriz)

    # Calcular la desviación estándar
    desviacion = np.std(matriz)

    # Mostrar el reporte
    print("\n========== DASHBOARD ESTADÍSTICO ==========")
    print(f"Dimensión: {dimension}")
    print(f"Número de filas: {filas}")
    print(f"Número de columnas: {columnas}")
    print(f"Total de datos: {total_datos}")
    print(f"Valor máximo: {maximo}")
    print(f"Valor mínimo: {minimo}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana}")
    print(f"Varianza: {varianza:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")


# Función principal
def main():

    # Ejecutar el dashboard estadístico
    dashboard_estadistico()


# Verificar que el archivo se ejecute directamente
if __name__ == "__main__":
    main()