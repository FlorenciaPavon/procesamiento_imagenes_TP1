"""
22
Rotar sin perder las esquinas
Rotá una imagen 30° y comprobá que las esquinas quedan 
fuera del lienzo. Corregilo: calculá el tamaño de lienzo 
necesario y ajustá los términos de traslación de la matriz
 de rotación para que entre la imagen completa.

PistaCon el coseno y el seno que ya trae la matriz de 
getRotationMatrix2D, el nuevo ancho es h · |sin| + w · |cos|. 
Después sumá la mitad de la diferencia a M[0,2] y M[1,2].
"""
import cv2
import numpy as np

ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20


def main():
    img = cv2.imread(RUTA)
    alto, ancho = img.shape[:2]

    # Centro de la imagen
    centro = (ancho / 2, alto / 2)

    # Matriz de rotación
    M = cv2.getRotationMatrix2D(
        centro,
        30,
        1
    )

    # Obtener seno y coseno de la matriz
    cos = abs(M[0, 0])
    sin = abs(M[0, 1])

    # Nuevo tamaño del lienzo
    nuevo_ancho = int(alto * sin + ancho * cos)
    nuevo_alto = int(alto * cos + ancho * sin)

    # Ajustar la traslación de la matriz
    M[0, 2] += (nuevo_ancho - ancho) / 2
    M[1, 2] += (nuevo_alto - alto) / 2

    # Aplicar la rotación
    resultado = cv2.warpAffine(
        img,
        M,
        (nuevo_ancho, nuevo_alto)
    )

    cv2.imwrite("rotacion_30_completa.png", resultado)

    print("Tamaño original:", (ancho, alto))
    print("Nuevo tamaño:", (nuevo_ancho, nuevo_alto))

if __name__ == "__main__":
    main()

