"""
25
Bordes con y sin suavizado previo
Aplicá Canny a una foto tal cual y a la misma foto suavizada 
con un gaussiano 5×5. Contá los píxeles de borde en cada caso y 
explicá por qué conviene filtrar antes de detectar.
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


def main():
    img = cv2.imread(
        RUTA,
        cv2.IMREAD_GRAYSCALE
    )

    # Canny sobre la imagen original
    bordes_original = aplicar_canny(
        img,
        30,
        90
    )

    # Suavizado y luego Canny
    suavizada = suavizar_imagen(img)

    bordes_suavizados = aplicar_canny(
        suavizada,
        30,
        90
    )

    # Contar píxeles de borde
    cantidad_original = contar_bordes(
        bordes_original
    )

    cantidad_suavizada = contar_bordes(
        bordes_suavizados
    )

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
Al aplicar Canny directamente sobre la imagen original se detectaron 7197 
píxeles de borde. Luego se aplicó un filtro gaussiano de 5×5 antes de utilizar 
Canny, obteniendo 3600 píxeles de borde.

La disminución en la cantidad de bordes se debe a que el suavizado reduce 
pequeñas variaciones de intensidad y ruido que podían ser interpretados 
como bordes. De esta manera, algunos contrastes menores desaparecen, 
mientras que los bordes más importantes de la imagen se mantienen. 
Por este motivo, suele ser conveniente aplicar un suavizado antes de la 
detección de bordes, ya que permite reducir detecciones producidas por ruido 
y obtener bordes más significativos.
'''

if __name__ == "__main__":
    main()
