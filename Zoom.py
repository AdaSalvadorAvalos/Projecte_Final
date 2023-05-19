import tkinter as tk
from PIL import Image, ImageTk

class ImagenZoom(tk.Canvas) :
    def __init__(self, master, **argumentos):
        super().__init__(master, **argumentos)
        self.imagen = None
        self.imagen_tk = None
        self.factor_zoom = 1.0
        self.x_start = None
        self.y_start = None
        self.bind('<MouseWheel>', self.zoom)
        self.bind('<Button-4>', self.zoom)
        self.bind('<Button-5>', self.zoom)
        self.bind('<ButtonPress-1>', self.start_scroll)
        self.bind('<B1-Motion>', self.scroll)
        self.bind('<ButtonRelease-1>', self.stop_scroll)
        self.bind('<MouseWheel>', self.zoom)
        self.bind('<Configure>', self.actualizar_imagen)

    def set_imagen(self, fin) :
        self.imagen = Image.open(fin)
        self.actualizar_imagen()
    

    def actualizar_imagen(self, event= None):
        ancho, largo = self.imagen.size
        ancho_conzoom = int(ancho * self.factor_zoom)
        largo_conzoom = int(largo * self.factor_zoom)
        self.imagenconzoom = self.imagen.resize((ancho_conzoom, largo_conzoom), Image.ANTIALIAS)
        self.imagen_tk = ImageTk.PhotoImage(self.imagenconzoom)
        self.config(scrollregion= self.bbox(tk.ALL))
        self.create_image(0,0,image=self.imagen_tk,anchor=tk.NW)

    def zoom(self, event):
        if event.delta > 0:
            self.factor_zoom *= 1.1
        else :
            self.factor_zoom *= 0.9
        self.actualizar_imagen()

    
    def start_scroll(self, event) :
        self.x_start = event.x
        self.y_start = event.y

    def scroll(self, event) :
        if self.x_start is not None and self.y_start is not None :
            delta_x = self.x_start - event.x 
            delta_y = self.y_start - event.y
            self.x_start = event.x
            self.y_start = event.y
            self.xview_scroll(delta_x,'units')
            self.yview_scroll(delta_y, 'units')

    def stop_scroll(self, event) :
        self.x_start = None
        self.y_start = None

        

