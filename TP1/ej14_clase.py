
import cv2


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def main():
    #histograma con cv2

    img = cv2.imread(RUTA)
    colores ¡ ¡[b,g,r]

    for canal, color in enumerate(colores):
        print(canal,color)

        histograma= cv2.calcHist(
            [img],
            [canal],
            None,
            [256],
            [0,256] #0 negro, 256 blanco
        )

'''
Desde la reduccion 1/4 se empieza a pixelar, pero en el 1/16 está casi irreconocible, 
le agregue 1/32 y ya no se sabe si es una naranja, una mancha o un globo
'''

if __name__ == "__main__":
    main()

