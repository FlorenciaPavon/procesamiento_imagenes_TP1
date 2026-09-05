"""
02
Leer un píxel en las dos bibliotecas
Imprimí el valor del píxel (0, 0) y el del píxel central usando Pillow y usando OpenCV. 
Verificá que los tres números son los mismos pero en orden invertido, y dejá escrito cuál es cuál.
"""

import cv2
from PIL import Image

ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def main():

    img = cv2.imread(RUTA)
    img_pill= Image.open(RUTA)
    #print(img)
    #print(img_pill)


    #con pillow    
    ancho_alto = img_pill.size
    print(type(ancho_alto))  #devuelve una tupla

    pixel_origen= img_pill.getpixel((0,0))
    print("El valor del origen de coordenadas es", pixel_origen) #Orden RGBA

    '''
    el metodo size devuelve una tupla con el orden (ancho, alto)
    puedo indexar para obterner estos valores y despues buscar el centro
    o directamente desempaquetar la tupla con los valores que ya se que da
    '''

    (ancho, alto) = img_pill.size
    print ("El ancho es: ", ancho)
    print ("El alto es: ", alto)

    pixel_centro = img_pill.getpixel((ancho//2, alto//2))
    print("El pixel central es: ", pixel_centro)
   
    #con OpenCV
    tamanio= img.shape 
    print(tamanio)

    '''
    OpenCV trabaja internamente con Numpy, por lo que se maneja con arrays
    El orden es distinto [alto, ancho]
    '''

    pixel_origen_ocv= img[0,0]    
    print("El pixel de oringen con OpenCV es: ", pixel_origen_ocv) #los presenta al reves BGRA

    (alto, ancho) = img.shape[:2]#slicing, porque necesito solo dos valores 
    pixel_centro_ocv= img[alto//2, ancho//2]
    print("El pixel del centro con OpenCV es, ", pixel_centro_ocv)

if __name__ == "__main__":
    main()

