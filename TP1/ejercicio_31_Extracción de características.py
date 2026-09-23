"""
31
Descriptor HOG
Calculá el descriptor HOG de un recorte de 64×128 píxeles e imprimí 
la longitud del vector resultante. Verificá a mano de dónde sale ese 
número a partir del tamaño de celda, del tamaño de bloque y de la 
cantidad de orientaciones.

Pistacv2.HOGDescriptor() con los valores por defecto y .compute(recorte).
"""
import cv2
import numpy as np

RUTA= "TP1/imagen_bajo_contraste.jpg"

def main():
    
    img = cv2.imread(RUTA, cv2.IMREAD_GRAYSCALE)

    recorte = img[0:128, 0:64] #recorte alto 128, ancho 64 NumPy muestra alto × ancho

    hog = cv2.HOGDescriptor() #aca estan todos los parametros para los gradientes ver notas

    descriptor = hog.compute(recorte)

    print("Tamaño del recorte:", recorte.shape)
    print("Longitud del descriptor HOG:", len(descriptor))


if __name__ == "__main__":
    main()
    

'''
hog = cv2.HOGDescriptor()

OpenCV utiliza estos valores por defecto:

Parámetro	Valor
Window size	64 × 128
Block size	16 × 16
Block stride	8 × 8
Cell size	8 × 8
Orientaciones	9

La imagen completa mide:

64 × 128

y cada celda mide:

8 × 8

Entonces tenemos:

Celdas horizontales
64 / 8 = 8
Celdas verticales
128 / 8 = 16

Por lo tanto:

8 × 16 = 128 celdas

Pero HOG no trabaja con cada celda individual directamente. Agrupa las celdas en bloques de:

16 × 16

Como cada celda mide 8×8:

16 / 8 = 2 celdas

Entonces cada bloque contiene:

2 × 2 = 4 celdas

Y cada celda tiene:

9 orientaciones

Por lo tanto, un bloque genera:

4 × 9 = 36 valores

¿Cuántos bloques tenemos?

El desplazamiento (block stride) es:

8 × 8

Es decir, avanzamos una celda por vez.

Horizontalmente:

(64 - 16) / 8 + 1
= 48 / 8 + 1
= 7

Verticalmente:

(128 - 16) / 8 + 1
= 112 / 8 + 1
= 15

Entonces tenemos:

7 × 15 = 105 bloques

Cada bloque aporta:

36 valores

Por lo tanto:

105 × 36 = 3780
La longitud esperada del descriptor HOG es 3780.
'''

'''
resumen de calculos
Recorte:          64 × 128

Celda:             8 × 8
Bloque:           16 × 16
Stride:             8 × 8
Orientaciones:          9

Bloques horizontales:
(64 - 16) / 8 + 1 = 7

Bloques verticales:
(128 - 16) / 8 + 1 = 15

Cantidad de bloques:
7 × 15 = 105

Valores por bloque:
2 × 2 celdas × 9 orientaciones = 36

Descriptor:
105 × 36 = 3780
no es que haya 3780 "puntos" en la imagen. Es un vector que representa la distribución de orientaciones de los gradientes en las distintas regiones de la imagen
'''

if __name__ == "__main__":
    main()
