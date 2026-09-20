"""
24
Gradiente completo con Sobel
Calculá las derivadas en x e y con Sobel y, a partir de ellas,
 la magnitud y el ángulo del gradiente. Guardá la magnitud
   normalizada a 0..255 y una visualización del ángulo en color 
   (el ángulo como tono H en HSV).
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

def derivada_x(img):
    gx = cv2.Sobel(
            img,
            cv2.CV_64F,
            1,
            0,
            ksize=3
        )
    return gx

def derivada_y(img):
    gy = cv2.Sobel(
            img,
            cv2.CV_64F,
            0,
            1,
            ksize=3
        )
    return gy

def magnitud_angulo(gx, gy):
    magnitud, angulo = cv2.cartToPolar(
    gx,
    gy,
    angleInDegrees=True
    )
    return magnitud, angulo

def normalizacion_magnitud(mag):
    magnitud_normalizada = cv2.normalize(
    mag,
    None,
    0,
    255,
    cv2.NORM_MINMAX
    ).astype(np.uint8)

    return magnitud_normalizada

def imagen_HSV(img, hue):
    hsv = np.zeros(
        (img.shape[0], img.shape[1], 3),
        dtype=np.uint8
    )

    hsv[:, :, 0] = hue
    hsv[:, :, 1] = 255
    hsv[:, :, 2] = 255
    return hsv

def main():
    img = cv2.imread(RUTA, cv2.IMREAD_GRAYSCALE)

    gx= derivada_x(img)
    gy= derivada_y(img)

    mag, angulo= magnitud_angulo(gx, gy)

    magnitud_normalizada = normalizacion_magnitud(mag)
    # Convertir ángulo a tono H de HSV
    hue = (angulo / 2).astype(np.uint8)

    # Convertir HSV a BGR para guardar/mostrar
    hue = (angulo / 2).astype(np.uint8)

     # Crear imagen HSV
    hsv = imagen_HSV(img, hue)

    # Convertir HSV a BGR para guardar/mostrar
    angulo_color = cv2.cvtColor(
        hsv,
        cv2.COLOR_HSV2BGR
    )

    cv2.imwrite(
        "gradiente_magnitud.png",
        magnitud_normalizada
    )

    cv2.imwrite(
        "gradiente_angulo_color.png",
        angulo_color
    )

    # Mostrar resultados
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(magnitud_normalizada, cmap="gray")
    plt.title("Magnitud del gradiente")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(
        angulo_color,
        cv2.COLOR_BGR2RGB
    ))
    plt.title("Ángulo del gradiente")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

