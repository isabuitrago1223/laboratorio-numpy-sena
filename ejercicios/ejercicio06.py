# Importar la biblioteca NumPy
import numpy as np


# Función principal
def procesar_imagen():

    # Crear una matriz de 15 x 15 con valores entre 0 y 255
    imagen = np.random.randint(0, 256, (15, 15))

    # Mostrar la imagen original
    print("\n========== IMAGEN ORIGINAL ==========")
    print(imagen)

    # Incrementar el brillo
    brillo = np.clip(imagen + 50, 0, 255)

    # Disminuir el brillo
    oscuro = np.clip(imagen - 50, 0, 255)

    # Invertir colores
    invertida = 255 - imagen

    # Obtener la imagen transpuesta
    transpuesta = np.transpose(imagen)

    # Mostrar resultados
    print("\n========== IMAGEN CON MÁS BRILLO ==========")
    print(brillo)

    print("\n========== IMAGEN CON MENOS BRILLO ==========")
    print(oscuro)

    print("\n========== IMAGEN INVERTIDA ==========")
    print(invertida)

    print("\n========== IMAGEN TRANSPUESTA ==========")
    print(transpuesta)


# Función principal del programa
def main():

    # Ejecutar el procesamiento de la imagen
    procesar_imagen()


# Verificar que el archivo se ejecute directamente
if __name__ == "__main__":
    main()