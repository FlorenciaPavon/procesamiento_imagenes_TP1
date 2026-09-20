"""
23
Comparar interpolaciones
Reducí una foto al 25 % y 
volvé a ampliarla al tamaño original con INTER_NEAREST, 
INTER_LINEAR, INTER_CUBIC e INTER_AREA. 
Calculá el error cuadrático medio de cada versión contra la original 
y decidí cuál conviene para reducir y cuál para ampliar.
"""
import cv2
import numpy as np

ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def calcular_mse(original, resultado):
    diferencia = original.astype(np.float32) - resultado.astype(np.float32)
    mse = np.mean(diferencia ** 2)
    return mse #mse mide que pasa con las reducciones+ampliaciones de este ejercicio


def main():
    img = cv2.imread(RUTA)
    alto, ancho = img.shape[:2]

    nuevo_ancho = int(ancho * 0.25)
    nuevo_alto = int(alto * 0.25)

    interpolaciones = {
        "INTER_NEAREST": cv2.INTER_NEAREST,
        "INTER_LINEAR": cv2.INTER_LINEAR,
        "INTER_CUBIC": cv2.INTER_CUBIC,
        "INTER_AREA": cv2.INTER_AREA
    }

    resultados = []

    for nombre, metodo in interpolaciones.items():

        # Reducir al 25 %
        reducida = cv2.resize(
            img,
            (nuevo_ancho, nuevo_alto),
            interpolation=metodo
        )

        # Volver al tamaño original
        ampliada = cv2.resize(
            reducida,
            (ancho, alto),
            interpolation=metodo
        )

        mse = calcular_mse(img, ampliada)

        resultados.append((nombre, mse))

        cv2.imwrite(
            f"interpolacion_{nombre}.png",
            ampliada
        )

    print("Error cuadrático medio:")
    for nombre, mse in resultados:
        print(f"{nombre}: {mse:.2f}")

'''
El error cuadrático medio obtenido fue de 112,39 para INTER_NEAREST, 
15,04 para INTER_LINEAR, 
14,21 para INTER_CUBIC y 
25,87 para INTER_AREA.
Como un MSE menor indica una mayor similitud con la imagen original,
 en este experimento INTER_CUBIC presentó el menor error después de
   realizar ambas operaciones
'''

if __name__ == "__main__":
    main()

