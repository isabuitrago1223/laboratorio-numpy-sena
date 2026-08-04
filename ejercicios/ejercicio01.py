# Importar la biblioteca NumPy
import numpy as np


# Función que genera y analiza las temperaturas
def analizar_temperaturas():

    # Generar un arreglo con 30 temperaturas aleatorias
    # entre 18 y 37 grados Celsius
    temperaturas = np.random.randint(18, 38, 30)

    # Mostrar todas las temperaturas generadas
    print("\n========== TEMPERATURAS DEL MES ==========")
    print(temperaturas)

    # Calcular el promedio de las temperaturas
    promedio = np.mean(temperaturas)

    # Obtener la temperatura máxima registrada
    maxima = np.max(temperaturas)

    # Obtener la temperatura mínima registrada
    minima = np.min(temperaturas)

    # Calcular la desviación estándar
    desviacion = np.std(temperaturas)

    # Calcular la varianza
    varianza = np.var(temperaturas)

    # Obtener la posición del día más caluroso
    # Se suma 1 porque los arreglos empiezan en la posición 0
    dia_caluroso = np.argmax(temperaturas) + 1

    # Obtener la posición del día más frío
    dia_frio = np.argmin(temperaturas) + 1

    # Mostrar el reporte final de resultados
    print("\n========== REPORTE ==========")
    print(f"Temperatura promedio: {promedio:.2f} °C")
    print(f"Temperatura máxima: {maxima} °C")
    print(f"Temperatura mínima: {minima} °C")
    print(f"Desviación estándar: {desviacion:.2f}")
    print(f"Varianza: {varianza:.2f}")
    print(f"Día más caluroso: Día {dia_caluroso}")
    print(f"Día más frío: Día {dia_frio}")


# Función principal del programa
def main():

    # Llamar la función que realiza todo el proceso
    analizar_temperaturas()


# Verificar que el archivo se esté ejecutando directamente
if __name__ == "__main__":
    main()