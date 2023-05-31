import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
#clases hechas para el programa
from Zoom import ImagenZoom
from fewfilters import Fewfilters

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
    HideFiltersOptions()
    combo.current(0)
    global direccion_archivo
    direccion_archivo = filedialog.askopenfilename()
    if direccion_archivo:
       # messagebox.showinfo("Alerta", direccion_archivo)
        return direccion_archivo
    return ""


def RefreshFFTHist(direccion_archivo):
    global canvas_fft
    global pil_image
    global back_image
    global item_fft

    global canvas_histo
    global pil_image2
    global back_image2
    global item_histo

    filtro1 = Fewfilters()
    filtro1.histograma_imagen(direccion_archivo, "resultado/hist.jpg")

    
    filtro2 = Fewfilters()
    filtro2.transformada_fft(direccion_archivo, "resultado/fft.jpg")


    canvas_histo.delete(item_histo)
    pil_image2 = Image.open("resultado/hist.jpg")
    pil_image2 = pil_image2.resize((200, 200))
    back_image2 = ImageTk.PhotoImage(pil_image2)
    item_histo = canvas_histo.create_image(0, 0, image=back_image2, anchor=tk.NW)
   
   
    canvas_fft.delete(item_fft)
    pil_image = Image.open("resultado/fft.jpg")
    pil_image = pil_image.resize((200, 200))
    back_image = ImageTk.PhotoImage(pil_image)
    item_fft = canvas_fft.create_image(0, 0, image=back_image, anchor=tk.NW)
    

def boton1():
    global direccion_archivo
    direccion_archivo = abrir_archivos()
    if direccion_archivo:
        combo.current(0)
        canvas.ResetZoom()
        canvas.set_imagen(direccion_archivo)

        RefreshFFTHist(direccion_archivo)


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
        RefreshFFTHist("resultado/bw.jpg")
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
        RefreshFFTHist(file)
        
def on_combobox_change(event):
    valor_selec = combo.get()
    aplicar_filtro()
    

def actualizar_regionscroll(event):
    canvas.config(scrollregion=canvas.bbox('all'))

def HideFiltersOptions():
    comboRGB.place_forget()
    comboRGB.current(0)


def on_resize(event):
    # Access the new window size
    if event.widget == ventana:
        new_width = event.width
        new_height = event.height
        canvas.place(x=200, y=0,width= event.width-200, height= event.height)
        scrollbarX.place(x=200, y=event.height-18,width=event.width-200-16, height= 18)
        canvas_histo.place(x=0, y=event.height-400)
        canvas_fft.place(x=0, y=event.height-200)

#ventana principal
ventana = tk.Tk()
ventana.geometry("1000x600")
ventana.title("Proyecto APA")
ventana.bind('<Configure>', on_resize)

#creacion de un boton
boton = tk.Button(ventana,text="Abrir Archivo", command= boton1)

#sitio del boton para la ventana
boton.place(x=0, y=0,width=200, height= 30)


combo = Combobox(ventana)
combo['values'] = ('Selecciona Filtro', 'RGB', 'BW', 'Blur', 'Contour', 'Edges', 'Emboss', 'Sharpen','ModeFilter')
combo.current(0)
combo.place(x=0, y=25,width=200, height= 30)
combo.bind("<<ComboboxSelected>>", on_combobox_change)

comboRGB = Combobox(ventana)
comboRGB['values'] = ('Selecciona color', 'R', 'G', 'B')
comboRGB.current(0)
comboRGB.place(x=0, y=75,width=200, height= 30)
comboRGB.bind("<<ComboboxSelected>>", on_combobox_change_rgb)

canvas = ImagenZoom(ventana)

scrollbarY = tk.Scrollbar(ventana, orient='vertical',command=canvas.yview)
scrollbarY.pack(side='right', fill= 'y')
canvas.configure(yscrollcommand=scrollbarY.set)

scrollbarX = tk.Scrollbar(ventana, orient='horizontal',command=canvas.xview)
scrollbarX.place(x=200, y=600-18,width=800-16, height= 18)
canvas.configure(xscrollcommand=scrollbarX.set)


canvas.pack(fill='both', expand=True)
canvas.place(x=200, y=0,width=800, height= 600)


canvas_fft = tk.Canvas(ventana, width=196, height=200)
pil_image = Image.open("image/white.png")
pil_image = pil_image.resize((200, 200))
back_image = ImageTk.PhotoImage(pil_image)
item_fft = canvas_fft.create_image(0, 0, image=back_image, anchor=tk.NW)
canvas_fft.place(x=0, y=400)

canvas_histo = tk.Canvas(ventana, width=196, height=200)
pil_image2 = Image.open("image/white.png")
pil_image2 = pil_image2.resize((200, 200))
back_image2 = ImageTk.PhotoImage(pil_image2)
item_histo = canvas_histo.create_image(0, 0, image=back_image2, anchor=tk.NW)
canvas_histo.place(x=0, y=200)



#------------------
HideFiltersOptions()


ventana.mainloop()