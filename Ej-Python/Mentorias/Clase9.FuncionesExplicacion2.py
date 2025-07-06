### PARAMETROS DE POSICION ###

#Para que tenga un valor por defecto es poniendo por ej a = 2, b = 2.
#Si ponemos el valor predeterminado a = 2 y b no le asignamos valor. Cuando nosotros le damos el rdo por ej print(multiplicar(5)) va a mutiplicar el valor 5 por a = 2.

# def multiplicar(a = 2, b = 2):
#     return a * b

# print(multiplicar())




# def presentacion_persona(nombre, edad, pais):
#     """"Esta funcion es una presentacion de una persona indicando el nombre, edad y pais""" #6 comillas para poner un comentario
#     print(f"Me llamo {nombre}, tengo {edad} años, soy de {pais}.")

# presentacion_persona("argentina", "Elias", 19) #POR POSICION > argentina va a tomarse como nombre, elias como edad y 19 como pais.
# presentacion_persona(pais="argentina", nombre="Elias",edad=19) #FUNCION POR CLAVE > como si fuera diccionario clave valor.


#USANDO PARAMETRO POR DEFECTO
# def presentacion_persona(nombre="Nicolas", edad = 20, pais=""):
#     print(f"Me llamo {nombre}, tengo {edad} años, soy de {pais}.")

# presentacion_persona(pais="argentina", edad=19)