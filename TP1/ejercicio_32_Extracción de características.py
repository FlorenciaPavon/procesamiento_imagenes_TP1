"""
32
Robustez de los descriptores
Generá cuatro versiones de una foto: rotada 20°, escalada al 60 %, 
con brillo aumentado y con ruido. Extraé ORB de la original y de cada 
versión, emparejá con BFMatcher y armá una tabla con la cantidad de 
coincidencias buenas de cada caso. Concluí ante qué transformación ORB 
es más débil.

PistaConsiderá buena una coincidencia con distancia de Hamming menor a 
un umbral fijo, y usá el mismo umbral en los cuatro casos.
"""
import cv2
import numpy as np

RUTA= "TP1/imagen_bajo_contraste.jpg"
UMBRAL = 50

def generar_versiones(img):
    alto, ancho = img.shape[:2]

    # Rotación de 20 grados
    centro = (ancho // 2, alto // 2)
    matriz_rotacion = cv2.getRotationMatrix2D(
        centro,
        20, #grados
        1
    )

    rotada = cv2.warpAffine(
        img,
        matriz_rotacion,
        (ancho, alto)
    )

    # Escala al 60 %
    escalada = cv2.resize(
        img,
        None,
        fx=0.6,
        fy=0.6
    )

    # Aumento de brillo
    brillo = cv2.convertScaleAbs( #nuevo= alfa×original+ beta
        img,
        alpha=1,
        beta=50
    )#queda nuevo = original (porque alfa es 1) + 50. Aumentamos el brillo sin cambiar el contraste

    # Ruido gaussiano
    ruido = np.random.normal(
        0, #media
        25, #desvio estandar
        img.shape #para que genere ruido con el mismo tamaño de la imagen
    ).astype(np.int16)

    imagen_ruido = img.astype(np.int16) + ruido
    imagen_ruido = np.clip(
        imagen_ruido,
        0,
        255
    ).astype(np.uint8)

    return rotada, escalada, brillo, imagen_ruido


def extraer_orb(img):
    orb = cv2.ORB_create(
        nfeatures=1000
    )

    keypoints, descriptores = orb.detectAndCompute(
        img,
        None
    )

    return keypoints, descriptores


def contar_coincidencias(descriptores_original, descriptores_version):
    matcher = cv2.BFMatcher(
        cv2.NORM_HAMMING, #distancia de Hamming básicamente cuenta cuántos bits son diferentes entre dos descriptores.
                        #como estamos usando orb que trabaja con descriptores binarios hay que usar hamming esta normalizacion es binaria porque trabaja con bits. Cuanto menor sea la distancia mas parecidos son los descriptores
        crossCheck=True   
    )

    coincidencias = matcher.match(
        descriptores_original,
        descriptores_version
    )

    buenas = [
        coincidencia
        for coincidencia in coincidencias
        if coincidencia.distance < UMBRAL #Si la distancia de Hamming es menor a 50, considero que esa coincidencia es buena.
    ]

    return len(buenas)

def main():
    
    img = cv2.imread(
        RUTA,
        cv2.IMREAD_GRAYSCALE
    )

    rotada, escalada, brillo, ruido = generar_versiones(img)

    versiones = {
        "Rotación 20°": rotada,
        "Escala 60%": escalada,
        "Brillo aumentado": brillo,
        "Ruido": ruido
    }

    _, descriptores_original = extraer_orb(img)

    print("Cantidad de coincidencias buenas:")
    print()

    resultados = []

    for nombre, version in versiones.items():

        _, descriptores_version = extraer_orb(version)

        cantidad = contar_coincidencias(
            descriptores_original,
            descriptores_version
        )

        resultados.append(
            (nombre, cantidad)
        )

        print(f"{nombre}: {cantidad}")

    print()
    print("Tabla de resultados:")
    print("-------------------------------")
    print("Transformación       Coincidencias")
    print("-------------------------------")

    for nombre, cantidad in resultados:
        print(f"{nombre:<20} {cantidad}")
        
    print("-------------------------------")



if __name__ == "__main__":
    main()

'''
Se generaron cuatro versiones de la imagen original: una rotada 20°, 
una escalada al 60 %, una con aumento de brillo y otra con ruido. 
Se extrajeron los descriptores ORB de la imagen original y de cada versión, 
y se utilizaron BFMatcher y la distancia de Hamming para realizar 
las coincidencias. Se consideró buena una coincidencia cuando su distancia de 
Hamming fue menor a 50, utilizando el mismo umbral para todos los casos.
Los resultados muestran que el aumento de brillo produjo la mayor cantidad 
de coincidencias buenas, mientras que la imagen con ruido presentó la menor 
cantidad. La rotación de 20° mantuvo una cantidad considerable de coincidencias,
 mientras que la reducción de escala produjo una cantidad menor.

Por lo tanto, para la imagen utilizada y bajo los parámetros seleccionados, 
ORB mostró mayor dificultad frente al ruido, ya que se obtuvieron 269 
coincidencias buenas. El resultado obtenido para el ruido puede variar
 ligeramente entre ejecuciones debido a que el ruido se genera aleatoriamente.
'''
    

'''
ORB no compara directamente los píxeles de las imágenes. 
Compara sus descriptores binarios mediante distancia de Hamming.
'''

