import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
#clases hechas para el programa
from Zoom import ImagenZoom
from fewfilters import Fewfilters


direccion_archivo = ""
def abrir_archivos():
    HideFiltersOptions()
    combo.current(0)
    global direccion_archivo
    direccion_archivo = filedialog.askopenfilename()
    if direccion_archivo:
       # messagebox.showinfo("Alerta", direccion_archivo)
        return direccion_archivo
    return ""

def boton1():
    global direccion_archivo
    direccion_archivo = abrir_archivos()
    if direccion_archivo:
        combo.current(0)
        canvas.ResetZoom()
        canvas.set_imagen(direccion_archivo)
       # image =Image.open(direccion_archivo)
       # resized_image = image.resize((800, 600))   
       # img = ImageTk.PhotoImage(resized_image)
       # canvas.create_image(0, 0, anchor="nw", image=img)
       # canvas.image = img


def aplicar_filtro():
    HideFiltersOptions()
    valor_selec = combo.get()
   # direccion_archivo = abrir_archivos()
    if valor_selec == 'RGB' :
        comboRGB.current(0)
        comboRGB.place(x=0, y=75,width=200, height= 30)
        filtro = Fewfilters()
        filtro.imagenes_RGB(direccion_archivo, "resultado/red.jpg", "resultado/green.jpg", "resultado/blue.jpg")

    elif valor_selec == 'BW' :
        filtro = Fewfilters()
        filtro.imagen_BW(direccion_archivo, "resultado/bw.jpg")
        image =Image.open("resultado/bw.jpg")
        canvas.set_imagen("resultado/bw.jpg")

    elif valor_selec == 'Blur' :
        filtro = Fewfilters()
        filtro.imagen_borrosa(direccion_archivo, "resultado/blur.jpg")
        canvas.set_imagen("resultado/blur.jpg")

    elif valor_selec == 'Edges' :
        filtro = Fewfilters()
        filtro.imagen_edges(direccion_archivo, "resultado/edges.jpg")
        canvas.set_imagen("resultado/edges.jpg")

    elif valor_selec == 'ModeFilter' :
        filtro = Fewfilters()
        filtro.imagen_modefilter(direccion_archivo, "resultado/mode.jpg")
        canvas.set_imagen("resultado/mode.jpg")

    elif valor_selec == 'Emboss' :
        filtro = Fewfilters()
        filtro.imagen_EMBOSS(direccion_archivo, "resultado/emboss.jpg")
        canvas.set_imagen("resultado/emboss.jpg")

    elif valor_selec == 'Sharpen' :
        filtro = Fewfilters()
        filtro.imagen_sharpen(direccion_archivo, "resultado/sharp.jpg")
        canvas.set_imagen("resultado/sharp.jpg")

    elif valor_selec == 'Contour' :
        filtro = Fewfilters()
        filtro.imagen_contorno(direccion_archivo, "resultado/contorno.jpg")
        canvas.set_imagen("resultado/contorno.jpg")
    
    elif valor_selec == 'FFT':
        filtro = Fewfilters()
        filtro.transformada_fft(direccion_archivo, "resultado/fft.jpg")
        canvas.set_imagen("resultado/fft.jpg")

    elif valor_selec == 'Histograma':
        filtro = Fewfilters()
        filtro.histograma_imagen(direccion_archivo, "resultado/histograma.jpg")
        canvas.set_imagen("resultado/histograma.jpg")
 
    #messagebox.showinfo("Alerta", "Filtro" + valor_selec)

def on_combobox_change_rgb(event):
    valor_selec_rgb = comboRGB.get()
    filtro = Fewfilters()
    file = ""
    filtro.imagenes_RGB(direccion_archivo, "resultado/red.jpg", "resultado/green.jpg", "resultado/blue.jpg")
    if valor_selec_rgb=='R': file = "resultado/red.jpg"
    elif valor_selec_rgb=='G': file = "resultado/green.jpg"
    elif valor_selec_rgb=='B': file = "resultado/blue.jpg"

    if file != "":
        canvas.set_imagen(file)
        
def on_combobox_change(event):
    valor_selec = combo.get()
    aplicar_filtro()
    

def actualizar_regionscroll(event):
    canvas.config(scrollregion=canvas.bbox('all'))

def HideFiltersOptions():
    comboRGB.place_forget()
    comboRGB.current(0)

#ventana principal
ventana = tk.Tk()
ventana.geometry("1000x600")
ventana.title("Proyecto APA")
ventana.resizable(False, False)

#creacion de un boton
boton = tk.Button(ventana,text="Abrir Archivo", command= boton1)

#sitio del boton para la ventana
boton.place(x=0, y=0,width=200, height= 30)


#boton = tk.Button(ventana, text= "Selcciona filtro", command= aplicar_filtro)
#boton.place(x=0, y=50,width=200, height= 30)


combo = Combobox(ventana)
combo['values'] = ('Selecciona Filtro', 'RGB', 'BW', 'Blur', 'Contour', 'Edges', 'Emboss', 'Sharpen','ModeFilter','FFT','Histograma')
combo.current(0)
combo.place(x=0, y=25,width=200, height= 30)
combo.bind("<<ComboboxSelected>>", on_combobox_change)

comboRGB = Combobox(ventana)
comboRGB['values'] = ('Selecciona color', 'R', 'G', 'B')
comboRGB.current(0)
comboRGB.place(x=0, y=75,width=200, height= 30)
comboRGB.bind("<<ComboboxSelected>>", on_combobox_change_rgb)


#canvas = tk.Canvas(ventana)

canvas = ImagenZoom(ventana)

scrollbarY = tk.Scrollbar(ventana, orient='vertical',command=canvas.yview)
scrollbarY.pack(side='right', fill= 'y')
canvas.configure(yscrollcommand=scrollbarY.set)

scrollbarX = tk.Scrollbar(ventana, orient='horizontal',command=canvas.xview)
scrollbarX.place(x=200, y=600-18,width=800-16, height= 18)
canvas.configure(xscrollcommand=scrollbarX.set)


canvas.pack(fill='both', expand=True)
canvas.place(x=200, y=0,width=800, height= 600)


#------------------
HideFiltersOptions()


ventana.mainloop()