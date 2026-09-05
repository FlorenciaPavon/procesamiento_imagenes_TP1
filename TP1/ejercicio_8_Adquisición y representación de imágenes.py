"""
08
Recorrido por los espacios de color
Pasá la misma imagen a gris, HSV y Lab. Guardá cada canal por separado e indicá en 
cuál de ellos está la información de color y en cuál la de iluminación.

Pista Guardar el canal H directamente se ve raro porque va de 0 a 179: reescalalo para inspeccionarlo.
"""

import cv2
import numpy as np


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def gris(img):
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gris.jpg", gris)
    #todo iluminacion sin color

def lab(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    L= lab[:,:,0]
    A= lab[:,:,1]
    B= lab[:,:,2]

    cv2.imwrite("lab_l.jpg", L) #color
    cv2.imwrite("lab_a.jpg", A)
    cv2.imwrite("lab_b.jpg", B) #iluminacion
    

def hsv(img):
    hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    H= hsv[:,:,0]
    S= hsv[:,:,1]
    V=hsv[:,:,2]

    H_visual = (H.astype(np.float32) * 255 / 179).astype(np.uint8) #reescalado

    cv2.imwrite("hsv_H.jpg", H_visual) #color
    cv2.imwrite("hsv_S.jpg", S)
    cv2.imwrite("hsv_V.jpg", V) #iluminacion    

def main():

    img = cv2.imread(RUTA, cv2.IMREAD_UNCHANGED) 

    gris(img)
    lab(img)
    hsv(img) 
         

if __name__ == "__main__":
    main()

