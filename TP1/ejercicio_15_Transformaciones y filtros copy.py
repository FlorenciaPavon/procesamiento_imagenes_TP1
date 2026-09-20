"""
15
Ecualización contra CLAHE
Tomá una foto con poco contraste. Aplicá cv2.equalizeHist
y cv2.createCLAHE, y guardá las dos salidas junto con sus 
histogramas. Explicá en qué casos CLAHE conviene más que la 
ecualización global.

PistaCLAHE trabaja por bloques, así que no arrastra el 
contraste de una zona a toda la imagen.
"""

import cv2
import matplotlib.pyplot as plt

ALFA = 1.4
RUTA="TP1\imagen_bajo_contraste.jpg"
BETA = 20

def ecualizacion_normal(img):
    ecualizada = cv2.equalizeHist(img)
    
    return ecualizada

'''
cv2.equalizeHist(gris)

Hace una ecualización global. Mira el histograma de
toda la imagen y redistribuye las intensidades para 
aumentar el contraste.

El problema es que trata a toda la imagen como un único conjunto.

Por ejemplo, si tenemos:

una zona oscura con detalles importantes
otra zona muy iluminada

la ecualización global busca una transformación que funcione para 
las dos zonas juntas.

CLAHE 
Contrast Limited Adaptive Histogram Equalization.

La diferencia fundamental es que divide la imagen 
en pequeños bloques (tileGridSize=(8, 8)) y trabaja 
el contraste de cada zona por separado.
Además, clipLimit=2.0 limita cuánto puede aumentar el 
contraste, evitando que el método amplifique demasiado el ruido.

'''

def ecualizacion_clahe(img):
    clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
    )
    clahe_resultado = clahe.apply(img)
    
    return clahe_resultado


def main():

    img = cv2.imread(RUTA)
    
#cv2.equalizeHist() trabaja con imagenes en escala de grises
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    normal= ecualizacion_normal(gris)
    clahe= ecualizacion_clahe(gris)

    #histogramas    
    hist_original = cv2.calcHist([gris], [0], None, [256], [0, 256])
    hist_ecualizada = cv2.calcHist([normal], [0], None, [256], [0, 256])
    hist_clahe = cv2.calcHist([clahe], [0], None, [256], [0, 256])
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.plot(hist_original)
    plt.title("Histograma original")
    plt.xlim([0, 256])

    plt.subplot(1, 3, 2)
    plt.plot(hist_ecualizada)
    plt.title("Histograma ecualizado")
    plt.xlim([0, 256])

    plt.subplot(1, 3, 3)
    plt.plot(hist_clahe)
    plt.title("Histograma CLAHE")
    plt.xlim([0, 256])

    plt.tight_layout()
    plt.show()


    cv2.imwrite("ecualizada.png", normal)
    cv2.imwrite("clahe.png", clahe)

    # Mostrar imágenes
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(gris, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(normal, cmap="gray")
    plt.title("Ecualización global")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(clahe, cmap="gray")
    plt.title("CLAHE")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

'''
CLAHE conviene cuando la imagen tiene zonas con diferentes niveles
 de iluminación o detalles locales que la ecualización global 
 podría perder. Al trabajar por bloques y limitar el aumento 
 del contraste, permite mejorar los detalles de cada zona sin 
 afectar tanto a las demás.
'''

if __name__ == "__main__":
    main()

