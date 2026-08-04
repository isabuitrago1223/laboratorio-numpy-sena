# Importar la función principal de cada ejercicio
from ejercicios.ejercicio01 import main as ejercicio1
from ejercicios.ejercicio02 import main as ejercicio2
from ejercicios.ejercicio03 import main as ejercicio3
from ejercicios.ejercicio04 import main as ejercicio4
from ejercicios.ejercicio05 import main as ejercicio5
from ejercicios.ejercicio06 import main as ejercicio6
from ejercicios.ejercicio07 import main as ejercicio7


# Función que muestra el menú principal
def mostrar_menu():

    print("\n" + "=" * 55)
    print(" LABORATORIO DE ANÁLISIS DE DATOS CON NUMPY")
    print("=" * 55)
    print("1. Ejercicio 1 - Registro de temperaturas")
    print("2. Ejercicio 2 - Análisis de ventas mensuales")
    print("3. Ejercicio 3 - Análisis de calificaciones")
    print("4. Ejercicio 4 - Inventario inteligente")
    print("5. Ejercicio 5 - Sistema de producción")
    print("6. Ejercicio 6 - Procesamiento de imágenes")
    print("7. Ejercicio 7 - Simulación de sensores IoT")
    print("0. Salir")


# Función principal
def main():

    # Mantener el programa en ejecución
    while True:

        # Mostrar el menú
        mostrar_menu()

        # Solicitar una opción
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            ejercicio1()

        elif opcion == "2":
            ejercicio2()

        elif opcion == "3":
            ejercicio3()

        elif opcion == "4":
            ejercicio4()

        elif opcion == "5":
            ejercicio5()

        elif opcion == "6":
            ejercicio6()

        elif opcion == "7":
            ejercicio7()

        elif opcion == "0":
            print("\nGracias por utilizar el programa.")
            break

        else:
            print("\n❌ Opción no válida. Intente nuevamente.")


# Verificar que este archivo se ejecute directamente
if __name__ == "__main__":
    main()