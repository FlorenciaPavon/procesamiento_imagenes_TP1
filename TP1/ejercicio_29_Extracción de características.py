"""
29
Keypoints ORB
Extraé keypoints y descriptores ORB con nfeatures en {50, 200, 1000}.
 Para cada caso imprimí cuántos puntos se encontraron realmente y la forma 
 de la matriz de descriptores, y guardá la visualización.

PistaFijate que ORB puede devolver menos puntos que los pedidos: depende 
de la textura de la imagen.
"""
import cv2


RUTA="TP1/naranja.jpg"
BETA = 20


def detectar_orb(img, cantidad):
    orb = cv2.ORB_create(nfeatures=cantidad) #crea el detector ORB indicando cuántos puntos como máximo queremos que busque.
                                            #le pase 50 pero puede detectar o devolver menos de lo pedido
    keypoints, descriptores = orb.detectAndCompute(
        img,
        None
    )

    return keypoints, descriptores


def guardar_visualizacion(img, keypoints, cantidad):
    resultado = cv2.drawKeypoints(
        img,
        keypoints,
        None,
        color=None,
        flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS
    )

    cv2.imwrite(
        f"orb_{cantidad}.png",
        resultado
    )

def main():
    
    #rectas-----------
    img = cv2.imread(RUTA, cv2.IMREAD_GRAYSCALE)

    cantidades = [50, 200, 1000]

    for cantidad in cantidades:

        keypoints, descriptores = detectar_orb(
            img,
            cantidad
        )

        print(f"\nnfeatures = {cantidad}")
        print(f"Keypoints encontrados: {len(keypoints)}")

        if descriptores is not None:
            print(f"Forma de descriptores: {descriptores.shape}")
        else:
            print("No se encontraron descriptores.")

        guardar_visualizacion(
            img,
            keypoints,
            cantidad
        )

if __name__ == "__main__":
    main()
    

'''
Se aplicó el detector ORB utilizando nfeatures de 50, 200 y 1000. Para 50 se 
encontraron 49 keypoints, para 200 se encontraron 180 y para 1000 se 
encontraron 534. En todos los casos, la matriz de descriptores presentó 32 
columnas, correspondientes al descriptor generado por ORB para cada keypoint.
 Los resultados muestran que nfeatures establece una cantidad máxima de características
 a buscar, pero ORB puede encontrar una cantidad menor dependiendo de las características
   y la textura presentes en la imagen. En este caso, al solicitar 1000 
   características solo se encontraron 534.
'''

'''
NOTAS:
keypoints, descriptores = orb.detectAndCompute(
    img,
    None
)

hace dos cosas:

1. keypoints

Son los puntos interesantes encontrados en la imagen.

Por ejemplo, pueden estar en:

esquinas
cambios de textura
detalles
zonas con bastante variación de intensidad

2. descriptores

Para cada keypoint, ORB genera una descripción numérica de la zona alrededor del punto.

Por eso la matriz normalmente tiene esta forma:

(número_de_keypoints, 32)

Por ejemplo, si obtenés:

Keypoints encontrados: 47
Forma de descriptores: (47, 32)

significa:

ORB encontró 47 puntos y generó un descriptor de 32 valores para cada uno.
'''

if __name__ == "__main__":
    main()
