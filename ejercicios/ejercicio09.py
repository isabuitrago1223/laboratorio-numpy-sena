# Importar la biblioteca NumPy
import numpy as np


# Función que analiza los precios de la acción
def analizar_acciones():

    # Generar los precios de la acción durante 100 días
    precios = np.random.randint(100, 501, 100)

    # Mostrar los precios
    print("\n========== PRECIOS DE LA ACCIÓN ==========")
    print(precios)

    # Calcular el precio promedio
    promedio = np.mean(precios)

    # Obtener el precio máximo
    maximo = np.max(precios)

    # Obtener el precio mínimo
    minimo = np.min(precios)

    # Calcular la variación porcentual
    variacion = ((precios[-1] - precios[0]) / precios[0]) * 100

    # Encontrar los días donde el precio fue superior al promedio
    dias_superiores = np.where(precios > promedio)

    # Mostrar resultados
    print("\n========== REPORTE ==========")
    print(f"Precio promedio: {promedio:.2f}")
    print(f"Precio máximo: {maximo}")
    print(f"Precio mínimo: {minimo}")
    print(f"Variación porcentual: {variacion:.2f}%")

    print("\nDías donde el precio fue superior al promedio:")

    for dia in dias_superiores[0]:
        print(f"Día {dia + 1}: {precios[dia]}")


# Función principal
def main():

    # Ejecutar el análisis financiero
    analizar_acciones()


# Verificar que el archivo se ejecute directamente
if __name__ == "__main__":
    main()