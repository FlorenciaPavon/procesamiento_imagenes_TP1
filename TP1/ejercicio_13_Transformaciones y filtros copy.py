"""
13
13
Corrección gamma con tabla de consulta
Construí una LUT de 256 entradas y aplicá corrección gamma con
 γ = 0.4, 1.0 y 2.2. 
 Compará el tiempo de ejecución de la LUT contra hacer la misma 
 cuenta píxel por píxel con dos bucles.

Pistacv2.LUT(img, tabla); la tabla es ((i / 255) ** gamma) * 255 
para i entre 0 y 255. Medí con time.perf_counter().

¿Qué es una LUT?

Una LUT es simplemente una tabla que tiene precalculado el 
resultado para cada posible valor de píxel.

Como una imagen de 8 bits puede tener valores de 0 a 255,
necesitamos solamente 256 entradas. Entonces, en lugar de
calcular la fórmula para cada píxel, buscamos directamente el resultado correspondiente en la tabla.
"""



import cv2
import numpy as np
import time
import matplotlib.pyplot as plt



ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def crear_lut(gamma):
    tabla = np.array([
        ((i / 255) ** gamma) * 255 #formula del ejercicio, calculo el resultado paara cada uno
        for i in range(256)
    ], dtype=np.uint8)

    return tabla

def gamma_pixel_por_pixel(img, gamma):
    resultado = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            resultado[i, j] = (
                (img[i, j] / 255.0) ** gamma
            ) * 255

    return resultado


def main():

    img = cv2.imread(RUTA)
    # Convertimos a RGB para mostrarla correctamente
    gammas = [0.4, 1.0, 2.2]

    for gamma in gammas:
        tabla = crear_lut(gamma)

        inicio = time.perf_counter()

        resultado_lut = cv2.LUT(img, tabla)

        fin = time.perf_counter()

        tiempo_lut = fin - inicio

        # Método píxel por píxel
    
        inicio = time.perf_counter()

        resultado_pixel = gamma_pixel_por_pixel(img, gamma)

        fin = time.perf_counter()

        tiempo_pixel = fin - inicio

        print(f"\nGamma = {gamma}")
        print(f"Tiempo con LUT: {tiempo_lut:.6f} segundos")
        print(f"Tiempo píxel por píxel: {tiempo_pixel:.6f} segundos")

        plt.figure(figsize=(12, 4))

for i, gamma in enumerate(gammas):
    tabla = crear_lut(gamma)
    resultado = cv2.LUT(img, tabla)

    plt.subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
    plt.title(f"Gamma = {gamma}")
    plt.axis("off")

plt.tight_layout()
plt.show()

'''
Tiempo con LUT: 0.000287 segundos
Tiempo píxel por píxel: 1.604238 segundos

El tiempo con LUT es mucho mas rapido ya que partimos desde una tabla
ya creada. una LUT evita repetir una operación matemática 
para cada píxel. Como solamente existen 256 valores posibles 
por canal, calculamos esos 256 resultados una sola vez 
y después simplemente buscamos el resultado correspondiente

tambien:
gana = 0.4 → aclara bastante las zonas oscuras.
gama  = 1.0 → prácticamente no modifica la imagen.
gama = 2.2 → oscurece las zonas de la imagen.

'''

    

if __name__ == "__main__":
    main()

