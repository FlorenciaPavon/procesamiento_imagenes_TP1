"""
12
Negativo e involución
Calculá el negativo de una imagen como 255 - f. Aplicá la operación
dos veces y comprobá con np.array_equal que se recupera exactamente 
la imagen original.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def main():

    img = cv2.imread(RUTA)
    # Convertimos a RGB para mostrarla correctamente
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #para calcular el negativo se usa una formula g = 255-f (valor nuevo = 255 - valor original)

    negativo = 255 - img_rgb
    negativo2 = 255 - negativo     #recupero la imagen original

    #compruebo que sea la imagen original
    print("La imagen original y el segundo negativo son iguales?")
    print(np.array_equal(img_rgb, negativo2)) #true

    # Mostrar las imágenes
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(negativo)
    plt.title("Primer negativo")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(negativo2)
    plt.title("Segundo negativo")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    '''
    El negativo de una imagen se obtiene aplicando la transformación
    g = 255 - f a cada píxel. Despues con la misma operación sobre 
    el negativo, se recupera el valor original.
    Esto queda verificado mediante np.array_equal, que devuelve True, 
    demostrando que ambas imágenes son exactamente iguales.
    '''

if __name__ == "__main__":
    main()

