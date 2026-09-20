"""
19
Realce y máscara de enfoque
Realzá una foto de dos maneras: con el kernel de 
sharpening de la sección 2 y con unsharp masking 
(original + k · (original - suavizada)). Probá k en
 {0.5, 1.0, 2.0} y describí a partir de qué valor aparecen halos.
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20


def main():

    img = cv2.imread(RUTA)

     # Kernel de sharpening
    kernel_sharpening = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ], dtype=np.float32)

    resultado_sharpening = cv2.filter2D(
        img,
        -1,
        kernel_sharpening
    )

    # Imagen suavizada para unsharp masking
    suavizada = cv2.GaussianBlur(
        img,
        (5, 5),
        0
    )

    valores_k = [0.5, 1.0, 2.0, 2.5, 3.0, 3.5, 4.0] #suavizado leve, moderado, fuerte

    resultados = []

    for k in valores_k:

        detalle = img.astype(np.float32) - suavizada.astype(np.float32)

        resultado = (
            img.astype(np.float32) + k * detalle
        )

        resultado = np.clip(
            resultado,
            0,
            255
        ).astype(np.uint8)

        resultados.append((k, resultado))

    # Mostrar resultados
    plt.figure(figsize=(17, 8))

    plt.subplot(2, 5, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(2, 5, 2)
    plt.imshow(cv2.cvtColor(resultado_sharpening, cv2.COLOR_BGR2RGB))
    plt.title("Sharpening")
    plt.axis("off")

    for i, (k, resultado) in enumerate(resultados):

        plt.subplot(2, 5, i +2 )

        plt.imshow(
            cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB)
        )

        plt.title(f"Unsharp masking - k = {k}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Guardar resultados
    cv2.imwrite(
        "realce_sharpening.png",
        resultado_sharpening
    )

    for k, resultado in resultados:

        nombre = f"unsharp_k_{k}.png"

        cv2.imwrite(
            nombre,
            resultado
        )

'''
En el unsharp masking, al aumentar el valor de k se incrementa 
progresivamente el realce de los detalles y bordes. 
En la imagen analizada no se observaron halos evidentes 
con k = 0,5, 1,0, 2,0 ni 3,0. A partir de k = 4,0 comenzaron 
a observarse halos alrededor de algunos bordes, 
y el efecto se vuelve más marcado al continuar aumentando k.
'''

if __name__ == "__main__":
    main()

