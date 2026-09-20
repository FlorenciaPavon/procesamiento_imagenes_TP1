"""
25
Elegir los umbrales de Canny
Aplicá Canny con cinco pares de umbrales distintos y 
contá los píxeles de borde de cada resultado. Después 
implementá la regla automática basada en la mediana de 
la imagen y compará su salida con tu mejor elección manual.

PistaRegla habitual: bajo = 0.66 · mediana, alto = 1.33 · 
mediana. Contá bordes con np.count_nonzero.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

import cv2
import numpy as np
import matplotlib.pyplot as plt

def aplicar_canny(img, bajo, alto):
    bordes = cv2.Canny(
        img,
        bajo,
        alto
    )
    return bordes


def contar_bordes(bordes):
    cantidad = np.count_nonzero(bordes) #cuenta los píxeles que no son cero. Como Canny genera una imagen donde los bordes son normalmente 255 y el fondo 0, esto nos permite contar los píxeles considerados borde.
    return cantidad


def umbrales_automaticos(img):
    mediana = np.median(img)

    bajo = int(0.66 * mediana)
    alto = int(1.33 * mediana)

    return bajo, alto


def main():
    img = cv2.imread(RUTA, cv2.IMREAD_GRAYSCALE)

    umbrales = [
        (30, 90),
        (50, 100),
        (70, 140),
        (100, 200),
        (150, 250)
    ]

    resultados = []

    for bajo, alto in umbrales:
        bordes = aplicar_canny(
            img,
            bajo,
            alto
        )

        cantidad = contar_bordes(bordes)

        resultados.append(
            (bajo, alto, cantidad, bordes)
        )

        print(f"Umbrales ({bajo}, {alto}): ")
        print(f"{cantidad} píxeles de borde")
        

# Umbrales automáticos
    bajo_auto, alto_auto = umbrales_automaticos(img)

    bordes_auto = aplicar_canny(
        img,
        bajo_auto,
        alto_auto
    )

    cantidad_auto = contar_bordes(bordes_auto)

    print()
    print("Método automático:")
    print("Mediana:", np.median(img))
    print("Umbral bajo:", bajo_auto)
    print("Umbral alto:", alto_auto)
    print("Píxeles de borde:", cantidad_auto)

    # resultados visibles
    plt.figure(figsize=(12, 8))

    for i, (bajo, alto, cantidad, bordes) in enumerate(
        resultados
    ):
        plt.subplot(2, 3, i + 1)
        plt.imshow(bordes, cmap="gray")
        plt.title(
            f"Canny {bajo}-{alto}\n"
            f"Bordes: {cantidad}"
        )
        plt.axis("off")

    plt.subplot(2, 3, 6)
    plt.imshow(bordes_auto, cmap="gray")
    plt.title(
        f"Automático {bajo_auto}-{alto_auto}\n"
        f"Bordes: {cantidad_auto}"
    )
    plt.axis("off")

    plt.tight_layout()
    plt.show()

'''
En las pruebas manuales, la configuración de 30 y 90 presentó 
visualmente la mejor detección de bordes, con 7197 píxeles detectados. 

El método automático, utilizando la mediana de la imagen (238) y la 
regla bajo = 0,66 × mediana y alto = 1,33 × mediana, 
obtuvo los umbrales 157 y 316, y detectó 969 píxeles de borde. 
La diferencia se debe a que los umbrales automáticos resultaron 
considerablemente más altos, haciendo que Canny fuera más selectivo 
en la detección. En conclusion: la elección manual permitió detectar 
una mayor cantidad de bordes.
'''


if __name__ == "__main__":
    main()

