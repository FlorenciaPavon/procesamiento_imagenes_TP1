"""
03
Cuánto pesa una imagen
Calculá cuántos bytes ocupa la imagen en memoria (alto × ancho × canales × bytes por valor) 
y compará ese número con el tamaño del archivo en disco. Explicá la diferencia.
"""

import cv2
from PIL import Image

ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def main():

    img = cv2.imread(RUTA, cv2.IMREAD_UNCHANGED) #UNCHANGED, no me saca el canal Alpha de transparencia  
    tipo = img.dtype
    shape= img.shape

    print("Shape: ", shape) 
    print("Tipo de dato: ", tipo) #uint8, cada canal ocupa un byte, son 4 canales RGBA

    bytes_totales= shape[0] * shape[1] * shape[2] * 1  
    print("Los bytes totales de la imagen pura son: ", bytes_totales)  
    #tambien se podia usar nbytes --> print(img.nbytes)   
    
    # 1024 bytes = 1 KB
    byte_a_kb = bytes_totales // 1024 
    print("En Kb: ", byte_a_kb, " KB")


    '''
    En el disco la imagen pesa 155KB JPG, mientras que en los cálculos verdaderos 
    da 825KB. Esto se debe a que el formato JPG comprime la imagen para hacerla 
    eficiente para almacenamiento, pero puede ocasionar perdidas de informacion
    '''

if __name__ == "__main__":
    main()

