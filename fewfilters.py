"""
Treball Final: Ada Salvador Avalos i Milene Soledad Granda Becerra

"""
#pip install opencv-python
import cv2 as cv
#pip install pillow
from PIL import Image, ImageFilter


class Fewfilters:  
    @staticmethod
    def componentes_rgb(fin) :
        """
        Función que como argumento recibe el archivo de la imagen y devuelve una lista con las componentes R,G,B por 
        separado.
        
        """
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
        """
        Función que recibe como argumentos la dirección del archivo de la imagen que queremos separar
        por componentes R,G,B y la dirección de las tres imágenes pasadas a jpeg, cada una con una 
        lista de un componente R, G, B, respectivamente.
        """
        rgb_componentes = Fewfilters.componentes_rgb(fin)
        image =Image.open(fin)

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
        """
        Función que transforma una imagen de entrada en esa misma imagen pero en escala de grises.
        Como entrada tenemos la dirección del archivo que queremos pasar a escala de grises y la direción de la imagen
        trasformada.

        """
        image= Image.open(fin).convert("L") #de esta manera convertimos a escala de grises
        image.save(fout,"JPEG")

    @staticmethod
    def imagen_borrosa(fin, fout):
        """
        Función filtra la señal con un filtro pasa-bajos guasiano de manera que la imagen que guardamos nueva
        parece borrosa.
        Como argumentos tenemos la dirección del archivo que queremos filtrar y la dirección del archivo filtrado. 
        """
        image = cv.imread(fin)
        #usamos un filtro pasa-bajos gausiano para conseguir que la imagen sea borrosa
        imagen_borrosa = cv.GaussianBlur(image,(7,7), 0) #(7,7) es el tamaño del kernel y 0 la sigma

        cv.imwrite(fout, imagen_borrosa)

    @staticmethod
    def imagen_sharpen(fin,fout):
        imagen = Image.open(fin)
        imagen_detalle = imagen.filter(ImageFilter.EDGE_ENHANCE)
        imagen_detalle.save(fout, "JPEG")

    @staticmethod
    def imagen_contorno(fin,fout):
        imagen = Image.open(fin)
        imagen_contorno = imagen.filter(ImageFilter.CONTOUR)
        imagen_contorno.save(fout, "JPEG")

    @staticmethod
    def imagen_EMBOSS(fin,fout):
        imagen = Image.open(fin)
        imagen_EMBOSS = imagen.filter(ImageFilter.EMBOSS)
        imagen_EMBOSS.save(fout, "JPEG")
    
    @staticmethod
    def imagen_edges(fin,fout):
        imagen = Image.open(fin)
        resultado = imagen.filter(ImageFilter.FIND_EDGES)
        resultado.save(fout, "JPEG")
    
    @staticmethod
    def imagen_modefilter(fin, fout):

        imagen = Image.open(fin)
        resultado = imagen.filter(ImageFilter.ModeFilter(size=9))
        resultado.save(fout, "JPEG")

    @staticmethod
    def transformada_dft(fin,fout):
        pass
    #PRUEBAS
    
filtro = Fewfilters()
"""
filtro.imagenes_RGB("image/water.jpg", "resultat/red1_w.jpg", "resultat/green1_w.jpg", "resultat/blue1_w.jpg")
filtro.imagenes_RGB("image/colors.png", "resultat/red1_c.jpg", "resultat/green1_c.jpg", "resultat/blue1_c.jpg")
filtro.imagen_BW("image/water.jpg", "resultat/water1_bw.jpg")
filtro.imagen_borrosa("image/water.jpg", "resultat/water1_blur.jpg")

filtro.imagen_sharpen("image/water.jpg", "resultado/sharp.jpg")
filtro.imagen_contorno("image/water.jpg", "resultado/contorno.jpg")
filtro.imagen_EMBOSS("image/water.jpg", "resultado/EMBOSS.jpg")
filtro.imagen_edges("image/water.jpg", "resultado/EDGES.jpg")
filtro.imagen_modefilter("image/water.jpg", "resultado/mode.jpg")
"""
    #prueba zoom :
"""
    raiz = tk.Tk()
    raiz.geometry('800x600')
    imagen = ImagenZoom(raiz)
    imagen.pack(fill= tk.BOTH, expand= tk.YES)
    imagen.set_imagen("image/water.jpg")
    raiz.mainloop()
 """