import tkinter as tk

#CREAR UNA VENTANA
ventana = tk.Tk()
ventana.title("Menu desplegable")
ventana.geometry("400x200")

#FUNCION PARA OPCIONES DEL MENU
def mostrar_mensaje():
    print("Hola desde la terminal")
    
#CREAR UN MENU
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu) #vinculamos el barra menu en la ventana, falta ubicarlo.

menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Principal", menu=menu_principal)

submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label="Opciones", menu=submenu) #damos el texto

button = tk.Button(ventana, text="Boton Saludar", command=mostrar_mensaje)
button.pack()


#EJECUTAR ESA FUNCION
submenu.add_command(label="Salir", command=ventana.quit)
submenu.add_command(label="Saludar", command=mostrar_mensaje)


#MOSTRAR LA VENTANA
ventana.mainloop()