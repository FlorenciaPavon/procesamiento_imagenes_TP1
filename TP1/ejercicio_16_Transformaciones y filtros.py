"""
16
Tres umbralizaciones
Sobre desigual.png aplicá umbral fijo en 127, 
umbral de Otsu y umbral adaptativo. 
Guardá las tres binarias y explicá por qué el 
umbral global falla con iluminación despareja.

Pistacv2.threshold con THRESH_OTSU, y 
cv2.adaptiveThreshold con ADAPTIVE_THRESH_GAUSSIAN_C.
"""

import cv2


ALFA = 1.4
RUTA="TP1/imagen_bajo_contraste.jpg"
BETA = 20

def umbral_fijo(img):
    _, umbral_fijo = cv2.threshold(
    img,
    127, #limite si es mayor a este nro se considera 255 o blanco, si es menor negro
    255,
    cv2.THRESH_BINARY
    )
    return umbral_fijo

def umbral_otsu(img): #(otsu es global)
    _, umbral_otsu = cv2.threshold(
    img,
    0, # #Otsu analiza el histograma y busca automáticamente un valor que separe los niveles de intensidad en dos grupos.
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return umbral_otsu

'''
Adaptativo: En lugar de usar un único umbral para toda la imagen,
 calcula el umbral considerando los píxeles de una zona cercana.

Por eso puede funcionar mejor cuando una parte de la imagen 
está más iluminada que otra.
'''

def umbral_adaptativo(img):
    umbral_adaptativo = cv2.adaptiveThreshold(
    img,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, #ventana de 11x11 pixeles
    2
    )
    return umbral_adaptativo

def main():

    img = cv2.imread(RUTA)
    

    img_gris = cv2.imread(RUTA, cv2.IMREAD_GRAYSCALE)
    

    fijo= umbral_fijo(img_gris)
    otsu= umbral_otsu(img_gris)
    adaptativo = umbral_adaptativo(img_gris)

    cv2.imwrite("umbral_fijo.png", fijo)
    cv2.imwrite("umbral_otsu.png", otsu)
    cv2.imwrite("umbral_adaptativo.png", adaptativo)


    '''
    El umbral global utiliza un único valor para toda la imagen, 
    por lo que una zona oscura y una zona iluminada reciben 
    el mismo tratamiento. Con iluminación despareja, algunos 
    objetos pueden quedar correctamente separados en una zona
    pero perderse en otra. 
    El umbral adaptativo puede solucionar este problema porque 
    calcula el umbral según las características locales de cada región.
    '''

if __name__ == "__main__":
    main()

