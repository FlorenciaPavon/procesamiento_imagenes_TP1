"""
01
Ficha técnica de una imagen
Cargá la misma foto con Pillow y con OpenCV. Imprimí, para cada biblioteca, las dimensiones,
el modo o la cantidad de canales y el tipo de dato. Explicá en un comentario por qué Pillow 
informa (ancho, alto) y NumPy informa (alto, ancho, canales).
"""

import cv2
from PIL import Image
import numpy as np

ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

#verifico si se cargo la imagen
#imagen= cv2.imread(RUTA)
#print (imagen)

def main():
    #con pillow
    img = Image.open(RUTA)
    print("Size= ", img.size)
    print("Mode= ", img.mode)

    #con numpy
    img_np = np.asarray(img)
    print(img_np)
    print("Size con numpy= ", img_np.shape)    
    print ("Tipo de dato con numpy ", img_np.dtype)
    print("pixel (0,0) =", img_np[0, 0]) 

    #con cv2
    img_cv2=cv2.imread(RUTA,  cv2.IMREAD_UNCHANGED)
    #img2 = cv2.imread("img", cv2.IMREAD_UNCHANGED)
    
    print("Size con cv2", img_cv2.shape)
    print("Tipo de dato con cv2 ", img_cv2.dtype)

    """
    pillow siempre devuelve (alto, ancho)
    openCV internamente trabaja con un array de Numpy entonces devuelve 3 valores (alto, ancho, cantidad_canales)
    tambien por defecto open cv ignora el A (alpha) de las imagenes RGBA por eso muestra 3
    para poder ver todos los canales hay que ejecutar:
    img = cv2.imread("imagen.png", cv2.IMREAD_UNCHANGED)
    Numpy transforma la imagen en un array y muestra todo, (ancho, alto, canales_totales), por eso en este caso aparecen 4
    """

if __name__ == "__main__":
    main()