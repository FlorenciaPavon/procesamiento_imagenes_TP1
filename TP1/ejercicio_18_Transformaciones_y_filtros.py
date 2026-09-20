"""
18
Comparar suavizados
Aplicá blur, GaussianBlur, medianBlur y bilateralFilter 
con parámetros equivalentes sobre la misma foto. Ordená 
los cuatro resultados de más a menos nítido usando la
 varianza del laplaciano como medida.

Pistacv2.Laplacian(gris, cv2.CV_64F).var() es un estimador 
simple de nitidez.
"""
'''
recordar: 
blur → promedio simple de los vecinos.
GaussianBlur → promedio ponderado, dando más importancia a 
los píxeles cercanos.
medianBlur → reemplaza cada píxel por la mediana de sus vecinos; 
es especialmente útil contra ruido tipo “sal y pimienta”.
bilateralFilter → suaviza pero intenta conservar los bordes.
'''


import cv2
import numpy as np
import time

ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def calcular_nitidez(img):
    if len(img.shape) == 3:
        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gris = img

    laplaciano = cv2.Laplacian(gris, cv2.CV_64F)

    return laplaciano.var()
def main():

    img = cv2.imread(RUTA, cv2.IMREAD_GRAYSCALE)

    # cuatro suavizados
    resultado_blur = cv2.blur(img, (5, 5))

    resultado_gaussian = cv2.GaussianBlur(
        img,
        (5, 5), #kernel
        0
    )

    resultado_median = cv2.medianBlur(
        img,
        5 #vecindario de 5x5
    )

    resultado_bilateral = cv2.bilateralFilter(
        img,
        9, #diametro
        75, #cuanto influya la diferencia de intensidad o color
        75 #cuanto influye la distancia espacial
    )

    # nitidez
    nitidez_blur = calcular_nitidez(resultado_blur)
    nitidez_gaussian = calcular_nitidez(resultado_gaussian)
    nitidez_median = calcular_nitidez(resultado_median)
    nitidez_bilateral = calcular_nitidez(resultado_bilateral)

    resultados = [
        ("blur", nitidez_blur),
        ("GaussianBlur", nitidez_gaussian),
        ("medianBlur", nitidez_median),
        ("bilateralFilter", nitidez_bilateral)
    ]

    # Ordenamos de mayor a menor nitidez
    resultados.sort(key=lambda x: x[1], reverse=True)

    print("Orden de más a menos nítido:")

    for nombre, valor in resultados:
        print(f"{nombre}: {valor:.2f}")    
  


'''
Orden de nitidez: medianBlur (11,03) > GaussianBlur (4,76) > bilateralFilter (2,78) > blur (2,45). 
La varianza del Laplaciano se utilizó como medida de nitidez,
ya que valores mayores indican una mayor presencia de cambios 
bruscos de intensidad asociados a los bordes. 
El orden obtenido corresponde a la imagen utilizada y a
 los parámetros seleccionados para cada filtro.
'''

if __name__ == "__main__":
    main()

