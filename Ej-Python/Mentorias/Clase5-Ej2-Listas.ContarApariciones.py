#Dada la lista:
#colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
#1- Mostrá cuántas veces aparece “rojo” usando .count().
#2- Reemplazá el primer “verde” por “amarillo”
#3- Mostrá la lista final
#El objetivo es usar el método .count(), acceso por índice, asignación de valor. 


colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]

#Punto 1
cantidad_rojo = colores.count("rojo")
print("La cantidad de veces que se repite rojo es: ", cantidad_rojo)

#Punto 2
busca_verde = colores.index("verde")
print("El color verde se encuentra en el indice: ",busca_verde)

reemplazar_verde = colores[busca_verde] = "amarillo"
#O tambien reemplazar_verde = colores[2] = "amarillo"

#Punto 3
print("La nueva lista de colores es: ", colores)

