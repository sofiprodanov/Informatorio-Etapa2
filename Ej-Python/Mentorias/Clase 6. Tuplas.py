print("----TUPLAS----")

frutas = ("manzana", "sandia", "cereza", "manzana")

print(f"Frutas (tupla) {frutas}, tipo: {type(frutas)}")

uno, dos, tres, cuatro = frutas

print("La fruta individual que elegiste es:", uno)

#Buscando por indice
print("Elemento del indice 0", frutas[0])
print("Elemento del indice 2", frutas[2])

#Longitud de una tupla
print("La longitud de la tupla es:", len(frutas)) #cantidad de elementos

#Mas metodos
print("La fruta manzana aparece:", frutas.count("manzana"))
print("El indice de cereza es:", frutas.index("cereza"))

frutas = ("manzana", "sandia", "cereza")
verduras = ("cebolla", "lechuga", "zapallo")

tupla3 = frutas + verduras

print(f"Concatenacion de tuplas: {tupla3}")

