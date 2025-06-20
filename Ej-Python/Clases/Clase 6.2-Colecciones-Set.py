#Se definen con llaves {} y pueden contener cualquier tipo de elementos, sin embargo no los unhashable (no diccionario, no lista) - si tupla. 
#Aceptan elementos inmutables
#Son deordenados (sus elementos no tienen indices) y son mutables, sin embargo no pueden contener elementos duplicados.

colores_set = {"rojo", "azul", "verde"}
print(f"Conjunto set: {colores_set}, {type(colores_set)}")

#print(f"Intento acceder al primer elemento: {colores_set[0]}") #no se puede acceder ya que no tiene indice

colores_set.add("amarillo")
print(f"Set luego del add: {colores_set}")

colores_set.add("amarillo")
print(f"Set luego del segundo add: {colores_set}") #como ya esta el amarillo no se agrega un segundo amarillo.


colores_set.remove("verde") #borra y si se intenta borrar de la misma forma arroja error. Podes indicar el valor a borrar
print(f"Set luego del remove: {colores_set}")

colores_set.discard("verde") #borra y si se intenta borrar de la misma forma otra vez no arroja error.
print(f"Set luego del discard: {colores_set}") 

elemento_eliminado = colores_set.pop() #elimina el elemento sin poder indicar cual.
print(f"Elemento eliminado: {elemento_eliminado}") 
print(f"Set luego del pop: {colores_set}") 

colores_set.clear()
print(f"Set luego del clear: {colores_set}") 

colores_set = {"rojo", "azul", "verde"}
print(f"E color 'rojo' esta en el set?: {"rojo" in colores_set}") 
print(f"E color 'violeta' esta en el set?: {"violeta" in colores_set}") 

conj1 = {1, 2, 3}
conj2 = {2, 4, 5, 6}

union_conj = conj1.union(conj2)
print(f"Union: {union_conj}") 

interseccion_conj = conj1.intersection(conj2)
print(f"Interseccion: {interseccion_conj}") 

diferencia_conj = conj1.difference(conj2) #busca del elemento 1 lo diferente al 2
print(f"Diferencia: {diferencia_conj}") 

#Elimina duplicado y ademas lo ordena
lista_con_duplicado = {1, 1, 2, 3, 4, 9, 5, 7, 9, 8}
lista_sin_duplicado = list(set(lista_con_duplicado))
print(f"Lista sin duplicado: {lista_sin_duplicado}")

