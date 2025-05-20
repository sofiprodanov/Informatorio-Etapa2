#CREAR UNA LISTA
#lista de numeros
numeros = [1, 2, 3, 4, 5]

#lista de strings
nombres = ["Juan", "Maria", "Pedro"]

#lista de varios tipos de datos
lista = ["Juan", "Maria", "Pedro", 1, 2, 3, True, False, 3.14]


#ACCEDER A UN ELEMENTO DE UNA LISTA
#acceder a un elemento de la lista
print(numeros[0]) #va a mostrar el numero 1


#MOSTRAR TODOS LOS ELEMENTOS DE LA LISTA
#si queremos mostrar todos los elementos de la lista lo hacemos sin poner indice
print(numeros)
print(nombres)
print(lista)


#LISTA QUE CONTIENE OTRAS LISTAS
lista = ["Juan", "Maria", "Pedro", [numeros], True, False, 3.14]
print(lista[3]) #llama a la lista numeros


#LLAMAR A LOS ELEMENTOS DE UNA LISTA
#Podemos incluir una lista que no declaramos antes y lo hacemos abriendo corchetes e incluyendo los elementos que queremos en la lista
lista1 = ["Juan", "Maria", "Pedro", [6, 7, 8, 9], True, False, 3.14]
print(lista[3])

#Podemos acceder a un rango de elementos de la lista. Escribimos el nro de la 1° posicion separado por dos puntos (:) y el nro de la ultima posicion
#a la que queremos acceder. Python cuenta desde el cero en adelante (1 es dos)
print(lista1[1:4])

#Tambien se puede dar un rango desde una posicion hasta el final de la lista
print(lista1[2:])

#Se puede dar un rango desde el principio hasta un posicion
print(lista1[:3])

#Se puede acceder a los elementos de la lista desde el final hacia adelante, usando numeros negativos.
print(lista1[-1])

#Se puede acceder a los elementos de la lista desde el final hacia adelante (anteultimo), usando numeros negativos.
print(lista1[-2])


#MODIFICAR UN ELEMENTO DE LA LISTA
#Asignando el nuevo valor a la posicion del elemento que deseamos cambiar
lista2 = ["Juan", "Maria", "Pedro", [6, 7, 8, 9], True, False, 3.14]
lista2[1] = "Ana"
print(lista) #imprimir la lista

lista2 = ["Juan", "Maria", "Pedro", [6, 7, 8, 9], True, False, 3.14]
lista2 = ["Hola", "Mundo", 1, True]
print(lista)

#Metodos mas comunes que se puede usar con listas
# append(elemento) agrega un elemento al final de la lista
# extend(iterable) agrega los elementos de un iterable al final de la lista
# insert(i, elemento) inserta un elemento en una posicion especifica en la lista
# remove(elemento) elimina la primera aparicion de un elemento de la lista
# pop([i]) elimina el elemento en la posicion especificada y lo devuelve. Si no se especifica una posicion, elimina y devuelve el ultimo elemento de la lista
# clear() elimina todos los elementos de la lista
# index(elemento[ , inicio[ , fin]]) devuelve la posicion de la primera aparicion de un elemento en la lista. Se puede especificar los indices de inicio
    #y fin para hacer un slicing
# count(elemento) devuelve el nro de veces que un elemento aparece en la lista
# reverse() #invierte el orden de los elementos en la lista
# copy() #devuelve una copia superficial de la lista
# sort(key=none, reverse=false) #ordena los elementos de lalista en orden ascendente (excepto que se especifique lo contrario con reverse=true).
    #Se puede especificar una funcion de clave opcional para definir el orden de clasificacion.
#len() #devuelve el nro de elementos de la lista

#EJEMPLO CON APPEND()
#lista de varios tipos de datos
lista = ["Hola", "Mundo", 1, True]
print(lista)
lista.append("otro elemento")
print(lista) #va a mostrar lista = ["Hola", "Mundo", 1, True, "otro elemento"]

#EJEMPLO DE REMOVED()
#lista de varios tipos de datos
lista1 = ["Hola", "Mundo", 1, True]
print(lista)
lista.remove("Mundo")
print(lista) #va a mostrar lista = ["Hola", 1, True]

#EJEMPLO DE LEN()
#lista de varios tipos de datos
lista1 = ["Hola", "Mundo", 1, True]
print(len(lista)) #va a mostrar lista = ["Hola", 1, True]









