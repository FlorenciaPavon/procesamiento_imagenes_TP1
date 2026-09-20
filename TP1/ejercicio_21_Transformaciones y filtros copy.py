"""
21Transformaciones geométricas básicas

Sobre una misma foto aplicá: traslación de (60, -25) 
píxeles, rotación de 45° respecto del centro, escalado 
al 150 % y espejado horizontal y vertical. Guardá las cinco salidas.

Pistacv2.warpAffine con la matriz correspondiente, 
y cv2.flip para el espejado.
"""


import cv2


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def traslacion(img, ancho, alto):
    matriz_traslacion = cv2.getRotationMatrix2D(
        (0, 0),
        0,
        1
    )
    matriz_traslacion[0, 2] = 60
    matriz_traslacion[1, 2] = -25

    traslacion = cv2.warpAffine(
        img,
        matriz_traslacion,
        (ancho, alto)
    )
    return traslacion

def rotacion(img, ancho, alto):
    centro = (ancho // 2, alto // 2)

    matriz_rotacion = cv2.getRotationMatrix2D(
        centro,
        45,
        1
    )

    rotacion = cv2.warpAffine(
        img,
        matriz_rotacion,
        (ancho, alto)
    )
    return rotacion

def escalado(img):
    escalado = cv2.resize(
        img,
        None, #tamaño final
        fx=1.5, #factor de escala horizontal
        fy=1.5 #factor de escala vertical
    )
    return escalado


def espejado_horizontal(img):
    espejado_horizontal = cv2.flip(img, 1)
    return espejado_horizontal

def espejado_vertical(img):
    espejado_vertical = cv2.flip(img, 0)
    return espejado_vertical

def main():
    img = cv2.imread(RUTA)
    alto, ancho = img.shape[:2]

    traslacion_img= traslacion(img, ancho, alto)
    rotacion_img= rotacion(img, ancho, alto)
    escalado_img= escalado(img)   
    espejado_horizontal_img = espejado_horizontal(img)    
    espejado_vertical_img= espejado_vertical(img)  

    cv2.imwrite("traslacion.png", traslacion_img)
    cv2.imwrite("rotacion.png", rotacion_img)
    cv2.imwrite("escalado.png", escalado_img)
    cv2.imwrite("espejado_horizontal.png", espejado_horizontal_img)
    cv2.imwrite("espejado_vertical.png", espejado_vertical_img)

'''
A
'''

if __name__ == "__main__":
    main()

