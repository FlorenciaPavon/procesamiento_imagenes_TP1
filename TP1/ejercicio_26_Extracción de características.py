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
from ejercicio_25_Extraccion_de_caracteristicas import aplicar_canny, contar_bordes


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

import cv2
import numpy as np
import matplotlib.pyplot as plt

def suavizar_imagen(img):
    suavizada = cv2.GaussianBlur(
        img,
        (5, 5),
        0
    )
    return suavizada

def cantidad_pixeles():
    cantidad_original = contar_bordes(
        bordes_original
    )

    cantidad_suavizada = contar_bordes(
        bordes_suavizados
    )

   


def main():
    img = cv2.imread(RUTA, cv2.IMREAD_GRAYSCALE)

    # Canny sobre la imagen original
    bordes_original = aplicar_canny(img, 30, 90)    
    cantidad_original = contar_bordes(bordes_original)
    suavizada = suavizar_imagen(img)
    bordes_suavizados = detectar_bordes(suavizada)

    # Contar píxeles de borde
    cantidad_original = contar_bordes(bordes_original)
    cantidad_suavizada = contar_bordes(bordes_suavizados)

    print(
        "Píxeles de borde sin suavizado:",
        cantidad_original
    )

    print(
        "Píxeles de borde con suavizado:",
        cantidad_suavizada
    )

    # Mostrar resultados
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap="gray")
    
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(bordes_original, cmap="gray")
    plt.title(
        f"Canny sin suavizado\n"
        f"Bordes: {cantidad_original}"
    )
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(bordes_suavizados, cmap="gray")
    plt.title(
        f"Canny con Gaussiano 5×5\n"
        f"Bordes: {cantidad_suavizada}"
    )
    plt.axis("off")

    plt.tight_layout()
    plt.show()
'''

'''


if __name__ == "__main__":
    main()

