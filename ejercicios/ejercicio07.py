# Importar la biblioteca NumPy
import numpy as np


# Función que analiza las mediciones
def analizar_sensores():

    # Generar 100 mediciones aleatorias entre 20 y 100
    sensores = np.random.uniform(20, 100, 100)

    # Mostrar las mediciones
    print("\n========== MEDICIONES DE LOS SENSORES ==========")
    print(sensores)

    # Calcular el promedio
    promedio = np.mean(sensores)

    # Calcular la desviación estándar
    desviacion = np.std(sensores)

    # Encontrar sensores fuera del rango permitido (30 a 80)
    fuera_rango = np.where((sensores < 30) | (sensores > 80))

    # Encontrar sensores críticos (menores de 25 o mayores de 90)
    sensores_criticos = np.where((sensores < 25) | (sensores > 90))

    # Mostrar resultados
    print("\n========== REPORTE ==========")
    print(f"Promedio: {promedio:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")
    print(f"Sensores fuera del rango permitido: {len(fuera_rango[0])}")
    print(f"Cantidad de sensores críticos: {len(sensores_criticos[0])}")


# Función principal
def main():

    # Ejecutar el análisis de sensores
    analizar_sensores()


# Verificar que el archivo se ejecute directamente
if __name__ == "__main__":
    main()