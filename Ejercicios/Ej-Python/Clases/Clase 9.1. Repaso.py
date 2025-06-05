# def mostrar_info(nombre): # es posicional, muestra en pantalla en el orden en que se da
#     print(f"Posicionales: {nombre}")
#     print(f"Hola {nombre}")

# mostrar_info(27, "Pablo")

########################################
# *args lleva como una tupla

def mostrar_info(nombre, edad, *args, actividad = "Estudiante", **kawargs):
    print(f"Hola {nombre}, tenes {edad} años y es {actividad}")
    print(f"*args: {args}")
    print(f"**kwargs: {kawargs}")

mostrar_info(27, "Pablo", "Manzana", "Banana", actividad="Programador, algo=True")