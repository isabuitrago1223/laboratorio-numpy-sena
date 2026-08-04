"""
---------------------------------------------------------
Archivo principal del proyecto

Descripción:
Este archivo permite ejecutar los diferentes ejercicios
del laboratorio de Análisis de Datos con NumPy.
---------------------------------------------------------
"""

# Importar los ejercicios
from ejercicios.ejercicio01 import main as ejercicio1
from ejercicios.ejercicio02 import main as ejercicio2


# Función que muestra el menú principal
def mostrar_menu():
    print("\n" + "=" * 50)
    print(" LABORATORIO DE ANÁLISIS DE DATOS CON NUMPY")
    print("=" * 50)
    print("1. Ejercicio 1 - Registro de temperaturas")
    print("2. Ejercicio 2 - Análisis de ventas mensuales")
    print("0. Salir")


# Función principal
def main():

    while True:

        # Mostrar el menú
        mostrar_menu()

        # Solicitar la opción al usuario
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            ejercicio1()

        elif opcion == "2":
            ejercicio2()

        elif opcion == "0":
            print("\nGracias por utilizar el programa.")
            break

        else:
            print("\n❌ Opción no válida. Intente nuevamente.")


# Punto de inicio del programa
if __name__ == "__main__":
    main()