diccionario = {"Juan": 24, "Ana": 30, "Cristian": 28}
print(diccionario)
print(diccionario["Juan"])

#Modificacion de valor
diccionario1 = {"Juan": 24, "Ana": 30, "Cristian": 28}
diccionario1["Ana"] = 18
print(diccionario1)

#OTRA FORMA DE CREAR DICCIONARIOS
#Con la funcion dict()
una_lista = [("clave1", "valor1"), ("clave2", "valor2"), ("clave3", "valor3")]
un_diccionario = dict(una_lista)
print(un_diccionario)
print(type(un_diccionario))

#o usando sintaxis de argumentos de palabras claves para especificar las claves y los valores
mi_diccionario = dict(clave1 ="valor1", clave2 = "valor2", clave3 = "valor3")
print(mi_diccionario)
print(type(mi_diccionario))

#METODOS PARA DICCIONARIOS
# clear() elimina todos los elementos del diccionario
# copy() devuelve una copia superficial del diccionario
# get() devuelve el valor asociado a una clave dada, o un valor predeterminado
# items() devuelve una vista de lista de todos los pares clave-valor en el diccionario
# keys() devuelve una vista de lista de todas las claves en el diccionario
# pop() elimina y devuelve el valor asociado a una clave dada
# popitems() elimina y devuelve un par clave-valor aleatorio del diccionario
# setdefault() devuelve el valor asociado a una clave dada, o lo crea con un valor predeterminado si la clave no esta presente
# update() actualiza el diccionario con los pares clave-valor de otro diccionario o iterable
# values() devuelve una vista de lsita de todos los valroes en el diccionario
