"""
17
Convolución a mano
Implementá la convolución 2D con bucles para un kernel de
promedio 3×3 sobre una imagen en gris. Compará el resultado 
con cv2.filter2D usando la diferencia absoluta máxima, y medí
 cuántas veces más lento es tu código.

PistaUna diferencia de un nivel es esperable por redondeo. 
Si la diferencia es grande, revisá si estás invirtiendo el 
kernel: filter2D hace correlación, no convolución estricta.
"""

import cv2
import numpy as np
import time

ALFA = 1.4
RUTA="TP1/imagen_bajo_contraste.jpg"
BETA = 20

def convolucion_manual(img, kernel):
    alto, ancho = img.shape

    resultado = np.zeros_like(img, dtype=np.float32) #matriz llena de 0

    # solamente los píxeles que tienen vecinos alrededor
    for i in range(1, alto - 1): #menos los bordes por eso alto - 1 , ancho - 1
        for j in range(1, ancho - 1):

            region = img[i - 1:i + 2, j - 1:j + 2] #los 9 pixeles que rodean al pixel actual

            resultado[i, j] = np.sum(region * kernel)

    return np.clip(resultado, 0, 255).astype(np.uint8) #resultados limitados entre 0 y 2555


def main():

    img = cv2.imread(RUTA, cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((3, 3), dtype=np.float32) / 9 #matriz a aplicar 1/9

    # Convolución manual
    inicio = time.perf_counter()
    resultado_manual = convolucion_manual(img, kernel)
    fin = time.perf_counter()
    tiempo_manual = fin - inicio

     # OpenCV
    inicio = time.perf_counter()
    resultado_opencv = cv2.filter2D(img, -1, kernel) #-1 es para que use la misma profundodad que la imagen de entrada (uint8)
    fin = time.perf_counter()
    tiempo_opencv = fin - inicio

     # Diferencia absoluta máxima
    diferencia = cv2.absdiff(resultado_manual, resultado_opencv)
    diferencia_maxima = np.max(diferencia)
    print("Diferencia absoluta máxima:", diferencia_maxima)

    #no daba bien la diferencia absoluta, daba 197, veo si es el borde
    # Diferencia máxima solamente en el interior de la imagen
    diferencia_interior = cv2.absdiff(
        resultado_manual[1:-1, 1:-1],
        resultado_opencv[1:-1, 1:-1]
    )

    # Diferencia sin tener en cuenta los bordes
    diferencia_interior = cv2.absdiff(
    resultado_manual[1:-1, 1:-1],
    resultado_opencv[1:-1, 1:-1]
    )

    diferencia_maxima_interior = np.max(diferencia_interior)

    print("Diferencia absoluta máxima en el interior:", diferencia_maxima_interior)

    diferencia_maxima_interior = np.max(diferencia_interior)

    print("Diferencia absoluta máxima en el interior:",
        diferencia_maxima_interior)

    # Cuántas veces es más lento el método manual
    veces_mas_lento = tiempo_manual / tiempo_opencv

    print("Tiempo convolución manual:", tiempo_manual)
    print("Tiempo filter2D:", tiempo_opencv)
    print("Diferencia absoluta máxima:", diferencia_maxima)
    print("El método manual es aproximadamente",
          veces_mas_lento,
          "veces más lento.")

    cv2.imwrite("convolucion_manual.png", resultado_manual)
    cv2.imwrite("convolucion_filter2D.png", resultado_opencv)


'''
La convolucion manual presentó una diferencia 
absoluta máxima de 197 respecto de cv2.filter2D. Sin embargo, 
al excluir los bordes de la imagen, la diferencia máxima fue 
de 1 nivel, lo cual coincide con el margen de redondeo esperado.
 La diferencia en los bordes se debe a que ambas implementaciones 
 utilizan un tratamiento diferente de los píxeles que no tienen
   un vecindario 3×3 completo.

En cuanto al rendimiento, la implementación manual tardó 
aproximadamente 102,51 segundos, mientras que cv2.filter2D 
tardó 0,0166 segundos. Por lo tanto, la implementación manual
fue aproximadamente 6172 veces más lenta. Esto muestra 
la ventaja de utilizar funciones optimizadas de OpenCV 
frente a recorrer los píxeles mediante bucles de Python
'''

if __name__ == "__main__":
    main()

