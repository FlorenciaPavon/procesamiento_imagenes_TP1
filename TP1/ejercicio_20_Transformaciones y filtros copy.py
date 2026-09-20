"""
20
Efecto del tamaño del kernel
Aplicá desenfoque gaussiano con kernels de 3, 7, 15 y 31 píxeles de lado. Guardá cada salida y graficá la varianza del laplaciano en función del tamaño del kernel.

PistaEl lado del kernel tiene que ser impar.
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
from ejercicio_18_Transformaciones_y_filtros import calcular_nitidez

ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20


def main():
    img = cv2.imread(RUTA)

    tamanios = [3, 7, 15, 31]

    resultados = []

    for tamanio in tamanios:

        resultado = cv2.GaussianBlur(
            img,
            (tamanio, tamanio),
            0
        )

        nitidez = calcular_nitidez(resultado)

        resultados.append((tamanio, nitidez))

        cv2.imwrite(
            f"gaussian_{tamanio}.png",
            resultado
        )

    print("Varianza del Laplaciano:")

    for tamanio, nitidez in resultados:
        print(f"Kernel {tamanio}x{tamanio}: {nitidez:.2f}")

    # Gráfico
    tamanios_grafico = [x[0] for x in resultados]
    nitidez_grafico = [x[1] for x in resultados]

    plt.figure(figsize=(8, 5))

    plt.plot(
        tamanios_grafico,
        nitidez_grafico,
        marker="o"
    )

    plt.title("Nitidez según el tamaño del kernel")
    plt.xlabel("Tamaño del kernel")
    plt.ylabel("Varianza del Laplaciano")
    plt.xticks(tamanios)
    plt.grid(True)

    plt.show()


'''
Al aumentar el tamaño del kernel gaussiano, 
aumenta el nivel de desenfoque y disminuye 
la nitidez de la imagen.
 Esto se observa en la varianza del Laplaciano, 
 que disminuye de 9,47 para un kernel de 3×3 a 1,09 
 para un kernel de 31×31. Por lo tanto, cuanto mayor es el kernel,
   mayor es el suavizado y menor es la cantidad de cambios bruscos de 
   intensidad presentes en la imagen.
'''

if __name__ == "__main__":
    main()

