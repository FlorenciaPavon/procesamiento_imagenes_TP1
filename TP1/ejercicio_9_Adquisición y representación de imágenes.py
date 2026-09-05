"""
09
El error clásico BGR contra RGB
Abrí una foto con Pillow, convertila a arreglo NumPy y guardala con cv2.imwrite sin conversión previa. 
Mirá el archivo resultante, explicá qué pasó y corregilo.
"""

import cv2
import numpy as np
from PIL import Image


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def main():

    img = Image.open(RUTA)

    img_np= np.asarray(img)

    cv2.imwrite("imagen_ej_9.jpg", img_np)
    #La naranja esta toda celeste porque los colores mas rojizos se pasaron a
    #color azul. Pillow lee las imagenes como RGB(rojo, verde, azul), pero OpenCV
    #las lee como BGR (azul, verde, rojo). El primer valor es justamente el que se cambio
    #de rojo en pillow a azul en OpenCV

    img_corregida= cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imwrite("imagen_corregida_RGB.jpg", img_corregida)

if __name__ == "__main__":
    main()

