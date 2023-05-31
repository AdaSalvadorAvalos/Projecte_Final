"""
Treball Final: Ada Salvador Avalos i Milene Soledad Granda Becerra

"""
#pip install opencv-python
import cv2 as cv
#pip install pillow
from PIL import Image, ImageFilter
# python -m pip install -U matplotlib
from matplotlib import pyplot as plt
import numpy as np


class Fewfilters:  
    @staticmethod
    def componentes_rgb(fin) :
        """
        Método estático de la clase que como argumento recibe el archivo de la imagen y devuelve una lista con las componentes R,G,B por 
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
        Método estático de la clase que recibe como argumentos la dirección del archivo de la imagen que queremos separar
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
        Método estático de la clase que transforma una imagen de entrada en esa misma imagen pero en escala de grises.
        Como entrada tenemos la dirección del archivo que queremos pasar a escala de grises y la direción de la imagen
        trasformada.

        """
        image= Image.open(fin).convert("L") #de esta manera convertimos a escala de grises
        image.save(fout,"JPEG")

    @staticmethod
    def imagen_borrosa(fin, fout):
        """
        Método estático de la clase que filtra la señal con un filtro pasa-bajos guasiano de manera que la imagen que guardamos nueva
        parece borrosa.
        Como argumentos tenemos la dirección del archivo que queremos filtrar y la dirección del archivo filtrado. 
        """
        image = cv.imread(fin)
        #usamos un filtro pasa-bajos gausiano para conseguir que la imagen sea borrosa
        imagen_borrosa = cv.GaussianBlur(image,(7,7), 0) #(7,7) es el tamaño del kernel y 0 la sigma

        cv.imwrite(fout, imagen_borrosa)

    @staticmethod
    def imagen_sharpen(fin,fout):
        """
        Método estático de la clase que filtra la imagen con un filtro de la librería PIL, y realza los bordes para poder acentuar los detalles
        de la imagen.

        Como argumentos tenemos la dirección del archivo que queremos filtrar y la dirección del archivo filtrado. 

        """
        imagen = Image.open(fin)
        imagen_detalle = imagen.filter(ImageFilter.EDGE_ENHANCE)
        imagen_detalle.save(fout, "JPEG")

    @staticmethod
    def imagen_contorno(fin,fout):
        """
        Método estático de la clase que filtra la imagen con un filtro de la librería PIL, y realza el contorno y bordes.
        Detecta las áreas de cambio de intensidad y las resalta, creando un efecto de contorno.

        Como argumentos tenemos la dirección del archivo que queremos filtrar y la dirección del archivo filtrado. 

        """
        imagen = Image.open(fin)
        imagen_contorno = imagen.filter(ImageFilter.CONTOUR)
        imagen_contorno.save(fout, "JPEG")

    @staticmethod
    def imagen_EMBOSS(fin,fout):
        """
        Método estático de la clase que filtra la imagen con un filtro de la librería PIL, y realza con un filtro paso-alto(alta frecuencia) los relieves.

        Como argumentos tenemos la dirección del archivo que queremos filtrar y la dirección del archivo filtrado. 

        """
        imagen = Image.open(fin)
        imagen_EMBOSS = imagen.filter(ImageFilter.EMBOSS)
        imagen_EMBOSS.save(fout, "JPEG")
    
    @staticmethod
    def imagen_edges(fin,fout):
        """
        Método estático de la clase que filtra la imagen con un filtro de la librería PIL, y resalta los límites entre las
        regiones de la imagen, se usa para detectar los bordes.

        Como argumentos tenemos la dirección del archivo que queremos filtrar y la dirección del archivo filtrado. 

        """
        imagen = Image.open(fin)
        resultado = imagen.filter(ImageFilter.FIND_EDGES)
        resultado.save(fout, "JPEG")
    
    @staticmethod
    def imagen_modefilter(fin, fout):
        """
        Método estático de la clase que filtra la imagen con un filtro de la librería PIL, y reemplaza cada píxel con el
        más frecuente de su vecindario.

        Como argumentos tenemos la dirección del archivo que queremos filtrar y la dirección del archivo filtrado. 

        """
        imagen = Image.open(fin)
        resultado = imagen.filter(ImageFilter.ModeFilter(size=9)) #(size=9) : el tamaño de la vecindad = 3x3 alrededor de cada píxel
        resultado.save(fout, "JPEG")

    @staticmethod
    def transformada_fft(fin,fout):
        """
        Método estático de la clase que hace la transformada de fourier de la imagen fin.

        Como argumentos tenemos la dirección del archivo que queremos filtrar y la dirección del archivo filtrado. 
        """
        imagen = cv.imread(fin, 0) # 0: el cálculo se hace en escala de grises
        f = np.fft.fft2(imagen) #hace la transformada de fourier  rápida en 2D
        ffshift = np.fft.fftshift(f) # mueve el componente de 0 frecuencia al centro del espectro
        G = 20 * np.log(np.abs(ffshift))  # para ver la representación de manera logarítmica
        plt.figure()
        plt.imshow(G, cmap='gray')
        #plt.show(G)
        
        plt.savefig(fout)


    @staticmethod
    def histograma_imagen(fin,fout):
        """
        Método de la clase que calcula el histograma de la imagen de entrada.
        Parámetros:
        - fin : dirección de la imagen de entrada
        - fout : dirección de la imagen de salida
        """
        imagen = cv.imread(fin,0)
        hist = cv.calcHist([imagen],[0],None, [256],[0,256]) # calcula el histograma usando la función calcHist 
        # de la librería OpenCV. [imagen] : imagen de la que queremos calcular el histograma.[0]: indice del canal, en este caso
        # es 0 porque solo se quiere calcular del primer canal.None :máscara, ponemos None porque consideramos todos los pixeles(sin máscara) 
        # [256] : numero de bins que usamos. [0, 256] : rango de valores de pixeles  
        plt.figure() 
        plt.plot(hist)
        plt.savefig(fout) # guarda la imagen de salida

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
filtro.histograma_imagen("image/water.jpg", "resultado/hist.jpg")
filtro.transformada_fft("image/water.jpg", "resultado/fft.jpg")

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