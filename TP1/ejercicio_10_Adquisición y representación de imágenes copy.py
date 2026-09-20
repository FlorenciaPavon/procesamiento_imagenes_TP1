"""
10
Vecindad de un píxel
Escribí una función que reciba una imagen en gris y una coordenada, y devuelva la ventana de 
3×3 centrada en ese píxel. Probala en el centro de la imagen y en la esquina superior izquierda,
y decidí qué hace tu función cuando la ventana se sale del borde.
"""

import cv2
import numpy as np
from PIL import Image
import random


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def vecindad(img, coordenada):
    (fila, columna) = coordenada

    ventana = img[
        fila - 1:fila + 2, #tomo la fila de la coordenada y -1 tambien +2 de ese nro
        columna - 1:columna + 2
    ]
    return ventana

def vecindad_borde(img, coordenada):
    (fila, columna) = coordenada

    alto, ancho = img.shape

    fila_inicio = max(0, fila - 1)
    fila_fin = min(alto, fila + 2)

    columna_inicio = max(0, columna - 1)
    columna_fin = min(ancho, columna + 2)

    return img[fila_inicio:fila_fin, columna_inicio:columna_fin] #recorte los bordes que no tienen info
def main():

    img = cv2.imread(RUTA)
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (alto, ancho)= img_gris.shape

    #centro
    fila_centro = alto // 2
    columna_centro = ancho // 2

    coordenadas_centro = (fila_centro, columna_centro)
    resultado_centro = vecindad(img_gris, coordenadas_centro)    
    print("Coordenadas centro:", coordenadas_centro)
    print("Ventana centro:")
    print(resultado_centro)

    #esquina
    coordenadas_esquina = (0, 0)
    resultado_esq = vecindad_borde(img_gris, coordenadas_esquina)    
    print("Coordenadas esquina:", coordenadas_esquina)
    print("Ventana esquina:")
    print(resultado_esq)  
    
if __name__ == "__main__":
    main()

