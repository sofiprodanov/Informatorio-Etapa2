#Ejercicio 1: Gestión de una lista de compras
#Crea una lista vacía llamada lista_compras
#Luego:
#1- Agregá 3 productos usando .append()
#2- Mostrá cuántos productos hay con len()
#3- Eliminá el último producto con .pop()
#4- Mostrá la lista actualizada
#El objetivo es aprender .append(), .pop() y .len()

#Punto 1
lista_compras = []


#Punto 2
#.append() permite agregar enteros tambien.
lista_compras.append("manzana")
lista_compras.append("naranaja")
lista_compras.append("sandia")

print("Esta es tu lista de compras: ", lista_compras)


#Punto 3
cantidad_elementos = len(lista_compras) 

print("La cantidad de elementos que hay en la lista de compras es: ", cantidad_elementos) #o tambien print(len(lista_compras))


#Punto 4
#Si no le ponemos el indice, elimina el ultimo de la lista. Si queremos eliminar otro elemento debemos indicar con el indice
elemento_eliminado = lista_compras.pop() 

print("El producto eliminado es: ", elemento_eliminado)


#Punto 5
print("Finalmente tu lista de compras quedo asi: ", lista_compras)



