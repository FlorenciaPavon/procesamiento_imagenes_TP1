"""
28
Transformada de Hough
Detectá las rectas de una foto de un edificio o de una hoja cuadriculada 
con HoughLinesP, y los círculos de piezas.png con HoughCircles. Dibujá las
 detecciones y ajustá los parámetros hasta que no queden falsos positivos
   evidentes.

PistaHough trabaja sobre bordes: pasá primero por Canny para las rectas. 
En HoughCircles, minDist y param2 son los que más cambian el resultado.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


ALFA = 1.4
RUTA="TP1/hoja_cuadriculada.png"
RUTA2="TP1/monedas.png"
BETA = 20


def detectar_rectas(img):
    gris = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    bordes = cv2.Canny(
        gris,
        50,
        150
    )

    rectas = cv2.HoughLinesP(
        bordes,
        rho=1, #resolución de distancia utilizada para buscar las rectas
        theta=np.pi / 180, #Es la resolución angular buscando direcciones cada 1 grado
        #threshold=50, #umbral minimo que necesita una recta para ser considerada
        threshold=45,
        minLineLength=50, #long minima de una recta detectada
        maxLineGap=10 #Permite unir segmentos que están separados por pequeños espacios
    )

    return rectas

def dibujar_rectas(img, rectas):
    resultado = img.copy()

    if rectas is not None:
        for recta in rectas:
            x1, y1, x2, y2 = recta[0]

            cv2.line(
                resultado,
                (x1, y1),
                (x2, y2),
                (0, 0, 255), #en OCV es rojo BGR
                2
            )

    return resultado

def detectar_circulos(img):
    gris = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    gris = cv2.GaussianBlur(
        gris,
        (5, 5),
        0
    )

    circulos = cv2.HoughCircles(
        gris,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=30,  #distancia mínima entre los centros de dos círculos detectados. Si es muy bajo ej 000 puede detectar varios círculos muy cercanos para el mismo objeto, pero si es mas alto ej: 0        0 obliga a que las detecciones estén más separadas
        param1=100,
        #param2=30, #umbral utilizado para decidir qué candidatos se consideran círculos si es bajo hay +detecciones y mas falsos positivos, pero si es mas alto menos detecciones y mas selectivas
        param2=35, #ajuste porque detecto mas circulos com 30 (falsos positivos)
        minRadius=10,
        maxRadius=100
    )

    return circulos

def dibujar_circulos(img, circulos):
    resultado = img.copy()

    if circulos is not None:
        circulos = np.uint16(
            np.around(circulos)
        )

        for x, y, radio in circulos[0]:
            cv2.circle(
                resultado,
                (x, y),
                radio,
                (0, 255, 0),
                2
            )

            cv2.circle(
                resultado,
                (x, y),
                2,
                (0, 255, 0),
                3
            )

    return resultado

def main():
    
    #rectas-----------
    img_rectas = cv2.imread(RUTA)

    rectas = detectar_rectas(
        img_rectas
    )

    resultado_rectas = dibujar_rectas(
        img_rectas,
        rectas
    )

    #circulos--------------------
    img_circulos = cv2.imread(RUTA2)

    circulos = detectar_circulos(
        img_circulos
    )

    resultado_circulos = dibujar_circulos(
        img_circulos,
        circulos
    )

    #guardado---------------------------------------
    cv2.imwrite(
        "hough_rectas.png",
        resultado_rectas
    )

    cv2.imwrite(
        "hough_circulos.png",
        resultado_circulos
    )

if __name__ == "__main__":
    main()
    

'''
En la detección de círculos se utilizó inicialmente param2=30, 
con el cual se detectaron las seis monedas, pero también aparecieron 
tres falsos positivos. Al aumentar param2 a 35, se mantuvieron las seis
 monedas detectadas y desaparecieron los falsos positivos. Por lo tanto, 
 se seleccionó param2=35, ya que permitió obtener una detección más precisa
   para la imagen utilizada.
'''

'''
NOTAS:
subir param2 hace que HoughCircles sea más exigente antes de considerar 
que encontró un círculo
'''

if __name__ == "__main__":
    main()
