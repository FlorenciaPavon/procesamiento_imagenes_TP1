"""
06
Separar y recombinar canales
Separá los canales de una imagen a color y guardá cada uno como imagen en escala de grises.
Después reconstruí la imagen invirtiendo el orden de los canales y observá el resultado.
Pista cv2.split y cv2.merge, o el slicing img[:, :, 0].
"""

from PIL import Image


ALFA = 1.4
RUTA="TP1/naranja.jpg"
BETA = 20

def main():

    img = Image.open(RUTA).convert("RGBA")

    rojo, verde, azul, alpha = img.split() #cuando separo se vuelve a escala de grises, por eso dice "L"

    rojo.save("Imagen_gris_rojo.png")
    verde.save("Imagen_gris_verde.png")
    azul.save("Imagen_gris_azul.png")
    alpha.save("Imagen_gris_alpha.png")

    #reconstituir pero con canales invertidos
    img_reconstituida= Image.merge("RGBA", (verde, azul, rojo, alpha))
    img_reconstituida.save("Imagen_reconstituida_desordenada.png")

if __name__ == "__main__":
    main()

