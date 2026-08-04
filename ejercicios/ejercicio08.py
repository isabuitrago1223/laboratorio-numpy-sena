# Importar la biblioteca NumPy
import numpy as np


# Función que analiza las edades
def analizar_edades():

    # Generar 500 edades aleatorias entre 1 y 90 años
    edades = np.random.randint(1, 91, 500)

    # Mostrar las edades
    print("\n========== EDADES REGISTRADAS ==========")
    print(edades)

    # Calcular el promedio
    promedio = np.mean(edades)

    # Calcular la mediana
    mediana = np.median(edades)

    # Calcular la moda
    valores, cantidad = np.unique(edades, return_counts=True)
    moda = valores[np.argmax(cantidad)]

    # Obtener la edad máxima
    maxima = np.max(edades)

    # Obtener la edad mínima
    minima = np.min(edades)

    # Contar los mayores de edad
    mayores_edad = np.sum(edades >= 18)

    # Mostrar resultados
    print("\n========== REPORTE ==========")
    print(f"Promedio de edad: {promedio:.2f}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Edad máxima: {maxima}")
    print(f"Edad mínima: {minima}")
    print(f"Cantidad de mayores de edad: {mayores_edad}")


# Función principal
def main():

    # Ejecutar el análisis de edades
    analizar_edades()


# Verificar que el archivo se ejecute directamente
if __name__ == "__main__":
    main()