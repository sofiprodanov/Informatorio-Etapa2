tupla = ("manzana", "naranja", "banana")
tupla1 = "manzana", "naranja", "banana"

#indica la clase tupla
print(type(tupla))
print(type(tupla1))

#tupla de un solo elemento
tupla3 = ("manzana",)
print(type(tupla3))

#acceder a un elemento de la tupla mediante indice
tupla = ("manzana", "naranja", "banana")
print(tupla[1])

#No se puede modificar mediante indices (un solo valor de la tupla), sino que debemos reescribir completamente todos los valores
tupla3 = ("manzana", "naranja", "banana")
print(tupla3)

tupla3 = ("pomelo", "melon", "kiwi")
print(tupla3)


#POWERPOINT
tupla = ("Informatorio", "Chaco", 2030) #creando una tupla
print(tupla[1]) #accediendo a un elemento de la tupla mediante indice
tupla[1] = "Modificacion" #intentando modificar un elemento, arroja error.
tupla = ("Cargando", "nuevos", "datos") #reemplazando los elementos
print(tupla) #mostrando por consola