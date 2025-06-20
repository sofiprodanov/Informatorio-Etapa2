#Las listas se define con [] y puede contener cualquier elemento, incluso otras listas o coleccion. 
#Son ordenadas (tienen indice) y mutables (agregar, eliminar, o modificar)

       #  0  1  2  3  4
numeros = [1, 2, 3, 4, 5]

#primer elemento
print(numeros[0])

#ultimo elemento
print(numeros[-1])

#sublista(slicing)
print(f"Primeros 3 elementos: {numeros[:3]}")
print(f"Ultimos 2 elementos: {numeros[-2:]}")
print(f"Elementos del medio: {numeros[1:-1]}")

print(f"Longitud de la lista: {len(numeros)}")


print("### METODOS ###") # si ponemos numero. > muestran todos los metodos
print(f"Cuantas veces aparece el elemento con valor 3: {numeros.count(3)}")
print(f"Cual es el indice del elemento con valor 4: {numeros.index(4)}")

numeros[0] = 0  #se cambia el valor del indice cero, de 1 a 0
print(f"Despues de modificar: {numeros}")

numeros.append(6)
print(f"Lista luego del append: {numeros}")

numeros.insert(0, 8) #en el indice cero inserto el valor 8, mueve de lugar cambiando el indice de los restantes.
print(f"Lista luego del insert: {numeros}")

numeros.pop() #pop elimina elementos, si no tiene indice elimina el ultimo, sino queremos eliminar un elemento particular indicamos su indice
print(f"Lista luego del pop: {numeros}")

numeros.remove(0) #elimina un valor particular (solo elimina el primero que encuentra)
print(f"Lista luego del remove: {numeros}")


numeros = [1,3, 7, 2, 5] 
numeros.sort() #ordena de forma ascendente
print(f"Lista luego del sort: {numeros}")

numeros.sort(reverse=True) #ordena de forma descendente
print(f"Lista luego del sort: {numeros}")



print("### MATRIZ ###") #LISTA DE LISTA
matriz = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
]

print(f"Matriz: {matriz}")
print(f"Elemento [1][1]: {matriz[1][1]}")


print(f"El elemento con valor 5 esta en la lista?: {5 in numeros}")
print(f"El elemento con valor 5 esta en la lista?: {"SI" if 5 in numeros else "NO"}")
