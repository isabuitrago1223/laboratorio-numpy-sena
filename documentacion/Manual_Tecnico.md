# Manual Técnico

## Laboratorio de Análisis de Datos con NumPy

---

## Información General

**Proyecto:** Laboratorio de Análisis de Datos con NumPy

**Autor:** Isabella Buitrago

**Institución:** Servicio Nacional de Aprendizaje - SENA

**Programa:** Análisis y Desarrollo de Software (ADSO)

**Lenguaje de programación:** Python

**Biblioteca utilizada:** NumPy

---

# 1. Introducción

Este documento describe la estructura, funcionamiento e instalación del proyecto **Laboratorio de Análisis de Datos con NumPy**, desarrollado como evidencia de aprendizaje del programa ADSO del SENA.

El proyecto tiene como objetivo aplicar las principales funciones de la biblioteca NumPy mediante diferentes ejercicios relacionados con el análisis de datos, matrices y operaciones estadísticas.

---

# 2. Objetivo General

Desarrollar un laboratorio práctico utilizando la biblioteca NumPy para fortalecer los conocimientos sobre arreglos, matrices y funciones estadísticas en Python.

---

# 3. Objetivos Específicos

- Utilizar la biblioteca NumPy.
- Crear y manipular arreglos y matrices.
- Aplicar operaciones estadísticas.
- Resolver problemas mediante programación.
- Implementar un menú para ejecutar los ejercicios.

---

# 4. Requisitos del Sistema

Para ejecutar correctamente el proyecto se requiere:

- Sistema Operativo Windows 10 o superior.
- Python 3.13 o superior.
- Visual Studio Code.
- Git.
- GitHub.
- Biblioteca NumPy.

---

# 5. Instalación

## Clonar el repositorio

```bash
git clone https://github.com/isabuitrago1223/laboratorio-numpy-sena.git
```

Ingresar al proyecto

```bash
cd laboratorio-numpy-sena
```

---

## Crear el entorno virtual

```bash
python -m venv .venv
```

---

## Activar el entorno virtual

Windows

```bash
.venv\Scripts\activate
```

Git Bash

```bash
source .venv/Scripts/activate
```

---

## Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

# 6. Tecnologías Utilizadas

- Python
- NumPy
- Git
- GitHub
- Visual Studio Code

---

# 7. Estructura del Proyecto

```
laboratorio-numpy-sena/
│
├── documentacion/
│   └── Manual_Tecnico.md
│
├── ejercicios/
│   ├── ejercicio01.py
│   ├── ejercicio02.py
│   ├── ejercicio03.py
│   ├── ejercicio04.py
│   ├── ejercicio05.py
│   ├── ejercicio06.py
│   ├── ejercicio07.py
│   ├── ejercicio08.py
│   ├── ejercicio09.py
│   └── ejercicio10.py
│
├── investigacion/
│   └── funciones_numpy.pdf
│
├── recursos/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 8. Descripción de las Carpetas

## documentacion

Contiene el manual técnico del proyecto.

## ejercicios

Contiene los diez ejercicios desarrollados durante el laboratorio.

## investigacion

Almacena la investigación sobre las funciones de NumPy.

## recursos

Carpeta destinada para imágenes, evidencias o archivos adicionales.

---

# 9. Descripción de los Ejercicios

## Ejercicio 1

Registro de temperaturas utilizando arreglos.

## Ejercicio 2

Análisis de ventas mensuales mediante matrices.

## Ejercicio 3

Análisis de calificaciones.

## Ejercicio 4

Inventario inteligente.

## Ejercicio 5

Sistema de producción.

## Ejercicio 6

Procesamiento de imágenes.

## Ejercicio 7

Simulación de sensores IoT.

## Ejercicio 8

Encuesta nacional.

## Ejercicio 9

Simulación financiera.

## Ejercicio 10

Dashboard estadístico.

---

# 10. Funcionamiento del Programa

El archivo principal del proyecto es **main.py**.

Al ejecutarlo se muestra un menú con los diez ejercicios disponibles.

El usuario selecciona el ejercicio que desea ejecutar ingresando el número correspondiente.

Cada ejercicio genera información aleatoria y presenta un análisis utilizando funciones de NumPy.

---

# 11. Funciones de NumPy Utilizadas

Durante el desarrollo del proyecto se utilizaron, entre otras, las siguientes funciones:

- mean()
- median()
- max()
- min()
- sum()
- var()
- std()
- argmax()
- argmin()
- where()
- unique()
- random.randint()
- random.uniform()
- clip()
- transpose()

---

# 12. Ejecución del Proyecto

Para ejecutar el laboratorio se utiliza el siguiente comando:

```bash
python main.py
```

Posteriormente se selecciona el número del ejercicio que se desea ejecutar.

---

# 13. Posibles Errores

## Error

```
ModuleNotFoundError
```

### Solución

Instalar las dependencias.

```bash
pip install -r requirements.txt
```

---

## Error

```
No module named numpy
```

### Solución

Instalar NumPy.

```bash
pip install numpy
```

---

# 14. Buenas Prácticas Implementadas

- Organización por carpetas.
- Código documentado.
- Uso de funciones.
- Menú principal.
- Separación de cada ejercicio.
- Uso de Git y GitHub.
- Control de versiones mediante commits.

---

# 15. Conclusiones

Durante el desarrollo de este laboratorio se fortalecieron los conocimientos sobre la biblioteca NumPy y el manejo de arreglos y matrices en Python.

La implementación de funciones estadísticas permitió analizar diferentes conjuntos de datos de forma eficiente, mientras que el uso de Git y GitHub facilitó el control de versiones del proyecto.

El desarrollo del laboratorio permitió aplicar buenas prácticas de programación, organización del código y documentación técnica, generando un proyecto estructurado y fácil de mantener.