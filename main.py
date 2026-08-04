# Importar el ejercicio 1
from ejercicios.ejercicio01 import main as ejercicio1


def menu():
    print("=" * 40)
    print("LABORATORIO DE ANÁLISIS DE DATOS CON NUMPY")
    print("=" * 40)
    print("1. Ejercicio 1 - Registro de temperaturas")
    print("0. Salir")


def main():

    while True:
        menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            ejercicio1()

        elif opcion == "0":
            print("\n¡Hasta luego!")
            break

        else:
            print("\nOpción no válida.\n")


if __name__ == "__main__":
    main()