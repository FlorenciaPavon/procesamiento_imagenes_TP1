"""
04
Simular el muestreo
Reducí la imagen a 1/2, 1/4, 1/8 y 1/16 de su tamaño, y volvé a ampliar cada versión al 
tamaño original con INTER_NEAREST. Guardá las cuatro salidas y describí a partir de cuál 
deja de reconocerse el contenido.
"""


import cv2


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def main():

    img = cv2.imread(RUTA)
    shape= img.shape
    print (shape) #alto, ancho, canales

    alto = shape[:3][0]
    ancho = shape[:3][1]

    denominadores = [2,4,6,8,16,32]

    for denominador in denominadores: 
        reduccion = cv2.resize (img, (alto//denominador, ancho//denominador)) 

        ampliacion= cv2.resize (reduccion, (alto, ancho), interpolation=cv2.INTER_NEAREST)

        cv2.imwrite(f"Imagen1_{denominador}.jpg", ampliacion)

'''
Desde la reduccion 1/4 se empieza a pixelar, pero en el 1/16 está casi irreconocible, 
le agregue 1/32 y ya no se sabe si es una naranja, una mancha o un globo
'''

if __name__ == "__main__":
    main()

