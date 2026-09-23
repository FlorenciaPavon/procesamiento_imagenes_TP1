"""
30
Descriptor global: histograma de color
Elegí tres fotos, dos parecidas y una distinta. Describí cada una con su 
histograma de color normalizado y comparalas de a pares con cv2.compareHist.
 Verificá que el par más parecido es el que esperabas.

PistaNormalizá los histogramas antes de comparar; si no, el tamaño de la 
imagen contamina la medida. Probá también la métrica de Bhattacharyya.
"""
import cv2
import numpy as np


RUTA_1 = "TP1/monedas.png"
RUTA_2 = "TP1/monedas2.png"
RUTA_3 = "TP1/imagen_bajo_contraste.jpg"

def calcular_histograma(img):
    # histograma = cv2.calcHist(
    #     [img],
    #     [0, 1, 2],
    #     None,
    #     [8, 8, 8], #divide cada canal de color en 8 intervalos 8 para B, 8 para g, 8 para R (8*8*8=512 comb de color para el histograma 3d)
    #     [0, 256, 0, 256, 0, 256]
    # )

    histogramas = []

    for canal in range(3):
        histograma = cv2.calcHist(
            [img],
            [canal],
            None,
            [256],
            [0, 256]
        )


    histograma = cv2.normalize(  #Aunque tengan exactamente la misma distribución de colores, sus histogramas tendrían cantidades diferentes porque una imagen tiene muchos más píxeles. Al normalizar, nos interesa más la distribución de los colores que la cantidad absoluta de píxeles.
        histograma,
        None,
        alpha=0,
        beta=1,
        norm_type=cv2.NORM_MINMAX
    )

    histogramas.append(histograma)

    histograma_final = np.concatenate(histogramas)

    return histograma_final


def comparar_histogramas(hist1, hist2):
    correlacion = cv2.compareHist(
        hist1,
        hist2,
        cv2.HISTCMP_CORREL
    )

    bhattacharyya = cv2.compareHist(
        hist1,
        hist2,
        cv2.HISTCMP_BHATTACHARYYA
    )

    return correlacion, bhattacharyya

def main():
    
    img1 = cv2.imread(RUTA_1)
    img2 = cv2.imread(RUTA_2)
    img3 = cv2.imread(RUTA_3)

    print("Monedas 1:", img1.shape)
    print("Monedas 2:", img2.shape)
    print("Playa:", img3.shape)

    hist1 = calcular_histograma(img1)
    hist2 = calcular_histograma(img2)
    hist3 = calcular_histograma(img3)

    comparaciones = [
        ("Foto 1 - Foto 2", hist1, hist2),
        ("Foto 1 - Foto 3", hist1, hist3),
        ("Foto 2 - Foto 3", hist2, hist3)
    ]

    for nombre, hist_a, hist_b in comparaciones:

        correlacion, bhattacharyya = comparar_histogramas(
            hist_a,
            hist_b
        )

        print(f"\n{nombre}")
        print(f"Correlación: {correlacion:.4f}")
        print(f"Bhattacharyya: {bhattacharyya:.4f}")



if __name__ == "__main__":
    main()
    

'''
NOTAS:
la correlación sea negativa. No significa automáticamente que las imágenes
 sean "muy diferentes". Lo importante en este ejercicio es comparar las tres 
 parejas usando la misma métrica y ver cuál obtiene el valor más favorable.

Para Correlación buscamos el valor más alto.

Para Bhattacharyya buscamos el valor más bajo.

Y en ambos casos gana como similitud Monedas 1 ↔ Monedas 2.
'''

if __name__ == "__main__":
    main()
