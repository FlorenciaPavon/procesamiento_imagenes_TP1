"""
10
11
Brillo y contraste
Implementá la transformación g = alfa · f + beta y generá seis variantes de una foto combinando alfa en
{0.5, 1.0, 1.8} y beta en {-40, +40}. Explicá qué pasa con los píxeles que se pasan de 255.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def main():

    img = cv2.imread(RUTA)
    
# Es necesario convertir de BGR a RGB para mostrar correctamente con matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#selecciono combinaciones de alfa y beta
    combinaciones = [
        (0.5, -40),
        (0.5, 40),
        (1.0, -40),
        (1.0, 40),
        (1.8, -40),
        (1.8, 40)
    ]

#combino las variantes
    resultados = []

    for alpha, beta in combinaciones:
        resultado = cv2.convertScaleAbs( # si un pixel es mayor a 255 automaticamente lo deja en 255, o si es menor que 0 lo deha en 0
            img_rgb,
            alpha=alpha,
            beta=beta
        )
        resultados.append((alpha, beta, resultado))

        # Mostrar
    plt.figure(figsize=(12, 8))

    for i, (alpha, beta, resultado) in enumerate(resultados):
        plt.subplot(2, 3, i + 1) #necesita saber en que posicion coloca cada imagen, subplot empieza los indices desde 1
        plt.imshow(resultado)
        plt.title(f"α = {alpha}, β = {beta}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

