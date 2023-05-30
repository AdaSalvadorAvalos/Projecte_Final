import tkinter as tk
from PIL import Image, ImageTk

class ImagenZoom(tk.Canvas) : # deriva de la clase tk.Canvas para tener una área rectangular para poder mostrar la imagen seleccionada.
    """
    Clase que consigue que en un archivo de imagen se pueda hacer zoom in y zoom out y verse a tiempo real en una ventana
    usando la libreria tkinter, también usa el módulo PIL para trabajar con imágenes.
    
    """
    def __init__(self, master, **argumentos): 
        """
        Constructor de la clase, relaciona el hardware con la función que se quiere realizar.
        Inicializa la imagen, el factor de zoom, y la posición inicial para hacer el zoom. Une la rueda del ratón,
        los eventos de los botones, y el evento de cambio de tamaño de la ventana a sus funciones respectivas.
        Parámetros del método:
        - master: "widget" maestro, donde está la ventana inicial(raíz), instáncia de tk.Tk() en la que se colocará el 
        "widget" de ImagenZoom.
        - **argumentos : permite pasar argumentos de palabras clave adicionales al constructor, se pueden usar para 
        configurar el "widget" de ImagenZoom entre otras cosas.
        - self: instáncia de la clase, para poder acceder a los métodos de la clase.

        """
        super().__init__(master, **argumentos) # llama al constructor de la clase heredada tk.Canvas para poder inicializar el "widget"
        self.imagen = None
        self.imagen_tk = None
        self.factor_zoom = 1.0
        self.x_start = None
        self.y_start = None
        self.bind('<MouseWheel>', self.zoom)
        self.bind('<Button-4>', self.zoom)
        self.bind('<Button-5>', self.zoom)
        self.bind('<MouseWheel>', self.zoom)
        self.bind('<Configure>', self.actualizar_imagen)

    def set_imagen(self, fin) :
        """
        Método que abre la imagen y la actualiza.
        Parámetros del método:
        - self: instáncia de la clase, para poder acceder a los métodos de la clase.
        - fin : dirección del archivo que queremos usar.
        """
        self.imagen = Image.open(fin)
        self.actualizar_imagen()
    

    def actualizar_imagen(self, event= None):
        """
        Método que cambia el tamaño de la imagen basándose en el factor de zoom y actualiza el canvas con la imagen cambiada de tamaño.
        Este método se puede usar directamente o como resultado de que ha sucedido un evento.
        Parámetros del método:
        - self: instáncia de la clase, para poder acceder a los métodos de la clase.
        - event= None: parámetro opcional que representa un evento. Se utliza cuando se llama al objeto porque ha sucedido un
        evento (ej. al cambiar el tamaño de la ventana). De forma predeterminada es None.
        """
        if self.imagen!=None: #mira si la imagen se ha pasado como atributo de la imagen
            ancho, largo = self.imagen.size
            # calcula las nuevas dimensiones, multiplica el factor de zoom con el ancho y largo inicial de la imagen (conseguidos en la línea anterior)
            ancho_conzoom = int(ancho * self.factor_zoom)
            largo_conzoom = int(largo * self.factor_zoom)
            # cambia el tamaño de la imagen con el metodo resize del módulo PIL para cambiar el tamaño de la imagen original
            # a el nuevo como argumentos toma el nuevo ancho  y largo  y usa el filtro Image.ANTIALIAS para mejorar la calidad de la imagen.
            self.imagenconzoom = self.imagen.resize((ancho_conzoom, largo_conzoom), Image.ANTIALIAS)
            # crea una imagen compatible con tkinter a partir de la nueva imagen, que se utliza para mostrar la imagen en el canvas
            self.imagen_tk = ImageTk.PhotoImage(self.imagenconzoom)
            # actualiza el lienzo (canvas) configura la región desplazable (scrollregion) usando el método bbox para usar toda la imagen
            self.config(scrollregion= self.bbox(tk.ALL))
            # finalmente, llama al método create_image para mostrar la imagen en el canvas anchor=tk.NW: la imagen esta en la esquina noroeste del canvas.
            self.create_image(0,0,image=self.imagen_tk,anchor=tk.NW)

    def zoom(self, event):
        """
        Este método ajusta el factor de zoom en función de la rueda del ratón o del los eventos del botón y llama al método
        actualizar_imagen() para actualizar esta.
        Parámetros del método:
        - self: instáncia de la clase, para poder acceder a los métodos de la clase.
        - event : es el objeto del evento que provocó la acción del zoom.(Con el ratón o un botón)
        """
        if event.delta > 0: # si delta es más grande que 0 significa que se ha movido la rueda del ratón hacía arriba 
            # o se ha picado al botón de zoom-in
            self.factor_zoom *= 1.1 #por tanto se multiplicará el factor de zoom por 1.1 , esto hace que el nivel del zoom
            #incremente un 10%
        else : # si delta es más pequeña que 0 significa que se ha movido la rueda del ratón hacía abajo 
            # o se ha picado al botón de zoom-out
            self.factor_zoom *= 0.9 # por tanto se multiplicará el factor de zoom por 0.9 , esto hace que el nivel del zoom
            #disminuya un 10%
        self.actualizar_imagen() #actualiza la imagen a tiempo real


    def ResetZoom(self):
        """
        Este método restablece el factor de zoom a su valor predeterminado de 1.0 y actualiza la imagen.
        Parámetros del método:
        - self: instáncia de la clase, para poder acceder a los métodos de la clase.
        """
        self.factor_zoom = 1.0
        self.actualizar_imagen()
