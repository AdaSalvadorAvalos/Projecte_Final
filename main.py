"""
Treball Final: Ada Salvador Avalos i Milene Soledad Granda Becerra

"""
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
#clases hechas para el programa
from Zoom import ImagenZoom 
from fewfilters import Fewfilters

#inicializamos las variables globales de manera que se pueden usar en todo el código los mismos objetos.
item_fft = None
canvas_fft = None
pil_image = None
back_image = None

item_histo = None
canvas_histo = None
pil_image2 = None
back_image2 = None

direccion_archivo = ""
def abrir_archivos():
    """
    Función que abre los archivos de imágenes usando un diálogo de documento abierto.
    
    """
    HideFiltersOptions() #función que usamos para esconder algunos botones
    combo.current(0) # se coloca el combo en el valor inicial
    global direccion_archivo #llamamos a la variable global 
    direccion_archivo = filedialog.askopenfilename() #hacemos un objeto que sea la dirección del archivo que hemos conseguido gracias la diálogo de askopenfilename()
    if direccion_archivo: #hacemos una comprovación que consiste en ver si la direccón del archivo se ha pasado o no.
       # messagebox.showinfo("Alerta", direccion_archivo)
        return direccion_archivo # si se ha pasado esta dirección se devuelve
    return ""


def RefreshFFTHist(direccion_archivo):
    """
    Función que crea la ImagenTK del histograma y FFT.
    Como parámetros recibe la direccion del archivo (variable global escogida en abrir_archivos()) 
    
    """
    global canvas_fft
    global pil_image
    global back_image
    global item_fft

    global canvas_histo
    global pil_image2
    global back_image2
    global item_histo

    #creación de un filtro que haga el histograma de la imagen.
    filtro1 = Fewfilters()
    filtro1.histograma_imagen(direccion_archivo, "resultado/hist.jpg")

    #creación de un filtro que haga la transformada de fourier de la imagen.
    filtro2 = Fewfilters()
    filtro2.transformada_fft(direccion_archivo, "resultado/fft.jpg")

    # actualiza de la ImagenTK en la ventana  del histograma
    canvas_histo.delete(item_histo) # elimina el objeto de la imagen inicial
    pil_image2 = Image.open("resultado/hist.jpg") 
    pil_image2 = pil_image2.resize((200, 200)) # cambia el tamaño de la del objeto de la Image
    back_image2 = ImageTk.PhotoImage(pil_image2) # crea un objeto  ImageTk.PhotoImage con la Image cambiada de tamaño pil_image2
    # Llama al método create_image para mostrar la imagen en el canvas anchor=tk.NW: la imagen esta en la esquina noroeste del canvas.
    item_histo = canvas_histo.create_image(0, 0, image=back_image2, anchor=tk.NW) 
   
    # actuliza de la ImagenTK en la ventana  de la FFT
    canvas_fft.delete(item_fft)
    pil_image = Image.open("resultado/fft.jpg")
    pil_image = pil_image.resize((200, 200))
    back_image = ImageTk.PhotoImage(pil_image)
    item_fft = canvas_fft.create_image(0, 0, image=back_image, anchor=tk.NW)
    

def boton1():
    """
    Función que se relaciona con el "command=" que se usa al crear un botón. Es decir, es la reacción que obtendremos cuando se pulse el botón.
    
    """
    global direccion_archivo
    direccion_archivo = abrir_archivos()
    if direccion_archivo:
        combo.current(0)
        canvas.ResetZoom() # hace un Reset del Zoom
        canvas.set_imagen(direccion_archivo) # crea una imagen usando la clase Zoom de manera que en esta se puede hacer zoom-in y zoom-out

        RefreshFFTHist(direccion_archivo) # histograma y FFT de la imagen escogida


def aplicar_filtro():
    """
    Función que aplica los filtros cuando han sido seleccionados en el combo.
    """
    HideFiltersOptions() #esconde los filtros hasta que se ha escogido una imagen.
    valor_selec = combo.get() # recibe el valor que se ha seleccionado en el combo.
   # direccion_archivo = abrir_archivos()
   # si el valor escogido es 'RGB' se posiciona un combo especial solo para poder escoger entre las tres componentes.
    if valor_selec == 'RGB' :
        comboRGB.current(0)
        comboRGB.place(x=0, y=75,width=200, height= 30)
        # se crea el filtro RGB
        filtro = Fewfilters()
        filtro.imagenes_RGB(direccion_archivo, "resultado/red.jpg", "resultado/green.jpg", "resultado/blue.jpg")

    elif valor_selec == 'BW' : # si el valor seleccionado es 'BW'
        #se crea un filtro que usa el método estática imagen_BW para conseguir lo que buscamos.
        filtro = Fewfilters()
        filtro.imagen_BW(direccion_archivo, "resultado/bw.jpg")
        #image =Image.open("resultado/bw.jpg")
        canvas.set_imagen("resultado/bw.jpg") # crea la imagen usando la clase Zoom
        RefreshFFTHist("resultado/bw.jpg") # se hace el histograma y FFT de la imagen con este filtro aplicado
    #se usa el mismo procedimento en todos los filtros.
    elif valor_selec == 'Blur' :
        filtro = Fewfilters()
        filtro.imagen_borrosa(direccion_archivo, "resultado/blur.jpg")
        canvas.set_imagen("resultado/blur.jpg")
        RefreshFFTHist("resultado/blur.jpg")
    elif valor_selec == 'Edges' :
        filtro = Fewfilters()
        filtro.imagen_edges(direccion_archivo, "resultado/edges.jpg")
        canvas.set_imagen("resultado/edges.jpg")
        RefreshFFTHist("resultado/edges.jpg")
    elif valor_selec == 'ModeFilter' :
        filtro = Fewfilters()
        filtro.imagen_modefilter(direccion_archivo, "resultado/mode.jpg")
        canvas.set_imagen("resultado/mode.jpg")
        RefreshFFTHist("resultado/mode.jpg")
    elif valor_selec == 'Emboss' :
        filtro = Fewfilters()
        filtro.imagen_EMBOSS(direccion_archivo, "resultado/emboss.jpg")
        canvas.set_imagen("resultado/emboss.jpg")
        RefreshFFTHist("resultado/emboss.jpg")
    elif valor_selec == 'Sharpen' :
        filtro = Fewfilters()
        filtro.imagen_sharpen(direccion_archivo, "resultado/sharp.jpg")
        canvas.set_imagen("resultado/sharp.jpg")
        RefreshFFTHist("resultado/sharp.jpg")
    elif valor_selec == 'Contour' :
        filtro = Fewfilters()
        filtro.imagen_contorno(direccion_archivo, "resultado/contorno.jpg")
        canvas.set_imagen("resultado/contorno.jpg")
        RefreshFFTHist("resultado/contorno.jpg")
        
    #messagebox.showinfo("Alerta", "Filtro" + valor_selec) #alerta que avisa sobre el filtro seleccionado

def on_combobox_change_rgb(event):
    """
    Función que crea una imagen Zoom cuando se ha seleccionado una componente en el comboRGB.
    """
    valor_selec_rgb = comboRGB.get()
    filtro = Fewfilters()
    file = ""
    filtro.imagenes_RGB(direccion_archivo, "resultado/red.jpg", "resultado/green.jpg", "resultado/blue.jpg")
    if valor_selec_rgb=='R': file = "resultado/red.jpg" # si se ha escogido 'R' seleccionamos como file el archivo que se haya creado usando esa componente.
    elif valor_selec_rgb=='G': file = "resultado/green.jpg"
    elif valor_selec_rgb=='B': file = "resultado/blue.jpg"
    # si se ha seleccionado una "file" se crea una imagen con la clase Zoom y su respectivo histograma y FFT.
    if file != "":
        canvas.set_imagen(file)
        RefreshFFTHist(file)
        
def on_combobox_change(event):
    """
    Función que usa el combo para poder aplicar los filtros. Esta función tiene el valor actual del combo y llama a la función aplicar_filtro()
    """
    valor_selec = combo.get()
    aplicar_filtro()
    

def actualizar_regionscroll(event):
    """
    Función que actualiza la región de desplazamiento de un artilugio en función del cuadro que delimita el canvas.
    """
    #se llama la método canvas.config() para actualizar la región que se desplaza . scrollregion= : define la región que se puede desplazar.
    # el método canvas.bbox() se utiliza para obtener las coordenadas del cuadro que delimita el canvas. ALL: especifica que se deben utlizar todos 
    # los elementos del lienzo (canvas). De tal manera que gracias a las coordenadas podemos establecer la nueva región de desplazamiento.
    canvas.config(scrollregion=canvas.bbox('all'))

def HideFiltersOptions():
    """
    Función que oculta las opciones del comboRGB.
    """
    comboRGB.place_forget() # Método de la clase Tkinter para eliminar el widget de la ventana temporalmente. Se usa en comboRGB.
    comboRGB.current(0) # Una vez ocultado el combo se selecciona de manera predeterminada la primera opción.


def on_resize(event):
    """
    Función que cambia el tamaño de la ventana orginal: de ventana pequeña a ventana que ocupa toda la pantalla.
    """
    # se mira si el widget del evento es igual a la ventana 
    if event.widget == ventana:
        # si es igual se mira la nueva altura y el nuevo ancho de la ventana
        new_width = event.width
        new_height = event.height
        # se recalculan las proporciones de: el canvas, la barra de escroll de X, el canvas del histograma y el canvas de la FFT.
        # -18 pixeles: se deja ese margen abajo porque lo ocupa la scrollbarX, -200 pixeles:  se deja ese margen a la izquierda porque lo ocupan los botones
        # - 16 pixeles: ocupa la scrollbarY en la derecha por lo tanto se deja un margen en ese lado.
        canvas.place(x=200, y=0,width= event.width-200, height= event.height)
        scrollbarX.place(x=200, y=event.height-18,width=event.width-200-16, height= 18)
        canvas_histo.place(x=0, y=event.height-400) # deja un margen de 400 pixeles
        canvas_fft.place(x=0, y=event.height-200)  # deja un margen de 200 pixeles

#ventana principal
ventana = tk.Tk()
ventana.geometry("1000x600")
ventana.title("Proyecto APA")
# cambio de tamaño si es necesario. Si hay un "evento"
ventana.bind('<Configure>', on_resize)

#creacion de un boton
boton = tk.Button(ventana,text="Abrir Archivo", command= boton1)

#sitio del boton para la ventana
boton.place(x=0, y=0,width=200, height= 30)

# creación del cuadro combinado combo: selecciona todos los filtros 
combo = Combobox(ventana)
combo['values'] = ('Selecciona Filtro', 'RGB', 'BW', 'Blur', 'Contour', 'Edges', 'Emboss', 'Sharpen','ModeFilter')
combo.current(0)
combo.place(x=0, y=25,width=200, height= 30)
# Asocia el evento de "<<ComboboxSelected>>" con la función de devolución on_combobox_change
combo.bind("<<ComboboxSelected>>", on_combobox_change)

# creación del cuadro combinado comboRGB: selecciona que componente se quiere visualizar en el canvas. 
comboRGB = Combobox(ventana)
comboRGB['values'] = ('Selecciona color', 'R', 'G', 'B')
comboRGB.current(0)
comboRGB.place(x=0, y=75,width=200, height= 30)
# Asocia el evento de "<<ComboboxSelected>>" con la función de devolución on_combobox_change_rgb
comboRGB.bind("<<ComboboxSelected>>", on_combobox_change_rgb)

# creación de un nuevo objeto canvas
canvas = ImagenZoom(ventana)
# creación de una nueva barra vertical que se asocia al canvas usando la "command=canvas.yview" para poder desplazar el contenido del canvas.
scrollbarY = tk.Scrollbar(ventana, orient='vertical',command=canvas.yview)
# se empaqueta la barra de desplazamiento vertical en el lado derecho del widget.
scrollbarY.pack(side='right', fill= 'y')
# sincorniza la barra de desplazamiento con el desplazamiento del lienzo
canvas.configure(yscrollcommand=scrollbarY.set)

# se crea configura una barra horizontal de la misma manera que la vertical
scrollbarX = tk.Scrollbar(ventana, orient='horizontal',command=canvas.xview)
scrollbarX.place(x=200, y=600-18,width=800-16, height= 18)
canvas.configure(xscrollcommand=scrollbarX.set)

# el widget del canvas se empaqueta con fill='both' y expand=True para que llene todo el espacio disponible.
canvas.pack(fill='both', expand=True)
canvas.place(x=200, y=0,width=800, height= 600)

# creación del canvas donde estará la FFT
canvas_fft = tk.Canvas(ventana, width=196, height=200)
pil_image = Image.open("image/white.png")
pil_image = pil_image.resize((200, 200))
back_image = ImageTk.PhotoImage(pil_image)
item_fft = canvas_fft.create_image(0, 0, image=back_image, anchor=tk.NW)
canvas_fft.place(x=0, y=400)
# creación del canvas donde estará el histograma
canvas_histo = tk.Canvas(ventana, width=196, height=200)
pil_image2 = Image.open("image/white.png")
pil_image2 = pil_image2.resize((200, 200))
back_image2 = ImageTk.PhotoImage(pil_image2)
item_histo = canvas_histo.create_image(0, 0, image=back_image2, anchor=tk.NW)
canvas_histo.place(x=0, y=200)



#------------------
HideFiltersOptions() # se esconden las opciones de comboRGB


ventana.mainloop() # loop principal de Tkinter , matiene la aplicación ejecutándose y procesa los eventos necesarios.