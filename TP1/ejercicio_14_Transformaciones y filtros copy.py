"""
14
Histograma de una imagen
Calculá y graficá el histograma de una foto: primero en escala 
de grises y después los tres canales superpuestos. Describí en dos 
líneas qué te dice ese gráfico sobre la exposición de la foto.

Pistacv2.calcHist([img], [canal], None, [256], [0, 256]) y matplotlib 
para el gráfico.
"""

import cv2
import matplotlib.pyplot as plt

ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def histograma_gris(img_gris):
    hist_gris = cv2.calcHist( #cv2.calcHist([imagen], [canal], máscara, [cantidad_de_bins], [rango])
    [img_gris], #inagen
    [0], #un solo canal
    None, #sin mascara
    [256], # 256 intervalos
    [0, 256] #rangos de intensidades
    )

    plt.figure()
    plt.plot(hist_gris)
    plt.title("Histograma en escala de grises")
    plt.xlabel("Intensidad")
    plt.ylabel("Cantidad de píxeles")
    plt.xlim([0, 256])
    plt.show()

def histograma_color(img_color):
    hist_b = cv2.calcHist([img_color], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([img_color], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([img_color], [2], None, [256], [0, 256])

    plt.figure()

    plt.plot(hist_b, color="blue", label="Azul")
    plt.plot(hist_g, color="green", label="Verde")
    plt.plot(hist_r, color="red", label="Rojo")

    plt.title("Histograma de los canales de color")
    plt.xlabel("Intensidad")
    plt.ylabel("Cantidad de píxeles")
    plt.xlim([0, 256])
    plt.legend()

    plt.show()    

def main():

    img = cv2.imread(RUTA)
    # Convertimos a gris
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    histograma_gris(gris)
    histograma_color(img)

'''
El histograma muestra valores acumulados cerca del area de 255 
(imagen a color y gris) esto indica que hay tonos muy claros cercanos
al blanco en la mayoria de la imagen, explicado por el color del
fondo de la misma.
'''

    

if __name__ == "__main__":
    main()

