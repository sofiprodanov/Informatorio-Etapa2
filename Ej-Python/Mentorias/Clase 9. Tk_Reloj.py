import tkinter as tk
import time

ventana = tk.Tk()  #crea la ventana, no muestra

#TAMAÑO
ventana.geometry("600x200") #personalizamos el tamaño de la ventana, apertura principal
#ventana.geometry("500x300+500+400") #se indica con coordenadas donde debe abrirse
ventana.minsize(200, 100) #sin string, otorga un tamaño min 
ventana.maxsize(600, 200) #sin string, otorga un tamaño max
ventana.resizable(True, False) #hace que no permite agrandar o achicar(ancho, altura)

#COLOR
ventana.configure(bg="lightgreen")

#TRANSPARENTE
#ventana.attributes(alpha=0.1)

#CAMBIAR ICONO
#ventana.iconbitmap("/url") #para cambiar el icono de la pluma

#AGREGAMOS RELOJ
#le decimos a donde pertenece indicando ventana, indicamos la tipografia y el tamaño en px, bg es el tamaño de fondo de la letra, gf el color del reloj
reloj = tk.Label(ventana, font=("Arial", 60), bg="black", fg="white")

def hora():
    tiempo_actual = time.strftime("%H:%M:%S")
    reloj.config(text=tiempo_actual)

    ventana.after(1000, hora) #tiempo en que se va a ejecutar en milisegundos 


reloj.pack()
hora() #llamo a la funcion
ventana.mainloop() #muestra la ventana(si no se aclara tamaño, tiene uno predeterminado)
