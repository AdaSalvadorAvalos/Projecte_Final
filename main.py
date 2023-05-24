from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
#clases hechas para el programa
from Zoom import ImagenZoom
from fewfilters import Fewfilters

def abrir_archivos():
    direccion_archivo = filedialog.askopenfilename()
    if direccion_archivo:
        messagebox.showinfo("Alerta", direccion_archivo)
        
    return direccion_archivo


def aplicar_filtro():
    valor_selec = combo.get()
    messagebox.showinfo("Alerta", "Filtro" + valor_selec)
    


def actualizar_regionscroll(event):
    canvas.config(scrollregion=canvas.bbox('all'))

#ventana principal
ventana = Tk()
ventana.geometry("1000x600")
ventana.title("Proyecto APA")
ventana.resizable(False, False)
#creacion de un boton
boton = Button(ventana,text="Abrir Archivo", command= abrir_archivos)

#sitio del boton para la ventana
boton.place(x=0, y=0,width=200, height= 30)

boton = Button(ventana, text= "Filtros", command= aplicar_filtro)
boton.place(x=0, y=50,width=200, height= 30)

combo = Combobox(ventana)
combo['values'] = ('Selecciona Filtro', 'rgb', 'bw', 'blur')
combo.current(0)
if combo['values']== 'rgb':
    filtro = Fewfilters()
    resultado = filtro.componentes_rgb(abrir_archivos)
    
combo.place(x=0, y=25,width=200, height= 30)

canvas = Canvas(ventana)
scrollbarY = Scrollbar(ventana, orient='vertical',command=canvas.yview)
scrollbarY.pack(side='right', fill= 'y')
canvas.configure(yscrollcommand=scrollbarY.set)

scrollbarX = Scrollbar(ventana, orient='horizontal',command=canvas.xview)
scrollbarX.place(x=200, y=600-18,width=800-16, height= 18)
canvas.configure(xscrollcommand=scrollbarX.set)


canvas.pack(fill='both', expand=True)
canvas.place(x=200, y=0,width=800, height= 600)

ventana.mainloop()