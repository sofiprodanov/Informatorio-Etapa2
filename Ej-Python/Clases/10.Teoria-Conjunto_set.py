conjunto = {1, 5, "Hola", "Mundo", 3.14, True} #se repite el tipo de dato
print(conjunto)
print(type(conjunto))


#POWERPOINT
#Ejemplo con condicional
conjunto = {"Info", "Chaco", "Info", 123, 123}
print(conjunto)

if "Info" in conjunto:
    print("El valor 'Info' se encuentra en el conjunto.")
else:
    print("El valor 'Info' se encuentra en el conjunto.")

#otra forma de buscar es un una variable
conjunto = {"Info", "Chaco", "Info", 123, 123}
print(conjunto)

valor_buscado = "Chaco"

if "Info" in conjunto:
    print("El valor", valor_buscado," se encuentra en el conjunto.")
else:
    print("El valor", valor_buscado," se encuentra en el conjunto.")

#usamos for para hacer el recorrido de cada elemento
conjunto = {"Info", "Chaco", "Info", 123, 123}

for i in conjunto:
    print(i)



#OPERACIONES CON CONJUNTO
#Union (|) > mediante esta operacion, podemos combinar dos conjuntos en un nuevo (similar a concatenar)
frutas = {"naranja", "manzana", "pera"}
verduras = {"lechuga", "tomate", "zanahoria"}

frutas_y_verduras = frutas | verduras
print(frutas_y_verduras)

#Interseccion (&) > esta operacion es ideal cuando necesitamos crear un nuevo conjunto con elementos que estan presentes end os o mas conjuntos
caja_1 = {"remera", "camisa", "pantalon"}
caja_2 = {"zapato", "remera", "campera"}

repetidos_en_las_cajas = caja_1 & caja_2
print(repetidos_en_las_cajas)

#Diferencias (-) > podemos crear un nuevo conjunto con los elementos que se encuentran en el primer conjunto, pero no en el segundo
caja_1 = {"remera", "camisa", "pantalon"}
caja_2 = {"zapato", "remera", "campera"}

repetidos_en_las_cajas = caja_1 - caja_2
print(repetidos_en_las_cajas)


#LISTAS DE FUNCIONES UTILES PARA LOS CONJUNTOS:
# len(conjunto): Devuelve la cantidad de elementos en el conjunto. Esta función se puede usar en listas, tuplas e incluso variables.
# conjunto.add(elemento): Agrega un elemento al conjunto si no está presente.
# conjunto.remove(elemento): Elimina un elemento del conjunto si está presente.
# conjunto.discard(elemento): Intenta eliminar un elemento del conjunto (sin error si no está presente). 
# conjunto.clear(): Vacía el conjunto, eliminando todos sus elementos.
# conjunto.copy(): Crea una copia del conjunto original.
