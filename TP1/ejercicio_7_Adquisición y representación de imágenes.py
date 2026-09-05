"""
07
Tres formas de pasar a gris
Convertí una foto a escala de grises de tres maneras: promedio simple de los canales,
luminancia ponderada (0.299 R + 0.587 G + 0.114 B) y cv2.COLOR_BGR2GRAY. 
Calculá la diferencia absoluta media entre cada par de resultados e interpretá cuál se parece más al de OpenCV.

Pista Convertí a float32 antes de promediar para no perder precisión ni desbordar el uint8.
"""

from PIL import Image
import cv2
import numpy as np


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def gris_promedio(img):
    (azul, verde, rojo) = cv2.split(img)

    promedio = (azul.astype(float) + verde.astype(float) + rojo.astype(float))/3
    promedio = promedio.astype(np.uint8)
    cv2.imwrite("gris_promedio.jpg", promedio)


def luminancia_ponderada(img):
    (azul, verde, rojo) = cv2.split(img)

    promedio_ponderado= (0.299 * rojo + 0.587* verde + 0.114*azul)
    promedio_ponderado= promedio_ponderado.astype(np.uint8)
    cv2.imwrite("Imagen_ponderada.jpg", promedio_ponderado)

def cv2togray(img):
    img_ocv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Imagen_gris_ocv.jpg", img_ocv)

def main():

    img = cv2.imread(RUTA) #sin transparencia recordar que es BGR

    gris_promedio(img) #es un promedio comun de los 3 canales
    luminancia_ponderada(img)
    cv2togray(img)

if __name__ == "__main__":
    main()

