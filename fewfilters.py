"""
Treball Final: Ada Salvador Avalos i Milene Soledad Granda Becerra

"""
#pip install opencv-python
import cv2 as cv
#pip install pillow
from PIL import Image
#visuales
import tkinter as tk
#clase hecha para poder hacer el zoom en la imagen
from Zoom import ImagenZoom

class Fewfilters:
    @staticmethod
    def componentes_rgb(fin) :
        image = Image.open(fin)
        #convierte a RGB dado que contenedores como png no usan estos componentes.
        image = image.convert("RGB")
        #creamos una lista con las mismas dimensiones que la imagen de entrada
        ancho, alto = image.size
        lista_RGB = []
        
        for y in range(alto):
            for x in range(ancho):
                r, g, b = image.getpixel((x,y))
                lista_RGB.append((r, g, b))

        return lista_RGB

    @staticmethod
    def imagenes_RGB(fin, fout_R, fout_G, fout_B ) :
        rgb_componentes = Fewfilters.componentes_rgb(fin)
        image =Image.open(fin)

        nombre_archivo, nom_extension = fin.split('.')

        #creamos una imagen en blanco
        image_R = Image.new("RGB", image.size)
        image_G = Image.new("RGB", image.size)
        image_B = Image.new("RGB", image.size)

        #cargamos cada valor para cada pixel
        pixel_R = [(value[0], 0, 0) for value in rgb_componentes]
        pixel_G = [(0,value[1], 0) for value in rgb_componentes]
        pixel_B = [(0, 0, value[2]) for value in rgb_componentes]

        image_R.putdata(pixel_R)
        image_G.putdata(pixel_G)
        image_B.putdata(pixel_B)

        #ahora lo guardamos todo como jpg 
        image_R.save(fout_R,"JPEG")
        image_G.save(fout_G,"JPEG")
        image_B.save(fout_B,"JPEG")

    @staticmethod
    def imagen_BW(fin, fout):
        image= Image.open(fin).convert("L") #de esta manera convertimos a escala de grises
        image.save(fout,"JPEG")

    @staticmethod
    def imagen_borrosa(fin, fout):
        image = cv.imread(fin)
        #usamos un filtro pasa-bajos gausiano para conseguir que la imagen sea borrosa
        imagen_borrosa = cv.GaussianBlur(image,(7,7), 0) #(7,7) es el tamaño del kernel y 0 la sigma

        cv.imwrite(fout, imagen_borrosa)


"""
    #PRUEBAS
    imagenes_RGB("image/water.jpg", "resultat/red_w.jpg", "resultat/green_w.jpg", "resultat/blue_w.jpg")
    imagenes_RGB("image/colors.png", "resultat/red_c.jpg", "resultat/green_c.jpg", "resultat/blue_c.jpg")
    imagen_BW("image/water.jpg", "resultat/water_bw.jpg")
    imagen_borrosa("image/water.jpg", "resultat/water_blur.jpg")
    #prueba zoom :
    raiz = tk.Tk()
    raiz.geometry('800x600')
    imagen = ImagenZoom(raiz)
    imagen.pack(fill= tk.BOTH, expand= tk.YES)
    imagen.set_imagen("image/water.jpg")
    raiz.mainloop()
    """