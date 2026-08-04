# Importar la biblioteca NumPy
import numpy as np


# Función que analiza las calificaciones
def analizar_calificaciones():

    # Generar una matriz de 5 estudiantes y 4 materias
    notas = np.random.randint(1, 6, (5, 4))

    # Mostrar la matriz
    print("\n========== CALIFICACIONES ==========")
    print(notas)

    # Promedio por estudiante
    promedio_estudiantes = np.mean(notas, axis=1)

    # Promedio por materia
    promedio_materias = np.mean(notas, axis=0)

    # Estudiante con mejor promedio
    mejor_estudiante = np.argmax(promedio_estudiantes) + 1

    print("\n========== REPORTE ==========")

    print("\nPromedio por estudiante:")
    for i, promedio in enumerate(promedio_estudiantes, start=1):
        print(f"Estudiante {i}: {promedio:.2f}")

    print("\nPromedio por materia:")
    for i, promedio in enumerate(promedio_materias, start=1):
        print(f"Materia {i}: {promedio:.2f}")

    print(f"\nMejor estudiante: Estudiante {mejor_estudiante}")


# Función principal
def main():
    analizar_calificaciones()


# Punto de inicio
if __name__ == "__main__":
    main()