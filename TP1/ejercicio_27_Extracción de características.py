"""
27
Esquinas: Harris contra Shi-Tomasi
Detectá esquinas con cornerHarris y con goodFeaturesToTrack sobre la misma
 imagen. Dibujá los puntos de cada método en un color distinto sobre la misma
foto y comentá cuál devuelve puntos más separados entre sí.

PistagoodFeaturesToTrack tiene el parámetro minDistance, que impone esa 
separación.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

from ejercicio_25_Extraccion_de_caracteristicas import aplicar_canny, contar_bordes


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

import cv2
import numpy as np
import matplotlib.pyplot as plt

def detectar_harris(img):
    gris = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    gris = np.float32(gris)

    harris = cv2.cornerHarris(
        gris,
        blockSize=2,
        ksize=3,
        k=0.04
    )

    return harris


def detectar_shi_tomasi(img):
    puntos = cv2.goodFeaturesToTrack(
        img,
        maxCorners=100,
        qualityLevel=0.01,
        minDistance=10 #ños puntos detectados deben estar separados al menos 10 pixeles
    )

    return puntos


def dibujar_harris(img, harris):
    resultado = img.copy()

    umbral = 0.01 * harris.max() #ummbral que se usa para limite

    resultado[harris > umbral] = [0, 0, 255] #que puntos superan este umbral
                                            #recordar que 0,0,255 es rojo BGR
    return resultado


def dibujar_shi_tomasi(img, puntos):
    resultado = img.copy()

    if puntos is not None:
        for punto in puntos:
            x, y = punto.ravel()
            cv2.circle(
                resultado,
                (int(x), int(y)),
                4,
                (0, 255, 0),
                -1
            )

    return resultado


def main():
    img = cv2.imread(RUTA)

    harris = detectar_harris(img)

    puntos_shi = detectar_shi_tomasi(
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    )

    resultado_harris = dibujar_harris(
        img,
        harris
    )

    resultado_shi = dibujar_shi_tomasi(
        img,
        puntos_shi
    )

    # Guardar resultados
    cv2.imwrite(
        "esquinas_harris.png",
        resultado_harris
    )

    cv2.imwrite(
        "esquinas_shi_tomasi.png",
        resultado_shi
    )

    # Mostrar resultados
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    )
    plt.title("Imagen original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(
        cv2.cvtColor(
            resultado_harris,
            cv2.COLOR_BGR2RGB
        )
    )
    plt.title("Harris - rojo")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(
        cv2.cvtColor(
            resultado_shi,
            cv2.COLOR_BGR2RGB
        )
    )
    plt.title("Shi-Tomasi - verde")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


'''
Al aplicar ambos métodos sobre la misma imagen, Harris produjo una cantidad 
reducida de detecciones, mientras que Shi-Tomasi detectó una mayor cantidad 
de esquinas. En el caso de Shi-Tomasi se utilizó minDistance=10, que establece 
una distancia mínima entre los puntos seleccionados y evita que las detecciones 
queden demasiado agrupadas.

Por lo tanto, en esta prueba Shi-Tomasi permitió obtener una distribución de 
puntos más controlada y separados entre sí, mientras que la cantidad de 
detecciones de Harris dependió principalmente del umbral utilizado para 
seleccionar las respuestas de esquina.
'''

'''
NOTAS:
Harris devuelve una respuesta de esquina para cada píxel y después nosotros 
decidimos qué respuestas superan el umbral.

Shi-Tomasi selecciona directamente los puntos más relevantes y minDistance 
controla qué tan cerca pueden estar entre ellos.

Por eso la pista de la consigna apunta específicamente a minDistance: es el 
parámetro que te permite controlar la separación de los puntos.
'''

if __name__ == "__main__":
    main()
