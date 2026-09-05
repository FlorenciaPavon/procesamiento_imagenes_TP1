"""
05
Simular la cuantización
Escribí una función cuantizar(img, niveles) que reduzca la imagen a 128, 32, 8, 4 y 2 niveles por canal. 
Guardá cada resultado y señalá en cuál aparece el efecto de bandas (banding).
"""


import cv2
import numpy as np


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def cuantizar(img, niveles):
    paso = 256 // niveles #defino el "salto" que debe pegar
    img_modificada= (img//paso)*paso #reasigno los valores de intensidad segun el agrupamiento de valores definidos con el salto
    return img_modificada.astype(np.uint8) #uint es para asegurarme que lo tome de nuevo como imagen


def guardar(img, nivel):
    cv2.imwrite(f"img_nivel_{nivel}.jpg", img)


def main():

    img = cv2.imread(RUTA)

    niveles = [128,32,8,4,2]

    for i in niveles:
        img_cuantizada= cuantizar(img, i)
        guardar(img_cuantizada, i)

"""
En el agrupamiento de nivel 8 se comienza a ver el banding
"""

if __name__ == "__main__":
    main()

