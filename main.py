# Importar la función principal de cada ejercicio
from ejercicios.ejercicio01 import main as ejercicio1
from ejercicios.ejercicio02 import main as ejercicio2
from ejercicios.ejercicio03 import main as ejercicio3


# Función que muestra el menú principal
def mostrar_menu():

    print("\n" + "=" * 55)
    print(" LABORATORIO DE ANÁLISIS DE DATOS CON NUMPY")
    print("=" * 55)
    print("1. Ejercicio 1 - Registro de temperaturas")
    print("2. Ejercicio 2 - Análisis de ventas mensuales")
    print("3. Ejercicio 3 - Análisis de calificaciones")
    print("0. Salir")


# Función principal del programa
def main():

    # Ciclo que mantiene el programa en ejecución
    while True:

        # Mostrar el menú de opciones
        mostrar_menu()

        # Solicitar al usuario una opción
        opcion = input("\nSeleccione una opción: ")

        # Ejecutar el ejercicio 1
        if opcion == "1":
            ejercicio1()

        # Ejecutar el ejercicio 2
        elif opcion == "2":
            ejercicio2()

        # Ejecutar el ejercicio 3
        elif opcion == "3":
            ejercicio3()

        # Finalizar el programa
        elif opcion == "0":
            print("\nGracias por utilizar el programa.")
            break

        # Validar una opción incorrecta
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")


# Verificar que este archivo se ejecute directamente
if __name__ == "__main__":
    main()